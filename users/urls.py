from . import views
from django.urls import path, include


urlpatterns = [
    path('', include('asset.urls')),  # api/asset-create-list/
    path('', include('loan.urls')),  # api/loan/
    path('', include('clients.urls')),  # api/create-client/
    path('', include('remedial.urls')),  # api/remedial-create-list/
    path('register/', views.user_create_view,
         name='user-register'),  # /api/register/
    path('login/', views.user_login_view,
         name='user-login'),  # /api/login/
]
