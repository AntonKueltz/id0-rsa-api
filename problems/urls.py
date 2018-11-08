from problems import views

from django.urls import path

urlpatterns = [
    path('', views.ProblemList.as_view()),
    path('<int:pk>/', views.ProblemDetail.as_view()),
    path('<int:pk>/check', views.CheckAnswer.as_view()),
]