from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=40)
    type_transaction = models.BooleanField(default=0)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,default=1)
    
    
