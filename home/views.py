from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template import loader
from .models import Book, Darkmode
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
    color = theme[Darkmode.objects.filter(user=request.user)[0].choice]
    return HttpResponse(template.render({'color':color}, request))

# load list of all books
def library(request):
    template = loader.get_template('home/library.html')
    test = request.user.id
    books = Book.objects.filter(user = request.user.id)
    color = theme[Darkmode.objects.filter(user=request.user)[0].choice]
    context = {
        'books': books,
        'color':color,
    }
    print(books)
    return HttpResponse(template.render(context, request))

# this takes the book_id in the url and displays a message to say which id you are viewing
def specific(request, book_id):
    try:
        if request.user == Book.objects.filter(book_id = book_id)[0].user:
            name = Book.objects.filter(book_id = book_id)
            response = "You're looking at the book %s."
            return HttpResponse(response % book_id)
        else:
            return HttpResponseNotFound("This is not a valid ID")
    except:
        return HttpResponseNotFound("This book does not exist")

def search(request):
    response = "You're looking at the book %s."
    return HttpResponse(response % book_id)

# display the regiter book page with no context
def register_book(request):
    template = loader.get_template('home/register_book.html')
    context = {}
    color = theme[Darkmode.objects.filter(user=request.user)[0].choice]
    return HttpResponse(template.render({'color':color}, request))

# takes the users input from the form on register_book and creates a new DB entry
def register_book_process(request):
    if request.method == 'POST':
        # request.post.get will not throw an error if values arent found in the POST but default to 'None'
        book_name = request.POST.get('book_name')
        book_id = request.POST.get('book_id')
        print(request.user)
        user = request.user
        
        
        # Create a new book entry in the database using the Book model
        book = Book(book_id=book_id, book_name=book_name, user=user)
        book.save()

        return redirect('/library/')
    else:
        return HttpResponse("Invalid request method.")

def BootstrapFilter(request):
    '''template = loader.get_template('home/bookentry.html')
    context = {}
    color = theme[Darkmode.objects.filter(user=request.user)[0].choice]
    return HttpResponse(template.render({'color':color}, request))'''
    return render(request, "home/bootstrap_filter.html", {})

# load login page
def login_user(request):
    template = loader.get_template('home/login.html')
    return HttpResponse(template.render(None, request))

def login_process(request):
    # request.post will throw an error if values arent found in the POST
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['pass']
        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')

# logs out user
def logout_process(request):
    logout(request)
    return redirect('login')

# Brings user to register_user page
def register_user(request):
    template = loader.get_template('home/register_user.html')
    return HttpResponse(template.render(None, request))

# Enter's user's details into dababase
def register_user_process(request):
    if request.method == 'POST':
        # request.post.get will not throw an error if values arent found in the POST but default to 'None'
        name = request.POST.get('name')
        password = request.POST.get('pass')
        
        # Create a new user entry in the database using the User model
        user = User(username=name, password=password)
        user.save()
        darkmode = Darkmode(user=user)
        darkmode.save()
        login(request, user)
        return redirect('home')
    else:
        return redirect('register_user')

# Save the users theme preference
def toggle_darkmode(request):
    mode = {'light':False,'dark':True}
    dark = Darkmode.objects.filter(user=request.user)[0]
    dark.choice = mode[request.GET.get('color')]
    dark.save()
    success = 'User preference updated succesdully'
    return HttpResponse(success)

