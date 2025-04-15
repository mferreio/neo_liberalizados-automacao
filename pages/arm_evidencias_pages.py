from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

class ArmEvidenciasLocators:
    """Locators para a página de gerenciamento de evidências."""
    BOTAO_UPLOAD = (By.XPATH, "//button[text()='Upload']")
    INPUT_ARQUIVO = (By.XPATH, "//input[@type='file']")
    MENSAGEM_SUCESSO = (By.XPATH, "//div[text()='Arquivo enviado com sucesso']")
    MENSAGEM_ACESSO_NEGADO = (By.XPATH, "//div[text()='Acesso negado. Você não tem permissão para enviar arquivos.']")
    MENSAGEM_ARQUIVO_NAO_ENCONTRADO = (By.XPATH, "//div[text()='Arquivo não encontrado.']")
    BOTAO_DOWNLOAD = (By.XPATH, "//button[text()='Download']")
    MENSAGEM_DOWNLOAD_SUCESSO = (By.XPATH, "//div[text()='Arquivo retornado com sucesso']")

class ArmEvidenciasPage:
    def __init__(self, driver):
        self.driver = driver

    def realizar_upload_arquivo(self, caminho_arquivo):
        """Realiza o upload de um arquivo de evidência."""
        try:
            botao_upload = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(ArmEvidenciasLocators.BOTAO_UPLOAD)
            )
            botao_upload.click()
            input_arquivo = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(ArmEvidenciasLocators.INPUT_ARQUIVO)
            )
            input_arquivo.send_keys(caminho_arquivo)
            logging.info(f"Arquivo '{caminho_arquivo}' enviado com sucesso.")
        except TimeoutException:
            raise AssertionError("Erro ao realizar o upload do arquivo.")

    def verificar_mensagem_sucesso_upload(self):
        """Verifica se a mensagem de sucesso do upload é exibida."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(ArmEvidenciasLocators.MENSAGEM_SUCESSO)
            )
            logging.info("Mensagem de sucesso do upload exibida com sucesso.")
        except TimeoutException:
            raise AssertionError("Mensagem de sucesso do upload não foi exibida.")

    def verificar_mensagem_acesso_negado(self):
        """Verifica se a mensagem de acesso negado é exibida."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(ArmEvidenciasLocators.MENSAGEM_ACESSO_NEGADO)
            )
            logging.info("Mensagem de acesso negado exibida com sucesso.")
        except TimeoutException:
            raise AssertionError("Mensagem de acesso negado não foi exibida.")

    def realizar_download_arquivo(self, nome_arquivo):
        """Realiza o download de um arquivo de evidência."""
        try:
            botao_download = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(ArmEvidenciasLocators.BOTAO_DOWNLOAD)
            )
            botao_download.click()
            logging.info(f"Download do arquivo '{nome_arquivo}' iniciado com sucesso.")
        except TimeoutException:
            raise AssertionError("Erro ao realizar o download do arquivo.")

    def verificar_mensagem_arquivo_nao_encontrado(self):
        """Verifica se a mensagem de arquivo não encontrado é exibida."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(ArmEvidenciasLocators.MENSAGEM_ARQUIVO_NAO_ENCONTRADO)
            )
            logging.info("Mensagem de arquivo não encontrado exibida com sucesso.")
        except TimeoutException:
            raise AssertionError("Mensagem de arquivo não encontrado não foi exibida.")

    def verificar_mensagem_download_sucesso(self):
        """Verifica se a mensagem de sucesso do download é exibida."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(ArmEvidenciasLocators.MENSAGEM_DOWNLOAD_SUCESSO)
            )
            logging.info("Mensagem de sucesso do download exibida com sucesso.")
        except TimeoutException:
            raise AssertionError("Mensagem de sucesso do download não foi exibida.")
