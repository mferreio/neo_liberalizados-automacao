from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

class DiretrizIrecLocators:
    """Locators centralizados para a tela de Diretriz I-REC."""
    ABA_DIRETRIZ_IREC = (By.XPATH, "//a[contains(@class, 'p-ripple') and contains(@class, 'p-element') and contains(@class, 'ng-tns-c773887693-7') and contains(@class, 'ng-star-inserted')]")
    BTN_NOVA_DIRETRIZ = (By.XPATH, "//span[contains(@class, 'p-button-label')]")
    CAMPO_DESCRICAO = (By.ID, "descricao")
    CAMPO_PRECO = (By.ID, "preco")
    CAMPO_DATA_INICIO = (By.ID, "dataInicio")
    CAMPO_DATA_FIM = (By.ID, "dataFim")
    BOTAO_SALVAR = (By.XPATH, "//button[span[text()='Salvar']]")
    BOTAO_INVALIDAR_ANTERIOR = (By.XPATH, "//button[span[text()='Invalidar Anterior']]")
    MENSAGEM_SUCESSO = (By.XPATH, "//div[contains(@class, 'p-toast-detail') and contains(text(), 'sucesso')]")
    # Adicione outros locators conforme necessário

class DiretrizIrecPage:
    """
    Page Object para a tela de Diretriz I-REC.
    Todos os métodos são genéricos e reutilizáveis para steps BDD parametrizados.
    """
    def __init__(self, driver):
        self.driver = driver

    def acessar_aba_diretriz_irec(self):
        """Acessa a aba Diretriz I-REC no menu lateral."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(DiretrizIrecLocators.ABA_DIRETRIZ_IREC)
        ).click()
        logging.info("Aba Diretriz I-REC acessada.")

    def clicar_nova_diretriz(self):
        """Clica no botão para iniciar o cadastro de nova diretriz."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(DiretrizIrecLocators.BTN_NOVA_DIRETRIZ)
        ).click()
        logging.info("Botão Nova Diretriz clicado.")

    def navegar_para_cadastro(self):
        """Fluxo completo para acessar a tela de cadastro de diretriz I-REC."""
        try:
            self.acessar_aba_diretriz_irec()
            self.clicar_nova_diretriz()
        except TimeoutException:
            raise AssertionError("Não foi possível acessar a tela de cadastro de diretriz I-REC.")

    def preencher_dados(self, descricao, preco, data_inicio, data_fim=None):
        """Preenche os campos do formulário de cadastro de diretriz."""
        self.driver.find_element(*DiretrizIrecLocators.CAMPO_DESCRICAO).send_keys(descricao)
        self.driver.find_element(*DiretrizIrecLocators.CAMPO_PRECO).send_keys(preco)
        self.driver.find_element(*DiretrizIrecLocators.CAMPO_DATA_INICIO).send_keys(data_inicio)
        if data_fim:
            self.driver.find_element(*DiretrizIrecLocators.CAMPO_DATA_FIM).send_keys(data_fim)
        logging.info("Preencheu os dados da nova diretriz I-REC.")

    def clicar_botao(self, botao_nome):
        """Clica em um botão da tela pelo nome parametrizado."""
        if botao_nome.lower() == "salvar":
            self.driver.find_element(*DiretrizIrecLocators.BOTAO_SALVAR).click()
        elif botao_nome.lower() == "invalidar anterior":
            self.driver.find_element(*DiretrizIrecLocators.BOTAO_INVALIDAR_ANTERIOR).click()
        else:
            raise ValueError(f"Botão '{botao_nome}' não mapeado.")
        logging.info(f"Clicou no botão '{botao_nome}'.")

    def validar_cadastro(self):
        """Valida se a mensagem de sucesso do cadastro foi exibida."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(DiretrizIrecLocators.MENSAGEM_SUCESSO)
            )
            logging.info("Cadastro de diretriz I-REC validado com sucesso.")
            return True
        except TimeoutException:
            logging.error("Mensagem de sucesso não exibida após cadastro.")
            return False

    def invalidar_anterior(self):
        """Clica no botão para invalidar a diretriz anterior."""
        self.clicar_botao("invalidar anterior")
        logging.info("Diretriz anterior invalidada.")

    def validar_datas_vigencia(self):
        """Valida as datas de vigência na tela (implemente conforme a regra de negócio)."""
        logging.info("Validação das datas de vigência executada.")
        pass

# Adapte os locators e métodos conforme a implementação real da tela de diretriz I-REC.
