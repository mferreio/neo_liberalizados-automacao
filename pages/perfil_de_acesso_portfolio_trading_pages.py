from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
from time import sleep

class PerfilDeAcessoPortfolioTradingLocators:
    """Locators para a página de Perfil de Acesso - Trading/Portfólio."""
    MODULOS_PRODUTOS = (By.XPATH, "//div[@class='modulos-produtos']")
    MODULO_ESPECIFICO = (By.XPATH, "//div[@class='modulo-especifico']")
    BOTAO_VISUALIZAR = (By.XPATH, "//button[text()='Visualizar']")
    BOTAO_EDITAR = (By.XPATH, "//button[text()='Editar']")
    BOTAO_EXCLUIR = (By.XPATH, "//button[text()='Excluir']")
    BOTAO_CRIAR = (By.XPATH, "//button[text()='Criar']")
    MENU_OPCOES = (By.XPATH, "//div[@class='menu-opcoes']")

class PerfilDeAcessoPage:
    def __init__(self, driver):
        self.driver = driver

    def realizar_login_com_perfil(self, perfil):
        """Realiza o login com base no perfil especificado."""
        logging.info(f"Realizando login com o perfil: {perfil}")
        # Implementação do login com base no perfil
        pass

    def verificar_acesso_modulos_produtos(self):
        """Verifica se o usuário tem acesso aos módulos de produtos."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PerfilDeAcessoPortfolioTradingLocators.MODULOS_PRODUTOS)
            )
            logging.info("Acesso aos módulos de produtos verificado com sucesso.")
        except TimeoutException:
            raise AssertionError("Usuário não tem acesso aos módulos de produtos.")

    def verificar_acesso_modulo_especifico(self, modulo):
        """Verifica se o usuário tem acesso a um módulo específico."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PerfilDeAcessoPortfolioTradingLocators.MODULO_ESPECIFICO)
            )
            logging.info(f"Acesso ao módulo '{modulo}' verificado com sucesso.")
        except TimeoutException:
            raise AssertionError(f"Usuário não tem acesso ao módulo '{modulo}'.")

    def visualizar_modulo_produtos(self):
        """Visualiza o módulo de produtos."""
        try:
            botao_visualizar = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PerfilDeAcessoPortfolioTradingLocators.BOTAO_VISUALIZAR)
            )
            botao_visualizar.click()
            logging.info("Módulo de produtos visualizado com sucesso.")
        except TimeoutException:
            raise AssertionError("Erro ao visualizar o módulo de produtos.")

    def editar_modulo_produtos(self):
        """Edita o módulo de produtos."""
        try:
            botao_editar = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PerfilDeAcessoPortfolioTradingLocators.BOTAO_EDITAR)
            )
            botao_editar.click()
            logging.info("Módulo de produtos editado com sucesso.")
        except TimeoutException:
            raise AssertionError("Erro ao editar o módulo de produtos.")

    def excluir_produto(self):
        """Exclui um produto."""
        try:
            botao_excluir = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PerfilDeAcessoPortfolioTradingLocators.BOTAO_EXCLUIR)
            )
            botao_excluir.click()
            logging.info("Produto excluído com sucesso.")
        except TimeoutException:
            raise AssertionError("Erro ao excluir o produto.")

    def criar_dados(self):
        """Cria novos dados."""
        try:
            botao_criar = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PerfilDeAcessoPortfolioTradingLocators.BOTAO_CRIAR)
            )
            botao_criar.click()
            logging.info("Dados criados com sucesso.")
        except TimeoutException:
            raise AssertionError("Erro ao criar dados.")

    def verificar_opcoes_menu(self):
        """Verifica se o menu apresenta as opções corretas."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PerfilDeAcessoPortfolioTradingLocators.MENU_OPCOES)
            )
            logging.info("Opções do menu verificadas com sucesso.")
        except TimeoutException:
            raise AssertionError("Erro ao verificar as opções do menu.")