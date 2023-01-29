from django.db import models

# APP BUDGET
class Budget(models.Model):    
    orcamento = models.CharField(max_length=60)
    valor_limite = models.FloatField(default=0)