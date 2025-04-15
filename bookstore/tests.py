from rest_framework.test import APITestCase
from rest_framework import status
from .models import MeuModelo

class MeuModeloAPITestCase(APITestCase):
    def setUp(self):
        # Criando objetos para teste
        MeuModelo.objects.create(nome="Teste 1", descricao="Descrição do Teste 1")
        MeuModelo.objects.create(nome="Teste 2", descricao="Descrição do Teste 2")

    def test_lista_meumodelo(self):
        # Testando a listagem de objetos
        response = self.client.get('/meumodelo/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_criar_meumodelo(self):
        # Testando a criação de um novo objeto
        data = {"nome": "Novo Modelo", "descricao": "Descrição do Novo Modelo"}
        response = self.client.post('/meumodelo/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)