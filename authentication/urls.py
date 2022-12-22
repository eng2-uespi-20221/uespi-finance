from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='welcome'),
    path('login', views.login, name='login'),
    path('signin', views.signin, name='signin'),
    path('register', views.register, name='register'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('secure', views.secure, name='secure'),
]