from django.urls import path, include
from django.conf.urls import *
from django.contrib import admin

from . import views

urlpatterns = [
    
    path(r'authokens/', views.authtokens_list),
    #path(r'users/',views.index)
    #path(r'environment',views.environment_list)
]