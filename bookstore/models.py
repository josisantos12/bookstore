from django.db import models

class MeuModelo(models.Model):
    nome = models.CharField(max_length=100)  # Campo de texto com limite de 100 caracteres
    descricao = models.TextField(blank=True, null=True)  # Campo de texto mais longo
    data_criacao = models.DateTimeField(auto_now_add=True)  # Data e hora de criação

    def __str__(self):
        return self.nome  # Representação do objeto como string

    class Meta:
        ordering = ['id']  # Substitua 'id' pelo campo desejado