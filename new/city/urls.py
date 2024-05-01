from django.urls import path
from .views import *


urlpatterns = [
    path( '' , get_info, nama='get_info')
]