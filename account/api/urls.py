from django.urls import path
from .views import AccountList, ObtainAuthToken, ChangePasswordView, does_account_exist_view
# for Automatic login
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
    path('register', AccountList.as_view(), name='register'),
    # path('login', obtain_auth_token, name='login'),  # Generate a token when user logs in (Automatic Login).
    path('login', ObtainAuthToken.as_view(), name='login'),
    path('detail/', AccountList.as_view(), name='detail'),
    path('update', AccountList.as_view(), name='update'),
    path('delete', AccountList.as_view(), name='delete'),
    path('check_if_account_exist/', does_account_exist_view, name='check_if_account_exist'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password')
]