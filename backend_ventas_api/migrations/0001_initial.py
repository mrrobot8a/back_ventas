# Generated by Django 5.1 on 2024-08-31 17:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('name_user', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
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
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('document', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('profile_image_url', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to=settings.AUTH_USER_MODEL)),
                ('document_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_ventas_api.documenttype')),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id_sale', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('sale_date', models.DateField()),
                ('id_customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales', to='backend_ventas_api.customer')),
            ],
            options={
                'db_table': 'sales',
            },
        ),
        migrations.CreateModel(
            name='SaleDetail',
            fields=[
                ('id_sale_detail', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_details', to='backend_ventas_api.product')),
                ('id_sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_details', to='backend_ventas_api.sale')),
            ],
            options={
                'db_table': 'sale_details',
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
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='suppliers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'suppliers',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='id_supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='backend_ventas_api.supplier'),
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_users', to='backend_ventas_api.role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_roles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_role',
                'constraints': [models.UniqueConstraint(fields=('user', 'role'), name='unique_user_role')],
            },
        ),
    ]
