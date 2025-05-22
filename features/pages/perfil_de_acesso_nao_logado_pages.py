import logging
logger = logging.getLogger(__name__)

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PerfilDeAcessoNaoLogadoLocators:
    """Locators para a página de acesso não logado."""

    TELA_LOGIN = (By.XPATH, "//div[contains(@class, 'login-container')]")
    MENSAGEM_ACESSO_NEGADO = (By.XPATH, "//p[text()='Acesso negado']")
    URL_LOGIN = "https://diretrizes.dev.neoenergia.net/auth/login"
    BOTAO_ENTRAR = (
        By.XPATH,
        "/html/body/app-root/app-login/div/div/div/div/div[2]/button",
    )
    MENSAGEM_ERRO = (
        By.CSS_SELECTOR,
        "div.row > div[role='alert'] > div[id='usernameError']",
    )
    URL_RECURSO = "https://diretrizes.dev.neoenergia.net/pages/perfil/listar"
    URL_LOGIN_MICROSOFT = "login.microsoftonline.com"


class PerfilDeAcessoNaoLogadoPage:

    def __init__(self, driver):
        self.driver = driver
        logger.info("Instanciando page object: PerfilDeAcessoNaoLogadoPage")

    def acessar_aplicacao(self):
        """Acessa a URL da aplicação sem realizar login."""
        logger.info("Acessando a aplicação sem realizar login.")
        self.driver.get(PerfilDeAcessoNaoLogadoLocators.URL_LOGIN)

    def esperar_overlay_sumir(self, timeout=10):
        """Espera o overlay/modal sumir antes de interagir com a tela."""
        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".p-dialog-mask.p-component-overlay.p-component-overlay-enter"))
            )
        except Exception:
            logger.debug("Overlay não encontrado ou já sumiu.")
            pass  # Se não existir overlay, segue normalmente


    def clicar_botao_entrar(self):
        """Clica no botão 'Entrar', aguardando o overlay sumir se necessário."""
        try:
            logger.info("Aguardando overlay/modal sumir antes de clicar no botão 'Entrar'.")
            self.esperar_overlay_sumir()
            logger.info("Clicando no botão 'Entrar'.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PerfilDeAcessoNaoLogadoLocators.BOTAO_ENTRAR)
            ).click()
            logger.info("Botão 'Entrar' clicado.")
        except TimeoutException:
            logger.error("Botão 'Entrar' não foi encontrado ou não está clicável.")
            raise AssertionError(
                "Botão 'Entrar' não foi encontrado ou não está clicável."
            )

    def clicar_elemento_generico(self, locator, timeout=10):
        """
        Método utilitário para clicar em qualquer elemento, aguardando o overlay sumir antes.
        Exemplo de uso: self.clicar_elemento_generico((By.XPATH, "//button[@id='meu-botao']"))
        """
        try:
            logger.info(f"Aguardando overlay/modal sumir antes de clicar no elemento: {locator}")
            self.esperar_overlay_sumir()
            logger.info(f"Clicando no elemento: {locator}")
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            ).click()
            logger.info(f"Elemento clicado: {locator}")
        except TimeoutException:
            logger.error(f"Elemento {locator} não foi encontrado ou não está clicável.")
            raise AssertionError(f"Elemento {locator} não foi encontrado ou não está clicável.")

    def validar_tela_login(self):
        """Valida se a tela de login está sendo exibida."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    PerfilDeAcessoNaoLogadoLocators.TELA_LOGIN
                )
            )
            logger.info("Tela de login exibida com sucesso.")
        except TimeoutException:
            logger.error("Tela de login não foi exibida.")
            raise AssertionError("Tela de login não foi exibida.")

    def validar_mensagem_acesso_negado(self):
        """Valida se a mensagem de acesso negado é exibida."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    PerfilDeAcessoNaoLogadoLocators.MENSAGEM_ACESSO_NEGADO
                )
            )
            logger.info("Mensagem de acesso negado exibida com sucesso.")
        except TimeoutException:
            logger.error("Mensagem de acesso negado não foi exibida.")
            raise AssertionError("Mensagem de acesso negado não foi exibida.")

    def validar_e_capturar_mensagem_erro(self):
        """Valida e captura o texto do elemento de erro."""
        try:
            elemento = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    PerfilDeAcessoNaoLogadoLocators.MENSAGEM_ERRO
                )
            )
            mensagem = elemento.text
            logger.info(f"Mensagem capturada: {mensagem}")
            return mensagem
        except TimeoutException:
            logger.error("Elemento de mensagem de erro não encontrado.")
            return None

    def acessar_recurso_direto(self):
        """Tenta acessar diretamente um recurso da aplicação."""
        logger.info(
            f"Tentando acessar diretamente a URL: {PerfilDeAcessoNaoLogadoLocators.URL_RECURSO}"
        )
        self.driver.get(PerfilDeAcessoNaoLogadoLocators.URL_RECURSO)

    def validar_redirecionamento_para_login(self):
        """
        Valida se o usuário foi redirecionado para a tela de login Microsoft (login.microsoftonline.com).
        """
        try:
            WebDriverWait(self.driver, 15).until(
                EC.url_contains(PerfilDeAcessoNaoLogadoLocators.URL_LOGIN_MICROSOFT)
            )
            logger.info("Usuário foi redirecionado para a tela de login Microsoft.")
            return True
        except TimeoutException:
            logger.error("Usuário não foi redirecionado para a tela de login Microsoft.")
            return False

    def exibir_mensagem_acesso_negado(self):
        """Exibe uma mensagem indicando que o usuário deve realizar login."""
        mensagem = (
            "Usuário deve realizar login antes de acessar uma funcionalidade do sistema"
        )
        logger.info(mensagem)
        return mensagem
