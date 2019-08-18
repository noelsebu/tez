from django.urls import path, include
from django.conf.urls import *
from django.contrib import admin

from . import views

urlpatterns = [
    
    #path(r'testcases/', views.testcases_list),
    path(r'jira/',views.jira_list)
    #path(r'environment',views.environment_list)
]