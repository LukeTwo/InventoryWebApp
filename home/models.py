from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    book_id = models.CharField(max_length=15, primary_key=True)
    book_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name

class RentBook(models.Model):
    book_id = models.CharField(max_length=15)
    book_name = models.CharField(max_length=200)
    student_name = models.CharField(max_length=100)
    transaction_id = models.AutoField(primary_key=True)
