from django.urls import path
from . import views

# declarar rota
urlpatterns = [
    path('vcreate/', views.vcreate),
    path('vdelete/', views.vdelete),
    path('vread/', views.vread, name="transacao"),
    path('vupdate/', views.vupdate),
]