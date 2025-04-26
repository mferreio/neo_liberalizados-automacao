from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

class PerfilDeAcessoNaoLogadoLocators:
    """Locators para a página de acesso não logado."""
    TELA_LOGIN = (By.XPATH, "//div[contains(@class, 'login-container')]")
    MENSAGEM_ACESSO_NEGADO = (By.XPATH, "//p[text()='Acesso negado']")
    URL_LOGIN = "https://diretrizes.dev.neoenergia.net/auth/login"
    BOTAO_ENTRAR = (By.XPATH, "/html/body/app-root/app-login/div/div/div/div/div[2]/button")
    MENSAGEM_ERRO = (By.CSS_SELECTOR, "div.row > div[role='alert'] > div[id='usernameError']")
    URL_RECURSO = "https://diretrizes.dev.neoenergia.net/pages/perfil"
    URL_LOGIN_MICROSOFT = "https://login.microsoftonline.com/"

class PerfilDeAcessoNaoLogadoPage:
    def __init__(self, driver):
        self.driver = driver

    def acessar_aplicacao(self):
        """Acessa a URL da aplicação sem realizar login."""
        logging.info("Acessando a aplicação sem realizar login.")
        self.driver.get(PerfilDeAcessoNaoLogadoLocators.URL_LOGIN)

    def clicar_botao_entrar(self):
        """Clica no botão 'Entrar'."""
        try:
            logging.info("Clicando no botão 'Entrar'.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PerfilDeAcessoNaoLogadoLocators.BOTAO_ENTRAR)
            ).click()
        except TimeoutException:
            raise AssertionError("Botão 'Entrar' não foi encontrado ou não está clicável.")

    def validar_tela_login(self):
        """Valida se a tela de login está sendo exibida."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PerfilDeAcessoNaoLogadoLocators.TELA_LOGIN)
            )
            logging.info("Tela de login exibida com sucesso.")
        except TimeoutException:
            raise AssertionError("Tela de login não foi exibida.")

    def validar_mensagem_acesso_negado(self):
        """Valida se a mensagem de acesso negado é exibida."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PerfilDeAcessoNaoLogadoLocators.MENSAGEM_ACESSO_NEGADO)
            )
            logging.info("Mensagem de acesso negado exibida com sucesso.")
        except TimeoutException:
            raise AssertionError("Mensagem de acesso negado não foi exibida.")

    def validar_e_capturar_mensagem_erro(self):
        """Valida e captura o texto do elemento de erro."""
        try:
            elemento = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PerfilDeAcessoNaoLogadoLocators.MENSAGEM_ERRO)
            )
            mensagem = elemento.text
            logging.info(f"Mensagem capturada: {mensagem}")
            return mensagem
        except TimeoutException:
            logging.error("Elemento de mensagem de erro não encontrado.")
            return None

    def acessar_recurso_direto(self):
        """Tenta acessar diretamente um recurso da aplicação."""
        logging.info(f"Tentando acessar diretamente a URL: {PerfilDeAcessoNaoLogadoLocators.URL_RECURSO}")
        self.driver.get(PerfilDeAcessoNaoLogadoLocators.URL_RECURSO)

    def validar_redirecionamento_para_login(self):
        """Valida se o usuário foi redirecionado para a tela de login."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains(PerfilDeAcessoNaoLogadoLocators.URL_LOGIN_MICROSOFT)
            )
            logging.info("Usuário foi redirecionado para a tela de login.")
            return True
        except TimeoutException:
            logging.error("Usuário não foi redirecionado para a tela de login.")
            return False

    def exibir_mensagem_acesso_negado(self):
        """Exibe uma mensagem indicando que o usuário deve realizar login."""
        mensagem = "Usuário deve realizar login antes de acessar uma funcionalidade do sistema"
        logging.info(mensagem)
        return mensagem
