from django.db import models
from django.contrib.auth.models import User
from category.models import Category

class Transacao(models.Model):
    data = models.DateField(auto_now_add=True)
    descricao = models.CharField(null=True, max_length=60)
    valor = models.DecimalField(null=True, default=0,decimal_places=2,max_digits=20)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,default=1)
    categoria = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return self.categoria


