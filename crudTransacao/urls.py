from django.urls import path
from . import views

# declarar rota
urlpatterns = [
    path('vcreate/', views.vcreate),
    path('vdelete/', views.vdelete),
    path('vread/', views.vread),
    path('vupdate/', views.vupdate),
]