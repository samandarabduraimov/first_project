from django.contrib import admin
from .models import SerialEvent,SerialNumber
# Register your models here.
admin.site.register(SerialEvent)
admin.site.register(SerialNumber)