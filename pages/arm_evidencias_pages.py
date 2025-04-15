from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class ArmEvidenciasSelectors:
    """Classe para armazenar os seletores da página de evidências."""
    DIRETRIZ_CURTO_PRAZO = "//a[@href='/pages/diretrizes-short' and contains(@class, 'p-ripple')][span[text()='Diretriz Curto Prazo']]"
    BOTAO_NOVO = "//div[@data-pc-section='start']//button[@label='Novo' and @routerlink='/pages/diretrizes-short-create']"
    CAMPO_DATA_FIM = "//input[@id='fimVigencia' and @placeholder='Data Fim' and @type='text']"
    BOTAO_ANEXAR = "//span[contains(@class, 'p-fileupload-choose') and span[contains(@class, 'p-button-label') and text()='Anexar Evidência']]"
    INPUT_ARQUIVO = "input[type='file']"

class ArmEvidenciasPage:
    def __init__(self, driver):
        self.driver = driver

    def clicar_diretriz_curto_prazo(self):
        """Clica no botão 'Diretriz Curto Prazo'."""
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, ArmEvidenciasSelectors.DIRETRIZ_CURTO_PRAZO))
        ).click()

    def clicar_botao_novo(self):
        """Clica no botão 'Novo'."""
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, ArmEvidenciasSelectors.BOTAO_NOVO))
        ).click()

    def preencher_campo_data_fim(self, data_fim):
        """Preenche o campo 'Data Fim'."""
        campo_data_fim = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, ArmEvidenciasSelectors.CAMPO_DATA_FIM))
        )
        campo_data_fim.click()
        campo_data_fim.clear()
        campo_data_fim.send_keys(data_fim)

    def fazer_upload_evidencia(self, arquivo):
        """Faz o upload de um arquivo de evidência."""
        botao_anexar = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, ArmEvidenciasSelectors.BOTAO_ANEXAR))
        )
        botao_anexar.click()
        caminho_arquivo = os.path.join(os.getcwd(), "arquivos_upload", arquivo)
        if not os.path.exists(caminho_arquivo):
            raise FileNotFoundError(f"O arquivo '{caminho_arquivo}' não foi encontrado.")
        self.driver.find_element(By.CSS_SELECTOR, ArmEvidenciasSelectors.INPUT_ARQUIVO).send_keys(caminho_arquivo)