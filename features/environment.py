import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
from datetime import datetime
from credentials import LOGIN_EMAIL
from features.pages.login_page import LoginPage
from features.utils_general import send_email
from docx import Document
from docx.shared import Inches as DocxInches
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
import matplotlib.pyplot as plt
from fpdf import FPDF

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

def esperar_e_executar(context, locator, metodo, *args):
    """Espera por um elemento clicável e executa uma ação."""
    try:
        WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable(locator))
        metodo(*args)
    except Exception as e:
        logging.error(f"Erro durante a execução: {e}")
        raise
    finally:
        sleep(1)

def before_all(context):
    """Configura o ambiente antes de todos os testes."""
    logging.basicConfig(level=logging.INFO)
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--allow-insecure-localhost")
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
    os.makedirs('reports/allure-results', exist_ok=True)  # Cria a pasta allure-results

    login(context)

def before_scenario(context, scenario):
    """Inicializa os atributos necessários para cada cenário."""
    context.passed_steps = []
    context.failed_steps = []
    logging.info(f"Iniciando cenário: {scenario.name}")

def before_step(context, step):
    """Adiciona informações do passo ao log."""
    logging.info(f"Iniciando passo: {step.name}")

def sanitize_filename(filename):
    """Remove caracteres inválidos do nome do arquivo."""
    return "".join(c if c.isalnum() or c in (" ", ".", "_") else "_" for c in filename)

def after_step(context, step):
    """Captura o print de cada passo e salva no diretório de screenshots."""
    sanitized_step_name = sanitize_filename(step.name)
    screenshot_path = f'reports/screenshots/{sanitized_step_name}.png'

    # Garante que a pasta "reports/screenshots" exista
    os.makedirs('reports/screenshots', exist_ok=True)

    # Captura a evidência do passo
    try:
        context.driver.save_screenshot(screenshot_path)
        logging.info(f"Screenshot capturado: {screenshot_path}")
    except Exception as e:
        logging.error(f"Erro ao capturar screenshot: {e}")

    # Registra o passo no relatório
    if step.status == 'passed':
        context.passed_steps.append((step.name, screenshot_path))
    else:
        context.failed_steps.append((step.name, screenshot_path))

    # Manter a janela aberta em caso de erro
    if step.status == 'failed':
        context.driver.execute_script("window.onbeforeunload = function() {};")
        try:
            context.driver.save_screenshot(screenshot_path)
        except Exception as e:
            logging.error(f"Erro ao capturar screenshot: {e}")

def after_scenario(context, scenario):
    """Adiciona informações do cenário ao log."""
    if scenario.status == 'failed':
        context.failed_scenarios.append(scenario.name)
    else:
        context.passed_scenarios.append(scenario.name)
    logging.info(f"Finalizando cenário: {scenario.name}")

def send_test_results_email(recipient, subject, passed_steps=None, failed_steps=None, passed_scenarios=None, failed_scenarios=None):
    """
    Centraliza a lógica de envio de e-mails com o link do relatório Allure.
    """
    allure_report_link = "https://mferreio.github.io/neo_liberalizados-automacao/"

    email_body = f"""
    <html>
    <body>
        <p>Olá,</p>
        <p>Os resultados dos testes foram gerados. Você pode acessar o relatório completo no link abaixo:</p>
        <p><a href="{allure_report_link}">Relatório Allure</a></p>
        <p>Resumo dos testes:</p>
        <ul>
            <li><strong>Cenários Bem-Sucedidos:</strong> {len(passed_scenarios) if passed_scenarios else 0}</li>
            <li><strong>Cenários Falhados:</strong> {len(failed_scenarios) if failed_scenarios else 0}</li>
            <li><strong>Passos Bem-Sucedidos:</strong> {len(passed_steps) if passed_steps else 0}</li>
            <li><strong>Passos Falhados:</strong> {len(failed_steps) if failed_steps else 0}</li>
        </ul>
        <p>Atenciosamente,</p>
        <p><strong>Equipe de Automação</strong></p>
    </body>
    </html>
    """

    # Ajuste a chamada para `send_email` para usar argumentos compatíveis
    send_email(
        recipient_email=recipient,  # Substitua `to` por `recipient_email`
        subject=subject,
        body=email_body
    )

def after_all(context):
    """Finaliza o ambiente após todos os testes e envia o relatório por e-mail."""
    try:
        # Garante que a pasta "reports/allure-results" exista
        os.makedirs('reports/allure-results', exist_ok=True)

        email_subject = "Relatório de Resultados dos Testes Automatizados"
        send_test_results_email(
            recipient="matheus.drens@gmail.com",
            subject=email_subject,
            passed_steps=context.passed_steps,
            failed_steps=context.failed_steps,
            passed_scenarios=context.passed_scenarios,
            failed_scenarios=context.failed_scenarios
        )
    except Exception as e:
        logging.error(f"Erro ao enviar o e-mail: {e}")
    finally:
        if hasattr(context, 'driver'):
            context.driver.quit()
            logging.info("Navegador fechado com sucesso.")

def generate_evidence_report(context):
    """Gera o arquivo de evidência utilizando o modelo '1.evidencia.docx'."""
    try:
        evidencia_template = 'modelos de evidencias/1.evidencia.docx'
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        evidencia_dest = f'reports/evidencias/Evidencia_{timestamp}.docx'

        # Garante que a pasta "reports/evidencias" exista
        os.makedirs('reports/evidencias', exist_ok=True)

        # Carrega o modelo de evidência
        doc = Document(evidencia_template)

        # Adiciona os passos bem-sucedidos
        doc.add_paragraph("Passos Bem-Sucedidos:")
        for i, (step_name, screenshot_path) in enumerate(context.passed_steps, 1):
            doc.add_paragraph(f"{i}. {step_name}")
            try:
                doc.add_picture(screenshot_path, width=DocxInches(5))
            except Exception as e:
                logging.warning(f"Erro ao adicionar imagem {screenshot_path}: {e}")

        # Adiciona os passos falhados, se houver
        if context.failed_steps:
            doc.add_paragraph("\nPassos Falhados:")
            for i, (step_name, screenshot_path) in enumerate(context.failed_steps, 1):
                doc.add_paragraph(f"{i}. {step_name}")
                try:
                    doc.add_picture(screenshot_path, width=DocxInches(5))
                except Exception as e:
                    logging.warning(f"Erro ao adicionar imagem {screenshot_path}: {e}")

        # Salva o arquivo de evidência
        doc.save(evidencia_dest)
        logging.info(f"Arquivo de evidência gerado: {evidencia_dest}")
    except Exception as e:
        logging.error(f"Erro ao gerar o arquivo de evidência: {e}")
        raise

def generate_report(context):
    evidencia_template = 'modelos de evidencias/1.evidencia.docx'
    bug_template = 'modelos de evidencias/2.bug.docx'
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')

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
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    resumo_dest = f'reports/evidencias/Resumo do teste {timestamp}.pptx'

    # Garante que a pasta "reports/evidencias" exista
    os.makedirs('reports/evidencias', exist_ok=True)

    prs = Presentation(resumo_template)
    
    total_passed = len(context.passed_steps)
    total_failed = len(context.failed_steps)
    total_steps = total_passed + total_failed

    slide_layout = prs.slide_layouts[5]
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    title.text = "Resumo dos Testes"
    title.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

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
    explode = (0.1, 0)

    grafico_path = f'reports/evidencias/resumo_grafico_{timestamp}.jpeg'

    # Garante que a pasta "reports/evidencias" exista
    os.makedirs('reports/evidencias', exist_ok=True)

    # Gerar gráfico de passos bem-sucedidos e falhados
    labels = ['Passos bem-sucedidos', 'Passos falhados']
    sizes = [total_passed, total_failed]
    colors = ['#4CAF50', '#F44336']
    explode = (0.1, 0)

    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.savefig(grafico_path, format='jpeg')
    plt.close()

    # Adicionar gráfico ao slide
    left = Inches(5.5)
    top = Inches(1.5)
    slide.shapes.add_picture(grafico_path, left, top, width=Inches(4.5), height=Inches(4.5))
    os.remove(grafico_path)

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
        pdf.cell(200, 10, txt=f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", ln=True, align='C')

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

def gerar_documento_evidencia(nome_teste, sucesso=True, erros=None):
    """
    Gera um documento de evidência ou bug com base no modelo fornecido.
    """
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
    print(f"Documento gerado: {nome_arquivo}")

def gerar_resumo_testes(total_testes, testes_sucesso, testes_falha):
    """
    Gera um documento de resumo com métricas dos testes realizados.
    """
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
    print(f"Resumo gerado: {nome_arquivo}")
