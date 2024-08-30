from django.contrib import admin
from .models.customer_model import Customer
from .models.document_type_model import DocumentType
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

# Register your models here.
admin.site.register(Customer)
admin.site.register(DocumentType)
admin.site.register(Role)
#admin.site.register(User)
admin.site.register(UserRole)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(SaleDetail)
admin.site.site_title = 'Ventas App'
admin.site.site_header = 'Ventas App'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('name_user', 'email')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('name_user', 'email', 'password', 'is_active', 'is_staff', 'is_superuser')

class UserAdmin(BaseUserAdmin):
    # Forms to add and change user instances
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    # The fields to be used in displaying the User model.
    list_display = ('name_user', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('name_user', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name_user', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('name_user', 'email')
    ordering = ('name_user',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
