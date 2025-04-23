from rest_framework import serializers
from .models import MeuModelo

class MeuModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeuModelo
        fields = '__all__'  # Inclui todos os campos do modelo
        # fields = ['id', 'titulo', 'autor', 'preco']  # Ou especifique os campos manualmente