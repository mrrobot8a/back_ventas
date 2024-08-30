from django.db import models


class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    name_user = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=50, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    # roles = models.ManyToManyField('Role', through='UserRole', related_name='users')

    def __str__(self):
        return self.name_user
    class Meta:
        db_table = 'user'