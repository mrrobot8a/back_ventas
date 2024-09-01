from django.db import models
from .document_type_model import DocumentType
from .user_model import User


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    
    document = models.CharField(max_length=20)
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)  # Relación con DocumentType
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_image_url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True) 

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        db_table = 'customer'
