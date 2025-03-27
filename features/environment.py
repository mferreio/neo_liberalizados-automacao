import os
import logging  # Importação corrigida
import matplotlib.pyplot as plt
import smtplib
import json
import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from docx import Document
from docx.shared import Inches as DocxInches
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from credentials import LOGIN_EMAIL, CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN, REMETENTE_DE_EMAIL
from email.mime.base import MIMEBase
from email import encoders
from docx2pdf import convert
from features.pages.login_page import LoginPage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
import datetime
from docx import Document
import allure
from fpdf import FPDF  # Adicionada biblioteca para gerar PDFs

def login(context):
    try:
        context.login_page.navegar_para_pagina_de_login()
        context.login_page.clicar_botao_entrar()
        context.login_page.enter_email(context.login_email)
        context.login_page.click_next_button()
    except TimeoutException as e:
        print(f"TimeoutException: {e}")
        context.driver.save_screenshot('reports/screenshots/timeout_exception.png')
        raise

def esperar_e_executar(context, locator, metodo, *args):
    """Função de alto nível que espera por um elemento clicável e então executa uma ação."""
    try:
        WebDriverWait(context.driver, 20).until(
            EC.element_to_be_clickable(locator)
        )
        metodo(*args)  # Execução do método passado
    except Exception as e:
        print(f"Erro durante a execução: {e}")
        raise
    finally:
        sleep(1)  # Pequeno delay para garantir a conclusão

def before_all(context):
    """Configura o ambiente antes de todos os testes."""
    logging.basicConfig(level=logging.INFO)  # Configuração do logging
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")  # Modo anônimo
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--allow-insecure-localhost")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.delete_all_cookies()  # Limpar o cache
    context.login_page = LoginPage(context.driver)  # Inicializar a página de login
    context.login_email = LOGIN_EMAIL
    #context.login_password = LOGIN_PASSWORD
    context.passed_steps = []  # Inicializar a lista de passos bem-sucedidos
    context.failed_steps = []  # Inicializar a lista de passos falhados
    context.passed_scenarios = []  # Inicializar a lista de cenários bem-sucedidos
    context.failed_scenarios = []  # Inicializar a lista de cenários falhados
    if not os.path.exists('reports/screenshots'):
        os.makedirs('reports/screenshots')
    if not os.path.exists('reports/evidencias'):
        os.makedirs('reports/evidencias')
    login(context)  # Executar o login antes dos testes
    context.allure = allure  # Inicializa o Allure no contexto

def before_scenario(context, scenario):
    """Adiciona informações do cenário ao Allure."""
    with allure.step(f"Iniciando cenário: {scenario.name}"):
        logging.info(f"Iniciando cenário: {scenario.name}")  # Corrigido o uso do logging

def before_step(context, step):
    """Adiciona informações do passo ao Allure."""
    with allure.step(f"Iniciando passo: {step.name}"):
        logging.info(f"Iniciando passo: {step.name}")

def sanitize_filename(filename):
    """
    Remove caracteres inválidos do nome do arquivo.
    """
    return "".join(c if c.isalnum() or c in (" ", ".", "_") else "_" for c in filename)

def after_step(context, step):
    # Sanitiza o nome do arquivo para evitar caracteres inválidos
    sanitized_step_name = sanitize_filename(step.name)
    screenshot_path = f'reports/screenshots/{sanitized_step_name}.png'
    
    # Garante que a pasta "reports/screenshots" exista
    os.makedirs('reports/screenshots', exist_ok=True)
    
    # Captura a evidência do passo
    context.driver.save_screenshot(screenshot_path)
    
    # Registra o passo no relatório, independentemente do status
    context.passed_steps.append((step.name, screenshot_path)) if step.status == 'passed' else context.failed_steps.append((step.name, screenshot_path))
    
    # Manter a janela aberta em caso de erro
    if step.status == 'failed':
        context.driver.execute_script("window.onbeforeunload = function() {};")
        try:
            context.driver.save_screenshot(screenshot_path)
            allure.attach.file(screenshot_path, name=step.name, attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            logging.error(f"Erro ao capturar screenshot: {e}")

def after_scenario(context, scenario):
    """Adiciona informações do cenário ao Allure."""
    if scenario.status == 'failed':
        context.failed_scenarios.append(scenario.name)
        allure.attach(f"Cenário falhou: {scenario.name}", name="Detalhes do Cenário", attachment_type=allure.attachment_type.TEXT)
    else:
        context.passed_scenarios.append(scenario.name)
    logging.info(f"Finalizando cenário: {scenario.name}")  # Corrigido o uso do logging

def after_all(context):
    """Finaliza o ambiente após todos os testes."""
    try:
        # Validação de dados antes de gerar gráficos
        total_passed = len(context.passed_steps)
        total_failed = len(context.failed_steps)
        if total_passed + total_failed == 0:
            logging.warning("Nenhum passo foi executado. Gráficos não serão gerados.")
            return

        # Geração de gráficos corrigida
        labels = ['Passos bem-sucedidos', 'Passos falhados']
        sizes = [total_passed, total_failed]
        if any(size <= 0 for size in sizes):
            logging.warning("Dados inválidos para geração de gráficos. Gráficos não serão gerados.")
            return

        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.savefig('reports/evidencias/resumo_grafico.png')
        plt.close()
    except Exception as e:
        logging.error(f"Erro ao gerar gráficos: {e}")
    finally:
        if hasattr(context, 'driver'):
            context.driver.quit()
            logging.info("Navegador fechado com sucesso.")

def generate_report(context):
    evidencia_template = 'modelos de evidencias/1.evidencia.docx'
    bug_template = 'modelos de evidencias/2.bug.docx'
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M')  # Corrigido para usar datetime.datetime.now()
    
    # Garante que a pasta "reports/evidencias" exista
    os.makedirs('reports/evidencias', exist_ok=True)

    # Gerar evidências dos testes realizados
    evidencia_dest = f'reports/evidencias/Evidencia do Teste {timestamp}.docx'
    doc = Document(evidencia_template)
    
    # Adicionar título "Passos Bem-sucedidos" com estilo "Normal"
    p = doc.add_paragraph('Passos Bem-sucedidos')
    p.style = 'Normal'
    
    for i, (step, screenshot_path) in enumerate(context.passed_steps, 1):
        p = doc.add_paragraph(f'{i}. Passo bem-sucedido: {step}')
        p.style = 'Normal'
        doc.add_picture(screenshot_path, width=DocxInches(5))
        p = doc.add_paragraph()
        p.paragraph_format.keep_with_next = True
    
    # Adicionar título "Passos Falhados" com estilo "Normal" apenas se houver falhas
    if context.failed_steps:
        p = doc.add_paragraph('Passos Falhados')
        p.style = 'Normal'
        
        for i, (step, screenshot_path) in enumerate(context.failed_steps, 1):
            p = doc.add_paragraph(f'{i}. Passo falhado: {step}')
            p.style = 'Normal'
            doc.add_picture(screenshot_path, width=DocxInches(5))
            p = doc.add_paragraph()
            p.paragraph_format.keep_with_next = True
    
    doc.save(evidencia_dest)

    # Gerar arquivo de bug se houver falhas
    if context.failed_steps:
        bug_dest = f'reports/evidencias/Bug {timestamp}.docx'
        doc = Document(bug_template)
        
        for i, (step, screenshot_path) in enumerate(context.failed_steps, 1):
            p = doc.add_paragraph(f'{i}. Passo falhado: {step}')
            p.style = 'Normal'
            doc.add_picture(screenshot_path, width=DocxInches(5))
            p = doc.add_paragraph()
            p.paragraph_format.keep_with_next = True
        
        doc.save(bug_dest)

def generate_summary_report(context):
    resumo_template = 'modelos de evidencias/3.Resumo.pptx'
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M')  # Corrigido para usar datetime.datetime.now()
    resumo_dest = f'reports/evidencias/Resumo do teste {timestamp}.pptx'

    # Garante que a pasta "reports/evidencias" exista
    os.makedirs('reports/evidencias', exist_ok=True)

    prs = Presentation(resumo_template)
    
    total_passed = len(context.passed_steps)
    total_failed = len(context.failed_steps)
    total_steps = total_passed + total_failed

    slide_layout = prs.slide_layouts[5]  # Layout de título e conteúdo
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    title.text = "Resumo dos Testes"
    title.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER  # Centralizar o título

    # Adicionar caixa de texto manualmente ao slide
    left = Inches(0.5)
    top = Inches(1.5)
    width = Inches(4.5)
    height = Inches(2.5)
    textbox = slide.shapes.add_textbox(left, top, width, height)
    text_frame = textbox.text_frame
    text_frame.text = f'Total de passos: {total_steps}'
    p = text_frame.add_paragraph()
    p.text = f'Passos bem-sucedidos: {total_passed}'
    p.space_after = Pt(0)
    p = text_frame.add_paragraph()
    p.text = f'Passos falhados: {total_failed}'

    # Gerar gráfico de passos bem-sucedidos e falhados
    labels = ['Passos bem-sucedidos', 'Passos falhados']
    sizes = [total_passed, total_failed]
    colors = ['#4CAF50', '#F44336']
    explode = (0.1, 0)  # Explode o primeiro pedaço

    grafico_path = f'reports/evidencias/resumo_grafico_{timestamp}.jpeg'

    # Garante que a pasta "reports/evidencias" exista
    os.makedirs('reports/evidencias', exist_ok=True)

    # Gerar gráfico de passos bem-sucedidos e falhados
    labels = ['Passos bem-sucedidos', 'Passos falhados']
    sizes = [total_passed, total_failed]
    colors = ['#4CAF50', '#F44336']
    explode = (0.1, 0)  # Explode o primeiro pedaço

    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')  # Assegura que o gráfico é desenhado como um círculo.
    plt.savefig(grafico_path, format='jpeg')  # Salva o gráfico antes de usá-lo
    plt.close()

    # Adicionar gráfico ao slide
    left = Inches(5.5)
    top = Inches(1.5)
    slide.shapes.add_picture(grafico_path, left, top, width=Inches(4.5), height=Inches(4.5))
    os.remove(grafico_path)  # Exclui o arquivo após adicioná-lo ao slide

    prs.save(resumo_dest)

def generate_pdf_report(context):
    """Gera o relatório PDF com base nos resultados dos testes."""
    try:
        pdf_dest = 'reports/evidencias/Relatorio_de_Teste.pdf'

        # Garante que a pasta "reports/evidencias" exista
        os.makedirs(os.path.dirname(pdf_dest), exist_ok=True)

        # Cria o PDF usando FPDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Relatório de Testes Automatizados", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Data: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", ln=True, align='C')

        # Adiciona informações sobre os passos
        pdf.ln(10)
        pdf.cell(200, 10, txt="Passos Bem-Sucedidos:", ln=True)
        for step, _ in context.get("passed_steps", []):
            pdf.cell(200, 10, txt=f"- {step}", ln=True)

        pdf.ln(10)
        pdf.cell(200, 10, txt="Passos Falhados:", ln=True)
        for step, _ in context.get("failed_steps", []):
            pdf.cell(200, 10, txt=f"- {step}", ln=True)

        # Salva o PDF
        pdf.output(pdf_dest)
        print(f"Relatório PDF gerado com sucesso: {pdf_dest}")
    except Exception as e:
        logging.error(f"Erro ao gerar o relatório PDF: {e}")
        raise

def authenticate_gmail():
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']
    try:
        creds = Credentials(
            None,
            refresh_token=REFRESH_TOKEN,
            token_uri='https://oauth2.googleapis.com/token',
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET
        )
        if creds.expired:
            creds.refresh(Request())
        return creds
    except Exception as e:
        logging.error(f"Erro ao autenticar no Gmail: {e}")
        raise

def send_email_report(context):
    creds = authenticate_gmail()
    allure_report_path = context.get("allure_report_path")  # Caminho do relatório HTML do Allure
    pdf_report_path = context.get("pdf_report_path")  # Caminho do relatório PDF
    test_failed = context.get("test_failed", False)

    try:
        # Verifica se o relatório HTML do Allure existe
        if allure_report_path and not os.path.exists(allure_report_path):
            logging.error(f"Relatório HTML do Allure não encontrado: {allure_report_path}")
            raise FileNotFoundError(f"Relatório HTML do Allure não encontrado: {allure_report_path}")

        # Verifica se o relatório PDF existe
        if pdf_report_path and not os.path.exists(pdf_report_path):
            logging.error(f"Relatório PDF não encontrado: {pdf_report_path}")
            raise FileNotFoundError(f"Relatório PDF não encontrado: {pdf_report_path}")

        email_subject = "Relatório de Resultados dos Testes Automatizados"
        email_body = f"""
        <html>
        <body>
            <p>Prezados,</p>
            <p>Segue o relatório detalhado dos testes automatizados realizados.</p>
            <p>Status dos testes: {"Falharam" if test_failed else "Bem-sucedidos"}.</p>
            <p>Os relatórios HTML do Allure e PDF estão anexados a este e-mail.</p>
            <p>Atenciosamente,</p>
            <p>Equipe de Automação de Testes</p>
        </body>
        </html>
        """

        msg = MIMEMultipart()
        msg['From'] = REMETENTE_DE_EMAIL
        msg['To'] = 'matheus.drens@gmail.com'
        msg['Subject'] = email_subject
        msg.attach(MIMEText(email_body, 'html'))

        # Adicionar relatório HTML do Allure como anexo
        if allure_report_path and os.path.exists(allure_report_path):
            with open(allure_report_path, 'rb') as f:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename="Allure_Report.html"')
                msg.attach(part)

        # Adicionar relatório PDF como anexo
        if pdf_report_path and os.path.exists(pdf_report_path):
            with open(pdf_report_path, 'rb') as f:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename="Relatorio_de_Teste.pdf"')
                msg.attach(part)

        raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
        message = {'raw': raw}

        service = build('gmail', 'v1', credentials=creds)
        service.users().messages().send(userId='me', body=message).execute()
        logging.info("E-mail enviado com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao enviar o e-mail: {e}")
        if "invalid_grant" in str(e):
            logging.error("O token de autenticação é inválido ou expirou. Regere um novo refresh_token.")
        raise

def gerar_documento_evidencia(nome_teste, sucesso=True, erros=None):
    """
    Gera um documento de evidência ou bug com base no modelo fornecido.
    """
    data_teste = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
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
    print(f"Documento gerado: {nome_arquivo}")

def gerar_resumo_testes(total_testes, testes_sucesso, testes_falha):
    """
    Gera um documento de resumo com métricas dos testes realizados.
    """
    modelo = "modelos de evidencias/3.Resumo.docx"
    data_teste = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"reports/evidencias/Resumo_{data_teste}.docx"

    doc = Document(modelo)
    doc.add_paragraph(f"Data do Teste: {data_teste}")
    doc.add_paragraph(f"Total de Testes: {total_testes}")
    doc.add_paragraph(f"Testes com Sucesso: {testes_sucesso}")
    doc.add_paragraph(f"Testes com Falha: {testes_falha}")

    # Garante que a pasta "reports/evidencias" exista
    os.makedirs(os.path.dirname(nome_arquivo), exist_ok=True)

    doc.save(nome_arquivo)
    print(f"Resumo gerado: {nome_arquivo}")
