from django.http import HttpResponse
from django.template import loader
from .models import Book
# this shows hello world
def index(request):
    return HttpResponse('Hello World')

# this loads a template, finds all books in table Book and returns a list of books sorted in html
def detail(request):
    template = loader.get_template('home/index.html')
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return HttpResponse(template.render(context, request))

# this simple returns a list of all books in table Book with no spaces in 1 line
'''def detail(request):
    return HttpResponse(Book.objects.all())'''

# this takes the book_id in the url and displays a message to say which id you are viewing
def specific(request, book_id):
    response = "You're looking at the book %s."
    return HttpResponse(response % book_id)