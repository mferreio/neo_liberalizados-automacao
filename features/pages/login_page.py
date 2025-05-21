import logging
logger = logging.getLogger(__name__)
from time import sleep

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPageLocators:
    BOTAO_ENTRAR = (
        By.XPATH,
        "/html/body/app-root/app-login/div/div/div/div/div[2]/button",
    )
    EMAIL_FIELD = (By.XPATH, "//*[@id='i0116']")
    NEXT_BUTTON = (By.XPATH, "//*[@id='idSIButton9']")
    AVANCED_OPTIONS_BUTTON = (By.XPATH, "//*[@id='details-button']")
    GO_TO_NEOENERGIA_BUTTON = (By.XPATH, "//*[@id='proceed-link']")
    ADFS_USERNAME_FIELD = (
        By.XPATH,
        "//input[@type='text' and @placeholder='Nome de usuário']",
    )
    ADFS_PASSWORD_FIELD = (By.XPATH, "//*[@id='passwordInput']")
    ADFS_LOGIN_BUTTON = (By.XPATH, "//*[@id='submitButton']")
    VALIDAR_ADMINISTRADOR = (By.XPATH, "//span[text()='Administrador']")
    VALIDAR_TRADING_E_PORTIFOLIO = (
        By.CSS_SELECTOR,
        "div.p-toolbar-group-left.flex.flex-column.align-items-start.justify-content-center > div.flex.align-items-center.justify-content-between > span.font-bold.text-primary",
    )  # Exemplo de locator para validar portfólio


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        logger.info("Instanciando page object: LoginPage")

    def navegar_para_pagina_de_login(self):
        logger.info("Navegando para a página de login.")
        self.driver.get(
            "https://{USUARIO}:{SENHA}@diretrizes.dev.neoenergia.net/auth/login"
        )

    def acessar_pagina_login(self):
        try:
            logger.info("Aguardando campo de e-mail na página de login.")
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.email_input)
            ).click()
            logger.info("Campo de e-mail localizado e clicado.")
        except TimeoutException as e:
            logger.error(f"TimeoutException: {e}")
            self.driver.save_screenshot("reports/screenshots/timeout_exception.png")
            raise

    def clicar_botao_entrar(self):
        logger.info("Clicando no botão Entrar.")
        botao_entrar = self.driver.find_element(*LoginPageLocators.BOTAO_ENTRAR)
        botao_entrar.click()
        sleep(5)
        logger.info("Botão Entrar clicado.")

    def enter_email(self, email):
        logger.info(f"Preenchendo campo de e-mail com: {email}")
        email_field = self.driver.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)

    def click_next_button(self):
        logger.info("Clicando no botão Próximo.")
        next_button = self.driver.find_element(*LoginPageLocators.NEXT_BUTTON)
        next_button.click()

    def click_opcoes_avancadas_button(self):
        logger.info("Clicando no botão Opções Avançadas.")
        avanced_options_button = self.driver.find_element(
            *LoginPageLocators.AVANCED_OPTIONS_BUTTON
        )
        avanced_options_button.click()

    def click_ir_para_neoenergia_button(self):
        logger.info("Clicando no botão Ir para Neoenergia.")
        ir_neoenergia_button = self.driver.find_element(
            *LoginPageLocators.GO_TO_NEOENERGIA_BUTTON
        )
        ir_neoenergia_button.click()

    def enter_adfs_username(self, username):
        logger.info(f"Preenchendo campo de usuário ADFS com: {username}")
        username_field = self.driver.find_element(
            *LoginPageLocators.ADFS_USERNAME_FIELD
        )
        username_field.send_keys(username)

    def enter_adfs_password(self, password):
        logger.info("Preenchendo campo de senha ADFS.")
        password_field = self.driver.find_element(
            *LoginPageLocators.ADFS_PASSWORD_FIELD
        )
        password_field.send_keys(password)

    def validar_usuario_administrador(self):
        try:
            logger.info("Validando se usuário está logado como Administrador.")
            elemento = self.driver.find_element(
                *LoginPageLocators.VALIDAR_ADMINISTRADOR
            )
            assert elemento is not None, "Usuário não está logado como Administrador."
            logger.info("Usuário logado como administrador.")
        except NoSuchElementException:
            logger.error("Elemento de validação de Administrador não encontrado.")
            raise AssertionError(
                "Elemento de validação de Administrador não encontrado."
            )

    def validar_usuario_portifolio_e_trading(self):
        try:
            logger.info("Validando se usuário está logado como Portfólio e Trading.")
            elemento = self.driver.find_element(
                *LoginPageLocators.VALIDAR_TRADING_E_PORTIFOLIO
            )
            assert (
                elemento is not None
            ), "Usuário não está logado como Portfólio e Trading."
            logger.info("Usuário validado como Portfólio e Trading.")
        except NoSuchElementException:
            logger.error("Elemento de validação de Portfólio e Trading não encontrado.")
            raise AssertionError(
                "Elemento de validação de Portfólio e Trading não encontrado."
            )
