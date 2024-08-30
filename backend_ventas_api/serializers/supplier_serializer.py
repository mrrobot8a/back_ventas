from rest_framework import serializers
from backend_ventas_api.models import Supplier

class SupplierSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Supplier
        fields = ['name', 'nit', 'city', 'email',
                    'contact_number',
                    'created_at', 'updated_at']