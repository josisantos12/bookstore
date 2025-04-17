# Use uma imagem base com Python
FROM python:3.10-slim-bullseye

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Instala dependências do sistema necessárias para compilar pacotes como mysqlclient
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    libpq-dev \
    gcc \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Atualiza o pip
RUN pip install --upgrade pip

# Copia o arquivo de dependências e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos da aplicação
COPY . .

# Expõe a porta que sua aplicação irá rodar (no exemplo, 8000)
EXPOSE 8000

# Comando para iniciar o servidor de desenvolvimento do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]