
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('post/add/',post_add, name = 'post_add'),
    path('reset_password/',change_password,name = "change_password"),

]
