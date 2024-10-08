from django.db import models
from .user_model import User 

class Supplier(models.Model):
    id_supplier = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='suppliers')
    nit = models.CharField(max_length=20,unique=True)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'suppliers'

 