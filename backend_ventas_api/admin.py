from django.contrib import admin
from .models.customer_model import Customer
from .models.document_type_model import DocumentType
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(DocumentType)
admin.site.register(Role)
admin.site.register(User)
admin.site.register(UserRole)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(SaleDetail)
admin.site.site_title = 'Ventas App'
admin.site.site_header = 'Ventas App'