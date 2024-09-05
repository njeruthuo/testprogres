from . import views
from django.urls import path


urlpatterns = [
    path('register/', views.user_create_view,
         name='user-register'),  # /api/register/
    path('login/', views.user_login_view,
         name='user-login'),  # /api/login/
]
