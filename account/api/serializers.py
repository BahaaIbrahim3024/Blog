from rest_framework import serializers
from account.models import Account


# create serializer for Account operations
class AccountSerializer(serializers.ModelSerializer):
    # This is a way to hide this field (Password field) from the user & make it only write.
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'first_name', 'last_name', 'age', 'gender', 'password', 'password2']

        # This is for security we don't want people to be able to read the password
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # we want to make sure that the 2 passwords match
    def save(self):
        account = Account(email=self.validated_data['email'], username=self.validated_data['username'],
                          first_name=self.validated_data['first_name'], last_name=self.validated_data['last_name'],
                          age=self.validated_data['age'], gender=self.validated_data['gender'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match!!'})
        account.set_password(password)
        account.save()
        return account


# Serializer for get account properties
class AccountPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['pk', 'email', 'username']


# Serializer for edit & update account data
class AccountUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'username', 'first_name', 'last_name', 'age', 'gender']


# Serializer for change password
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)
