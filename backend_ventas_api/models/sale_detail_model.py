from django.db import models

def get_sale_model():
    from .sale_model import Sale
    return Sale

def get_product_model():
    from .product_model import Product
    return Product

class SaleDetail(models.Model):
    id_product = models.ForeignKey(get_product_model(), on_delete=models.CASCADE, related_name='sale_details')
    quantity = models.IntegerField()
     
    class Meta:
        db_table = 'sale_details'

    def __str__(self):
        return f"{self.id_product} ({self.quantity})"
