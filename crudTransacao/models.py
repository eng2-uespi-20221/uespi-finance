from django.db import models

class Transacao(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=60)
    tipo_transacao = models.BooleanField(default=1)
    valor = models.FloatField()
    


