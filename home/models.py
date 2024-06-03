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

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    contact_number = models.CharField(max_length=15)
    
# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    barcode = models.CharField(max_length=15)
    name = models.CharField(max_length=200)
    student =  models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    copies = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # This is just for debugging in console
    def __str__(self):
        return self.book_name

class RentBook(models.Model):
    book =  models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    transaction_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# Creating a field for darkmode for each user which defaults to False on User creation
class Darkmode(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    choice = models.BooleanField(default=False)

