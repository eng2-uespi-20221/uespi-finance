from django.urls import path
from . import views

# declarar rota
urlpatterns = [
    path('vcreate/', views.vcreate, name = "criart"),
    path('vdelete/<int:id>', views.vdelete, name = "vdelete"),
    path('vread/', views.vread, name ="transacao"),
    path('vupdate/', views.vupdate, name = "editar"),
    path('criar/', views.vcreate, name='post_create'),
]