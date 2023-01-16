from django.shortcuts import render, redirect
from django.views import View
from .models import Category
from django.views.generic import TemplateView

# Create your views here.
class CategoryHomeView(View):
    def get(self, request):  
        cat = Category.objects.all()
        return render(request, 'category.html', {'categories':cat})    
    
#def home (request):
 #   return HttpResponse('str')

class CategoryCreateView(View):
    def get(self, request):
        return render(request, 'create.html')

    def post(self, request):
        name = request.POST['name']
        description = request.POST['description']
        category = Category(name=name, description=description)
        category.save()
        return redirect('category_list')

class CategoryUpdateView(View):
    def get(self, request, id):
        category = Category.objects.get(id=id)
        return render(request, 'category_update.html', {'category': category})

    def post(self, request, id):
        category = Category.objects.get(id=id)
        category.name = request.POST['name']
        category.description = request.POST['description']
        category.save()
        return redirect('category_list')

class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'category_list.html', {'categories': categories})

class CategoryDeleteView(View):
    def get(self, request, id):
        category = Category.objects.get(id=id)
        category.delete()
        return redirect('category_list')