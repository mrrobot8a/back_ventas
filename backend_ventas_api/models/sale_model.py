from django.db import models
from .customer_model import Customer
from .sale_detail_model import SaleDetail

class Sale(models.Model):
    id_sale = models.AutoField(primary_key=True)
    id_customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name='sales')
    id_sale_detail = models.ForeignKey(SaleDetail, on_delete=models.CASCADE, related_name='sales_details')
    total = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)  # Se puede calcular automáticamente
    sale_date = models.DateField()

    def __str__(self):
        return f"Sale {self.id_sale} by {self.id_customer}"

    def calculate_total(self):
        total = sum(detail.quantity * detail.id_product.unit_price for detail in self.sales_details.all())
        self.total = total
        self.save()
        return total

    class Meta:
        db_table = 'sales'
