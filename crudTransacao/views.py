from .models import Transacao, Category
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
    vcategoria = request.POST.get('categoria')
    valor = str(vvalor).replace(',','.')
    #se os valores obtidos forem nulo
    if not vdescricao or not valor or not vcategoria: 
        #recupera o id da transacao
        transacao = Transacao.objects.get(id=id)        
        #retorna para o formulario updateT passando o id da transacao         
        return render(request, 'updateT.html', {'transacao':transacao})
    else:
        #obtem id do registro
        category  = Category.objects.get_or_create(name=vcategoria)[0]
        transacao = Transacao.objects.get(id=id)
        
        transacao.descricao = vdescricao
        transacao.tipo_transacao = vtipo_transacao

        transacao.categoria=category
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
    category = Category.objects.all()
    return render(request, 'createT.html', {'categories': category})


def vcreate(request):
    # Get data from the form
    if (request.method == 'POST'):
        vdata = request.POST.get('data')
        vdescricao = request.POST.get('descricao')
        vtipo_transacao = request.POST.get('tipo_transacao')
        vcategoria = request.POST.get('categoria')
        vvalor = request.POST.get('valor')
        valorformatado = str(vvalor).replace(',','.')

        
        # Check if all required fields are filled
        if not vdescricao or not vvalor or not vcategoria:
            return render(request, 'createT.html')

        else:
            category, created = Category.objects.get_or_create(id=vcategoria)
            Transacao.objects.create(data=vdata, descricao=vdescricao, categoria=category, valor=valorformatado, user=request.user)

    return redirect(vread)









