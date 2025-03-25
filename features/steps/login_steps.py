from behave import given, when, then
from selenium.common.exceptions import StaleElementReferenceException
from features.environment import esperar_e_executar
from features.pages.login_page import LoginPageLocators
from credentials import LOGIN_EMAIL, LOGIN_PASSWORD, LOGIN_USUARIO
import logging
from time import sleep
import pyautogui
from features.environment import gerar_documento_evidencia

logging.basicConfig(level=logging.INFO)

@given('que eu acesso a página de login')
def step_impl(context):
    logging.info("Navegando para a página de login")
    context.login_page.navegar_para_pagina_de_login()

@when('eu clico no botão Entrar')
def step_click_next_button(context):
    esperar_e_executar(context, LoginPageLocators.BOTAO_ENTRAR, context.login_page.clicar_botao_entrar, )

@when('eu insiro o email de usuario')
def step_insert_email(context):
    esperar_e_executar(context, LoginPageLocators.EMAIL_FIELD, context.login_page.enter_email, LOGIN_EMAIL)

@when('eu clico no botão Seguinte')
def step_click_next_button(context):
    esperar_e_executar(context, LoginPageLocators.NEXT_BUTTON, context.login_page.click_next_button)
    sleep(30)

@when('eu preencho o ADFS com usuário e senha')
def step_fill_adfs(context):
    sleep(3)  # Aguarda a interface estar pronta para interação
    pyautogui.write(LOGIN_USUARIO) # Digita o usuário respeitando o caso das letras
    pyautogui.press('tab')  # Navega até o campo de senha
    sleep(1)
    pyautogui.write(LOGIN_PASSWORD)# Digita a senha respeitando o caso das letras
    pyautogui.press('tab')  # Navega até o botão submit
    sleep(1)
    pyautogui.press('enter')  # Submete o login
    sleep(3)

@then('eu verifico que o usuário acessou o sistema')
def step_verify_user_logged_in(context):
    # Verifica a URL atual para confirmar que o usuário acessou o sistema
    expected_url = "https://diretrizes.dev.neoenergia.net/"
    current_url = context.driver.current_url

    if current_url.startswith(expected_url):
        context.is_logged_in = True
    else:
        context.is_logged_in = False
        raise AssertionError(f"O login não foi bem-sucedido; URL atual é {current_url}, mas deveria iniciar com {expected_url}.")
    sleep(5)

@then('o sistema gera evidências do login')
def step_gera_evidencias_login(context):
    try:
        # Captura evidências do teste de login
        gerar_documento_evidencia(nome_teste="Teste de Login", sucesso=True)
    except Exception as e:
        print(f"Erro ao gerar evidências do login: {e}")