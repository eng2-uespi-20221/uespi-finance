from django.urls import path
from . import views
from report.views import relatorio_pdf
urlpatterns = [
    path ('report/',relatorio_pdf.view(), name ='relatorio') ,
 
    
   # path('category', CategoryCreateView.as_view(), name='CreateCategory')
]