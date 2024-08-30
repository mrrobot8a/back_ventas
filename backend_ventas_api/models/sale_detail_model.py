from django.db import models
from .product_model import Product
from .sale_model import Sale

class SaleDetail(models.Model):
    id_sale_detail = models.AutoField(primary_key=True)
    id_sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='sale_details')
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sale_details')
    quantity = models.IntegerField()

    class Meta:
        db_table = 'sale_details'

    def __str__(self):
        return f"{self.id_product} ({self.quantity})"
