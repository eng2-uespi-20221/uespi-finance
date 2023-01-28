from django.shortcuts import render, redirect
from django.views import View
from .models import Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.views.generic import TemplateView

# Create your views here.
class CategoryHomeView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self, request):  
        cat = Category.objects.all()
        return render(request, 'category.html', {'categories':cat})       
#def home (request):
 #   return HttpResponse('str')
class CategoryCreateView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'create.html')
    def post(self, request):
        name = request.POST['name']
        type_transaction = request.POST['type_transaction']
        if len(name)<2:
            return redirect('create')
        category = Category(name=name, type_transaction=type_transaction)
        category.save()
        return redirect('category')

class CategoryUpdateView(LoginRequiredMixin,View):
    def get(self, request, id):
        category = Category.objects.get(id=id)
        print()
        return render(request, 'category_update.html', {'category': category})
    def post(self, request, id):
        category = Category.objects.get(id=id)
        category.name = request.POST['name']
        category.save()
        return redirect('category')      
class CategoryListView(LoginRequiredMixin,View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'category_list.html', {'categories': categories})
class CategoryDeleteView(LoginRequiredMixin,View):
    def get(self, request, id):
        category = Category.objects.get(id=id)
        category.delete()
        return redirect('category')