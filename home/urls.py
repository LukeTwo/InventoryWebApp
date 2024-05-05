from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('detail/',views.detail, name='detail'),
    path('detail/<int:book_id>/',views.specific, name='specific'),
    path('book_entry/',views.book_entry, name='book_entry'),
    path('book_entry_process/',views.book_entry_process, name='book_entry_process'),
]