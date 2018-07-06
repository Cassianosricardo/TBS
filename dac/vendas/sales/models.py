from django.db import models
from users.models import CustomUser
from datetime import date


class Sales(models.Model):
    # user # hora #lista de produtos(preço, quantidade, nome) total 
    user = models.ForeignKey(CustomUser, on_delete="")
    total = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    name = models.CharField(max_length=30)
    date = models.DateField(("Date"), default=date.today)  
