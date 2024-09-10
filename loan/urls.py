from django.urls import path
from .views import LoanAPIView,BankAPIView

urlpatterns = [
    path('loans/', LoanAPIView.as_view(), name='loan-create-list'),
    path('banks-list', BankAPIView.as_view(), name='banks-list'),
    path('loans/<int:pk>/detail/', LoanAPIView.as_view(), name='loan-detail'),
    path('loans/<int:pk>/update/', LoanAPIView.as_view(), name='loan-update'),
]
