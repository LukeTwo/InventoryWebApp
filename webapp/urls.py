
from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
    path('library/', views.library),
    path('library/<barcode>/',views.specific, name='specific'),
    path('register_book/',views.register_book, name='register_book'),
    path('login/',views.login_user, name='login'),
    path('logout_process/',views.logout_process, name='logout_process'),
    path('register_user/',views.register_user, name='register_user'),
    path('toggle_darkmode/',views.toggle_darkmode, name='toggle_darkmode'),
    path('library/<barcode>/delete/',views.delete_book, name='delete_book'),
]
