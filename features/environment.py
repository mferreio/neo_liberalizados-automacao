import os
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

def after_scenario(context, scenario):
    if scenario.status == 'failed':
        context.failed_scenarios.append(scenario.name)
    else:
        context.passed_scenarios.append(scenario.name)

def after_all(context):
    generate_report(context)
    generate_summary_report(context)
    generate_pdf_report(context)
    send_email_report(context)
    # Remover o fechamento automático do navegador
    # context.driver.quit()

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
    template_path = 'modelos de evidencias/4.Relatorio de Teste.docx'
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M')  # Corrigido para usar datetime.datetime.now()
    pdf_dest = f'reports/evidencias/Relatorio_de_Teste_{timestamp}.pdf'

    # Garante que a pasta "reports/evidencias" exista
    os.makedirs('reports/evidencias', exist_ok=True)

    doc = Document(template_path)
    
    # Adicionar sumário
    doc.add_paragraph('Sumário', style='Normal').runs[0].bold = True
    doc.add_paragraph('1. Gráfico de Barras de Resultados dos Testes', style='Normal')
    doc.add_paragraph('2. Gráfico de Pizza de Cobertura de Código', style='Normal')
    doc.add_paragraph('3. Resumo dos Testes', style='Normal')
    doc.add_paragraph('4. Versões das ferramentas de teste utilizadas', style='Normal')
    p = doc.add_paragraph()
    p.paragraph_format.keep_with_next = True

    # Adicionar gráficos e informações ao documento
    total_passed = len(context.passed_steps)
    total_failed = len(context.failed_steps)
    total_steps = total_passed + total_failed
    total_defects = len(context.failed_steps)
    pass_percentage = (total_passed / total_steps) * 100 if total_steps > 0 else 0
    fail_percentage = (total_failed / total_steps) * 100 if total_steps > 0 else 0

    # Gráfico de Barras de Resultados dos Testes
    p = doc.add_paragraph('1. Gráfico de Barras de Resultados dos Testes', style='Normal')
    p.alignment = 0  # Alinhar à esquerda
    bar_chart_path = f'reports/evidencias/bar_chart_{timestamp}.jpeg'
    pie_chart_path = f'reports/evidencias/pie_chart_{timestamp}.jpeg'
    plt.bar(['Aprovados', 'Reprovados', 'Em Aberto'], [total_passed, total_failed, 0], color=['#4CAF50', '#F44336', '#FFC107'])
    plt.title('Resultados dos Testes')
    plt.xlabel('Status')
    plt.ylabel('Quantidade')
    plt.savefig(bar_chart_path, format='jpeg')
    plt.close()
    doc.add_picture(bar_chart_path, width=DocxInches(4)).alignment = 1  # Centralizar o gráfico
    os.remove(bar_chart_path)  # Exclui o arquivo após adicioná-lo ao documento
    p = doc.add_paragraph()
    p.paragraph_format.keep_with_next = True
    
    # Adicionar quebra de página antes do próximo gráfico
    doc.add_page_break()

    # Gráfico de Pizza de Cobertura de Código
    # Adiciona parágrafos vazios para criar espaço no início do documento
    p = doc.add_paragraph('2. Gráfico de Pizza de Cobertura de Código', style='Normal')
    p.alignment = 0  # Alinhar à esquerda
    plt.pie([pass_percentage, 100 - pass_percentage], labels=['Coberto', 'Não Coberto'], colors=['#4CAF50', '#F44336'], autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.savefig(pie_chart_path, format='jpeg')
    plt.close()
    doc.add_picture(pie_chart_path, width=DocxInches(4)).alignment = 1  # Centralizar o gráfico
    os.remove(pie_chart_path)  # Exclui o arquivo após adicioná-lo ao documento
    p = doc.add_paragraph()
    p.paragraph_format.keep_with_next = True

    # Resumo dos Testes
    p = doc.add_paragraph('3. Resumo dos Testes', style='Normal')
    doc.add_paragraph(f'1. Número total de casos de teste executados: ').add_run(f'{total_steps}').bold = True
    doc.add_paragraph(f'2. Número de casos de teste aprovados: ').add_run(f'{total_passed}').bold = True
    doc.add_paragraph(f'3. Número de casos de teste reprovados: ').add_run(f'{total_failed}').bold = True
    doc.add_paragraph(f'4. Número de casos de teste em aberto: ').add_run('0').bold = True
    doc.add_paragraph(f'5. Percentual de aprovação: ').add_run(f'{pass_percentage:.2f}%').bold = True
    doc.add_paragraph(f'6. Percentual de falha: ').add_run(f'{fail_percentage:.2f}%').bold = True
    doc.add_paragraph(f'7. Número total de defeitos encontrados: ').add_run(f'{total_defects}').bold = True

    # Ambiente de Teste
    doc.add_paragraph()
    p = doc.add_paragraph('4. Versões das ferramentas de teste utilizadas', style='Normal')
    doc.add_paragraph('- Google Chrome: ').add_run(f'Vs {context.driver.capabilities["browserVersion"]}').bold = True
    doc.add_paragraph('- VSCode: ').add_run('Vs 1.60.0').bold = True  # Exemplo de versão
    doc.add_paragraph('- Selenium: ').add_run(f'Vs {webdriver.__version__}').bold = True
    doc.add_paragraph('- Python: ').add_run('Vs 3.12.0').bold = True
     
    doc.save(f'reports/evidencias/Relatorio_de_Teste_{timestamp}.docx')
    try:
        # Converte o documento Word para PDF
        convert(f'reports/evidencias/Relatorio_de_Teste_{timestamp}.docx', pdf_dest)
    except Exception as e:
        print(f"Erro ao converter o documento para PDF: {e}")
    finally:
        # Garante que o objeto Word.Application seja encerrado corretamente, se o módulo comtypes estiver disponível
        try:
            import importlib
            if importlib.util.find_spec("comtypes"):
                import comtypes.client
                word_app = comtypes.client.CreateObject("Word.Application")
                word_app.Quit()
            else:
                print("Aviso: O módulo 'comtypes' não está instalado. Pule o encerramento do Word.Application.")
        except Exception as e:
            print(f"Erro ao encerrar o Word.Application: {e}")

def authenticate_gmail():
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']
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

def send_email_report(context):
    creds = authenticate_gmail()
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M')  # Corrigido para usar datetime.datetime.now()
    current_date = datetime.datetime.now().strftime('%d/%m/%Y')  # Corrigido para usar datetime.datetime.now()
    bar_chart_path = f'reports/evidencias/bar_chart_{timestamp}.jpeg'
    pdf_report_path = f'reports/evidencias/Relatorio_de_Teste_{timestamp}.pdf'  # Definição da variável

    # Garante que o gráfico seja gerado antes de tentar usá-lo
    if not os.path.exists(bar_chart_path):
        print(f"Gerando o gráfico de barras em '{bar_chart_path}'...")
        plt.bar(['Aprovados', 'Reprovados', 'Em Aberto'], [len(context.passed_steps), len(context.failed_steps), 0], color=['#4CAF50', '#F44336', '#FFC107'])
        plt.title('Resultados dos Testes')
        plt.xlabel('Status')
        plt.ylabel('Quantidade')
        plt.savefig(bar_chart_path, format='jpeg')
        plt.close()

    # Verifica novamente se o gráfico foi gerado
    if not os.path.exists(bar_chart_path):
        raise FileNotFoundError(f"O gráfico de barras '{bar_chart_path}' não foi encontrado.")

    # Garante que o relatório PDF exista antes de tentar usá-lo
    if not os.path.exists(pdf_report_path):
        raise FileNotFoundError(f"O relatório PDF '{pdf_report_path}' não foi encontrado.")

    total_test_cases = len(context.passed_steps) + len(context.failed_steps)  # Total de casos de teste executados
    total_passed = len(context.passed_steps)
    total_failed = len(context.failed_steps)
    total_features = len(context.passed_scenarios) + len(context.failed_scenarios)  # Total de features
    features_passed = len(context.passed_scenarios)
    features_failed = len(context.failed_scenarios)

    # Converter a imagem do gráfico para Base64
    with open(bar_chart_path, 'rb') as img_file:
        grafico_base64 = base64.b64encode(img_file.read()).decode('utf-8')

    email_subject = f"Relatório de Resultados dos Testes Automatizados – [Neoenergia - Liberalizados Diretrizes- {current_date}]"
    email_body = f"""
    <html>
    <body>
        <p>Prezados,</p>
        <p>Gostaria de compartilhar o relatório detalhado dos resultados dos testes automatizados realizados para o projeto <b>Liberalizados Diretrizes</b> na data <b>{current_date}</b>. Abaixo, seguem as principais informações e conclusões:</p>
        <p><b>1. Resumo dos Testes Executados:</b></p>
        <ul>
            <li>Total de Casos de Teste: <b>{total_test_cases}</b></li>
            <li>Casos de Teste Aprovados: <b>{total_passed}</b></li>
            <li>Casos de Teste Reprovados: <b>{total_failed}</b></li>
            <li>Casos de Teste em Aberto: <b>0</b></li>
        </ul>
        <p><b>2. Resumo dos produtos Executados:</b></p>
        <ul>
            <li>Total de produtos testados: <b>{total_features}</b></li>
            <li>Produtos Aprovados: <b>{features_passed}</b></li>
            <li>Produtos Reprovados: <b>{features_failed}</b></li>
            <li>Produtos em Aberto: <b>0</b></li>
        </ul>
        <p><b>3. Cenários que falharam:</b></p>
        <ul>
            {''.join(f'<li><b>{step.capitalize()}</b></li>' for step, _ in context.failed_steps)}
        </ul>
        <p><b>4. Recomendação e Próximos Passos:</b></p>
        <ul>
            <li>Ações Recomendadas: Recomendamos a análise e correção dos problemas identificados, seguida de uma nova rodada de testes para garantir a resolução das falhas identificadas e a qualidade do sistema.</li>
        </ul>
        <p><img src="data:image/jpeg;base64,{grafico_base64}" alt="Resumo Gráfico"></p>
        <p>Estamos à disposição para tratar os resultados em detalhes, realizar testes assistidos e responder a quaisquer perguntas que possam surgir. Agradecemos a colaboração de todos e estamos comprometidos em garantir a qualidade e a estabilidade do sistema.</p>
    </body>
    </html>
    """

    msg = MIMEMultipart()
    msg['From'] = REMETENTE_DE_EMAIL
    msg['To'] = 'matheus.drens@gmail.com'
    msg['Subject'] = email_subject
    msg.attach(MIMEText(email_body, 'html'))

    # Adicionar relatório PDF como anexo
    if os.path.exists(pdf_report_path):
        with open(pdf_report_path, 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(pdf_report_path)}"')
            msg.attach(part)

    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    message = {'raw': raw}

    service = build('gmail', 'v1', credentials=creds)
    service.users().messages().send(userId='me', body=message).execute()

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


