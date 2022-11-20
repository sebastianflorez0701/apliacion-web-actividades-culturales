from django.urls import path
from actividades import views

urlpatterns = [
    path('actividades/', views.ActividadesList.as_view()),
]
