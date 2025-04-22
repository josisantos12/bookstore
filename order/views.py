from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Order  # Certifique-se de que o modelo Order existe
from .serializers import OrderSerializer  # Certifique-se de que o serializer existe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.response import Response

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
 

class MinhaViewProtegida(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"mensagem": "Bem-vindo! Você está autenticado."})


class GerarTokenAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        user = User.objects.get(username=username)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
# Create your views here.
