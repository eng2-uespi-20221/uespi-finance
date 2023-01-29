from django.db import models

class Transacao(models.Model):
    data = models.DateField(auto_now_add=True)
    descricao = models.CharField(null=True, max_length=60)
    tipo_transacao = models.CharField(null=True, max_length=60)
    valor = models.FloatField(null=True, default=0)



