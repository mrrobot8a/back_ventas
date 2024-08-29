# backend_ventas_api/serializers/customer_serializer.py
from rest_framework import serializers
from backend_ventas_api.models import Customer, DocumentType

class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = '__all__'