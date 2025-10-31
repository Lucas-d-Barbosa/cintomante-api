# Imagem base leve do Python
FROM python:3.12-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o requirements
COPY requirements.txt .

# Instala as dependências sem cache (pra reduzir tamanho)
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY . .

# Expõe a porta que o Heroku usa
EXPOSE 8000

# Define o comando de inicialização (usa o gunicorn)
CMD gunicorn cintomante_api.wsgi:application --bind 0.0.0.0:$PORT
