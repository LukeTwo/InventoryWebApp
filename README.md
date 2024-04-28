# InventoryWebApp

Starting the Project:
Install
pip install virtualenv

Activate virtual enrviroment
.\venv\Scripts\activate.bat

StartProject
pip install django
django-admin startproject webapp
cd webapp

Test install with command and go to IP address printed
python manage.py runserver

Creating the application:
Create application
python manage.py startapp name

Create front end elements
appname - views.py

Add url path entries to app
appname - urls - add urls

Redirect from site to app
projectname - urls - add urls

Create app schema
appname - models.py
projectname - settings - installedapps - add appname.apps.appnameConfig
python manage.py makemigrations appname

To view sql models to be created
python manage.py sqlmigrate migrationnumber

Commit tables to database
python manage.py migrate

create admin account
python manage.py createsuperuser
admin
E-system1

Allow admin edit database tables
appname - admin.py - import table - admin.site.register(table)