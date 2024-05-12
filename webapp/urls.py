
from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
    path('library/', views.library),
    path('library/<int:book_id>/',views.specific, name='specific'),
    path('register_book/',views.register_book, name='register_book'),
    path('register_book_process/',views.register_book_process, name='register_book_process'),
    path('login/',views.login_user, name='login'),
    path('login_process/',views.login_process, name='login_process'),
    path('logout_process/',views.logout_process, name='logout_process'),
]
