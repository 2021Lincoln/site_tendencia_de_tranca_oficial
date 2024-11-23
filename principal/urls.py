# login_app/urls.py
from django.urls import path
from .views import findex

urlpatterns = [
    path('', findex),
]
