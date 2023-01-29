from .models import Transacao
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

def vdelete(request, id):
    transacao = get_object_or_404(Transacao, id=id)
    transacao.delete()
    return redirect('vcreate')

def abrirupdate(request, id):
    transacao = Transacao.objects.get(id=id)
    return render(request, 'updateT.html', {'transacao':transacao})
    

def vupdate(request, id):

    #recebe do template updateT os dados inseridos pelo usuario
    vdescricao = request.POST.get('descricao')
    vtipo_transacao = request.POST.get('tipo_transacao')
    vvalor = request.POST.get('valor')
    valor = str(vvalor).replace(',','.')
    #obtem id do registro
    transacao = Transacao.objects.get(id=id)
    
    transacao.descricao = vdescricao
    transacao.tipo_transacao = vtipo_transacao
    transacao.valor = valor
    transacao.save() 

    return redirect(vread)

@login_required(login_url='login')
def vread(request):

    transacaos = Transacao.objects.filter(user_id=request.user.id)
    print(transacaos)
    # print(request.user.id)
    return render(request, 'readT.html', {
        "transacaos": transacaos
    })

def abrircreate(request):
    transacaos = Transacao.objects.all()
    return render(request, 'createT.html', {'transacaos':transacaos})


def vcreate(request):
    # obtem o dado nome do form e armazena na var vnome
    if (request.method == 'POST'):
        vdata = request.POST.get('data')
        vdescricao = request.POST.get('descricao')
        vtipo_transacao = request.POST.get('tipo_transacao')
        vvalor = request.POST.get('valor')
        valorformatado = str(vvalor).replace(',','.')
        # cria um registro no bd no campo nome passando a ver vnome
        Transacao.objects.create(data=vdata, descricao=vdescricao, tipo_transacao=vtipo_transacao, valor=valorformatado, user=request.user)
        # envia lista atualizada do bd para o index.html
        #transacaos = Transacao.objects.all()
        # recarrega a página index.html com os dados atualizados
    return redirect(vread)







