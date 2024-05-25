from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
'''
This is to attempt to migrate to custom user model
from django.conf import settings
User = settings.AUTH_USER_MODEL

class User(AbstractUser):
    theme = models.CharField(max_length=5, default='light')
'''

# Create your models here.
class Book(models.Model):
    book_id = models.CharField(max_length=15, primary_key=True)
    book_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # This is just for debugging in console
    def __str__(self):
        return self.book_name

class RentBook(models.Model):
    book_id = models.CharField(max_length=15)
    book_name = models.CharField(max_length=200)
    student_name = models.CharField(max_length=100)
    transaction_id = models.AutoField(primary_key=True)

# Creating a field for darkmode for each user which defaults to False on User creation
class Darkmode(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    choice = models.BooleanField(default=False)

