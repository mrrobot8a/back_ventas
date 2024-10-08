# Generated by Django 5.1 on 2024-08-31 23:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_ventas_api', '0003_alter_supplier_nit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id_supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='backend_ventas_api.supplier', unique=True),
        ),
    ]
