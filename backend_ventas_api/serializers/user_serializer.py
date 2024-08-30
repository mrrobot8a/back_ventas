from rest_framework import serializers
from backend_ventas_api.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id_usuario', 'name_user', 'email']  # Incluye los campos que deseas en la respuesta

def validate_email(self, value):
        # Verifica que el email no exista en la base de datos
        if Customer.objects.filter(email=value).exists():
            raise serializers.ValidationError('El email ya existe en la base de datos')
        return value