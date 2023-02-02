from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, reverse
from .models import Transacao
from .models import Categoria
from django.urls import reverse_lazy
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Create your views here.

def relatorio_pdf(request):
    transacao = Transacao.objects.all()
    categoria = Categoria.objects.all()
    saldo = 0
    lines = []
    for trans in transacao:
        if (trans. == 'Despesa'):
            trans.valor = -trans.valor
        lines.append('NOME DO CLIENTE')
        lines.append(trans.data)
        lines.append(trans.descricao)
        lines.append(trans.valor)
        saldo += trans.valor
        lines.append('--------------------------')
    if (saldo > 0):
        lines.append('PARABÉNS, DE POUCO EM POUCO, SALVAMOS O BOLSO!')
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    texto = c.beginText()
    texto.setTextOrigin(inch, inch)
    texto.setFont('Helvetica', 12)
    for line in lines:
        texto.textLine(line)
    c.drawText(texto)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='Relatório_pdf.pdf')
