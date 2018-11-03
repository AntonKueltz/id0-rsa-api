from accounts import views

from django.urls import path

urlpatterns = [
    path('', views.CreateUser.as_view()),
]