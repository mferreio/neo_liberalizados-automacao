from pages.diretriz_irec_pages import DiretrizIrecPage
import base64
import io
import os
import shutil
import stat
import subprocess
import traceback
from datetime import datetime
from time import sleep

import matplotlib.pyplot as plt
import pyautogui
from pages.login_page import LoginPage, LoginPageLocators
from pages.perfil_de_acesso_pages import PerfilDeAcessoPage
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from credentials import LOGIN_EMAIL, LOGIN_PASSWORD, LOGIN_USUARIO


def login(context):
    """Realiza o login no sistema."""
    try:
        context.login_page.navegar_para_pagina_de_login()
        context.login_page.clicar_botao_entrar()
        context.login_page.enter_email(context.login_email)
        context.login_page.click_next_button()
        sleep(8)
        pyautogui.write(LOGIN_USUARIO.upper())
        pyautogui.press("tab")
        sleep(1)
        pyautogui.write(LOGIN_PASSWORD)
        pyautogui.press("tab")
        sleep(1)
        pyautogui.press("enter")
        sleep(10)

        # Aguarda a transição para a próxima página
        WebDriverWait(context.driver, 15).until(
            EC.url_contains("https://diretrizes.dev.neoenergia.net/")
        )
        # logging removido
    except TimeoutException as e:
        # logging removido
        context.driver.save_screenshot("reports/screenshots/timeout_exception.png")
        raise


def before_all(context):
    """Configura o ambiente antes de todos os testes."""
    # logging removido
    fixed_port = 8080  # Porta fixa para o Selenium

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument(
        f"--remote-debugging-port={fixed_port}"
    )  # Configura a porta
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
    os.makedirs("reports/screenshots", exist_ok=True)
    os.makedirs("reports/evidencias", exist_ok=True)
    os.makedirs("reports/allure-results", exist_ok=True)

    context.report_output_path = os.path.join(
        os.getcwd(), "docs"
    )  # Define o diretório de saída como 'docs'
    if not os.path.exists(context.report_output_path):
        os.makedirs(context.report_output_path)  # Cria o diretório se não existir
    context.github_pages_url = (
        "https://mferreio.github.io/neo_liberalizados-automacao/"  # URL do GitHub Pages
    )
    context.github_pages_branch = (
        "gh-pages"  # Define a branch usada para o GitHub Pages
    )

    context.perfil_de_acesso_pages = PerfilDeAcessoPage(context.driver)

    # Realiza o login apenas uma vez antes de todos os testes
    try:
        login(context)
    except Exception as e:
        # logging removido
        raise


def before_feature(context, feature):
    """Executa ações antes de cada feature."""
    # logging removido

    # Verifica se a feature é '07_perfil_de_acesso_nao_logado.feature'
    if "07_perfil_de_acesso_nao_logado.feature" in feature.filename:
        try:
            # logging removido
            context.driver.delete_all_cookies()  # Limpa o cache do navegador
            context.driver.get(
                "https://diretrizes.dev.neoenergia.net/"
            )  # Acessa a URL inicial
            # logging removido
        except Exception as e:
            # logging removido
            raise
    else:
        context.driver.get("https://diretrizes.dev.neoenergia.net/")
        # logging removido


def before_scenario(context, scenario):
    # Inicializa o page object DiretrizIrecPage para todos os cenários que envolvem diretriz I-REC
    if hasattr(context, "driver"):
        context.diretriz_irec_page = DiretrizIrecPage(context.driver)
    """Executa ações antes de cada cenário."""
    # logging removido
    context.start_time_scenario = datetime.now()  # Registra o início do cenário


def after_scenario(context, scenario):
    """Executa ações após cada cenário."""
    end_time_scenario = datetime.now()
    execution_time = end_time_scenario - context.start_time_scenario
    # logging removido
    if scenario.status == "failed":
        # logging removido
        context.failed_scenarios.append(scenario.name)
    else:
        context.passed_scenarios.append(scenario.name)


def esperar_e_executar(context, locator, metodo, *args):
    """Espera por um elemento clicável e executa uma ação."""
    from time import sleep

    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait

    try:
        WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable(locator))
        metodo(*args)
    except Exception as e:
        # logging removido
        raise
    finally:
        sleep(1)


def gerar_documento_evidencia(nome_teste, sucesso=True, erros=None):
    """
    Gera um documento de evidência ou bug com base no modelo fornecido.
    """
    import os

    from docx import Document

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
    # logging removido
    return nome_arquivo


def gerar_resumo_testes(total_testes, testes_sucesso, testes_falha):
    """
    Gera um documento de resumo com métricas dos testes realizados.
    """
    import os

    from docx import Document

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
    # logging removido
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
    labels = ["Sucesso", "Falhas"]
    sizes = [sucesso, falhas]
    colors = ["#4CAF50", "#F44336"]
    explode = (0, 0.1)  # Destaque para falhas

    # Evita divisão por zero ao gerar o gráfico
    if total == 0:
        sizes = [1]  # Exibe 100% como "Nenhum dado"
        labels = ["Nenhum dado"]
        colors = ["#B0BEC5"]  # Cor neutra para ausência de dados
        explode = (0,)

    fig, ax = plt.subplots(figsize=(4, 4))  # Reduz o tamanho do gráfico
    ax.pie(
        sizes,
        explode=explode,
        labels=labels,
        colors=colors,
        autopct="%1.1f%%",
        startangle=90,
    )
    ax.axis("equal")  # Garante que o gráfico seja um círculo
    ax.set_title(titulo, fontsize=10)

    # Salva o gráfico em memória
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", bbox_inches="tight")
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.read()).decode("utf-8")
    buffer.close()
    plt.close(fig)
    return img_base64


def gerar_grafico_percentual_completo(sucesso, falhas, ignorados, titulo):
    """Gera um gráfico de pizza com os percentuais de sucesso, falhas e ignorados."""
    total = sucesso + falhas + ignorados
    labels = ["Sucesso", "Falhas", "Ignorados"]
    sizes = [sucesso, falhas, ignorados]
    colors = ["#4CAF50", "#F44336", "#FFC107"]
    explode = (0, 0.1, 0)  # Destaque para falhas

    # Evita divisão por zero ao gerar o gráfico
    if total == 0:
        sizes = [1]  # Exibe 100% como "Nenhum dado"
        labels = ["Nenhum dado"]
        colors = ["#B0BEC5"]  # Cor neutra para ausência de dados
        explode = (0,)

    fig, ax = plt.subplots(figsize=(4, 4))  # Reduz o tamanho do gráfico
    ax.pie(
        sizes,
        explode=explode,
        labels=labels,
        colors=colors,
        autopct="%1.1%%",
        startangle=90,
    )
    ax.axis("equal")  # Garante que o gráfico seja um círculo
    ax.set_title(titulo, fontsize=10)

    # Salva o gráfico em memória
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", bbox_inches="tight")
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.read()).decode("utf-8")
    buffer.close()
    plt.close(fig)
    return img_base64

def after_all(context):
    """Finaliza o ambiente após todos os testes."""
    try:
        if hasattr(context, "driver"):
            context.driver.quit()
            # logging removido

        # Calcula o tempo de execução
        end_time = datetime.now()
        execution_time = end_time - context.start_time
    except Exception as e:
        # logging removido
        pass
