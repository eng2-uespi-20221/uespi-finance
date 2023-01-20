from django.db import models

# Create your models here.

class Category(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.TextField()
    tipoTransacao = models.BooleanField(default=0)
    