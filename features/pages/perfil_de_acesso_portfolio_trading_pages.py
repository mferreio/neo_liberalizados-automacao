import logging
import traceback
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from credentials import (CONS_PROD_MES, CONS_PROD_PERFIL,CONS_PROD_SUBMERCADO, CONS_PROD_TIPO_DE_PROD)

logger = logging.getLogger(__name__)
class PerfilDeAcessoPortfolioTradingLocators:
    TABELA_DE_NAVEGACAO = (By.XPATH, "//li[div[contains(text(), 'Páginas')]]")
    # Locators para validação do menu restrito
    ABA_PREMIO_SAZO = (By.XPATH, "//li/a[span[contains(text(),'Prêmio Sazonal')]]")
    ABA_PREMIO_FLEX = (By.XPATH, "//li/a[span[contains(text(),'Prêmio Flexível')]]")
    DIRETRIZ_CURTO_PRAZO = (By.XPATH, "//li/a[span[contains(text(),'Curto Prazo')]]")
    DIRETRIZ_I_REC = (By.XPATH, "//li/a[span[contains(text(),'I-REC')]]")
    DIRETRIZ_SEMANAL = (By.XPATH, "//li/a[span[contains(text(),'Diretriz Semanal')]]")
    BTN_NOVO_PRODUTO = (By.XPATH, "//div[@role='toolbar']//button[@label='Novo']")
    # Novo locator para o menu Diario Semanal com o XPath solicitado
    PRODUTO_DIARIO_SEMANAL_MENU = (By.XPATH, "//li/a[@href='/pages/produto-diario-semanal/listar']")
    """Locators para a página de Perfil de Acesso - Trading/Portfólio."""

    VALIDAR_MODULOS_PRODUTOS = (By.XPATH, "//a[span[text()='Produtos']]")
    CLICAR_MODULOS_PRODUTOS = (
        By.XPATH,
        "//a[@class='p-ripple p-element ng-tns-c183498709-14 ng-star-inserted' and span[text()='Produtos']]",
    )
    BOTAO_PRODUTOS = (By.XPATH,"//li/a[span[text()='Produtos']]",)
    MODULO_DIRETRIZES = (By.XPATH, "//div[text()='Diretrizes']")
    MODULO_PROPOSTA_DIRETRIZES = (
        By.XPATH,
        "//div[text()='Prêmio de Proposta de Diretrizes']",
    )
    MODULO_PREMIOS_PADRAO = (By.XPATH, "//div[text()='Prêmios Padrão']")
    MODULO_PREMIOS = (By.XPATH, "//div[text()='Prêmios']")
    BOTAO_VISUALIZAR = (By.XPATH, "//button[text()='Visualizar']")
    BOTAO_EDITAR = (By.XPATH, "//button[text()='Editar']")
    BOTAO_EXCLUIR = (By.XPATH, "//button[text()='Excluir']")
    BOTAO_CRIAR = (By.XPATH, "//button[text()='Criar']")
    MENU_OPCOES = (By.XPATH, "//div[@class='menu-opcoes']")
    IDENTIFICADOR_DE_PERFIL = (By.CSS_SELECTOR,"div.p-toolbar-group-left.flex.flex-column.align-items-start.justify-content-center > div.flex.align-items-center.justify-content-between > span.font-bold.text-primary",)
    PRODUTO_DIARIO_SEMANAL = (By.XPATH, "//li/a[span[text()='Diretriz Semanal']]")
    PRODUTO_I_REC = (By.XPATH, "//li/a[span[text()='I-REC']]")
    PRODUTO_CURTO_PRAZO = (By.XPATH, "//span[text()='Curto Prazo']")
    VALIDAR_PAGINA_PRODUTOS_DIARIOS = (By.XPATH,"//h5[text()='Gerenciar Produtos Diário/Semanal']",)
    PESQUISAR_PROD_POR_ANO = (By.XPATH, "//span/input[@placeholder='Procurar por Ano']")
    BTN_EDITAR_PROD = (By.XPATH,"//tbody//button[@icon='pi pi-pencil']",)
    ABRIR_MODULO_PRODUTOS = (By.XPATH,"//a[contains(@class, 'p-ripple') and contains(@class, 'p-element') and contains(@class, 'ng-tns-c183498709-14')]",)
    TITULO_PAGINA_EDICAO_PRODUTO = (By.XPATH,"//form/*[self::p and contains(text(), 'Editar Produto')]",)
    EXCLUIR_PRODUTO = (By.XPATH, "//button[contains(@class, 'p-button-warning')]")
    VALIDAR_TELA_EXCLUSAO_PRODUTOS = (By.XPATH,"//span[contains(text(), 'Você tem certeza de que quer deletar')]",)
    DROPDOWN_MES = (By.XPATH,"//span[@id='mes' and @role='combobox' and @class='p-element p-dropdown-label p-inputtext p-placeholder ng-star-inserted']",)
    MES_NOVO_PRODUTO = lambda mes: (By.XPATH,f"//span[text()='{mes.upper()}']/parent::li",)
    ANO_NOVO_PRODUTO = (By.XPATH, "//span[@data-pc-name='inputnumber']")
    DROPDOWN_PERFIL = (By.XPATH, "//span[@aria-label='Selecione o perfil']")
    PERFIL_NOVO_PRODUTO = lambda perfil: (By.XPATH, f"//li[@aria-label='{perfil}']")
    DROPDOWN_SUBMERCADO = (By.XPATH, "//span[@aria-label='Selecione o submercado']")
    SUBMERCADO_NOVO_PRODUTO = lambda submercado: (By.XPATH,f"//li[@aria-label='{submercado}']",)
    DROPDOWN_TIPOPRODUTO = (By.XPATH, "//span[@aria-label='Selecione o tipoProduto']")
    TIPOPRODUTO_NOVO_PRODUTO = lambda tipo: (By.XPATH,f"//li[@aria-label='{tipo.upper()}']",)
    BTN_CADASTRAR_PRODUTO = (By.XPATH, "//button[@label='Cadastrar']")


class PerfilDeAcessoPage:

    def verificar_opcoes_menu(self):
        """Valida se a TABELA_DE_NAVEGACAO contém todos os itens esperados no menu lateral."""
        itens_esperados = [
            "Perfil",
            "Diretriz Curto Prazo",
            "Diretriz I-REC",
            "Diretriz Semanal",
            "Diretriz Diária",
            "Diretriz Varejista",
            "Prêmio Sazo",
            "Prêmio Flex",
            "Preços de Mercado e Diretriz",
            "BBCE",
            "CNAE",
            "Shape Determinístico",
            "Produtos"
        ]
        try:
            logger.info("Validando itens do menu lateral na TABELA_DE_NAVEGACAO...")
            tabela = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PerfilDeAcessoPortfolioTradingLocators.TABELA_DE_NAVEGACAO)
            )
            textos = [el.text.strip() for el in tabela.find_elements(By.XPATH, ".//li | .//span | .//a | .//div") if el.text.strip()]
            logger.info(f"Itens encontrados no menu: {textos}")
            for item in itens_esperados:
                if not any(item in texto for texto in textos):
                    logger.error(f"Item '{item}' não encontrado no menu lateral!")
                    raise AssertionError(f"Item '{item}' não encontrado no menu lateral!")
            logger.info("Todos os itens esperados estão presentes no menu lateral.")
            return True
        except Exception as e:
            logger.error(f"Erro ao validar itens do menu lateral: {e}")
            raise AssertionError(f"Erro ao validar itens do menu lateral: {e}")

    def validar_menu_produtos_premios_diretrizes(self):
        """Valida se o menu apresenta apenas as opções de Produtos, Prêmios (Sazonal e Flexível) e Diretrizes (Curto Prazo, I-REC, Semanal)."""
        try:
            logger.info("Validando se o menu apresenta as opções de Produtos, Prêmios e Diretrizes.")
            # Produtos
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    PerfilDeAcessoPortfolioTradingLocators.BOTAO_PRODUTOS
                )
            )
            # Prêmios
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    PerfilDeAcessoPortfolioTradingLocators.ABA_PREMIO_SAZO
                )
            )
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    PerfilDeAcessoPortfolioTradingLocators.ABA_PREMIO_FLEX
                )
            )
            # Diretrizes
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    PerfilDeAcessoPortfolioTradingLocators.DIRETRIZ_CURTO_PRAZO
                )
            )
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    PerfilDeAcessoPortfolioTradingLocators.DIRETRIZ_I_REC
                )
            )
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    PerfilDeAcessoPortfolioTradingLocators.DIRETRIZ_SEMANAL
                )
            )
            logger.info("Menu validado com sucesso: Produtos, Prêmios e Diretrizes visíveis.")
        except TimeoutException as e:
            logger.error(f"Uma ou mais opções do menu não estão visíveis: {e}")
            logger.debug(traceback.format_exc())
            raise AssertionError(f"Uma ou mais opções do menu não estão visíveis: {e}")
        return True

    def clicar_em_novo_produto(self):
        """Clica no botão 'Novo Produto'."""
        try:
            logger.info("Clicando no botão 'Novo Produto'.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    PerfilDeAcessoPortfolioTradingLocators.BTN_NOVO_PRODUTO
                )
            ).click()
            logger.info("Botão 'Novo Produto' clicado com sucesso.")
        except TimeoutException:
            logger.error("Erro ao clicar no botão 'Novo Produto'.")
            logger.debug(traceback.format_exc())
            raise
        sleep(2)

    def acessar_produto_diario_semanal(self):
        """Clica no botão Produtos e depois no menu Diario Semanal pelo XPath correto."""
        try:
            logger.info("Clicando no botão Produtos (menu lateral).")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    PerfilDeAcessoPortfolioTradingLocators.BOTAO_PRODUTOS
                )
            ).click()
            logger.info("Clicando no menu Diario Semanal pelo XPath correto.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    PerfilDeAcessoPortfolioTradingLocators.PRODUTO_DIARIO_SEMANAL_MENU
                )
            ).click()
        except TimeoutException:
            logger.error("Erro ao acessar o produto Diario Semanal na aba produtos.")
            logger.debug(traceback.format_exc())
            raise
        sleep(2)

    def __init__(self, driver):
        self.driver = driver

    def realizar_login_com_perfil(self, perfil):
        """Realiza o login com base no perfil especificado."""
        logger.info(f"Realizando login com o perfil: {perfil}")
        # Implementação do login com base no perfil
        pass

    def validar_acesso_modulos_produtos(self):
        """Valida se o elemento MODULOS_PRODUTOS está visível na tela."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    PerfilDeAcessoPortfolioTradingLocators.VALIDAR_MODULOS_PRODUTOS
                )
            )
            logger.info("Usuário com acesso ao Modulo produtos.")
            return True
        except TimeoutException:
            logger.error("Usuário não tem acesso ao Módulo Produtos.")
            logger.debug(traceback.format_exc())
            return False
        sleep(2)

    def validar_modulos_produtos_existe(self):
        """Valida se o elemento VALIDAR_MODULOS_PRODUTOS está visível na tela."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    PerfilDeAcessoPortfolioTradingLocators.VALIDAR_MODULOS_PRODUTOS
                )
            )
            logger.info("O elemento 'VALIDAR_MODULOS_PRODUTOS' está disponivel.")
            return True
        except TimeoutException:
            logger.error("O elemento 'VALIDAR_MODULOS_PRODUTOS' não está disponivel.")
            logger.debug(traceback.format_exc())
            return False
        sleep(2)

    def clicar_em_produtos(self):
        """Clica no elemento Produtos."""
        try:
            logger.info("Clicando no elemento Produtos.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    PerfilDeAcessoPortfolioTradingLocators.CLICAR_MODULOS_PRODUTOS
                )
            ).click()
            logger.info("Clique no elemento Produtos realizado com sucesso.")
        except TimeoutException:
            logger.error("Erro ao clicar no elemento Produtos.")
            logger.debug(traceback.format_exc())
            raise
        sleep(2)

    def visualizar_modulo_produtos(self):
        """Visualiza o módulo de produtos."""
        try:
            botao_visualizar = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    PerfilDeAcessoPortfolioTradingLocators.BOTAO_VISUALIZAR
                )
            )
            botao_visualizar.click()
            logger.info("Módulo de produtos visualizado com sucesso.")
        except TimeoutException:
            logger.error("Erro ao visualizar o módulo de produtos.")
            logger.debug(traceback.format_exc())
            raise AssertionError("Erro ao visualizar o módulo de produtos.")
        sleep(2)

    def editar_modulo_produtos(self):
        """Edita o módulo de produtos."""
        try:
            botao_editar = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    PerfilDeAcessoPortfolioTradingLocators.BOTAO_EDITAR
                )
            )
            botao_editar.click()
            logger.info("Módulo de produtos editado com sucesso.")
        except TimeoutException:
            logger.error("Erro ao editar o módulo de produtos.")
            logger.debug(traceback.format_exc())
            raise AssertionError("Erro ao editar o módulo de produtos.")
        sleep(2)

    def excluir_produto(self):
        """Exclui um produto."""
        try:
            botao_excluir = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    PerfilDeAcessoPortfolioTradingLocators.BOTAO_EXCLUIR
                )
            )
            botao_excluir.click()
            logger.info("Produto excluído com sucesso.")
        except TimeoutException:
            logger.error("Erro ao excluir o produto.")
            logger.debug(traceback.format_exc())
            raise AssertionError("Erro ao excluir o produto.")
        sleep(2)

    def criar_dados(self):
        """Cria novos dados."""
        try:
            botao_criar = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    PerfilDeAcessoPortfolioTradingLocators.BOTAO_CRIAR
                )
            )
            botao_criar.click()
            logger.info("Dados criados com sucesso.")
        except TimeoutException:
            logger.error("Erro ao criar dados.")
            logger.debug(traceback.format_exc())
            raise AssertionError("Erro ao criar dados.")
        sleep(2)


    def validar_texto_perfil(self, texto_esperado):
        """Valida se o texto do elemento IDENTIFICADOR_DE_PERFIL corresponde ao texto esperado."""
        try:
            elemento = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    PerfilDeAcessoPortfolioTradingLocators.IDENTIFICADOR_DE_PERFIL
                )
            )
            texto_elemento = elemento.text.strip()
            logger.info(f"Texto encontrado no perfil: {texto_elemento}")
            return texto_elemento == texto_esperado
        except TimeoutException:
            logger.error("Elemento IDENTIFICADOR_DE_PERFIL não encontrado.")
            logger.debug(traceback.format_exc())
            return False
        sleep(2)

    def validar_acesso_diretrizes(self):
        """Valida se os módulos especificados estão visíveis na tela."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    PerfilDeAcessoPortfolioTradingLocators.PRODUTO_DIARIO_SEMANAL
                )
            )
            logger.info("Usuário com acesso ao produto Semanal/Diário.")
        except TimeoutException:
            logger.error("Erro: Produto Semanal/Diário não está visível na tela.")
            logger.debug(traceback.format_exc())
            return False

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    PerfilDeAcessoPortfolioTradingLocators.PRODUTO_I_REC
                )
            )
            logger.info("Usuário com acesso ao produto I-Rec.")
        except TimeoutException:
            logger.error("Erro: Produto I-Rec não está visível na tela.")
            logger.debug(traceback.format_exc())
            return False

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    PerfilDeAcessoPortfolioTradingLocators.PRODUTO_CURTO_PRAZO
                )
            )
            logger.info("Usuário com acesso ao produto Curto Prazo.")
        except TimeoutException:
            logger.error("Erro: Produto Curto Prazo não está visível na tela.")
            logger.debug(traceback.format_exc())
            return False

        sleep(2)
        return True


    def clicar_aba_produtos(self):
        """Clica no elemento VALIDAR_MODULOS_PRODUTOS."""
        try:
            logger.info("Clicando na aba produtos.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    PerfilDeAcessoPortfolioTradingLocators.ABRIR_MODULO_PRODUTOS
                )
            ).click()
        except TimeoutException:
            logger.error("Erro ao clicar na aba produtos.")
            logger.debug(traceback.format_exc())
            raise
        sleep(2)

    def selecionar_produto_diario_semanal(self):
        """Clica no elemento PRODUTO_DIARIO_SEMANAL."""
        try:
            logger.info("Selecionando o produto Diário Semanal.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    PerfilDeAcessoPortfolioTradingLocators.PRODUTO_DIARIO_SEMANAL
                )
            ).click()
        except TimeoutException:
            logger.error("Erro ao selecionar o produto Diário Semanal.")
            logger.debug(traceback.format_exc())
            raise
        sleep(2)

    def pesquisar_por_ano(self):
        """Pesquisa pelo ano utilizando o valor de CONS_PROD_ANO."""
        from credentials import CONS_PROD_ANO

        try:
            logger.info(f"Pesquisando pelo ano: {CONS_PROD_ANO}.")
            campo_ano = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    PerfilDeAcessoPortfolioTradingLocators.PESQUISAR_PROD_POR_ANO
                )
            )
            campo_ano.clear()
            campo_ano.send_keys(CONS_PROD_ANO)
            sleep(1)
            campo_ano.send_keys(Keys.ENTER)
        except TimeoutException:
            logger.error("Erro ao pesquisar pelo ano.")
            logger.debug(traceback.format_exc())
            raise
        sleep(2)

    def selecionar_produto_estipulado(self):
        try:
            logger.info("Selecionando o produto de acordo com as especificações.")
            # Implementar lógica para selecionar o produto com base nos valores de CONS_PROD_MES, CONS_PROD_PERFIL, CONS_PROD_SUBMERCADO e CONS_PROD_TIPO_DE_PROD
        except TimeoutException:
            logger.error("Erro ao selecionar o produto estipulado.")
            logger.debug(traceback.format_exc())
            raise
        sleep(2)

    def clicar_botao_editar(self):
        """Clica no botão editar."""
        try:
            logger.info("Buscando todos os botões editar na tela.")
            botoes_editar = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    PerfilDeAcessoPortfolioTradingLocators.BTN_EDITAR_PROD
                )
            )
            if not botoes_editar:
                logger.error("Nenhum botão editar encontrado na tela.")
                raise AssertionError("Nenhum botão editar encontrado na tela.")
            primeiro_botao = botoes_editar[0]
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
                PerfilDeAcessoPortfolioTradingLocators.BTN_EDITAR_PROD
            ))
            primeiro_botao.click()
            logger.info("Primeiro botão editar clicado com sucesso.")
        except TimeoutException:
            logger.error("Timeout ao buscar ou clicar no botão editar.")
            logger.debug(traceback.format_exc())
            raise
        except Exception as e:
            logger.error(f"Erro inesperado ao clicar no botão editar: {e}")
            logger.debug(traceback.format_exc())
            raise
        sleep(2)

    def validar_pagina_edicao_produto(self):
        """Valida se o título da página de edição do produto está visível."""
        try:
            logger.info(
                "Validando a existência do título da página de edição do produto."
            )
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    PerfilDeAcessoPortfolioTradingLocators.TITULO_PAGINA_EDICAO_PRODUTO
                )
            )
            logger.info(
                "Título da página de edição do produto encontrado com sucesso."
            )
            return True
        except TimeoutException:
            logger.error("Título da página de edição do produto não encontrado.")
            logger.debug(traceback.format_exc())
            return False
        sleep(2)

    def clicar_botao_excluir(self):
        """Clica no botão excluir."""
        try:
            logger.info("Clicando no botão excluir.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    PerfilDeAcessoPortfolioTradingLocators.EXCLUIR_PRODUTO
                )
            ).click()
            logger.info("Botão excluir clicado com sucesso.")
        except TimeoutException:
            logger.error("Erro ao clicar no botão excluir.")
            logger.debug(traceback.format_exc())
            raise

    def validar_tela_exclusao_produto(self):
        """Valida se a tela de exclusão do produto está visível."""
        try:
            logger.info("Validando a existência da tela de exclusão do produto.")
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    PerfilDeAcessoPortfolioTradingLocators.VALIDAR_TELA_EXCLUSAO_PRODUTOS
                )
            )
            logger.info("Tela de exclusão do produto validada com sucesso.")
            return True
        except TimeoutException:
            logger.error("Tela de exclusão do produto não encontrada.")
            logger.debug(traceback.format_exc())
            return False
        sleep(2)

    def clicar_em_cadastrar_produto(self):
        """Clica no botão 'Cadastrar Produto'."""
        try:
            logger.info("Clicando no botão 'Cadastrar Produto'.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    PerfilDeAcessoPortfolioTradingLocators.BTN_CADASTRAR_PRODUTO
                )
            ).click()
            logger.info("Botão 'Cadastrar Produto' clicado com sucesso.")
        except TimeoutException:
            logger.error("Erro ao clicar no botão 'Cadastrar Produto'.")
            logger.debug(traceback.format_exc())
            raise

    def preencher_campos_obrigatorios(self):
        """Preenche os campos obrigatórios para criar um novo produto."""
        from credentials import (ANO_NOVO_PRODUTO, MES_NOVO_PRODUTO,
                                 PERFIL_NOVO_PRODUTO, SUBMERCADO_NOVO_PRODUTO,
                                 TIPOPRODUTO_NOVO_PRODUTO)

        try:
            # Selecionar o mês
            logger.info("Abrindo o dropdown de mês.")
            self._interagir_com_elemento(
                PerfilDeAcessoPortfolioTradingLocators.DROPDOWN_MES
            )
            logger.info(f"Selecionando o mês: {MES_NOVO_PRODUTO}.")
            self._interagir_com_elemento(
                PerfilDeAcessoPortfolioTradingLocators.MES_NOVO_PRODUTO(
                    MES_NOVO_PRODUTO
                )
            )

            # Informar o ano
            logger.info(f"Informando o ano: {ANO_NOVO_PRODUTO}.")
            ano_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    PerfilDeAcessoPortfolioTradingLocators.ANO_NOVO_PRODUTO
                )
            )
            ano_input.clear()
            ano_input.send_keys(ANO_NOVO_PRODUTO)

            # Selecionar o perfil
            logger.info("Abrindo o dropdown de perfil.")
            self._interagir_com_elemento(
                PerfilDeAcessoPortfolioTradingLocators.DROPDOWN_PERFIL
            )
            logger.info(f"Selecionando o perfil: {PERFIL_NOVO_PRODUTO}.")
            self._interagir_com_elemento(
                PerfilDeAcessoPortfolioTradingLocators.PERFIL_NOVO_PRODUTO(
                    PERFIL_NOVO_PRODUTO
                )
            )

            # Selecionar o submercado
            logger.info("Abrindo o dropdown de submercado.")
            self._interagir_com_elemento(
                PerfilDeAcessoPortfolioTradingLocators.DROPDOWN_SUBMERCADO
            )
            logger.info(f"Selecionando o submercado: {SUBMERCADO_NOVO_PRODUTO}.")
            self._interagir_com_elemento(
                PerfilDeAcessoPortfolioTradingLocators.SUBMERCADO_NOVO_PRODUTO(
                    SUBMERCADO_NOVO_PRODUTO
                )
            )

            # Selecionar o tipo de produto
            logger.info("Abrindo o dropdown de tipo de produto.")
            self._interagir_com_elemento(
                PerfilDeAcessoPortfolioTradingLocators.DROPDOWN_TIPOPRODUTO
            )
            logger.info(f"Selecionando o tipo de produto: {TIPOPRODUTO_NOVO_PRODUTO}.")
            self._interagir_com_elemento(
                PerfilDeAcessoPortfolioTradingLocators.TIPOPRODUTO_NOVO_PRODUTO(
                    TIPOPRODUTO_NOVO_PRODUTO
                )
            )

        except TimeoutException as e:
            logger.error(f"Erro ao preencher os campos obrigatórios: {e}")
            logger.debug(traceback.format_exc())
            raise

    def _interagir_com_elemento(self, locator):
        """Interage com um elemento, utilizando JavaScript caso necessário."""
        try:
            elemento = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            elemento.click()
        except Exception:
            logger.warning("Interagindo com o elemento via JavaScript.")
            elemento = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", elemento)
