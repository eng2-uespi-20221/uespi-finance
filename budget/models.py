from django.db import models

# APP BUDGET
class Budget(models.Model):
    id = models.IntegerField(primary_key=True)
    dataCriacao = models.DateField()
    orcamento = models.CharField(max_length=60)