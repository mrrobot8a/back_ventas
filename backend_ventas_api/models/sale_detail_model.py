from django.db import models

def get_sale_model():
    from .sale_model import Sale
    return Sale

def get_product_model():
    from .product_model import Product
    return Product

class SaleDetail(models.Model):
    id_sale = models.ForeignKey(get_sale_model(), on_delete=models.CASCADE, related_name='sale_details')
    id_product = models.ForeignKey(get_product_model(), on_delete=models.CASCADE, related_name='product_details')
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('id_sale', 'id_product')  # Ensures that a product is only listed once per sale
        constraints = [
            models.UniqueConstraint(fields=['id_sale', 'id_product'], name='unique_product_sale')
        ]
        db_table = 'sale_details'

    def __str__(self):
        return f"{self.id_product} ({self.quantity}) in Sale {self.id_sale}"
