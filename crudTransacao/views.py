from django.shortcuts import render
from django.http import HttpResponse
from .models import Transacao
# Create your views here.

def vcreate(request):
    return ''

def vdelete(request):
    return ''

def vupdate(request):
    return ''


def vread(request):
    transacaos = Transacao.objects.all()
    return render(request, 'readT.html', {
        "transacaos": transacaos
    })


