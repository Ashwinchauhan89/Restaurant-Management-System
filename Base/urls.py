from django.contrib import admin
from django.urls import path,include
from Base import views

urlpatterns = [
    
    path('home/', views.home, name='home'), # Home view
    path('about/', views.about, name='about'), # About view
    path('contact/', views.contact, name='contact'), # Contact view
    path('menu/', views.menu, name='menu'), # Menu view
    path('reservation/', views.reservation, name='reservation'), # Reservation view
    path('login/', views.login, name='login'), # Admin login view
]
