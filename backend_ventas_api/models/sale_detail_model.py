from django.db import models
from .product_model import Product

class SaleDetail(models.Model):
    id_sale_detail = models.AutoField(primary_key=True)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sale_details')
    quantity = models.IntegerField()
         
    class Meta:
        db_table = 'sale_details'

    def __str__(self):
        return f"{self.id_product} ({self.quantity})"

    def save(self, *args, **kwargs):
        # Descuenta del stock antes de guardar
        if self.id_product.stock_units >= self.quantity:
            self.id_product.stock_units -= self.quantity
            self.id_product.save()
        else:
            raise ValueError("No hay suficiente stock disponible para completar la venta.")
        
        super().save(*args, **kwargs)  
