from django.db import models
from categories.models import Categorie

# Create your models here.

class Product(models.Model):
    # nome # cod # quantidade # categoria
    name = models.CharField(max_length=30, unique=True)
    quantity = models.IntegerField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    vendable = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)