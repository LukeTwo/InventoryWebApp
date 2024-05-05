from django.http import HttpResponse
from django.template import loader
from .models import Book
# this shows hello world
def index(request):
    template = loader.get_template('home/home.html')
    return HttpResponse(template.render(None, request))

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

def search(request):
    response = "You're looking at the book %s."
    return HttpResponse(response % book_id)

def book_entry(request):
    template = loader.get_template('home/bookentry.html')
    context = {}
    return HttpResponse(template.render(context, request))

def book_entry_process(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        book_id = request.POST.get('book_id')
        
        # Create a new patient entry in the database using the Patient model
        book = Book(book_id=book_id, book_name=book_name)
        book.save()

        return HttpResponse("Data successfully inserted!")
    else:
        return HttpResponse("Invalid request method.")