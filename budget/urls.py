from django.urls import path  # 004-srsa
from . import views

# declarar rota
urlpatterns = [
    path('', views.home, name='home'),
    # path('update/', views.update)
]
