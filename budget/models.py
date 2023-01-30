from django.db import models
from django.contrib.auth.models import User

# APP BUDGET
class Budget(models.Model):    
    orcamento = models.CharField(max_length=60)
    valor_limite = models.DecimalField(default=0,decimal_places=2,max_digits=20)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,default=1)
