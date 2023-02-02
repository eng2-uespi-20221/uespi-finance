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
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('welcome')), 
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('template/', TemplateView.as_view(template_name='layouts/base.html')),
    path('crudTransacao/', include('crudTransacao.urls')),
    path('category/', include('category.urls')),
    path('budget/', include('budget.urls')),  # 003-srsa
    path('report/', include('report.urls')),
]
