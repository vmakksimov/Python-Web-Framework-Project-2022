from django.db import models

from Crypto_web.accounts.managers import CryptoUserManager

from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models

from Crypto_web.common.validators import only_letters_validator


# Create your models here.
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from django.contrib import messages



class CryptoUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USER_NAME_MAX_LENGTH = 25

    username = models.CharField(
        max_length=USER_NAME_MAX_LENGTH,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,

    )

    is_staff = models.BooleanField(
        default=False,
    )




    USERNAME_FIELD = 'username'

    objects = CryptoUserManager()

    class Meta:
        verbose_name = 'User'




class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MIN_LENGTH = 2

    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30


    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]


    first_name = models.CharField(
        max_length= FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_letters_validator,
      )
    )

    last_name = models.CharField(
        max_length= LAST_NAME_MAX_LENGTH,
        validators= (
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            only_letters_validator,
        )
    )

    picture = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,

    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length= max(len(x) for x, _ in GENDERS),
        choices= GENDERS,
        default= DO_NOT_SHOW,
    )

    user = models.OneToOneField(
        CryptoUser,
        on_delete=models.CASCADE,
        primary_key=True,

    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


    class Meta:
        verbose_name = 'Profile'
