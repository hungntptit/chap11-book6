from django.urls import path

from product_model import views

urlpatterns = [
    path('getproduc/', views.get_product_data),
]