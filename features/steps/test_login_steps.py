import logging
from time import sleep

import allure
import pyautogui
from behave import given, then, when
from pages.login_page import LoginPage, LoginPageLocators
from selenium.common.exceptions import (StaleElementReferenceException,
                                        TimeoutException)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from credentials import LOGIN_EMAIL, LOGIN_PASSWORD, LOGIN_USUARIO
from features.environment import (esperar_e_executar, gerar_documento_evidencia)

logging.basicConfig(level=logging.INFO)


@given("que eu acesso a página de login")
def step_impl(context):
    from pages.login_page import LoginPageLocators
    esperar_e_executar(context, LoginPageLocators.BOTAO_ENTRAR, context.login_page.navegar_para_pagina_de_login)


@when("eu clico no botão Entrar")
def step_click_next_button(context):
    esperar_e_executar(context.login_page.clicar_botao_entrar)


@when("eu insiro o email de usuario")
@allure.step("Inserindo o email do usuário")
def step_insert_email(context):
    esperar_e_executar(
        context,
        LoginPageLocators.EMAIL_FIELD,
        context.login_page.enter_email,
        LOGIN_EMAIL,
    )


@when("eu clico no botão Seguinte")
@allure.step("Clicando no botão Seguinte")
def step_click_next_button(context):
    try:
        next_button = WebDriverWait(context.driver, 15).until(
            EC.element_to_be_clickable(LoginPageLocators.NEXT_BUTTON)
        )
        next_button.click()
        logging.info("Botão 'Seguinte' clicado com sucesso.")
    except TimeoutException as e:
        logging.error(f"Erro ao clicar no botão 'Seguinte': {e}")
        context.failed_steps.append(f"Erro no passo 'eu clico no botão Seguinte': {e}")
    except Exception as e:
        logging.error(f"Erro inesperado ao clicar no botão 'Seguinte': {e}")
        context.failed_steps.append(
            f"Erro inesperado no passo 'eu clico no botão Seguinte': {e}"
        )
        WebDriverWait(context.driver, 15).until(
            EC.presence_of_element_located(LoginPageLocators.ADFS_USERNAME_FIELD)
        )
        logging.info("Transição para a próxima etapa do login concluída com sucesso.")
    except Exception as e:
        logging.error("ADFS não carregou corretamente.")
    sleep(7)


@when("eu preencho o ADFS com usuário e senha")
@allure.step("Preenchendo o ADFS com usuário e senha")
def step_fill_adfs(context):
    sleep(3)  # Aguarda a interface estar pronta para interação
    pyautogui.write(LOGIN_USUARIO.upper())
    pyautogui.press("tab")  # Navega até o campo de senha
    sleep(1)
    pyautogui.write(LOGIN_PASSWORD)  # Digita a senha respeitando o caso das letras
    pyautogui.press("tab")  # Navega até o botão submit
    sleep(1)
    pyautogui.press("enter")  # Submete o login
    sleep(3)


@then("eu verifico que o usuário acessou o sistema")
def step_verify_user_logged_in(context):
    esperar_e_executar(_verificar_usuario_logado, context)


def _verificar_usuario_logado(context):
    expected_url = "https://diretrizes.dev.neoenergia.net/"
    current_url = context.driver.current_url
    assert current_url.startswith(
        expected_url
    ), f"O login não foi bem-sucedido; URL atual é {current_url}, mas deveria iniciar com {expected_url}."
    logging.info("Usuário acessou o sistema com sucesso.")


@then("o sistema gera evidências do login")
@allure.step("Gerando evidências do login")
def step_gera_evidencias_login(context):
    try:
        # Captura evidências do teste de login
        gerar_documento_evidencia(nome_teste="Teste de Login", sucesso=True)
    except Exception as e:
        print(f"Erro ao gerar evidências do login: {e}")

@when('que o usuário está logado como "Administrador"')
@given('que o usuário está logado como "Administrador"')
@allure.step("Validando que o usuário está logado como Administrador")
def validar_usuario_administrador(context):
    try:
        context.login_page = LoginPage(context.driver)
        context.login_page.validar_usuario_administrador()
    except Exception as e:
        logging.error(f"Erro ao validar o usuário como Administrador: {e}")
        raise


@given("que o usuário está logado como 'Trading Portifólio'")
@allure.step("Validando que o usuário está logado como Trading/Portifólio")
def validar_usuario_portifolio(context):
    try:
        context.login_page = LoginPage(context.driver)
        context.login_page.validar_usuario_portifolio_e_trading()
    except Exception as e:
        logging.error(f"Erro ao validar o usuário como Trading Portifólio: {e}")
        raise
