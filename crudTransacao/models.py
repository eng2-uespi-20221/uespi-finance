from django.db import models
import datetime

class Transacao(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField(default=datetime)
    descricao = models.CharField(null=True, max_length=60)
    tipo_transacao = models.BooleanField(null=True, default=1)
    valor = models.FloatField(null=True, default=0)



