from django.contrib import admin
from django.urls import path,include
from My_application import views

urlpatterns = [
   
    path('',views.home),
    path('admin/',admin.site.urls)
    
]
