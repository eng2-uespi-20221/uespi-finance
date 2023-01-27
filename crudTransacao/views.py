from .models import Transacao
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

def vdelete(request, id):
    transacaos = get_object_or_404(Transacao, id=id)
    transacaos.delete()
    return redirect('vcreate')

def vupdate(request):
    return render(request, 'updateT.html')


def vread(request):
    transacaos = Transacao.objects.all()
    return render(request, 'readT.html', {
        "transacaos": transacaos
    })

def abrircreate(request):
    transacaos = Transacao.objects.all()
    return render(request, 'createT.html', {'transacaos':transacaos})


def vcreate(request):
    # obtem o dado nome do form e armazena na var vnome
    vdata = request.POST.get('data')
    vdescricao = request.POST.get('descricao')
    vtipo_transacao = request.POST.get('tipo_transacao')
    vvalor = request.POST.get('valor')
    # cria um registro no bd no campo nome passando a ver vnome
    Transacao.objects.create(data=vdata, descricao=vdescricao, tipo_transacao=vtipo_transacao, valor=vvalor)
    # envia lista atualizada do bd para o index.html
    transacaos = Transacao.objects.all()
    # recarrega a página index.html com os dados atualizados
    return render(request, 'readT.html', {'transacaos': transacaos})







