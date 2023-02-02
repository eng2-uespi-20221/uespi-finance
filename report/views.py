from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from crudTransacao.models import Transacao
from category.models import Category as Categoria
from django.urls import reverse_lazy, reverse

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Create your views here.

def relatorio_pdf(request):
    transacao = Transacao.objects.filter(user=request.user)
    categoria = Categoria.objects.filter(user=request.user)
    saldo = 0
    lines = []

    lines.append(f'NOME DO CLIENTE:  {request.user.first_name} {request.user.last_name}')
    lines.append('------------------------------------------------------------------------------')
    for trans in transacao:
        if (trans.categoria.type_transaction):
            trans.valor = -trans.valor
        
        lines.append(f'{trans.descricao}; VALOR R$ {trans.valor}; DATA: {trans.data}')
        
        saldo += trans.valor
    

    lines.append('------------------------------------------------------------------------------')
    lines.append(f'SALDO: R$ {saldo}')
    if (saldo > 0):
        lines.append('PARABÉNS, DE POUCO EM POUCO, SALVAMOS O BOLSO!')
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    texto = c.beginText()
    texto.setTextOrigin(inch, inch)
    texto.setFont('Helvetica', 12)
    for line in lines:
        texto.textLine(str(line))
    c.drawText(texto)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='Relatório_pdf.pdf')
