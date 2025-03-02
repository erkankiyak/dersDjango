from django.contrib import admin
from django.urls import path
from contact.views import index, contact


urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),

]