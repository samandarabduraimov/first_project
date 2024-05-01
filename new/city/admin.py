from django.contrib import admin

# Register your models here.
from .models import city, People

admin.site.register(city)
admin.site.register(People)