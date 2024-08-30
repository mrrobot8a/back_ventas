from rest_framework import serializers
from backend_ventas_api.models import SaleDetail

class SaleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleDetail
        fields = '__all__'
        extra_kwargs = {
            'id_sale': {'required': False}  
        }

    def validate(self, data):
        product = data['id_product']
        if product.stock_units < data['quantity']:
            raise serializers.ValidationError("No hay suficiente stock disponible.")
        return data
