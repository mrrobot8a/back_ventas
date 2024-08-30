# backend_ventas_api/serializers/user_serializer.py
from rest_framework import serializers
from backend_ventas_api.models import User
from backend_ventas_api.models import Role  # Importa el modelo Role
from backend_ventas_api.serializers.role_serializer import RoleSerializer

class UserSerializer(serializers.ModelSerializer):
    roles = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def get_roles(self, obj):
        # Obtiene los roles asociados al usuario a través de UserRole
        roles = obj.user_roles.all().values_list('role', flat=True)
        return RoleSerializer(Role.objects.filter(id_rol__in=roles), many=True).data
