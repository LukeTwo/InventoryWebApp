
from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
    path('library/', views.library),
    path('library/<barcode>/',views.specific_book, name='specific_book'),
    path('register_book/',views.register_book, name='register_book'),
    path('login/',views.login_user, name='login'),
    path('logout_process/',views.logout_process, name='logout_process'),
    path('register_user/',views.register_user, name='register_user'),
    path('toggle_darkmode/',views.toggle_darkmode, name='toggle_darkmode'),
    path('library/<barcode>/delete/',views.delete_book, name='delete_book'),
    path('register_student/',views.register_student, name='register_student'),
    path('student_list/',views.student_list, name='student_list'),
    path('student_books/<id>/',views.student_book_list, name='student_book_list'),
    path('book_out/',views.book_out, name='book_out'),
    path('return_book/',views.return_book, name='return_book'),
]
