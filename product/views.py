from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product  # Certifique-se de que o modelo Product existe
from .serializers import ProductSerializer  # Certifique-se de que o serializer existe

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Create your views here.
