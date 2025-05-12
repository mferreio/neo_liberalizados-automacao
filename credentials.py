import os

from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Credenciais
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")  # Adicionada variável LOGIN_PASSWORD
LOGIN_USUARIO = os.getenv(
    "LOGIN_USUARIO"
)  # Adicionada variável LOGIN_USUARIO, se necessário
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

# envio de email
REMETENTE_DE_EMAIL = os.getenv("REMETENTE_DE_EMAIL")
DESTINATARIO = os.getenv("DESTINATARIO")
DESTINATARIO_EXTRA = os.getenv("DESTINATARIO_EXTRA")

DATA_FIM_DIRETRIZ = os.getenv("DATA_FIM_DIRETRIZ")

# Dados para consulta de produtos
CONS_PROD_ANO = os.getenv("CONS_PROD_ANO")
CONS_PROD_MES = os.getenv("CONS_PROD_MES")
CONS_PROD_PERFIL = os.getenv("CONS_PROD_PERFIL")
CONS_PROD_SUBMERCADO = os.getenv("CONS_PROD_SUBMERCADO")
CONS_PROD_TIPO_DE_PROD = os.getenv("CONS_PROD_TIPO_DE_PROD")

# Dados para criar um novo produto
MES_NOVO_PRODUTO = os.getenv("MES_NOVO_PRODUTO")
ANO_NOVO_PRODUTO = os.getenv("ANO_NOVO_PRODUTO")
PERFIL_NOVO_PRODUTO = os.getenv("PERFIL_NOVO_PRODUTO")
SUBMERCADO_NOVO_PRODUTO = os.getenv("SUBMERCADO_NOVO_PRODUTO")
TIPOPRODUTO_NOVO_PRODUTO = os.getenv("TIPOPRODUTO_NOVO_PRODUTO")

# Dados para cadastro de diretriz I-REC
DESCRICAO_DIRETRIZ_IREC = os.getenv("DESCRICAO_DIRETRIZ_IREC")
PRECO_DIRETRIZ_IREC = os.getenv("PRECO_DIRETRIZ_IREC")
DATA_INICIO_DIRETRIZ_IREC = os.getenv("DATA_INICIO_DIRETRIZ_IREC")
DATA_FIM_DIRETRIZ_IREC = os.getenv("DATA_FIM_DIRETRIZ_IREC")
