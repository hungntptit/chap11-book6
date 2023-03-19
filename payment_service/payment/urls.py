from django.urls import path

from payment import views

urlpatterns = [
    path('initiate_payment/', views.get_payment),
    path('payment_status/', views.user_transaction_info),
]