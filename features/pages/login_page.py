from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

class LoginPageLocators:
    BOTAO_ENTRAR = (By.XPATH, "/html/body/app-root/app-login/div/div/div/div/div[2]/button")
    EMAIL_FIELD = (By.XPATH, "//*[@id='i0116']")
    NEXT_BUTTON = (By.XPATH, "//*[@id='idSIButton9']")
    AVANCED_OPTIONS_BUTTON = (By.XPATH, "//*[@id='details-button']")
    GO_TO_NEOENERGIA_BUTTON = (By.XPATH, "//*[@id='proceed-link']")
    ADFS_USERNAME_FIELD = (By.XPATH, "//input[@type='text' and @placeholder='Nome de usuário']")
    ADFS_PASSWORD_FIELD = (By.XPATH, "//*[@id='passwordInput']")
    ADFS_LOGIN_BUTTON = (By.XPATH, "//*[@id='submitButton']")


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def navegar_para_pagina_de_login(self):
        self.driver.get("https://{USUARIO}:{SENHA}@diretrizes.dev.neoenergia.net/auth/login")

    def acessar_pagina_login(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.email_input)
            ).click()
        except TimeoutException as e:
            print(f"TimeoutException: {e}")
            self.driver.save_screenshot('reports/screenshots/timeout_exception.png')
            raise

    def clicar_botao_entrar(self):
        botao_entrar = self.driver.find_element(*LoginPageLocators.BOTAO_ENTRAR)
        botao_entrar.click()
        sleep(5)

    def enter_email(self, email):
        email_field = self.driver.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        
    def click_next_button(self):
        next_button = self.driver.find_element(*LoginPageLocators.NEXT_BUTTON)
        next_button.click()
        
    def click_opcoes_avancadas_button(self):
        avanced_options_button = self.driver.find_element(*LoginPageLocators.AVANCED_OPTIONS_BUTTON)
        avanced_options_button.click()
        
    def click_ir_para_neoenergia_button(self):
        ir_neoenergia_button = self.driver.find_element(*LoginPageLocators.GO_TO_NEOENERGIA_BUTTON)
        ir_neoenergia_button.click()

    def enter_adfs_username(self, username):
        username_field = self.driver.find_element(*LoginPageLocators.ADFS_USERNAME_FIELD)
        username_field.send_keys(username)

    def enter_adfs_password(self, password):
        password_field = self.driver.find_element(*LoginPageLocators.ADFS_PASSWORD_FIELD)
        password_field.send_keys(password)