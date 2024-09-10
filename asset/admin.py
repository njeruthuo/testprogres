from django.contrib import admin

# Register your models here.
from .models import Asset, Client

admin.site.register(Asset)

admin.site.register(Client)
