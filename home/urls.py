from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('bootstrap_filter/',views.BootstrapFilter, name='bootstrap_filter'),
]