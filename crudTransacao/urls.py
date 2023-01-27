from django.urls import path
from . import views

# declarar rota
urlpatterns = [
    path('vcreate/', views.vcreate, name = "vcreate"),
    path('vdelete/<int:id>', views.vdelete, name = "vdelete"),
    path('vread/', views.vread, name ="transacao"),
    path('vupdate/<int:id>', views.vupdate, name = "vupdate"),
    path('abrircreate', views.abrircreate, name = "abrircreate")
    #path('lista/', views.vcreate, name='lista'),
]