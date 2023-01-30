from django.db import models
from django.contrib.auth.models import User

# APP BUDGET
class Budget(models.Model):    
    orcamento = models.CharField(max_length=60)
    valor_limite = models.FloatField(default=0)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,default=1)
