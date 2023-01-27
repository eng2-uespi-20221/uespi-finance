from django.db import models
import datetime

class Transacao(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField()
    descricao = models.CharField(null=True, max_length=60)
    tipo_transacao = models.CharField(null=True, max_length=60)
    valor = models.FloatField(null=True, default=0)



