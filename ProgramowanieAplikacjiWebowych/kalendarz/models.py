from django.db import models
from django.core.validators import EmailValidator, RegexValidator
# Create your models here.

class Country(models.Model):
    country = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    language = models.CharField(max_length=5,default='en')

    def __str__(self):
        return self.country

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(validators=[EmailValidator],max_length=50)
    password = models.CharField(validators=[RegexValidator('^.*(?=.{8,})(?=.*[a-zA-Z])(?=.*\d)(?=.*[!#$%&? "]).*$')],max_length=50)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)

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
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
