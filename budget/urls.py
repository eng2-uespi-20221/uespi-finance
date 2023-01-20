from django.urls import path  # 004-srsa
from . import views

# declarar rota
urlpatterns = [
    path('teste/', views.teste),
    path('budget/', views.budget)
]
