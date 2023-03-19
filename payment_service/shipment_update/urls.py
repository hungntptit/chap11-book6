from django.urls import path

from shipment_update import views

urlpatterns = [
    path('shipment_update/', views.shipment_details_update),
]