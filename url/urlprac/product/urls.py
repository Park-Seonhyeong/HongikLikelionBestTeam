from django.urls import path
from product import views

urlpatterns = [
    path('', views.productlist),
    path('first/', views.productfirst),
]
