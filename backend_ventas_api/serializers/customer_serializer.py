# backend_ventas_api/serializers/customer_serializer.py
from rest_framework import serializers
from backend_ventas_api.models import Customer
from backend_ventas_api.serializers.user_serializer import UserSerializer
from backend_ventas_api.serializers.document_type_serializer import DocumentTypeSerializer

class CustomerSerializer(serializers.ModelSerializer):
  
    

    class Meta:
        model = Customer
        fields = '__all__'


    
    
