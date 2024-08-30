from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import *

#rutas de la api
router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'document-types', DocumentTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]