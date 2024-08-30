# backend_ventas_api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, DocumentTypeViewSet, UserViewSet, RoleViewSet, SupplierViewSet, ProductViewSet, SaleViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'document-types', DocumentTypeViewSet)
router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'products', ProductViewSet)
router.register(r'sales', SaleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
