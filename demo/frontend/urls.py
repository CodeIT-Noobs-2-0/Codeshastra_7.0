from django.urls import path
from . import views
from .views import *#RegisterUser

urlpatterns = [
    path('', views.index),
    path('user-register/', RegisterUser.as_view(), name='user-register'),
]