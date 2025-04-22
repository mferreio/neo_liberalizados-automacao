import os
import logging
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.login_page import LoginPageLocators
from time import sleep
from datetime import datetime
from credentials import LOGIN_EMAIL, LOGIN_USUARIO, LOGIN_PASSWORD
from pages.login_page import LoginPage
import pyautogui
import base64
import shutil
import stat
import matplotlib.pyplot as plt
import io
from pages.perfil_de_acesso_pages import PerfilDeAcessoPage
import traceback

def login(context):
    """Realiza o login no sistema."""
    try:
        context.login_page.navegar_para_pagina_de_login()
        context.login_page.clicar_botao_entrar()
        context.login_page.enter_email(context.login_email)
        context.login_page.click_next_button()
        sleep(7)  # Aguarda a interface estar pronta para interação
        pyautogui.write(LOGIN_USUARIO.upper())
        pyautogui.press('tab')  # Navega até o campo de senha
        sleep(1)
        pyautogui.write(LOGIN_PASSWORD)  # Digita a senha respeitando o caso das letras
        pyautogui.press('tab')  # Navega até o botão submit
        sleep(1)
        pyautogui.press('enter')  # Submete o login
        sleep(10)

        # Aguarda a transição para a próxima página
        WebDriverWait(context.driver, 15).until(
            EC.url_contains("https://diretrizes.dev.neoenergia.net/")
        )
        logging.info("Login realizado com sucesso.")
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
    context.failed_steps = []  # Lista para armazenar os erros capturados
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

    context.perfil_de_acesso_pages = PerfilDeAcessoPage(context.driver)

    context.skip_login = False

def before_feature(context, feature):
    """Executa ações antes de cada feature."""
    logging.info(f"INICIANDO A FEATURE: {feature.name}")
    if "perfil_de_acesso_nao_logado.feature" in feature.filename:
        context.skip_login = True
    else:
        context.skip_login = False
        login(context)

def before_scenario(context, scenario):
    """Executa ações antes de cada cenário."""
    logging.info(f"INICIANDO O CENÁRIO: {scenario.name}")
    context.start_time_scenario = datetime.now()  # Registra o início do cenário

def after_scenario(context, scenario):
    """Executa ações após cada cenário."""
    end_time_scenario = datetime.now()
    execution_time = end_time_scenario - context.start_time_scenario
    logging.info(f"FINALIZANDO O CENÁRIO: {scenario.name}")
    logging.info(f"Tempo de execução do cenário: {execution_time}")

    if scenario.status == "failed":
        logging.error(f"O cenário '{scenario.name}' falhou.")
        context.failed_scenarios.append(scenario.name)
    else:
        context.passed_scenarios.append(scenario.name)

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
    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1%%', startangle=90)
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
    """Finaliza o ambiente após todos os testes."""
    try:
        if hasattr(context, 'driver'):
            context.driver.quit()
            logging.info("Navegador fechado com sucesso.")

        # Calcula o tempo de execução
        end_time = datetime.now()
        execution_time = end_time - context.start_time

        # Obtém métricas do Allure Report
        passed_scenarios, failed_scenarios, ignored_scenarios = get_allure_metrics()
        total_cenarios = passed_scenarios + failed_scenarios + ignored_scenarios

        # Calcula o percentual de falhas
        percentual_falhas = (failed_scenarios / total_cenarios * 100) if total_cenarios > 0 else 0

        logging.info(f"Resumo dos testes: Total: {total_cenarios}, Sucesso: {passed_scenarios}, Falhas: {failed_scenarios}, Ignorados: {ignored_scenarios}")
        logging.info(f"Tempo de execução: {execution_time}")
        logging.info(f"Percentual de falhas: {percentual_falhas:.2f}%")
    except Exception as e:
        logging.error(f"Erro ao finalizar o ambiente: {e}")

def executar_com_erro_controlado(funcao, *args, **kwargs):
    """Executa uma função, captura erros e continua a execução."""
    try:
        funcao(*args, **kwargs)
    except Exception as e:
        logging.error(f"Erro ao executar {funcao.__name__}: {e}")
        logging.debug(traceback.format_exc())  # Log detalhado do erro
