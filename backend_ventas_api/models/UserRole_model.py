from django.db import models

# Importaciones diferidas para evitar importaciones circulares
def get_user_model():
    from .user_model import User
    return User

def get_role_model():
    from .role_model import Role
    return Role

class UserRole(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_roles')
    role = models.ForeignKey(get_role_model(), on_delete=models.CASCADE, related_name='role_users')

    class Meta:
        unique_together = ('user', 'role')  # Asegura que un usuario no tenga el mismo rol más de una vez
        constraints = [
            models.UniqueConstraint(fields=['user', 'role'], name='unique_user_role')
        ]
        db_table = 'user_role'
        
    def __str__(self):
        return f"{self.user} - {self.role}"
