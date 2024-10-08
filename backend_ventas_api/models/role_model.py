from django.db import models


class Role(models.Model):
    id_rol = models.AutoField(primary_key=True)
    name_rol = models.CharField(max_length=50, unique=True)
    description  = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name_rol
    class Meta:
        db_table = 'role'