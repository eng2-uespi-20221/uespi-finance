from django.shortcuts import render
from django.http import HttpResponse  # 003-srsa-Importar biblioteca

# Create your views here.
# 002-srsa-Criar uma view de teste


def teste(request):
    return HttpResponse("teste de retorno http")


def budget(request):
    return render(request, 'budget.html',)
