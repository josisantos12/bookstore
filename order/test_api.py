import requests

# URL do endpoint
url = "http://127.0.0.1:8000/api/token/"

# Dados da requisição
data = {
    "username": "seu_usuario"
}

# Enviando a requisição POST
response = requests.post(url, json=data)

# Exibindo a resposta
if response.status_code == 200:
    print("Token gerado:", response.json().get("token"))
else:
    print("Erro:", response.json())