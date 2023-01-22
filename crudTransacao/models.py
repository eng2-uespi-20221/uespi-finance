from django.db import models

class Transacao(models.Model):
    id = models.IntegerField(primary_key=True)
    data = models.DateField()
    descricao = models.CharField(max_length=60)
    tipo_transacao = models.BooleanField(default=1)
    valor = models.FloatField()


    


