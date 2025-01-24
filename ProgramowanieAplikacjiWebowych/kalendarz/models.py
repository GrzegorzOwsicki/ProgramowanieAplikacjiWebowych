from django.db import models
from django.contrib.auth.models import AbstractUser ,BaseUserManager
from django.core.validators import EmailValidator, RegexValidator
# Create your models here.

class CustomUserManager(BaseUserManager):
    """
    Custom manager for CustomUser model where email is the unique identifier
    for authentication instead of usernames.
    """
    def create_user(self, email, username, password=None, **extra_fields):
        """
        Create and return a regular user with the given email and password.
        """
        if not username:
            raise ValueError("The Username field must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        """
        Create and return a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)
    


class Country(models.Model):
    country = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    language = models.CharField(max_length=5,default='en')

    def __str__(self):
        return self.country

class User(AbstractUser):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True,null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username

class Holiday(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country,on_delete=models.CASCADE) 
    public = models.BooleanField()

    def __str__(self):
        return self.name

class UserHoliday(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name