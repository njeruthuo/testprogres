from django.urls import path

from .views import asset_api_view
from .register import AssetRegisterV2

urlpatterns = [
    path('asset-create-list/', asset_api_view, name='asset-create-list'),
    # path('asset-register/', AssetRegisterAPIView.as_view()),
    path('asset-register2/', AssetRegisterV2.as_view())
]
