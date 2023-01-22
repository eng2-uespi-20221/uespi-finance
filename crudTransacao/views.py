from .models import Transacao
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from .forms import PostForm
# Create your views here.

def vdelete(request, id):
    transacao = Transacao.objects.get(id=id)
    transacao.delete()
    return  render(request, 'transacao')

def vupdate(request):
    return render(request, 'updateT.html')


def vread(request):
    transacaos = Transacao.objects.all()
    return render(request, 'readT.html', {
        "transacaos": transacaos
    })

@login_required
def vcreate(request):
    form = PostForm()

    if(request.method == 'POST'):

        form = PostForm(request.POST)

        if(form.is_valid()):
            post_data = form.cleaned_data['data']
            post_descricao= form.cleaned_data['descricao']
            post_valor = form.cleaned_data['valor']
            post_tipo_transacao = form.cleaned_data['tipo_transacao']

            new_post = Transacao(data=post_data, descricao=post_descricao, valor=post_valor, tipo_transacao = post_tipo_transacao)
            new_post.save()

            return redirect('transacao')

    elif(request.method == 'GET'):
        return render(request, 'add_post.html', {'form': form})




