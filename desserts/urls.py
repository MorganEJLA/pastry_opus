from django.urls import path
from . import views

urlpatterns = [
    path('', views.desserts, name='desserts'),
    path('<int:id>/', views.dessert_detail, name='dessert_detail'),
    path('search', views.search, name='search'),
]
