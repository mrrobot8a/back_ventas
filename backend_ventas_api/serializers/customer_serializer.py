# backend_ventas_api/serializers/customer_serializer.py
from rest_framework import serializers
from backend_ventas_api.models import Customer, DocumentType

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
