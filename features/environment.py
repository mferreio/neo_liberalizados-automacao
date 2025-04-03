import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
from datetime import datetime
from credentials import LOGIN_EMAIL, REMETENTE_DE_EMAIL, DESTINATARIO
from features.pages.login_page import LoginPage
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64

def login(context):
    """Realiza o login no sistema."""
    try:
        context.login_page.navegar_para_pagina_de_login()
        context.login_page.clicar_botao_entrar()
        context.login_page.enter_email(context.login_email)
        context.login_page.click_next_button()
    except TimeoutException as e:
        logging.error(f"Erro durante o login: {e}")
        context.driver.save_screenshot('reports/screenshots/timeout_exception.png')
        raise

def before_all(context):
    """Configura o ambiente antes de todos os testes."""
    logging.basicConfig(level=logging.INFO)
    fixed_port = 8080  # Porta fixa para o Selenium

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument(f"--remote-debugging-port={fixed_port}")  # Configura a porta
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.delete_all_cookies()
    context.login_page = LoginPage(context.driver)
    context.login_email = LOGIN_EMAIL
    context.passed_steps = []
    context.failed_steps = []
    context.passed_scenarios = []
    context.failed_scenarios = []
    context.start_time = datetime.now()

    # Garante que as pastas necessárias existam
    os.makedirs('reports/screenshots', exist_ok=True)
    os.makedirs('reports/evidencias', exist_ok=True)
    os.makedirs('reports/allure-results', exist_ok=True)

    login(context)

def esperar_e_executar(context, locator, metodo, *args):
    """Espera por um elemento clicável e executa uma ação."""
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from time import sleep

    try:
        WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable(locator))
        metodo(*args)
    except Exception as e:
        logging.error(f"Erro durante a execução: {e}")
        raise
    finally:
        sleep(1)

def gerar_documento_evidencia(nome_teste, sucesso=True, erros=None):
    """
    Gera um documento de evidência ou bug com base no modelo fornecido.
    """
    from docx import Document
    import os

    data_teste = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    if sucesso:
        modelo = "modelos de evidencias/1.evidencia.docx"
        nome_arquivo = f"reports/evidencias/Evidência_{data_teste}.docx"
    else:
        modelo = "modelos de evidencias/2.bug.docx"
        nome_arquivo = f"reports/evidencias/Bug_{data_teste}.docx"

    doc = Document(modelo)
    doc.add_paragraph(f"Teste: {nome_teste}")
    doc.add_paragraph(f"Data do Teste: {data_teste}")

    if not sucesso and erros:
        doc.add_paragraph("Erros encontrados:")
        for erro in erros:
            doc.add_paragraph(f"- {erro}")

    # Garante que a pasta "reports/evidencias" exista
    os.makedirs(os.path.dirname(nome_arquivo), exist_ok=True)

    doc.save(nome_arquivo)
    logging.info(f"Documento gerado: {nome_arquivo}")
    return nome_arquivo

def gerar_resumo_testes(total_testes, testes_sucesso, testes_falha):
    """
    Gera um documento de resumo com métricas dos testes realizados.
    """
    from docx import Document
    import os

    modelo = "modelos de evidencias/3.Resumo.docx"
    data_teste = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"reports/evidencias/Resumo_{data_teste}.docx"

    doc = Document(modelo)
    doc.add_paragraph(f"Data do Teste: {data_teste}")
    doc.add_paragraph(f"Total de Testes: {total_testes}")
    doc.add_paragraph(f"Testes com Sucesso: {testes_sucesso}")
    doc.add_paragraph(f"Testes com Falha: {testes_falha}")

    # Garante que a pasta "reports/evidencias" exista
    os.makedirs(os.path.dirname(nome_arquivo), exist_ok=True)

    doc.save(nome_arquivo)
    logging.info(f"Resumo gerado: {nome_arquivo}")
    return nome_arquivo

def send_email(subject, body, attachment_path=None):
    """
    Envia um e-mail utilizando a API do Gmail com autenticação de 2 fatores.
    """
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']
    credentials_path = 'credentials.json'
    token_path = 'token.json'
    fixed_port = 8080  # Porta fixa para o redirecionamento

    # Carregar ou atualizar credenciais
    creds = None
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            flow.redirect_uri = f"http://localhost:{fixed_port}/"  # Usar URI fixo
            creds = flow.run_local_server(port=fixed_port, prompt='consent')
        with open(token_path, 'w') as token_file:
            token_file.write(creds.to_json())

    # Configurar e-mail
    sender_email = REMETENTE_DE_EMAIL
    recipient_email = DESTINATARIO
    if not sender_email or not recipient_email:
        raise ValueError("As variáveis 'REMETENTE_DE_EMAIL' e 'DESTINATARIO' não estão configuradas no arquivo credentials.py.")

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'html'))

    # Adicionar anexo, se fornecido
    if attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, 'rb') as attachment:
            part = MIMEText(attachment.read(), 'base64')
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')
            message.attach(part)

    # Enviar e-mail usando Gmail API
    try:
        service = build('gmail', 'v1', credentials=creds, cache_discovery=False)
        raw_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
        service.users().messages().send(userId="me", body=raw_message).execute()
        logging.info("E-mail enviado com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao enviar e-mail: {e}")

def after_all(context):
    """Finaliza o ambiente após todos os testes e envia um e-mail com os resultados."""
    try:
        if hasattr(context, 'driver'):
            context.driver.quit()
            logging.info("Navegador fechado com sucesso.")

        # Configurar e enviar o e-mail
        email_subject = "Relatório de Resultados dos Testes Automatizados"
        email_body = f"""
        <html>
        <body>
            <p>Prezados,</p>
            <p>Os testes foram finalizados em {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}.</p>
            <p>Atenciosamente,</p>
            <p><strong>Equipe de Automação</strong></p>
        </body>
        </html>
        """
        send_email(subject=email_subject, body=email_body)
    except Exception as e:
        logging.error(f"Erro ao finalizar o ambiente ou enviar o e-mail: {e}")
