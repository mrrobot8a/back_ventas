from rest_framework import serializers
from backend_ventas_api.models import Sale, SaleDetail, Product
from backend_ventas_api.serializers.sale_detail_serializer import SaleDetailSerializer

class SaleSerializer(serializers.ModelSerializer):
    sale_details = SaleDetailSerializer(many=True)

    class Meta:
        model = Sale
        fields = '__all__'

    def validate(self, data):
        """
        Validar los detalles de la venta para asegurar que el stock es suficiente.
        """
        sale_details_data = data.get('sale_details', [])
        for detail in sale_details_data:
            product = detail['id_product']
            if product.stock_units < detail['quantity']:
                raise serializers.ValidationError(f"Stock insuficiente para el producto {product.name} (ID: {product.id_product}).")
        return data

    def create(self, validated_data):
        sale_details_data = validated_data.pop('sale_details')
        sale = Sale.objects.create(**validated_data)

        for detail_data in sale_details_data:
            product = detail_data['id_product']
            quantity = detail_data['quantity']

            if product.stock_units < quantity:
                raise serializers.ValidationError(f"Stock insuficiente para el producto {product.name} (ID: {product.id_product}).")
            
            product.stock_units -= quantity
            product.save()

            SaleDetail.objects.create(id_sale=sale, **detail_data)

        sale.total = sum(detail['id_product'].unit_price * detail['quantity'] for detail in sale_details_data)
        sale.save()

        return sale
