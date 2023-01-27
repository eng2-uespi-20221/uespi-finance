from django.urls import path  # 004-srsa
from . import views

# declarar rota
urlpatterns = [
    path('home/', views.home)
]
