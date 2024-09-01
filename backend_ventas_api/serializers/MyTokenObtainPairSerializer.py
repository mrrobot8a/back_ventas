from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from backend_ventas_api.models import UserRole  # Importa la relación UserRole

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Agrega campos personalizados al token
        token['name_user'] = user.name_user
        token['email'] = user.email

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Obtener roles del usuario
        roles = UserRole.objects.filter(user=self.user).select_related('role')
        roles_list = [role.role.name_rol for role in roles]

        # Agrega la información del usuario y los roles a la respuesta
        data['user'] = {
            'id_usuario': self.user.id_usuario,
            'name_user': self.user.name_user,
            'email': self.user.email,
            'creation_date': self.user.creation_date,
            'is_staff': self.user.is_staff,
            'is_superuser': self.user.is_superuser,
            'is_active': self.user.is_active,
            'roles': roles_list,  # Aquí se agregan los roles
        }

        return data
