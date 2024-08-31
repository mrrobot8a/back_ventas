# backend_ventas_api/views.py
from rest_framework import viewsets
from backend_ventas_api.models import Customer, DocumentType, User, Role, Supplier , Product , Sale
from backend_ventas_api.serializers.customer_serializer import CustomerSerializer
from backend_ventas_api.serializers.document_type_serializer import DocumentTypeSerializer
from backend_ventas_api.serializers.user_serializer import UserSerializer
from backend_ventas_api.serializers.role_serializer import RoleSerializer
from backend_ventas_api.serializers.supplier_serializer import SupplierSerializer
from backend_ventas_api.serializers.product_serializer import ProductSerializer
from backend_ventas_api.serializers.sale_serializer import SaleSerializer
from backend_ventas_api.serializers.MyTokenObtainPairSerializer import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class DocumentTypeViewSet(viewsets.ModelViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    
class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    
class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer    
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer    
    

