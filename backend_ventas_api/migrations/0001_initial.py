# Generated by Django 5.1 on 2024-08-30 00:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'document_type',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id_product', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock_units', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('name_rol', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id_supplier', models.AutoField(primary_key=True, serialize=False)),
                ('nit', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('contact_number', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'suppliers',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('name_user', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('document', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('profile_image_url', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('document_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_ventas_api.documenttype')),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='SaleDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_details', to='backend_ventas_api.product')),
            ],
            options={
                'db_table': 'sale_details',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id_sale', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('sale_date', models.DateField()),
                ('id_customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales', to='backend_ventas_api.customer')),
                ('id_sale_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_details', to='backend_ventas_api.saledetail')),
            ],
            options={
                'db_table': 'sales',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='id_supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='backend_ventas_api.supplier'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='id_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='suppliers', to='backend_ventas_api.user'),
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_users', to='backend_ventas_api.role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_roles', to='backend_ventas_api.user')),
            ],
            options={
                'db_table': 'user_role',
                'constraints': [models.UniqueConstraint(fields=('user', 'role'), name='unique_user_role')],
                'unique_together': {('user', 'role')},
            },
        ),
    ]
