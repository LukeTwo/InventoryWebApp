# InventoryWebApp
# to-do
~~Register user~~\
~~Logout~~\
~~user specific data~~\
~~Session-id database calls(fixed using forced auth and user db calls)~~\
Search books\
~~Darkmode~~\
~~Home Directory~~\
~~Fix-NavBar~~\
~~NavBar~~\
~~View library~~\
~~View specific books~~\
~~Register books~~\
~~Login~~\
~~Force authentication~~\
Lend Book\
Return Book
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

2 ways to add URLs\
1.  Add url path entries to app folder:\
    appname - urls - add customurls\
    The full url would be website.com/appname/customurl\
2.  Add url path to project folder:\
    projectname - urls - add customurls\
    The full url would be website.com/customurl\

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
