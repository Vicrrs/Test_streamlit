FROM python:3.11-slim-buster

# Definir o diretório de trabalho do container
WORKDIR /code

# Copiar apenas os arquivos necessários para a instalação das dependências
COPY pyproject.toml poetry.lock* /code/

# Instalar o poetry
RUN pip install poetry

# Configurando o poetry para não criar um ambiente virtual dentro do Docker
RUN poetry config virtualenvs.create false

# Instalar as dependências do projeto usando poetry
RUN poetry install --no-dev

# Copiar o resto do código do projeto para o container
COPY . /code

# Comando pra rodar a aplicação
CMD [ "streamlit", "run", "Dashboard.py" ]
