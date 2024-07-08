# InventoryWebApp
This is a simple webApp that functions similar to a library system but was created for a local school giving students books for the year. This app uses a multi-tenant database pattern approach. Data can only be viewed by the orgnaization who created it. 

One consideration I needed to make was how to choose the primary key for the books. My first idea was to use the barcode but problem with that is the same books use the same barcode. Even if I just kept a 'no. of copies' field, if someone damaged a book, there would be no way to telling which of those copies it is, thus who damaged it. Then I thought just to use a generic auto incrementer field but the downside of this is the entity has no way of telling which physical book is which ID. I wanted to keep the process as streamlined as possible with little human work but it wasn't viable.

So it left me with 2 options:
1. Have the school make their own barcodes for their books and simply scan those and use those as a primary key
2. Have the school simply manually number each book. This way we can use a barcode + number as a composite key to indentify the books.

8/7/24 UPDATE: Client got the book seller to individually barcode each book which simplifies the process for me to use barcode as the ID

Another consideration was scaling the project. If I wanted to allow multiple schools use the shared DB, I would need a way to distinguish scanning the same books. This was fixed by having a custom id for each book which consistent of [request.user.id]+'Book'+[request.Barcode].


# to-do
~~Register user~~\
~~Logout~~\
~~user specific data~~\
~~Session-id database calls(fixed using forced auth and user db calls)~~\
~~Search books~~\
~~Darkmode~~\
~~Home Directory~~\
~~Fix-NavBar~~\
~~NavBar~~\
~~View library~~\
~~View specific books~~\
~~Register books~~\
~~Login~~\
~~Force authentication~~\
Delete Book\
Lend Book\
Return Book\
Host website on AWS or Azure\
Fix darkmode with admin bug
## Starting the Project:
Install:\
pip install virtualenv

Activate virtual enrviroment:\
.\venv\Scripts\activate.bat

StartProject:\
pip install django\
django-admin startproject webapp\
cd webapp

Test install with command and go to IP address printed:\
python manage.py runserver

## Creating the application:
Create application:\
python manage.py startapp name

Create request handlers:\
appname - views.py

2 ways to add URLs
1.  Add url path entries to app folder:\
    appname - urls - add customurls\
    The full url would be website.com/appname/customurl
    
2.  Add url path to project folder:\
    projectname - urls - add customurls\
    The full url would be website.com/customurl

Create app schema:\
appname - models.py\
projectname - settings - installedapps - add appname.apps.appnameConfig\
python manage.py makemigrations appname

To view sql models to be created:\
python manage.py sqlmigrate migrationnumber

Commit tables to database:\
python manage.py migrate

create admin account:\
python manage.py createsuperuser\
admin\
E1

Allow admin edit database tables:\
appname - admin.py - import table - admin.site.register(table)
