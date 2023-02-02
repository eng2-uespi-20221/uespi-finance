from django.contrib.auth.models import User
from django.db import models

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    balance = models.DecimalField(default=0,decimal_places=2,max_digits=20)
    income = models.DecimalField(default=0,decimal_places=2,max_digits=20)
    expense = models.DecimalField(default=0,decimal_places=2,max_digits=20)
    
