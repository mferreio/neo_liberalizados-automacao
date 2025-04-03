import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Credenciais
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")  # Adicionada variável LOGIN_PASSWORD
LOGIN_USUARIO = os.getenv("LOGIN_USUARIO")  # Adicionada variável LOGIN_USUARIO, se necessário
REMETENTE_DE_EMAIL = os.getenv("REMETENTE_DE_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

# Dados de teste
NOME = os.getenv("NOME")
EMAIL = os.getenv("EMAIL")
EDITAR_PERFIL = os.getenv("EDITAR_PERFIL")
EDITAR_NOME = os.getenv("EDITAR_NOME")
EDITAR_EMAIL = os.getenv("EDITAR_EMAIL")
PESQUISAR_NOME_CADASTRADO = os.getenv("PESQUISAR_NOME_CADASTRADO")
EXCLUIR_NOME = os.getenv("EXCLUIR_NOME")
TIPO_DE_PERFIL = os.getenv("TIPO_DE_PERFIL")