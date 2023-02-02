from .models import Transacao, Category
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from authentication.models import Account
from decimal import Decimal

# Create your views here.

def vdelete(request, id):
    transacao = get_object_or_404(Transacao, id=id)

    if transacao.categoria.type_transaction: # expense
        request.user.account.balance += transacao.valor
        request.user.account.expense -= transacao.valor
    else: # income
        request.user.account.balance -= transacao.valor
        request.user.account.income -= transacao.valor
    request.user.account.save()
    transacao.delete()
    return redirect('transacao')

def abrirupdate(request, id):
    transacao = Transacao.objects.get(id=id)
    category = Category.objects.filter(user_id=request.user.id)
    return render(request, 'updateT.html', {'transacao':transacao, 'categories': category } )
    

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
        category = Category.objects.filter(user_id=request.user.id)   
        #retorna para o formulario updateT passando o id da transacao         
        return render(request, 'updateT.html', {'transacao':transacao, 'categories': category})
    else:
        #obtem id do registro
        category  = Category.objects.get_or_create(name=vcategoria)[0]
        transacao = Transacao.objects.get(id=id)

        # Se tiver alteração de valor ou categoria da transação
        if Decimal(transacao.valor) != Decimal(valor) or transacao.categoria != category: 
            # Era receita e se tornou despesa
            if transacao.categoria.type_transaction != category.type_transaction and category.type_transaction: #expense
                request.user.account.balance -= transacao.valor + valor
                request.user.account.income -= transacao.valor + valor
                request.user.account.expense += valor
            
            # Era despesa se tornou receita
            elif transacao.categoria.type_transaction != category.type_transaction and not category.type_transaction: # income
                request.user.account.balance += transacao.valor + valor
                request.user.account.income += valor
                request.user.account.expense -= transacao.valor

            # mantem mesmo tipo
            else:
                diferenca = Decimal(transacao.valor) - Decimal(valor)

                if transacao.categoria.type_transaction: # expense
                    request.user.account.balance += diferenca
                    request.user.account.expense -= diferenca
                else: # income
                    request.user.account.balance -= diferenca
                    request.user.account.income -= diferenca
            request.user.account.save()
        
        transacao.descricao = vdescricao
        transacao.tipo_transacao = vtipo_transacao

        transacao.categoria=category
        transacao.valor = valor
        transacao.save() 

        return redirect(vread)

@login_required(login_url='login')
def vread(request):
    try:
        account = request.user.account
    except:
        account = Account.objects.create(user=request.user)

    transacaos = Transacao.objects.filter(user_id=request.user.id)
    #print(request.user.id)
    return render(request, 'readT.html', {
        "transacaos": transacaos,
        "account": account
    })

def abrircreate(request):
    category = Category.objects.filter(user_id=request.user.id)
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
        valorformatado = Decimal(valorformatado)

        # Check if all required fields are filled
        if not vdescricao or not vvalor or not vcategoria:
            return render(request, 'createT.html')

        category, created = Category.objects.get_or_create(id=vcategoria)

        if category.type_transaction: # expense
            request.user.account.balance -= valorformatado
            request.user.account.expense += valorformatado
        else: # income
            request.user.account.balance += valorformatado
            request.user.account.income += valorformatado
        request.user.account.save()

        Transacao.objects.create(data=vdata, descricao=vdescricao, categoria=category, valor=valorformatado, user=request.user)

    return redirect(vread)









