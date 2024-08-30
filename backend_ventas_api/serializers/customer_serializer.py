# backend_ventas_api/serializers/customer_serializer.py
from rest_framework import serializers
from backend_ventas_api.models import Customer
from backend_ventas_api.serializers.user_serializer import UserSerializer
from backend_ventas_api.serializers.document_type_serializer import DocumentTypeSerializer

class CustomerSerializer(serializers.ModelSerializer):
  
    

    # Campo calculado
    type_document = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = '__all__'

    def get_type_document(self, obj):
        # Obtiene el nombre del tipo de documento asociado
        return obj.document_type.name if obj.document_type else None
    
    def get_email(self, obj):
        # Obtiene el email del usuario asociado
        return obj.user_id.email if obj.user_id else None
    
    
