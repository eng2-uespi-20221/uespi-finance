from .models import Transacao
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

def vdelete(request, id):
    transacao = get_object_or_404(Transacao, id=id)
    transacao.delete()
    return redirect('transacao')

def abrirupdate(request, id):
    transacao = Transacao.objects.get(id=id)
    return render(request, 'updateT.html', {'transacao':transacao})
    

def vupdate(request, id):
    #recebe do template updateT os dados inseridos pelo usuario
    vdescricao = request.POST.get('descricao')
    vtipo_transacao = request.POST.get('tipo_transacao')
    vvalor = request.POST.get('valor')
    valor = str(vvalor).replace(',','.')
    #se os valores obtidos forem nulo
    if not vdescricao or not vtipo_transacao or not valor: 
        #recupera o id da transacao
        transacao = Transacao.objects.get(id=id)        
        #retorna para o formulario updateT passando o id da transacao         
        return render(request, 'updateT.html', {'transacao':transacao})

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
    #print(request.user.id)
    return render(request, 'readT.html', {
        "transacaos": transacaos
    })

def abrircreate(request):
    return render(request, 'createT.html')


def vcreate(request):
    # obtem o dado nome do form e armazena na var vnome
    if (request.method == 'POST'):
        vdata = request.POST.get('data')
        vdescricao = request.POST.get('descricao')
        vtipo_transacao = request.POST.get('tipo_transacao')
        vvalor = request.POST.get('valor')
        valorformatado = str(vvalor).replace(',','.')
        #verifica se os campos estão vazios
        if not vdescricao or not vtipo_transacao or not vvalor:
            
            return render(request, 'createT.html')

    Transacao.objects.create(data=vdata, descricao=vdescricao, tipo_transacao=vtipo_transacao, valor=valorformatado, user=request.user)
        
    return redirect(vread)

  









