
import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from credentials import (SUBMERCADO_NOVO_PRODUTO, PERFIL_NOVO_PRODUTO, ESCOLHER_PERFIL_DE_ENERGIA, ESCOLHER_SUBMERCADO, PERFIL_NOVO_PRODUTO_INVALIDO, SUBMERCADO_NOVO_PROD_INVALIDO)


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
    PRODUTOS_INATIVOS = (
        By.XPATH,
        "//tr[@class='ng-star-inserted']/td[6][span[@class='p-column-title' and text()='Ativo'] and contains(text(), 'Näo')]",
    )
    MES_PRODUTO = (By.XPATH, "//td[1][span[@class='p-column-title' and text()='Mês']]")
    ANO_PRODUTO = (By.XPATH, "//td[2][span[@class='p-column-title' and text()='Ano']]")
    BTN_SIM_EXCLUIR_PROD = (
        By.XPATH,
        "//div[@role='dialog']//button[contains(., 'Sim') and span[@class='p-button-label']]",
    )
    BTN_NAO_EXCLUIR_PROD = (
        By.XPATH,
        "//div[@role='dialog']//button[contains(., 'Não') and span[@class='p-button-label']]",
    )
    MSG_CONFIRMA_EXCLUSAO_PROD = (
        By.XPATH,
        "//p-toast//div[contains(., 'Produto Deletado') and @data-pc-section='detail']",
    )

    URL_TELA_PRODUTOS = "https://diretrizes.dev.neoenergia.net/pages/default-products"
    DROPDOWN_PERFIL_DE_ENERGIA = (
        By.XPATH,
        "//form[@class='p-fluid ng-untouched ng-pristine ng-invalid']//div[@id='pn_id_10' and div[@role='button']]",
    )
    DROPDOWN_SUBMERCADO = (
        By.XPATH,
        "//form[@class='p-fluid ng-untouched ng-pristine ng-invalid']//div[@id='pn_id_5' and div[@role='button']]",
    )


class TelaDeProdutosPage:
    logger = logging.getLogger(__name__)

    def __init__(self, driver):
        self.driver = driver



    logger = logging.getLogger(__name__)

    def validar_tela_cadastro(self):
        """Valida se o elemento da tela de cadastro de produtos está presente."""
        try:
            self.logger.info(
                "Validando a presença do elemento da tela de cadastro de produtos."
            )
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//p[contains(@class, 'text-3xl') and contains(@class, 'font-bold') and contains(@class, 'text-green-500')]",
                    )
                )
            )
            return True
        except TimeoutException:
            self.logger.error("Elemento da tela de cadastro de produtos não encontrado.")
            return False

    def obter_opcoes_disponiveis_no_dropdown(self):
        """Abre o dropdown de perfil e extrai as opções disponíveis."""
        try:
            self.logger.info(
                "Abrindo o dropdown de perfil para extrair as opções disponíveis."
            )
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    TelaDeProdutosPageLocators.DROPDOWN_ESCOLHER_PERFIL
                )
            ).click()

            # Localiza todas as opções dentro do dropdown
            opcoes = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//li[contains(@class, 'p-dropdown-item')]")
                )
            )

            # Extrai o texto de cada opção
            opcoes_texto = [
                opcao.text.strip() for opcao in opcoes if opcao.text.strip()
            ]
            self.logger.info(f"Opções disponíveis no dropdown: {opcoes_texto}")
            return opcoes_texto
        except TimeoutException:
            self.logger.error(
                "Erro ao extrair as opções do dropdown de perfil: elemento não encontrado ou não clicável."
            )
            raise AssertionError("Erro ao extrair as opções do dropdown de perfil.")

    def escolher_perfil(self):
        """Abre o dropdown de perfil e seleciona o perfil de acordo com o arquivo .env."""
        try:
            self.logger.info("Abrindo o dropdown de perfil.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    TelaDeProdutosPageLocators.DROPDOWN_ESCOLHER_PERFIL
                )
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

            self.logger.info(f"Selecionando o perfil: {PERFIL_NOVO_PRODUTO}.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(perfil)
            ).click()
            self.logger.info(f"Perfil '{PERFIL_NOVO_PRODUTO}' selecionado com sucesso.")
        except TimeoutException:
            self.logger.error(
                "Erro ao selecionar o perfil do produto: elemento não encontrado ou não clicável."
            )
            raise AssertionError("Erro ao selecionar o perfil do produto.")

    def escolher_perfil_invalido(self):
        try:
            self.logger.info(
                "Abrindo o dropdown de perfil para selecionar perfil inválido."
            )
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    TelaDeProdutosPageLocators.DROPDOWN_ESCOLHER_PERFIL
                )
            ).click()
            perfil = PERFIL_NOVO_PRODUTO_INVALIDO
            xpath_opcao = f"//li[@aria-label='{perfil}']"
            opcao = self.driver.find_element(By.XPATH, xpath_opcao)
            opcao.click()
            self.logger.info(f"Perfil inválido '{perfil}' selecionado.")
        except Exception as e:
            self.logger.error(f"Erro ao selecionar perfil inválido: {e}")
            raise AssertionError(f"Erro ao selecionar perfil inválido: {e}")

    def escolher_submercado(self):
        """Abre o dropdown de submercado e seleciona o submercado de acordo com o arquivo .env."""
        try:
            self.logger.info("Abrindo o dropdown de submercado.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    TelaDeProdutosPageLocators.DROPDOWN_ESCOLHER_SUBMERCADO
                )
            ).click()

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

            self.logger.info(f"Selecionando o submercado: {SUBMERCADO_NOVO_PRODUTO}.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(submercado)
            ).click()
            self.logger.info(
                f"Submercado '{SUBMERCADO_NOVO_PRODUTO}' selecionado com sucesso."
            )
        except TimeoutException:
            self.logger.error(
                "Erro ao selecionar o submercado: elemento não encontrado ou não clicável."
            )
            raise AssertionError("Erro ao selecionar o submercado.")

    def escolher_submercado_invalido(self):
        try:
            self.logger.info(
                "Abrindo o dropdown de submercado para selecionar submercado inválido."
            )
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    TelaDeProdutosPageLocators.DROPDOWN_ESCOLHER_SUBMERCADO
                )
            ).click()
            submercado = SUBMERCADO_NOVO_PROD_INVALIDO
            xpath_opcao = f"//li[@aria-label='{submercado}']"
            opcao = self.driver.find_element(By.XPATH, xpath_opcao)
            opcao.click()
            self.logger.info(f"Submercado inválido '{submercado}' selecionado.")
        except Exception as e:
            self.logger.error(f"Erro ao selecionar submercado inválido: {e}")
            raise AssertionError(f"Erro ao selecionar submercado inválido: {e}")

    def obter_opcoes_disponiveis_submercado(self):
        """Abre o dropdown de submercado e extrai as opções disponíveis."""
        try:
            self.logger.info(
                "Abrindo o dropdown de submercado para extrair as opções disponíveis."
            )
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    TelaDeProdutosPageLocators.DROPDOWN_ESCOLHER_SUBMERCADO
                )
            ).click()

            opcoes = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//li[contains(@class, 'p-dropdown-item')]")
                )
            )

            opcoes_texto = [
                opcao.text.strip() for opcao in opcoes if opcao.text.strip()
            ]
            self.logger.info(
                f"Opções disponíveis no dropdown de submercado: {opcoes_texto}"
            )
            return opcoes_texto
        except TimeoutException:
            self.logger.error(
                "Erro ao extrair as opções do dropdown de submercado: elemento não encontrado ou não clicável."
            )
            raise AssertionError("Erro ao extrair as opções do dropdown de submercado.")

    def obter_dados_produtos(self):
        """Coleta os dados de todos os produtos listados na tabela."""
        try:
            self.logger.info("Coletando dados dos produtos listados na tabela.")

            linhas = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//tbody/tr[@class='ng-star-inserted']")
                )
            )

            produtos = []

            for linha in linhas:
                mes = linha.find_element(
                    By.XPATH, ".//td[1][span[@class='p-column-title' and text()='Mês']]"
                ).text.strip()
                ano = linha.find_element(
                    By.XPATH, ".//td[2][span[@class='p-column-title' and text()='Ano']]"
                ).text.strip()
                perfil = linha.find_element(
                    By.XPATH, ".//td[span[@class='p-column-title'][text()='Perfil']]"
                ).text.strip()
                submercado = linha.find_element(
                    By.XPATH,
                    ".//td[span[@class='p-column-title'][text()='Submercado']]",
                ).text.strip()
                tipo = linha.find_element(
                    By.XPATH,
                    ".//td[5][span[@class='p-column-title' and text()='Tipo de Produto']]",
                ).text.strip()

                produtos.append(
                    {
                        "mes": mes,
                        "ano": ano,
                        "perfil": perfil,
                        "submercado": submercado,
                        "tipo": tipo,
                    }
                )

            self.logger.info(f"Dados coletados: {produtos}")
            return produtos
        except TimeoutException:
            self.logger.error(
                "Erro ao coletar os dados dos produtos: elemento não encontrado ou não clicável."
            )
            raise AssertionError("Erro ao coletar os dados dos produtos.")

    def obter_novos_produtos(self, produtos_anteriores):
        """Compara a lista atual de produtos com a lista anterior e retorna os novos produtos."""
        try:
            self.logger.info("Coletando a lista atual de produtos para comparação.")
            produtos_atuais = self.obter_dados_produtos()

            novos_produtos = [
                produto
                for produto in produtos_atuais
                if produto not in produtos_anteriores
            ]

            if novos_produtos:
                self.logger.info(f"Novos produtos encontrados: {novos_produtos}")
            else:
                self.logger.info("Nenhum novo produto foi encontrado.")

            return novos_produtos
        except Exception as e:
            self.logger.error(f"Erro ao comparar listas de produtos: {e}")
            raise

    def inativar_produto(self):
        """Seleciona o botão de inativação de um produto e confirma a ação."""
        try:
            self.logger.info("Tentando inativar o produto da primeira linha.")

            botao_inativar = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[@aria-label='desabilitar' and contains(@class, 'p-element') and contains(@class, 'p-ripple') and contains(@class, 'p-button-rounded') and contains(@class, 'p-button-secondary') and contains(@class, 'mr-2') and contains(@class, 'p-button') and contains(@class, 'p-component') and contains(@class, 'p-button-icon-only') and contains(@class, 'ng-star-inserted')]",
                    )
                )
            )
            botao_inativar.click()

            self.logger.info("Botão de inativação clicado com sucesso.")

            botao_confirmar = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//span[contains(@class, 'p-button-label') and text()='Sim']",
                    )
                )
            )
            botao_confirmar.click()

            self.logger.info("Produto inativado com sucesso.")
        except TimeoutException:
            self.logger.error(
                "Erro ao tentar inativar o produto: elemento não encontrado ou não clicável."
            )
            raise AssertionError("Erro ao tentar inativar o produto.")

    def validar_mensagem_inativacao(self):
        """Valida se a mensagem de inativação do produto é exibida e retorna o texto."""
        try:
            self.logger.info("Validando a exibição da mensagem de inativação do produto.")
            mensagem_elemento = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'p-toast-detail')]")
                )
            )
            mensagem_texto = mensagem_elemento.text.strip()
            self.logger.info(f"Mensagem exibida: {mensagem_texto}")
            return mensagem_texto
        except TimeoutException:
            self.logger.error("Mensagem de inativação do produto não foi exibida.")
            return None

    def obter_produtos_inativos(self):
        """Coleta os dados dos produtos inativos listados na tabela."""
        try:
            self.logger.info("Coletando dados dos produtos inativos.")

            produtos_inativos_elementos = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    TelaDeProdutosPageLocators.PRODUTOS_INATIVOS
                )
            )

            produtos_inativos = []

            for elemento in produtos_inativos_elementos:
                mes = elemento.find_element(
                    *TelaDeProdutosPageLocators.MES_PRODUTO
                ).text.strip()
                ano = elemento.find_element(
                    *TelaDeProdutosPageLocators.ANO_PRODUTO
                ).text.strip()

                produtos_inativos.append({"mes": mes, "ano": ano})

            self.logger.info(f"Produtos inativos encontrados: {produtos_inativos}")
            return produtos_inativos
        except TimeoutException:
            self.logger.info("Nenhum produto inativo foi encontrado.")
            return []

    def confirmar_exclusao_produto(self):
        """Clica no botão 'Sim' para confirmar a exclusão de um produto."""
        try:
            self.logger.info("Confirmando a exclusão do produto.")
            botao_sim = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    TelaDeProdutosPageLocators.BTN_SIM_EXCLUIR_PROD
                )
            )
            botao_sim.click()
            self.logger.info("Exclusão do produto confirmada com sucesso.")
        except TimeoutException:
            self.logger.error(
                "Erro ao tentar confirmar a exclusão do produto: botão 'Sim' não encontrado ou não clicável."
            )
            raise AssertionError("Erro ao tentar confirmar a exclusão do produto.")

    def validar_mensagem_confirmacao_exclusao(self):
        """Valida se a mensagem de confirmação da exclusão do produto é exibida e retorna o texto."""
        try:
            self.logger.info(
                "Validando a exibição da mensagem de confirmação da exclusão do produto."
            )
            mensagem_elemento = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    TelaDeProdutosPageLocators.MSG_CONFIRMA_EXCLUSAO_PROD
                )
            )
            mensagem_texto = mensagem_elemento.text.strip()
            self.logger.info(f"Mensagem exibida: {mensagem_texto}")
            return mensagem_texto
        except TimeoutException:
            self.logger.error(
                "Mensagem de confirmação da exclusão do produto não foi exibida."
            )
            return None

    def nao_confirmar_exclusao_produto(self):
        """Não confirma a exclusão de um produto clicando no botão 'Não'."""
        try:
            self.logger.info("Clicando no botão não para a exclusão do produto.")
            botao_nao = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    TelaDeProdutosPageLocators.BTN_NAO_EXCLUIR_PROD
                )
            )
            botao_nao.click()
            self.logger.info("Exclusão do produto não confirmada com sucesso.")
        except TimeoutException:
            self.logger.error(
                "Erro ao tentar não confirmar a exclusão do produto: botão 'Não' não encontrado ou não clicável."
            )
            raise AssertionError("Erro ao tentar não confirmar a exclusão do produto.")

    def validar_tela_produtos(self):
        """Valida se o usuário está na tela de produtos pelo link da página."""
        try:
            self.logger.info("Validando se o usuário está na tela de produtos.")
            current_url = self.driver.current_url
            if current_url == TelaDeProdutosPageLocators.URL_TELA_PRODUTOS:
                self.logger.info("Usuário retornou à tela de produtos com sucesso.")
                return True
            else:
                self.logger.error(
                    f"URL atual ({current_url}) não corresponde à esperada ({TelaDeProdutosPageLocators.URL_TELA_PRODUTOS})."
                )
                return False
        except Exception as e:
            self.logger.error(f"Erro ao validar a tela de produtos: {e}")
            return False

    # def escolher_perfil_de_energia(self):
    #     try:
    #         # Abre o dropdown de perfil de energia
    #         dropdown = self.driver.find_element(
    #             *TelaDeProdutosPageLocators.DROPDOWN_PERFIL_DE_ENERGIA
    #         )
    #         dropdown.click()
    #         # Seleciona o perfil de energia conforme o valor do .env
    #         perfil = ESCOLHER_PERFIL_DE_ENERGIA.upper()
    #         xpath_opcao = f"//li[@aria-label='{perfil}']"
    #         opcao = self.driver.find_element(By.XPATH, xpath_opcao)
    #         opcao.click()
    #         logging.info(f"Perfil de energia '{perfil}' selecionado com sucesso.")
    #     except Exception as e:
    #         logging.error(f"Erro ao selecionar perfil de energia: {e}")
    #         raise AssertionError(f"Erro ao selecionar perfil de energia: {e}")

    def escolher_submercado_dropdown(self):
        try:
            dropdown = self.driver.find_element(
                *TelaDeProdutosPageLocators.DROPDOWN_SUBMERCADO
            )
            dropdown.click()
            submercado = ESCOLHER_SUBMERCADO.upper()
            xpath_opcao = f"//div[@class='p-dropdown-items-wrapper']//li[span[text()='{submercado}']]"
            opcao = self.driver.find_element(By.XPATH, xpath_opcao)
            opcao.click()
            self.logger.info(f"Submercado '{submercado}' selecionado com sucesso.")
        except Exception as e:
            self.logger.error(f"Erro ao selecionar submercado: {e}")
            raise AssertionError(f"Erro ao selecionar submercado: {e}")
