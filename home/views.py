from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template import loader
from .models import Book, Darkmode, Student, RentBook
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
'''
This is for trying to migrate to a custom user model
from django.conf import settings
User = settings.AUTH_USER_MODEL
'''

# Global variable for that all functions call to set the correct theme
theme = {False:'light',True:'dark'}

# load home page
def home(request):
    template = loader.get_template('home/home.html')
    color = request.COOKIES.get('Darkmode')
    # An altnernative for checking darkmode preference would be to call from the DB directly theme[Darkmode.objects.filter(user=request.user)[0].choice]
    # Issue with using cookies is if the admin changes the darkmode preference, the user would need to relog for changes to take effect
    return HttpResponse(template.render({'color':color}, request))

# load list of all books
def library(request):
    template = loader.get_template('home/library.html')
    test = request.user.id
    books = Book.objects.filter(user = request.user.id)
    color = request.COOKIES.get('Darkmode')
    context = {
        'books': books,
        'color':color,
    }
    return HttpResponse(template.render(context, request))

# this takes the book_id in the url and displays a message to say which id you are viewing
def specific(request, barcode):
    try:
        if request.user == Book.objects.filter(barcode = barcode)[0].user:
            name = Book.objects.filter(barcode = barcode)
            response = "You're looking at the book %s."
            return HttpResponse(response % barcode)
        else:
            return HttpResponseNotFound("This is not a valid ID")
    except:
        return HttpResponseNotFound("This book does not exist")

# display the regiter book page with no context
def register_book(request):
    if request.method == 'POST':
        # request.post.get will not throw an error if values arent found in the POST but default to 'None'
        name = request.POST.get('name')
        barcode = request.POST.get('barcode')
        user = request.user
        
        # Create a new book entry in the database using the Book model
        book = Book(barcode=str(user.id)+barcode, name=name, user=user)
        book.save()

        return redirect('/library/')
    template = loader.get_template('home/register_book.html')
    context = {}
    color = request.COOKIES.get('Darkmode')
    return HttpResponse(template.render({'color':color}, request))

def delete_book(request, barcode):
    try:
        print('hello')
        if request.user == Book.objects.filter(barcode = barcode)[0].user:
            Book.objects.filter(barcode=barcode).delete()
            return redirect('/library/')
        else:
            return HttpResponseNotFound("This is not a valid ID")
    except:
        return HttpResponseNotFound("This book does not exist")
       
# load login page
def login_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['pass']
        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            response = redirect('home')
            # This will help with a bug - if a user is created in admin panel rather than using the app it will not generate a darkmode
            exists = Darkmode.objects.filter(user=request.user)
            if not exists:
                darkmode = Darkmode(user=user)
                darkmode.save()
            response.set_cookie('Darkmode', theme[Darkmode.objects.filter(user=request.user)[0].choice])
            return response
        else:
            return redirect('login')
    template = loader.get_template('home/login.html')
    return HttpResponse(template.render(None, request))

# logs out user
def logout_process(request):
    logout(request)
    response = redirect('login')
    response.delete_cookie('Darkmode')
    return response

# Brings user to register_user page
def register_user(request):
    if request.method == 'POST':
        print('WOOOOOOOOOOOOOOOOO')
        # request.post.get will not throw an error if values arent found in the POST but default to 'None'
        name = request.POST.get('name')
        password = request.POST.get('pass')
        
        # Create a new user entry in the database using the User model
        user = User(username=name)
        user.set_password(password)
        user.save()
        darkmode = Darkmode(user=user)
        darkmode.save()
        print('dig')
        login(request, user)
        response = redirect('home')
        response.set_cookie('Darkmode', theme[Darkmode.objects.filter(user=request.user)[0].choice])
        return response
    else:
        print('hello')
        template = loader.get_template('home/register_user.html')
        return HttpResponse(template.render(None, request))

# display the register student page with no context
def register_student(request):
    if request.method == 'POST':
        # request.post.get will not throw an error if values arent found in the POST but default to 'None'
        student_id = request.POST.get('student_id')
        name = request.POST.get('name')
        user = request.user
        number = request.POST.get('number')
        
        # Create a new student entry in the database using the Student model
        student = Student(id=str(user.id)+student_id, name=name, user=user,contact_number=number)
        student.save()

        return redirect('/student_list/')
    template = loader.get_template('home/register_student.html')
    context = {}
    color = request.COOKIES.get('Darkmode')
    return HttpResponse(template.render({'color':color}, request))

# List of all students
def student_list(request):
    template = loader.get_template('home/students.html')
    test = request.user.id
    students = Student.objects.filter(user = request.user.id)
    color = request.COOKIES.get('Darkmode')
    context = {
        'students': students,
        'color':color,
    }
    return HttpResponse(template.render(context, request))

def delete_book(request, barcode):
    try:
        print('hello')
        if request.user == Book.objects.filter(barcode = barcode)[0].user:
            Book.objects.filter(barcode=barcode).delete()
            return redirect('/library/')
        else:
            return HttpResponseNotFound("This is not a valid ID")
    except:
        return HttpResponseNotFound("This book does not exist")


# Save the users theme preference
def toggle_darkmode(request):
    mode = {'light':False,'dark':True}
    color = request.GET.get('color')
    dark = Darkmode.objects.filter(user=request.user)[0]
    dark.choice = mode[color]
    dark.save()
    response = HttpResponse('User preference updated succesdully')
    response.set_cookie('Darkmode', color)
    return response

def book_out(request):
    if request.method == 'POST':
        
        
        # request.post.get will not throw an error if values arent found in the POST but default to 'None'
        student_id = request.POST.get('student_id')
        barcode = request.POST.get('barcode')
        user = request.user
        
        book = Book.objects.filter(user=user,barcode=str(user.id)+barcode)
        student =  Student.objects.filter(user=user,id = student_id)
        print('hello')
        if not student.exists():
            return redirect('/home/')
        # Create a new book entry in the database using the Book model
        transaction = RentBook(book=book, student=student, user = user)
        transaction.save()

        #   to-do = CHANGE THIS TO REDIRECT TO A 'LOANED BOOKS' PAGE CONTAINING ALL BOOKS CURRENTLY OUT
        return redirect('/library/')
    template = loader.get_template('home/book_out.html')
    context = {}
    color = request.COOKIES.get('Darkmode')
    return HttpResponse(template.render({'color':color}, request))