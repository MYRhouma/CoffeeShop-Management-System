from django.urls import path, include
from .views import *
urlpatterns = [
    path('', table_scan, name='table_scan'),
]
