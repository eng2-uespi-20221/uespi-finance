"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
                                # path('endereço/', minhaView.as_view(), nome='nome-da-url');
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path
from . import views
from category.views import CategoryHomeView, CategoryCreateView , CategoryDeleteView 
from category.views import CategoryUpdateView, CategoryListView ;

urlpatterns = [
    path ('',CategoryHomeView.as_view(), name ='category') ,
    path ('create/',CategoryCreateView.as_view(), name ='create'),
    path ('update/<int:id>',CategoryUpdateView.as_view(), name ='update'),
    # path ('list/<int:id>',CategoryListView.as_view(), name ='list'),
    path ('delete/<int:id>',CategoryDeleteView.as_view(), name ='delete')
    
   # path('category', CategoryCreateView.as_view(), name='CreateCategory')


]