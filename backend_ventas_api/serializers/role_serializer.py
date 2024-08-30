from rest_framework import serializers
from backend_ventas_api.models import Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'