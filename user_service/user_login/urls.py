from django.urls import path

from user_login import views

urlpatterns = [
    path('userlogin/', views.user_login),
]