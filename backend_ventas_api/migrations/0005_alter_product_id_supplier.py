# Generated by Django 5.1 on 2024-08-31 23:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_ventas_api', '0004_alter_product_id_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id_supplier',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backend_ventas_api.supplier'),
        ),
    ]
