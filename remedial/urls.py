from django.urls import path

from .views import remedial_list_create

urlpatterns = [
    path('remedial-create-list/', remedial_list_create,
         name='remedial-create-list'),
    path('remedial-create-list', remedial_list_create,
         name='remedial/<int:pk>/detail/'),
    path('remedial/<int:pk>/update/', remedial_list_create,
         name='remedial-update'),
]
