from django.db import models
from .supplier_model import Supplier

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_units = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    id_supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
