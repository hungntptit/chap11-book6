from django.urls import path

from user_info import views

urlpatterns = [
    path('userinfo/', views.user_info),
]