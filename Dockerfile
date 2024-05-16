# Use uma imagem base do Python, especificando a versão desejada
FROM python:3.11-alpine

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do aplicativo usando o pip
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código fonte do aplicativo para o diretório de trabalho
COPY . .

# Exponha a porta em que o aplicativo será executado (se necessário)
EXPOSE 8080

# Defina o comando padrão para ser executado quando o contêiner for iniciado
CMD ["python", "run.py"]
