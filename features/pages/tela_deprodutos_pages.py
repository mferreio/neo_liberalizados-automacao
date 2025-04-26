from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
from credentials import PERFIL_NOVO_PRODUTO

class TelaDeProdutosPageLocators:
    DROPDOWN_ESCOLHER_PERFIL = (By.CSS_SELECTOR, "span.ng-star-inserted")
    PERFIL_CONVENCIONAL = (By.XPATH, "//li[@aria-label='Convencional']")
    PERFIL_I50 = (By.XPATH, "//li[@aria-label='I50']")
    PERFIL_I0 = (By.XPATH, "//li[@aria-label='I0']")
    PERFIL_I100 = (By.XPATH, "//li[@aria-label='I100']")
    PERFIL_CQI5 = (By.XPATH, "//li[@aria-label='CQI5']")
    DROPDOWN_ESCOLHER_SUBMERCADO = (By.CSS_SELECTOR, "span.ng-star-inserted")
    SUBMERCADO_NE = (By.XPATH, "//li[@aria-label='NE']")
    SUBMERCADO_SE = (By.XPATH, "//li[@aria-label='SE']")
    SUBMERCADO_S = (By.XPATH, "//li[@aria-label='S']")
    SUBMERCADO_N = (By.XPATH, "//li[@aria-label='N']")

class TelaDeProdutosPage:
    # ...existing code...

    def obter_opcoes_disponiveis_no_dropdown(self):
        """Abre o dropdown de perfil e extrai as opções disponíveis."""
        try:
            # Abre o dropdown
            logging.info("Abrindo o dropdown de perfil para extrair as opções disponíveis.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TelaDeProdutosPageLocators.DROPDOWN_ESCOLHER_PERFIL)
            ).click()

            # Localiza todas as opções dentro do dropdown
            opcoes = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@class, 'p-dropdown-item')]"))
            )

            # Extrai o texto de cada opção
            opcoes_texto = [opcao.text.strip() for opcao in opcoes if opcao.text.strip()]
            logging.info(f"Opções disponíveis no dropdown: {opcoes_texto}")
            return opcoes_texto
        except TimeoutException:
            logging.error("Erro ao extrair as opções do dropdown de perfil: elemento não encontrado ou não clicável.")
            raise AssertionError("Erro ao extrair as opções do dropdown de perfil.")

    def escolher_perfil(self):
        """Abre o dropdown de perfil e seleciona o perfil de acordo com o arquivo .env."""
        try:
            # Clica no dropdown para abrir as opções
            logging.info("Abrindo o dropdown de perfil.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TelaDeProdutosPageLocators.DROPDOWN_ESCOLHER_PERFIL)
            ).click()

            # Seleciona o perfil com base no valor de PERFIL_NOVO_PRODUTO
            if PERFIL_NOVO_PRODUTO == "CONV":
                perfil = TelaDeProdutosPageLocators.PERFIL_CONVENCIONAL
            elif PERFIL_NOVO_PRODUTO == "I50":
                perfil = TelaDeProdutosPageLocators.PERFIL_I50
            elif PERFIL_NOVO_PRODUTO == "I0":
                perfil = TelaDeProdutosPageLocators.PERFIL_I0
            elif PERFIL_NOVO_PRODUTO == "I100":
                perfil = TelaDeProdutosPageLocators.PERFIL_I100
            elif PERFIL_NOVO_PRODUTO == "CQI5":
                perfil = TelaDeProdutosPageLocators.PERFIL_CQI5
            else:
                raise ValueError(f"Perfil desconhecido: {PERFIL_NOVO_PRODUTO}")

            # Clica no perfil selecionado
            logging.info(f"Selecionando o perfil: {PERFIL_NOVO_PRODUTO}.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(perfil)
            ).click()
            logging.info(f"Perfil '{PERFIL_NOVO_PRODUTO}' selecionado com sucesso.")
        except TimeoutException:
            logging.error("Erro ao selecionar o perfil do produto: elemento não encontrado ou não clicável.")
            raise AssertionError("Erro ao selecionar o perfil do produto.")

    def escolher_submercado(self):
        """Abre o dropdown de submercado e seleciona o submercado de acordo com o arquivo .env."""
        try:
            # Abre o dropdown
            logging.info("Abrindo o dropdown de submercado.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TelaDeProdutosPageLocators.DROPDOWN_ESCOLHER_SUBMERCADO)
            ).click()

            # Seleciona o submercado com base no valor de SUBMERCADO_NOVO_PRODUTO
            if SUBMERCADO_NOVO_PRODUTO == "NE":
                submercado = TelaDeProdutosPageLocators.SUBMERCADO_NE
            elif SUBMERCADO_NOVO_PRODUTO == "SE":
                submercado = TelaDeProdutosPageLocators.SUBMERCADO_SE
            elif SUBMERCADO_NOVO_PRODUTO == "S":
                submercado = TelaDeProdutosPageLocators.SUBMERCADO_S
            elif SUBMERCADO_NOVO_PRODUTO == "N":
                submercado = TelaDeProdutosPageLocators.SUBMERCADO_N
            else:
                raise ValueError(f"Submercado desconhecido: {SUBMERCADO_NOVO_PRODUTO}")

            # Clica no submercado selecionado
            logging.info(f"Selecionando o submercado: {SUBMERCADO_NOVO_PRODUTO}.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(submercado)
            ).click()
            logging.info(f"Submercado '{SUBMERCADO_NOVO_PRODUTO}' selecionado com sucesso.")
        except TimeoutException:
            logging.error("Erro ao selecionar o submercado: elemento não encontrado ou não clicável.")
            raise AssertionError("Erro ao selecionar o submercado.")

    def obter_opcoes_disponiveis_submercado(self):
        """Abre o dropdown de submercado e extrai as opções disponíveis."""
        try:
            # Abre o dropdown
            logging.info("Abrindo o dropdown de submercado para extrair as opções disponíveis.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TelaDeProdutosPageLocators.DROPDOWN_ESCOLHER_SUBMERCADO)
            ).click()

            # Localiza todas as opções dentro do dropdown
            opcoes = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@class, 'p-dropdown-item')]"))
            )

            # Extrai o texto de cada opção
            opcoes_texto = [opcao.text.strip() for opcao in opcoes if opcao.text.strip()]
            logging.info(f"Opções disponíveis no dropdown de submercado: {opcoes_texto}")
            return opcoes_texto
        except TimeoutException:
            logging.error("Erro ao extrair as opções do dropdown de submercado: elemento não encontrado ou não clicável.")
            raise AssertionError("Erro ao extrair as opções do dropdown de submercado.")