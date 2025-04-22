from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
from time import sleep
import ipdb
from selenium.webdriver.common.keys import Keys

class PerfilDeAcessoPortfolioTradingLocators:
    """Locators para a página de Perfil de Acesso - Trading/Portfólio."""
    VALIDAR_MODULOS_PRODUTOS = (By.XPATH, "//a[span[text()='Produtos']]")
    CLICAR_MODULOS_PRODUTOS = (By.XPATH, "//a[@class='p-ripple p-element ng-tns-c183498709-14 ng-star-inserted' and span[text()='Produtos']]")
    BOTAO_PRODUTOS = (By.XPATH, "//li[@class='ng-tns-c183498709-19 ng-tns-c183498709-10 ng-star-inserted']")
    MODULO_DIRETRIZES = (By.XPATH, "//div[text()='Diretrizes']")
    MODULO_PROPOSTA_DIRETRIZES = (By.XPATH, "//div[text()='Prêmio de Proposta de Diretrizes']")
    MODULO_PREMIOS_PADRAO = (By.XPATH, "//div[text()='Prêmios Padrão']")
    MODULO_PREMIOS = (By.XPATH, "//div[text()='Prêmios']")
    BOTAO_VISUALIZAR = (By.XPATH, "//button[text()='Visualizar']")
    BOTAO_EDITAR = (By.XPATH, "//button[text()='Editar']")
    BOTAO_EXCLUIR = (By.XPATH, "//button[text()='Excluir']")
    BOTAO_CRIAR = (By.XPATH, "//button[text()='Criar']")
    MENU_OPCOES = (By.XPATH, "//div[@class='menu-opcoes']")
    IDENTIFICADOR_DE_PERFIL = (By.CSS_SELECTOR, "div.p-toolbar-group-left.flex.flex-column.align-items-start.justify-content-center > div.flex.align-items-center.justify-content-between > span.font-bold.text-primary")
    PRODUTO_DIARIO_SEMANAL = (By.XPATH, "//a[@href='/pages/default-products']")
    PRODUTO_I_REC = (By.XPATH, "//a[@href='/pages/irec-products']/span[text()='I-REC']")
    PRODUTO_CURTO_PRAZO = (By.XPATH, "//span[text()='Curto Prazo']")
    VALIDAR_PAGINA_PRODUTOS_DIARIOS = (By.XPATH, "//h5[text()='Gerenciar Produtos Diário/Semanal']")
    PESQUISAR_PROD_POR_ANO = (By.XPATH, "//input[@placeholder='Procurar por ano']")
    BTN_EDITAR_PROD = (By.CSS_SELECTOR, "div.flex > button.p-element.p-ripple.p-button-rounded.p-button-success.mr-2.p-button.p-component.p-button-icon-only.ng-star-inserted > span.p-button-icon.pi.pi-pencil")
    ABRIR_MODULO_PRODUTOS = (By.XPATH, "//a[contains(@class, 'p-ripple') and contains(@class, 'p-element') and contains(@class, 'ng-tns-c183498709-14')]")
    TITULO_PAGINA_EDICAO_PRODUTO = (By.CSS_SELECTOR, "div.card.px-6.py-6 > div.p-fluid > p.text-3xl.font-bold.text-green-500")

class PerfilDeAcessoPage:
    def __init__(self, driver):
        self.driver = driver

    def realizar_login_com_perfil(self, perfil):
        """Realiza o login com base no perfil especificado."""
        logging.info(f"Realizando login com o perfil: {perfil}")
        # Implementação do login com base no perfil
        pass

    def validar_acesso_modulos_produtos(self):
        """Valida se o elemento MODULOS_PRODUTOS está visível na tela."""
        try:
            ipdb.set_trace()  # Inicia o depurador
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PerfilDeAcessoPortfolioTradingLocators.VALIDAR_MODULOS_PRODUTOS)
            )
            logging.info("Usuário com acesso ao Modulo produtos.")
            return True
        except TimeoutException:
            logging.error("Usuário não tem acesso ao Módulo Produtos.")
            ipdb.set_trace()  # Inicia o depurador para analisar o erro
            return False
        sleep(2)

    def validar_modulos_produtos_existe(self):
        """Valida se o elemento VALIDAR_MODULOS_PRODUTOS está visível na tela."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PerfilDeAcessoPortfolioTradingLocators.VALIDAR_MODULOS_PRODUTOS)
            )
            logging.info("O elemento 'VALIDAR_MODULOS_PRODUTOS' está disponivel.")
            return True
        except TimeoutException:
            logging.error("O elemento 'VALIDAR_MODULOS_PRODUTOS' não está disponivel.")
            return False
        sleep(2)

    def clicar_em_produtos(self):
        """Clica no elemento Produtos."""
        try:
            ipdb.set_trace()  # Inicia o depurador
            logging.info("Clicando no elemento Produtos.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PerfilDeAcessoPortfolioTradingLocators.CLICAR_MODULOS_PRODUTOS)
            ).click()
            logging.info("Clique no elemento Produtos realizado com sucesso.")
        except TimeoutException:
            logging.error("Erro ao clicar no elemento Produtos.")
            ipdb.set_trace()  # Inicia o depurador para analisar o erro
            raise
        sleep(2)

    def visualizar_modulo_produtos(self):
        """Visualiza o módulo de produtos."""
        try:
            ipdb.set_trace()  # Inicia o depurador
            botao_visualizar = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PerfilDeAcessoPortfolioTradingLocators.BOTAO_VISUALIZAR)
            )
            botao_visualizar.click()
            logging.info("Módulo de produtos visualizado com sucesso.")
        except TimeoutException:
            raise AssertionError("Erro ao visualizar o módulo de produtos.")
        sleep(2)

    def editar_modulo_produtos(self):
        """Edita o módulo de produtos."""
        try:
            ipdb.set_trace()  # Inicia o depurador
            botao_editar = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PerfilDeAcessoPortfolioTradingLocators.BOTAO_EDITAR)
            )
            botao_editar.click()
            logging.info("Módulo de produtos editado com sucesso.")
        except TimeoutException:
            raise AssertionError("Erro ao editar o módulo de produtos.")
        sleep(2)

    def excluir_produto(self):
        """Exclui um produto."""
        try:
            ipdb.set_trace()  # Inicia o depurador
            botao_excluir = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PerfilDeAcessoPortfolioTradingLocators.BOTAO_EXCLUIR)
            )
            botao_excluir.click()
            logging.info("Produto excluído com sucesso.")
        except TimeoutException:
            raise AssertionError("Erro ao excluir o produto.")
        sleep(2)

    def criar_dados(self):
        """Cria novos dados."""
        try:
            ipdb.set_trace()  # Inicia o depurador
            botao_criar = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PerfilDeAcessoPortfolioTradingLocators.BOTAO_CRIAR)
            )
            botao_criar.click()
            logging.info("Dados criados com sucesso.")
        except TimeoutException:
            raise AssertionError("Erro ao criar dados.")
        sleep(2)

    def verificar_opcoes_menu(self):
        """Verifica se o menu apresenta as opções corretas."""
        try:
            ipdb.set_trace()  # Inicia o depurador
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PerfilDeAcessoPortfolioTradingLocators.MENU_OPCOES)
            )
            logging.info("Opções do menu verificadas com sucesso.")
        except TimeoutException:
            raise AssertionError("Erro ao verificar as opções do menu.")
        sleep(2)

    def validar_texto_perfil(self, texto_esperado):
        """Valida se o texto do elemento IDENTIFICADOR_DE_PERFIL corresponde ao texto esperado."""
        try:
            ipdb.set_trace()  # Inicia o depurador
            elemento = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PerfilDeAcessoPortfolioTradingLocators.IDENTIFICADOR_DE_PERFIL)
            )
            texto_elemento = elemento.text.strip()
            logging.info(f"Texto encontrado no perfil: {texto_elemento}")
            return texto_elemento == texto_esperado
        except TimeoutException:
            logging.error("Elemento IDENTIFICADOR_DE_PERFIL não encontrado.")
            return False
        sleep(2)

    def validar_acesso_diretrizes(self):
        """Valida se os módulos especificados estão visíveis na tela."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PerfilDeAcessoPortfolioTradingLocators.PRODUTO_DIARIO_SEMANAL)
            )
            logging.info("Usuário com acesso ao produto Semanal/Diário.")
        except TimeoutException:
            logging.error("Erro: Produto Semanal/Diário não está visível na tela.")
            ipdb.set_trace()  # Inicia o depurador para analisar o erro
            return False

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PerfilDeAcessoPortfolioTradingLocators.PRODUTO_I_REC)
            )
            logging.info("Usuário com acesso ao produto I-Rec.")
        except TimeoutException:
            logging.error("Erro: Produto I-Rec não está visível na tela.")
            ipdb.set_trace()  # Inicia o depurador para analisar o erro
            return False

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PerfilDeAcessoPortfolioTradingLocators.PRODUTO_CURTO_PRAZO)
            )
            logging.info("Usuário com acesso ao produto Curto Prazo.")
        except TimeoutException:
            logging.error("Erro: Produto Curto Prazo não está visível na tela.")
            ipdb.set_trace()  # Inicia o depurador para analisar o erro
            return False

        sleep(2)
        return True

    def acessar_premio_proposta_diretrizes(self):
        """Clica no elemento VALIDAR_MODULOS_PRODUTOS, depois no link de produtos e valida o título."""
        try:
            logging.info("Clicando no elemento VALIDAR_MODULOS_PRODUTOS.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PerfilDeAcessoPortfolioTradingLocators.VALIDAR_MODULOS_PRODUTOS)
            ).click()
            logging.info("Clique no elemento VALIDAR_MODULOS_PRODUTOS realizado com sucesso.")

            logging.info("Clicando no link de produtos '//a[@href='/pages/default-products']'.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/pages/default-products']"))
            ).click()
            logging.info("Clique no link de produtos realizado com sucesso.")

            logging.info("Validando a existência do título 'Gerenciar Produtos Diário/Semanal'.")
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PerfilDeAcessoPortfolioTradingLocators.VALIDAR_PAGINA_PRODUTOS_DIARIOS)
            )
            logging.info("Título 'Gerenciar Produtos Diário/Semanal' validado com sucesso.")
        except TimeoutException:
            logging.error("Erro ao acessar ou validar o título do produto Diário/Semanal.")
            ipdb.set_trace()  # Inicia o depurador
            raise
        sleep(2)

    def clicar_aba_produtos(self):
        """Clica no elemento VALIDAR_MODULOS_PRODUTOS."""
        try:
            logging.info("Clicando na aba produtos.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PerfilDeAcessoPortfolioTradingLocators.ABRIR_MODULO_PRODUTOS)
            ).click()
        except TimeoutException:
            logging.error("Erro ao clicar na aba produtos.")
            ipdb.set_trace()  # Inicia o depurador
            raise
        sleep(2)

    def selecionar_produto_diario_semanal(self):
        """Clica no elemento PRODUTO_DIARIO_SEMANAL."""
        try:
            logging.info("Selecionando o produto Diário Semanal.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PerfilDeAcessoPortfolioTradingLocators.PRODUTO_DIARIO_SEMANAL)
            ).click()
        except TimeoutException:
            logging.error("Erro ao selecionar o produto Diário Semanal.")
            ipdb.set_trace()  # Inicia o depurador para analisar o erro
            raise
        sleep(2)

    def pesquisar_por_ano(self):
        """Pesquisa pelo ano utilizando o valor de CONS_PROD_ANO."""
        from credentials import CONS_PROD_ANO
        try:
            logging.info(f"Pesquisando pelo ano: {CONS_PROD_ANO}.")
            campo_ano = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PerfilDeAcessoPortfolioTradingLocators.PESQUISAR_PROD_POR_ANO)
            )
            campo_ano.clear()
            campo_ano.send_keys(CONS_PROD_ANO)
            sleep(1)
            campo_ano.send_keys(Keys.ENTER)
        except TimeoutException:
            logging.error("Erro ao pesquisar pelo ano.")
            ipdb.set_trace()  # Inicia o depurador para analisar o erro
            raise
        sleep(2)

    def selecionar_produto_estipulado(self):
        """Seleciona o produto de acordo com os valores estipulados no arquivo credentials."""
        from credentials import CONS_PROD_MES, CONS_PROD_PERFIL, CONS_PROD_SUBMERCADO, CONS_PROD_TIPO_DE_PROD
        try:
            logging.info("Selecionando o produto de acordo com as especificações.")
            # Implementar lógica para selecionar o produto com base nos valores de CONS_PROD_MES, CONS_PROD_PERFIL, CONS_PROD_SUBMERCADO e CONS_PROD_TIPO_DE_PROD
        except TimeoutException:
            logging.error("Erro ao selecionar o produto estipulado.")
            ipdb.set_trace()  # Inicia o depurador
            raise
        sleep(2)

    def clicar_botao_editar(self):
        """Clica no botão editar."""
        try:
            logging.info("Clicando no botão editar.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PerfilDeAcessoPortfolioTradingLocators.BTN_EDITAR_PROD)
            ).click()
        except TimeoutException:
            logging.error("Erro ao clicar no botão editar.")
            ipdb.set_trace()  # Inicia o depurador para analisar o erro
            raise
        sleep(2)

    def validar_pagina_edicao_produto(self):
        """Valida se o título da página de edição do produto está visível."""
        try:
            logging.info("Validando a existência do título da página de edição do produto.")
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PerfilDeAcessoPortfolioTradingLocators.TITULO_PAGINA_EDICAO_PRODUTO)
            )
            logging.info("Título da página de edição do produto encontrado com sucesso.")
            return True
        except TimeoutException:
            logging.error("Título da página de edição do produto não encontrado.")
            return False
        sleep(2)

