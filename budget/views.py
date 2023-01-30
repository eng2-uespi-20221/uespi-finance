from . models import Budget
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')

def home(request):
    budgets = Budget.objects.filter(user_id=request.user.id)
    budgets = Budget.objects.all()
    return render(request, 'home.html', {'budgets': budgets})

def open_create_page(request):
    # budgets = Budget.objects.all()
    return render(request, 'create_budget.html')

def create_new_budget(request):
    if (request.method == 'POST'):
        orcamento = request.POST.get('orcamento')
        valor_limite = request.POST.get('valor_limite')
        valor_formatado = str(valor_limite).replace(',','.')
        Budget.objects.create(orcamento=orcamento, valor_limite=valor_formatado)
    return redirect(home)

def open_update_page(request, id):
    budget = Budget.objects.get(id=id)
    return render(request, 'update.html', {'budget':budget})

def update_budget(request, id):
    budget = Budget.objects.get(id=id)  
    orcamento = request.POST.get('orcamento')
    valor_limite = request.POST.get('valor_limite')
    valor_formatado = str(valor_limite).replace(',','.')
    budget.orcamento = orcamento
    budget.valor_limite = valor_formatado
    budget.save() 
    return redirect('home')
    
def delete_budget(request, id):
    budget = Budget.objects.get(id=id)
    budget.delete()
    return redirect('home')


