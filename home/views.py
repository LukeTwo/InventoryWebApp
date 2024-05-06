from django.http import HttpResponse
from django.template import loader
from .models import Book
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# load home page
def home(request):
    template = loader.get_template('home/home.html')
    return HttpResponse(template.render(None, request))

# load list of all books
def library(request):
    template = loader.get_template('home/library.html')
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return HttpResponse(template.render(context, request))

# this takes the book_id in the url and displays a message to say which id you are viewing
def specific(request, book_id):
    response = "You're looking at the book %s."
    return HttpResponse(response % book_id)

def search(request):
    response = "You're looking at the book %s."
    return HttpResponse(response % book_id)

# display the regiter book page with no context
def register_book(request):
    template = loader.get_template('home/register_book.html')
    context = {}
    return HttpResponse(template.render(context, request))

# takes the users input from the form on register_book and creates a new DB entry
def register_book_process(request):
    if request.method == 'POST':
        # request.post.get will not throw an error if values arent found in the POST but default to 'None'
        book_name = request.POST.get('book_name')
        book_id = request.POST.get('book_id')
        
        # Create a new patient entry in the database using the Patient model
        book = Book(book_id=book_id, book_name=book_name)
        book.save()

        return HttpResponse("Data successfully inserted!")
    else:
        return HttpResponse("Invalid request method.")

def BootstrapFilter(request):
    '''template = loader.get_template('home/bookentry.html')
    context = {}
    return HttpResponse(template.render(context, request))'''
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