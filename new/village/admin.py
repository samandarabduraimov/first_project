from django.contrib import admin

# Register your models here.
from .models import village, People

admin.site.register(village)
admin.site.register(People)
