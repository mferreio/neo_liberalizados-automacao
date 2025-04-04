import os
import logging
import subprocess
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
import shutil
import stat

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

    context.report_output_path = os.path.join(os.getcwd(), 'docs')  # Define o diretório de saída como 'docs'
    if not os.path.exists(context.report_output_path):
        os.makedirs(context.report_output_path)  # Cria o diretório se não existir
    context.github_pages_url = "https://mferreio.github.io/neo_liberalizados-automacao/"  # URL do GitHub Pages
    context.github_pages_branch = "gh-pages"  # Define a branch usada para o GitHub Pages

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

def reset_permissions(directory):
    """Redefine permissões de um diretório e seus arquivos."""
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            os.chmod(os.path.join(root, dir_name), stat.S_IRWXU)
        for file_name in files:
            os.chmod(os.path.join(root, file_name), stat.S_IRWXU)

def generate_allure_report():
    """Gera o relatório Allure e envia para o GitHub Pages."""
    allure_results_dir = "reports/allure-results"
    allure_report_dir = "reports/allure-report"
    allure_executable = r"C:\allure\bin\allure.bat"
    repo_url = "https://github.com/mferreio/neo_liberalizados-automacao.git"
    gh_pages_branch = "gh-pages"

    try:
        # Gera o relatório Allure
        logging.info("Gerando o relatório Allure...")
        subprocess.run([allure_executable, "generate", allure_results_dir, "-o", allure_report_dir, "--clean"], check=True)

        # Configura o diretório para o GitHub Pages
        logging.info("Enviando o relatório para o GitHub Pages...")
        if os.path.exists(".gh-pages"):
            reset_permissions(".gh-pages")  # Redefine permissões antes de excluir
            shutil.rmtree(".gh-pages")
        subprocess.run(["git", "clone", "--branch", gh_pages_branch, repo_url, ".gh-pages"], check=True)

        # Copia o relatório para a pasta docs na branch gh-pages
        docs_dir = os.path.join(".gh-pages", "docs")
        if os.path.exists(docs_dir):
            reset_permissions(docs_dir)  # Redefine permissões antes de excluir
            shutil.rmtree(docs_dir)
        shutil.copytree(allure_report_dir, docs_dir)

        # Faz commit e push para a branch gh-pages
        subprocess.run(["git", "-C", ".gh-pages", "add", "."], check=True)
        subprocess.run(["git", "-C", ".gh-pages", "commit", "-m", "Atualização do relatório Allure"], check=True)
        subprocess.run(["git", "-C", ".gh-pages", "push"], check=True)

        logging.info("Relatório enviado para o GitHub Pages com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao gerar ou enviar o relatório Allure: {e}")
        raise

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
    """Finaliza o ambiente após todos os testes, gera o relatório Allure e envia um e-mail com os resultados."""
    try:
        if hasattr(context, 'driver'):
            context.driver.quit()
            logging.info("Navegador fechado com sucesso.")

        # Gera o relatório Allure e envia para o GitHub Pages
        generate_allure_report()

        # Exemplo de lógica para sobrescrever relatórios antigos
        report_file = os.path.join(context.report_output_path, 'index.html')  # Renomeia para 'index.html' para compatibilidade com GitHub Pages
        os.makedirs(context.report_output_path, exist_ok=True)  # Garante que o diretório exista
        # Geração do novo relatório
        with open(report_file, 'w') as f:
            f.write(f"""
            <html>
            <head>
                <title>Relatório de Teste</title>
            </head>
            <body>
                <h1>Relatório de Teste</h1>
                <p>Data de geração: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
                <p>Os resultados dos testes foram atualizados com sucesso.</p>
            </body>
            </html>
            """)

        # Configurar e enviar o e-mail
        email_subject = f"[Neoenergia - Liberalizados Diretrizes] Report de automação {datetime.now().strftime('%d/%m/%Y')}"
        email_body = f"""
        <html>
        <head>
            <style>
            body {{
                font-family: Arial, sans-serif;
                color: #333;
            }}
            h1 {{
                color: #0056b3;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: center;
            }}
            th {{
                background-color: #f4f4f4;
                color: #333;
            }}
            .success {{
                color: green;
            }}
            .failure {{
                color: red;
            }}
            .ignored {{
                color: orange;
            }}
            </style>
        </head>
        <body>
            <h1>Relatório de Automação</h1>
            <p>Prezados,</p>
            <p>Segue o resumo dos testes realizados em {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}:</p>
            <table>
            <tr>
                <th>Total de Cenários</th>
                <th class="success">Cenários Aprovados</th>
                <th class="failure">Cenários Falhados</th>
                <th class="ignored">Cenários Ignorados</th>
            </tr>
            <tr>
                <td>{len(context.passed_scenarios) + len(context.failed_scenarios)}</td>
                <td class="success">{len(context.passed_scenarios)}</td>
                <td class="failure">{len(context.failed_scenarios)}</td>
                <td class="ignored">{0}</td> <!-- Ajuste conforme necessário -->
            </tr>
            </table>
            <p><strong>O relatório Allure pode ser acessado no link abaixo:</strong></p>
            <p><a href="https://mferreio.github.io/neo_liberalizados-automacao/" target="_blank">Clique aqui para acessar o relatório Allure</a></p>
            <p>Atenciosamente,</p>
            <p><strong>Equipe de Automação</strong></p>
        </body>
        </html>
        """
        send_email(subject=email_subject, body=email_body)
    except Exception as e:
        logging.error(f"Erro ao finalizar o ambiente, gerar o relatório ou enviar o e-mail: {e}")
