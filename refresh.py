import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


# Função para obter o refresh token
def get_refresh_token():
    SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
    creds = None
    token_path = "token.json"
    credentials_path = "credentials.json"

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            flow.redirect_uri = "http://localhost:8080/"
            creds = flow.run_local_server(port=8080)
        with open(token_path, "w") as token:
            token.write(creds.to_json())

    print("Refresh Token:", creds.refresh_token)


if __name__ == "__main__":
    get_refresh_token()
