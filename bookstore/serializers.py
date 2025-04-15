from rest_framework import serializers
from .models import MeuModelo

class MeuModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeuModelo
        fields = '__all__'