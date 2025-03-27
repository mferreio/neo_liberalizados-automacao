import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Credenciais sensíveis
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")
LOGIN_USUARIO = os.getenv("LOGIN_USUARIO")
REMETENTE_DE_EMAIL = os.getenv("REMETENTE_DE_EMAIL")

# Dados de teste
NOME = os.getenv("NOME")
EMAIL = os.getenv("EMAIL")
EDITAR_PERFIL = os.getenv("EDITAR_PERFIL")
EDITAR_NOME = os.getenv("EDITAR_NOME")
EDITAR_EMAIL = os.getenv("EDITAR_EMAIL")
PESQUISAR_NOME_CADASTRADO = os.getenv("PESQUISAR_NOME_CADASTRADO")
EXCLUIR_NOME = os.getenv("EXCLUIR_NOME")
TIPO_DE_PERFIL = os.getenv("TIPO_DE_PERFIL")