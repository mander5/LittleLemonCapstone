from django.contrib import admin
from django.urls import path
from .views import sayHello

urlpatterns = [
    path('sayhello/', sayHello, name='sayHello'),
]
