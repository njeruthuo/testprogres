from django.urls import path

from .views import asset_api_view, AssetStatusAPIView
from .register import AssetRegisterV2

urlpatterns = [
    path('asset-create-list/', asset_api_view, name='asset-create-list'),
    # path('asset-register/', AssetRegisterAPIView.as_view()),
    path('asset-register2/', AssetRegisterV2.as_view(), name="asset-register-2"),
    path('asset-status/', AssetStatusAPIView.as_view(), name='asset-status'),
]
