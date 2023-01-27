from django.db import models
import datetime

class Transacao(models.Model):
<<<<<<< HEAD
    id = models.AutoField(primary_key=True)
    data = models.DateField(default=datetime)
    descricao = models.CharField(null=True, max_length=60)
    tipo_transacao = models.BooleanField(null=True, default=1)
    valor = models.FloatField(null=True, default=0)
=======
    data = models.DateField()
    descricao = models.CharField(max_length=60)
    tipo_transacao = models.BooleanField(default=1)
    valor = models.FloatField()
>>>>>>> 74e420318f0a00d314ddeb56a37c66ae0fb83bfb



