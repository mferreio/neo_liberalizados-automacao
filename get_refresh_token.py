import os
import requests
from urllib.parse import urlencode
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import logging

# Desativar o cache do googleapiclient
logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

def atualizar_env_file(refresh_token):
    """Atualiza o arquivo .env com o novo refresh_token."""
    env_path = os.path.join(os.getcwd(), '.env')
    try:
        with open(env_path, 'r') as file:
            lines = file.readlines()

        with open(env_path, 'w') as file:
            for line in lines:
                if line.startswith("REFRESH_TOKEN="):
                    file.write(f"REFRESH_TOKEN={refresh_token}\n")
                else:
                    file.write(line)
        print(f"Arquivo .env atualizado com o novo REFRESH_TOKEN.")
    except Exception as e:
        print(f"Erro ao atualizar o arquivo .env: {e}")

def obter_novo_refresh_token():
    CLIENT_ID = '1089000521121-ql963a6ah7p7d2m2ubjr3noll10kdqqq.apps.googleusercontent.com'
    CLIENT_SECRET = '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'
    REDIRECT_URI = 'http://localhost:8080/'  # Alterado para usar o servidor local
    SCOPE = 'https://www.googleapis.com/auth/gmail.send'

    # Variável para armazenar o código de autorização
    auth_code_container = {}

    # Classe para lidar com requisições HTTP
    class AuthorizationHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            query = self.path.split('?')[-1]
            params = dict(qc.split('=') for qc in query.split('&'))
            auth_code_container['code'] = params.get('code')
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Codigo de autorizacao recebido. Pode fechar esta janela.")

    # Iniciar o servidor HTTP em uma thread separada
    server = HTTPServer(('localhost', 8080), AuthorizationHandler)
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()

    # URL para obter o código de autorização
    auth_url = (
        "https://accounts.google.com/o/oauth2/auth?"
        + urlencode({
            'response_type': 'code',
            'client_id': CLIENT_ID,
            'redirect_uri': REDIRECT_URI,
            'scope': SCOPE,
            'state': 'state_parameter',
            'access_type': 'offline',
            'prompt': 'consent'
        })
    )
    print(f"Please visit this URL to authorize this application: {auth_url}")

    # Aguardar o código de autorização
    print("Aguardando o código de autorização...")
    while 'code' not in auth_code_container:
        pass  # Aguarda até que o código seja capturado pelo servidor

    auth_code = auth_code_container['code']
    server.shutdown()  # Finaliza o servidor HTTP

    # Trocar o código de autorização pelo Refresh Token
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        'code': auth_code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
        'grant_type': 'authorization_code'
    }

    try:
        response = requests.post(token_url, data=data)
        response.raise_for_status()  # Levanta uma exceção para códigos de status HTTP 4xx/5xx
        tokens = response.json()
        refresh_token = tokens.get('refresh_token')
        if refresh_token:
            print("Refresh Token gerado com sucesso!")
            print(f"Refresh Token: {refresh_token}")
            atualizar_env_file(refresh_token)  # Atualiza o arquivo .env
        else:
            print("Erro: Refresh Token não foi gerado. Verifique se o acesso offline está habilitado.")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao se comunicar com a API: {e}")
    except ValueError as e:
        print(f"Erro ao processar a resposta: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    try:
        obter_novo_refresh_token()
    except Exception as e:
        print(f"Erro: {e}")
