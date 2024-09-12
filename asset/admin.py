from django.contrib import admin

# Register your models here.
from .models import Asset, Client, AssetRegister

admin.site.register(Asset)

admin.site.register(AssetRegister)

admin.site.register(Client)
