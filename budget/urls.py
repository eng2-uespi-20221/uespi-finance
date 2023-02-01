from django.urls import path  # 004-srsa
from . import views

# declarar rota
urlpatterns = [
    path('', views.home, name='home'),
    path('open_create_page/', views.open_create_page, name='open_create_page'),
    path('create_new_budget/',views.create_new_budget, name='create_new_budget'),
    path('open_update_page/<int:id>',views.open_update_page, name='open_update_page'),
    path('update_budget/<int:id>',views.update_budget, name='update_budget'),
    path('delete_budget/<int:id>',views.delete_budget, name='delete_budget'),
]
