from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

GENDERS = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]


# Create a custom user manager
class MyAccountManager(BaseUserManager):
    """ define what will happen when a new user is created and superuser is created """
    def create_user(self, email, username, first_name, last_name, age, gender, password=None):
        if not email:
            raise ValueError("User must has email address !!")
        if not username:
            raise ValueError("User must has a unique username !!")
        if not first_name:
            raise ValueError("User must enter First name !!")
        if not last_name:
            raise ValueError("User must enter Last name !!")
        if not age:
            raise ValueError("User must enter age !!")
        if not gender:
            raise ValueError("User must specify gender !!")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            age=age,
            gender=gender,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, age, gender, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            age=age,
            gender=gender,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Create a custom user model
class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(verbose_name='first name', max_length=40)
    last_name = models.CharField(verbose_name='last name', max_length=40)
    age = models.IntegerField(verbose_name='age', null=True)
    gender = models.CharField(max_length=1, choices=GENDERS)
    date_join = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # because Account Model isn't inherited from models.Model & Tell this account model where the manager is OR how to use the manager
    objects = MyAccountManager()

    # to login using email instead of username USERNAME_FIELD = What ever we want to login with
    USERNAME_FIELD = 'email'
    # Required Fields When register a new user
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'age', 'gender']

    def __str__(self):
        return str(self.email)+" , "+str(self.username)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'All Accounts'
