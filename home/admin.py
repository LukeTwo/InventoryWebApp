from django.contrib import admin

from .models import Book, Darkmode, Student, RentBook

admin.site.register(Book)
admin.site.register(Darkmode)
admin.site.register(Student)
admin.site.register(RentBook)
