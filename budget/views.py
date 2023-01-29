from django.shortcuts import render
from . models import Budget


# Create your views here.
# 002-srsa-Criar uma view de teste

# recupera lista bd / renderiza home.html
def home(request):
    budgets = Budget.objects.all()
    return render(request, 'home.html', {'budgets': budgets})

def opencreate(request):
    budgets = Budget.objects.all()
    return render(request, 'create_budget.html', {'budgets':budgets})

def abrirupdate(request, id):
    budget = Budget.objects.get(id=id)
    return render(request, 'updateT.html', {'budget':budget})

