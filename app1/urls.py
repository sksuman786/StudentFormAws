from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    
   path('test/',views.home),
   path('data/',views.myform)
]
