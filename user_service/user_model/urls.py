from django.urls import path

from user_model import views

urlpatterns = [
    path('userregistration/', views.registration_req),
]