from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Student(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    contact_number = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
# Create your models here.
class Book(models.Model):
    barcode = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class RentBook(models.Model):
    book =  models.ForeignKey(Book, on_delete=models.CASCADE,blank=False, null=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=False, null=False)
    transaction_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

# Creating a field for darkmode for each user which defaults to False on User creation
class Darkmode(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    choice = models.BooleanField(default=False)



