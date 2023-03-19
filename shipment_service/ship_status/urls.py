from django.urls import path

from ship_status import views

urlpatterns = [
    path('shipment_status/', views.shipment_status),
    path('shipment_updates/', views.shipment_reg_update),
]
