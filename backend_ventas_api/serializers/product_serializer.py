# backend_ventas_api/serializers/product_serializer.py
from rest_framework import serializers
from backend_ventas_api.models import Product
from backend_ventas_api.serializers.supplier_serializer import SupplierSerializer

class ProductSerializer(serializers.ModelSerializer):
    # Campos calculados para obtener el nombre y NIT del proveedor
    supplier_name = serializers.SerializerMethodField()
    supplier_nit = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'  # Incluye todos los campos del modelo Product en la respuesta

    def get_supplier_name(self, obj):
        # Obtiene el nombre del proveedor asociado a través del campo id_supplier
        if obj.id_supplier:
            return obj.id_supplier.name
        return None

    def get_supplier_nit(self, obj):
        # Obtiene el NIT del proveedor asociado a través del campo id_supplier
        if obj.id_supplier:
            return obj.id_supplier.nit
        return None
