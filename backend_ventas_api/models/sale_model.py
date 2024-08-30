from django.db import models
from .customer_model import Customer

class Sale(models.Model):
    id_sale = models.AutoField(primary_key=True)
    id_customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name='sales')
    total = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sale_date = models.DateField()

    def __str__(self):
        return f"Sale {self.id_sale} by {self.id_customer}"

    class Meta:
        db_table = 'sales'
