from django.contrib import admin
from .models.customer_model import Customer
from .models.document_type_model import DocumentType

# Register your models here.
admin.site.register(Customer)
admin.site.register(DocumentType)
admin.site.site_title = 'Ventas App'
admin.site.site_header = 'Ventas App'