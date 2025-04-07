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
from pages.login_page import LoginPage
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64
import shutil
import stat
import matplotlib.pyplot as plt
import io
from utils.utils_allure import upload_to_github_pages  # Importa a função necessária

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

def gerar_grafico_percentual(total, falhas, titulo):
    """Gera um gráfico de pizza com o percentual de falhas."""
    sucesso = total - falhas
    labels = ['Sucesso', 'Falhas']
    sizes = [sucesso, falhas]
    colors = ['#4CAF50', '#F44336']
    explode = (0, 0.1)  # Destaque para falhas

    # Evita divisão por zero ao gerar o gráfico
    if total == 0:
        sizes = [1]  # Exibe 100% como "Nenhum dado"
        labels = ['Nenhum dado']
        colors = ['#B0BEC5']  # Cor neutra para ausência de dados
        explode = (0,)

    fig, ax = plt.subplots(figsize=(4, 4))  # Reduz o tamanho do gráfico
    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Garante que o gráfico seja um círculo
    ax.set_title(titulo, fontsize=10)

    # Salva o gráfico em memória
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()
    plt.close(fig)
    return img_base64

def gerar_grafico_percentual_completo(sucesso, falhas, ignorados, titulo):
    """Gera um gráfico de pizza com os percentuais de sucesso, falhas e ignorados."""
    total = sucesso + falhas + ignorados
    labels = ['Sucesso', 'Falhas', 'Ignorados']
    sizes = [sucesso, falhas, ignorados]
    colors = ['#4CAF50', '#F44336', '#FFC107']
    explode = (0, 0.1, 0)  # Destaque para falhas

    # Evita divisão por zero ao gerar o gráfico
    if total == 0:
        sizes = [1]  # Exibe 100% como "Nenhum dado"
        labels = ['Nenhum dado']
        colors = ['#B0BEC5']  # Cor neutra para ausência de dados
        explode = (0,)

    fig, ax = plt.subplots(figsize=(4, 4))  # Reduz o tamanho do gráfico
    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Garante que o gráfico seja um círculo
    ax.set_title(titulo, fontsize=10)

    # Salva o gráfico em memória
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()
    plt.close(fig)
    return img_base64

def get_allure_metrics():
    """Obtém métricas do Allure Report a partir do arquivo summary.json."""
    summary_path = os.path.join("reports", "allure-report", "widgets", "summary.json")
    passed = failed = ignored = broken = 0

    try:
        with open(summary_path, "r") as summary_file:
            import json
            summary = json.load(summary_file)
            passed = summary.get("statistic", {}).get("passed", 0)
            failed = summary.get("statistic", {}).get("failed", 0)
            broken = summary.get("statistic", {}).get("broken", 0)
            ignored = summary.get("statistic", {}).get("skipped", 0)
    except Exception as e:
        logging.error(f"Erro ao obter métricas do Allure Report: {e}")

    # Inclui cenários "broken" no total de falhas
    failed += broken
    return passed, failed, ignored

def after_all(context):
    """Finaliza o ambiente após todos os testes, gera o relatório Allure e envia um e-mail com os resultados."""
    try:
        if hasattr(context, 'driver'):
            context.driver.quit()
            logging.info("Navegador fechado com sucesso.")

        # Calcula o tempo de execução
        end_time = datetime.now()
        execution_time = end_time - context.start_time

        # Gera o relatório Allure
        allure_results_dir = "reports/allure-results"
        allure_report_dir = "reports/allure-report"
        allure_executable = r"C:\allure\bin\allure.bat"
        repo_url = "https://github.com/mferreio/neo_liberalizados-automacao.git"
        gh_pages_branch = "gh-pages"

        logging.info("Gerando o relatório Allure...")
        subprocess.run([allure_executable, "generate", allure_results_dir, "-o", allure_report_dir, "--clean"], check=True)

        logging.info("Enviando o relatório para o GitHub Pages...")
        upload_to_github_pages(allure_report_dir, repo_url, gh_pages_branch)

        # Obtém métricas do Allure Report
        passed_scenarios, failed_scenarios, ignored_scenarios = get_allure_metrics()
        total_cenarios = passed_scenarios + failed_scenarios + ignored_scenarios

        # Calcula o percentual de falhas
        percentual_falhas = (failed_scenarios / total_cenarios * 100) if total_cenarios > 0 else 0

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
            .execution-time {{
                font-size: 20px;
                font-weight: bold;
            }}
            </style>
        </head>
        <body>
            <h1>Relatório de Automação</h1>
            <p>Prezados,</p>
            <p>Segue o resumo dos testes realizados em {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
            <p><strong>Tempo de execução:</strong> <span class="execution-time">{str(execution_time).split('.')[0]}</span></p>
            <p><strong>Percentual de falhas:</strong> <span class="execution-time">{percentual_falhas:.2f}%</span></p>
            <table>
            <tr>
                <th>Total de Cenários</th>
                <th class="success">Cenários Aprovados</th>
                <th class="failure">Cenários Falhados</th>
                <th class="ignored">Cenários Ignorados</th>
            </tr>
            <tr>
                <td>{total_cenarios}</td>
                <td class="success">{passed_scenarios}</td>
                <td class="failure">{failed_scenarios}</td>
                <td class="ignored">{ignored_scenarios}</td>
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
