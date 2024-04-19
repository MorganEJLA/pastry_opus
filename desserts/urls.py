from django.urls import path
from . import views

urlpatterns = [
    path('', views.desserts, name='desserts'),
]
