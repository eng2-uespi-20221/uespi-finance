from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=40)
    type_transaction = models.BooleanField(default=0)
    
