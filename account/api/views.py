from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from .serializers import AccountSerializer, AccountPropertiesSerializer, AccountUpdateSerializer, ChangePasswordSerializer
from account.models import Account
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication


# define API actions (GET, PUT, POST, DELETE requests)  Using class based views
class AccountList(APIView):
    # 1- POST request (Create new account)
    # This means every one can register (Create account ) we don't need to be authenticated
    @permission_classes([])
    @authentication_classes([])
    def post(self, request):
        if request.method == 'POST':
            data = {}
            email = request.data.get('email', '0').lower()
            if validate_email(email) != None:
                data['error_message'] = 'That email is already in use.'
                data['response'] = 'Error'
                return Response(data)

            username = request.data.get('username', '0')
            if validate_username(username) != None:
                data['error_message'] = 'That username is already in use.'
                data['response'] = 'Error'
                return Response(data)

            serializer = AccountSerializer(data=request.data)

            if serializer.is_valid():
                account = serializer.save()
                data['response'] = 'successfully registered new user.'
                data['email'] = account.email
                data['username'] = account.username
                data['pk'] = account.pk
                token = Token.objects.get(user=account).key
                data['token'] = token
            else:
                data = serializer.errors
            return Response(data)


    # 2- GET request (view or get user data)
    @permission_classes((IsAuthenticated, ))
    def get(self, request):
        try:
            account = request.user
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = AccountPropertiesSerializer(account)
            return Response(serializer.data)

    # 3- PUT request (edit or update user data)
    @permission_classes((IsAuthenticated, ))
    def put(self, request):
        try:
            account = request.user
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            serializer = AccountUpdateSerializer(account, data=request.data, partial=True)
            data = {}
            if serializer.is_valid():
                serializer.save()
                data['success'] = 'Account updated successful'
                return Response(data=data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 4- DELETE request (delete account)
    @permission_classes((IsAuthenticated, ))
    def delete(self, request):
        try:
            account = request.user
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        #token = Token.objects.get(user=account).key
        if request.method == 'DELETE':
            operation = account.delete()
            data = {}
            if operation:
                data['success'] = 'Account Deleted'
            else:
                data['fail'] = 'Delete Failed'
            return Response(data=data)

# Make sure that email & username are valid
def validate_email(email):
    account = None
    try:
        account = Account.objects.get(email=email)
    except Account.DoesNotExist:
        return None
    if account != None:
        return email


def validate_username(username):
    account = None
    try:
        account = Account.objects.get(username=username)
    except Account.DoesNotExist:
        return None
    if account != None:
        return username


# define a custom view for login to customize the returned data
class ObtainAuthToken(APIView):
    # This means every one can login we don't need to be authenticated
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        context = {}
        email = request.POST['username']
        password = request.POST['password']
        account = authenticate(email=email, password=password)
        if account:
            try:
                token = Token.objects.get(user=account)
            except Token.DoesNotExist:
                # if the token doesn't exist create one (Login for the first time)
                token = Token.objects.create(user=account)
            context['response'] = "Successfully authenticated."
            context['pk'] = account.pk
            context['email'] = email.lower()
            context['token'] = token.key
        else:
            context['response'] = 'Error in login'
            context['error_message'] = 'Invalid credentials'
        return Response(context)



@api_view(['GET', ])
@permission_classes([])
@authentication_classes([])
def does_account_exist_view(request):

	if request.method == 'GET':
		email = request.GET['email'].lower()
		data = {}
		try:
			account = Account.objects.get(email=email)
			data['response'] = email
		except Account.DoesNotExist:
			data['response'] = "Account does not exist"
		return Response(data)




class ChangePasswordView(UpdateAPIView):
	serializer_class = ChangePasswordSerializer
	model = Account
	permission_classes = (IsAuthenticated,)
	authentication_classes = (TokenAuthentication,)

	def get_object(self, queryset=None):
		obj = self.request.user
		return obj

	def update(self, request, *args, **kwargs):
		self.object = self.get_object()
		serializer = self.get_serializer(data=request.data)

		if serializer.is_valid():
			# Check old password
			if not self.object.check_password(serializer.data.get("old_password")):
				return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

			# confirm the new passwords match
			new_password = serializer.data.get("new_password")
			confirm_new_password = serializer.data.get("confirm_new_password")
			if new_password != confirm_new_password:
				return Response({"new_password": ["New passwords must match"]}, status=status.HTTP_400_BAD_REQUEST)

			# set_password also hashes the password that the user will get
			self.object.set_password(serializer.data.get("new_password"))
			self.object.save()
			return Response({"response":"successfully changed password"}, status=status.HTTP_200_OK)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)