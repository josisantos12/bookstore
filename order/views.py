from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Order  # Certifique-se de que o modelo Order existe
from .serializers import OrderSerializer  # Certifique-se de que o serializer existe

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# Create your views here.
