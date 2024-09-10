from django.urls import path

from .views import client_create_list

urlpatterns = [
    path('create-client/', client_create_list, name='create-list-client'),
]
