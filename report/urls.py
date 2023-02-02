from django.urls import path
from . import views
from report.views import relatorio_pdf
urlpatterns = [
    path ('',relatorio_pdf, name ='report') ,
 
    
   # path('category', CategoryCreateView.as_view(), name='CreateCategory')
]