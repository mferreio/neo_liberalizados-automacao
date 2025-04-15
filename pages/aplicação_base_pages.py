from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

class AplicacaoBaseLocators:
    """Locators para a página base da aplicação."""
    MENU_LATERAL = (By.XPATH, "(/html/body/app-root[1]/app-layout[1]/div[1]/div[1]/app-sidebar[1]/app-menu[1]/ul[1]/li[1]/div[1])")
    MODULO_REGISTRO_ITENS = (By.XPATH, "(/html/body/app-root[1]/app-layout[1]/div[1]/div[1]/app-sidebar[1]/app-menu[1]/ul[1]/li[2]/ul[1]/li[10]/a[1]/span[1])")
    LISTA_ITENS_CADASTRADOS = (By.XPATH, "//div[@class='lista-itens']")
    BOTAO_ADICIONAR_NOVO_ITEM = (By.XPATH, "//button[text()='Adicionar Novo Item']")
    FORMULARIO_NOVO_ITEM = (By.XPATH, "//form[@id='form-novo-item']")
    MODULO_RELATORIO_VENDAS = (By.XPATH, "//div[text()='Relatório de Vendas']")
    BOTAO_ADMINISTRADOR = (By.XPATH, "//button[text()='Administrador']")
    BOTAO_TRADING_PORTFOLIO = (By.XPATH, "//button[text()='Trading/Portifólio']")
    URL_PAGINA_PRINCIPAL = "https://diretrizes.dev.neoenergia.net/"
    MODULO_SEMANAL_DIARIO = (By.XPATH, "(/html/body/app-root[1]/app-layout[1]/div[1]/div[1]/app-sidebar[1]/app-menu[1]/ul[1]/li[2]/ul[1]/li[10]/ul[1]/li[1]/a[1]/span[1])")
    ELEMENTO_TELA_PRODUTOS_SEMANAL_DIARIO = (By.XPATH, "(//*[@id='pn_id_2']/div[1]/div[1]/h5[1])")
    MODULO_IREC = (By.XPATH, "(/html/body/app-root[1]/app-layout[1]/div[1]/div[1]/app-sidebar[1]/app-menu[1]/ul[1]/li[2]/ul[1]/li[10]/ul[1]/li[2]/a[1]/span[1])")
    MODULO_CURTO_PRAZO = (By.XPATH, "(/html/body/app-root[1]/app-layout[1]/div[1]/div[1]/app-sidebar[1]/app-menu[1]/ul[1]/li[2]/ul[1]/li[10]/ul[1]/li[3]/a[1]/span[1])")
    ELEMENTO_TELA_PRODUTOS_IREC = (By.XPATH, "(//*[@id='pn_id_2']/div[1]/div[1]/h5[1])")
    ELEMENTO_TELA_PRODUTOS_CURTO_PRAZO = (By.XPATH, "(//*[@id='pn_id_10']/div[1]/div[1]/h5[1])")
    LISTA_PRODUTOS = (By.XPATH, "//tr[@class='ng-star-inserted']/td[position()=1][span[text()='Mês']]")
    BOTAO_NOVO_ITEM = (By.XPATH, "//div[@class='p-toolbar-group-left p-toolbar-group-start ng-star-inserted']/div/button[@label='Novo']")
    FORMULARIO_VALIDACAO = (By.XPATH, "//div[@class='p-fluid']/p[@class='text-3xl font-bold text-green-500']")
    BOTAO_VOLTAR = (By.XPATH, "//button[contains(@class, 'p-button-secondary') and contains(@class, 'p-button-text') and span[text()='Voltar']]")

class AplicacaoBasePage:
    def __init__(self, driver):
        self.driver = driver

    def verificar_menu_lateral(self):
        """Verifica se o menu lateral está presente na página."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(AplicacaoBaseLocators.MENU_LATERAL)
            )
            logging.info("Menu lateral está presente na página.")
        except TimeoutException:
            raise AssertionError("Menu lateral não está presente na página.")

    def selecionar_modulo(self, modulo_locator):
        """Seleciona um módulo no menu lateral."""
        try:
            modulo = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(modulo_locator)
            )
            modulo.click()
            logging.info(f"Módulo selecionado com sucesso.")
        except TimeoutException:
            raise AssertionError("Erro ao selecionar o módulo no menu lateral.")

    def verificar_lista_itens_cadastrados(self):
        """Verifica se a lista de itens cadastrados está visível."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(AplicacaoBaseLocators.LISTA_ITENS_CADASTRADOS)
            )
            logging.info("Lista de itens cadastrados está visível.")
        except TimeoutException:
            raise AssertionError("Lista de itens cadastrados não está visível.")

    def clicar_botao_adicionar_novo_item(self):
        """Clica no botão 'Adicionar Novo Item'."""
        try:
            botao = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(AplicacaoBaseLocators.BOTAO_ADICIONAR_NOVO_ITEM)
            )
            botao.click()
            logging.info("Botão 'Adicionar Novo Item' clicado com sucesso.")
        except TimeoutException:
            raise AssertionError("Erro ao clicar no botão 'Adicionar Novo Item'.")

    def verificar_formulario_novo_item(self):
        """Verifica se o formulário para adicionar um novo item está visível."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(AplicacaoBaseLocators.FORMULARIO_NOVO_ITEM)
            )
            logging.info("Formulário para adicionar novo item está visível.")
        except TimeoutException:
            raise AssertionError("Formulário para adicionar novo item não está visível.")

    def verificar_modulo_invisivel(self, modulo_locator):
        """Verifica se um módulo está invisível no menu lateral."""
        try:
            WebDriverWait(self.driver, 10).until_not(
                EC.presence_of_element_located(modulo_locator)
            )
            logging.info("Módulo não está visível no menu lateral.")
        except TimeoutException:
            raise AssertionError("Módulo está visível no menu lateral.")

    def verificar_botoes_por_permissao(self, perfil):
        """Verifica os botões visíveis com base no perfil do usuário."""
        try:
            if perfil == "Administrador":
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(AplicacaoBaseLocators.BOTAO_ADMINISTRADOR)
                )
                WebDriverWait(self.driver, 10).until_not(
                    EC.presence_of_element_located(AplicacaoBaseLocators.BOTAO_ADICIONAR_NOVO_ITEM)
                )
                logging.info("Botões corretos visíveis para o perfil Administrador.")
            elif perfil == "Trading/Portifólio":
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(AplicacaoBaseLocators.BOTAO_TRADING_PORTFOLIO)
                )
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(AplicacaoBaseLocators.BOTAO_ADICIONAR_NOVO_ITEM)
                )
                logging.info("Botões corretos visíveis para o perfil Trading/Portifólio.")
            else:
                raise ValueError(f"Perfil desconhecido: {perfil}")
        except TimeoutException:
            raise AssertionError(f"Erro ao verificar botões para o perfil {perfil}.")

    def verificar_botao_trading_portfolio(self):
        """Verifica se o botão 'Trading/Portifólio' está visível."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(AplicacaoBaseLocators.BOTAO_TRADING_PORTFOLIO)
            )
            logging.info("Botão 'Trading/Portifólio' está visível.")
        except TimeoutException:
            raise AssertionError("Botão 'Trading/Portifólio' não está visível.")

    def verificar_botoes_trading_portfolio(self):
        """Verifica se os botões 'Trading/Portifólio' e 'Adicionar Novo Item' estão visíveis."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(AplicacaoBaseLocators.BOTAO_TRADING_PORTFOLIO)
            )
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(AplicacaoBaseLocators.BOTAO_ADICIONAR_NOVO_ITEM)
            )
            logging.info("Botões 'Trading/Portifólio' e 'Adicionar Novo Item' estão visíveis.")
        except TimeoutException:
            raise AssertionError("Os botões 'Trading/Portifólio' ou 'Adicionar Novo Item' não estão visíveis.")

    def validar_pagina_principal(self):
        """Valida se o sistema está na página principal."""
        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.current_url == AplicacaoBaseLocators.URL_PAGINA_PRINCIPAL
            )
            logging.info("Usuário está na página principal.")
        except TimeoutException:
            raise AssertionError(f"Usuário não está na página principal. URL atual: {self.driver.current_url}")

    def validar_modulo_visivel(self):
        """Valida se o módulo 'Produtos' está visível no menu lateral."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(AplicacaoBaseLocators.MODULO_REGISTRO_ITENS)
            )
            logging.info("O módulo 'Produtos' está visível no menu lateral.")
        except TimeoutException:
            raise AssertionError("O módulo 'Produtos' não está visível no menu lateral.")

    def clicar_modulo_produtos(self):
        """Clica no módulo 'Produtos' no menu lateral."""
        try:
            modulo_produtos = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(AplicacaoBaseLocators.MODULO_REGISTRO_ITENS)
            )
            modulo_produtos.click()
            logging.info("Clicou no módulo 'Produtos' com sucesso.")
        except TimeoutException:
            raise AssertionError("Erro ao clicar no módulo 'Produtos'.")

    def clicar_modulo_semanal_diario(self):
        """Clica no módulo 'Semanal Diario' no menu lateral."""
        try:
            modulo_semanal_diario = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(AplicacaoBaseLocators.MODULO_SEMANAL_DIARIO)
            )
            modulo_semanal_diario.click()
            logging.info("Clicou no módulo 'Semanal Diario' com sucesso.")
        except TimeoutException:
            raise AssertionError("Erro ao clicar no módulo 'Semanal Diario'.")

    def validar_tela_produtos_semanal_diario(self):
        """Valida se o usuário foi direcionado para a tela de visualização dos dados do módulo 'Produtos Semanal Diario'."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(AplicacaoBaseLocators.ELEMENTO_TELA_PRODUTOS_SEMANAL_DIARIO)
            )
            logging.info("Tela de visualização dos dados do módulo 'Produtos Semanal Diario' validada com sucesso.")
        except TimeoutException:
            raise AssertionError("Erro ao validar a tela de visualização dos dados do módulo 'Produtos Semanal Diario'.")

    def clicar_modulo_irec(self):
        """Clica no módulo 'IREC' no menu lateral."""
        try:
            modulo_irec = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(AplicacaoBaseLocators.MODULO_IREC)
            )
            modulo_irec.click()
            logging.info("Clicou no módulo 'IREC' com sucesso.")
        except TimeoutException:
            raise AssertionError("Erro ao clicar no módulo 'IREC'.")

    def validar_tela_produtos_irec(self):
        """Valida se o usuário foi direcionado para a tela de visualização dos dados do módulo 'Produtos IREC'."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(AplicacaoBaseLocators.ELEMENTO_TELA_PRODUTOS_IREC)
            )
            logging.info("Tela de visualização dos dados do módulo 'Produtos IREC' validada com sucesso.")
        except TimeoutException:
            raise AssertionError("Erro ao validar a tela de visualização dos dados do módulo 'Produtos IREC'.")

    def clicar_modulo_curto_prazo(self):
        """Clica no módulo 'Curto Prazo' no menu lateral."""
        try:
            modulo_curto_prazo = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(AplicacaoBaseLocators.MODULO_CURTO_PRAZO)
            )
            modulo_curto_prazo.click()
            logging.info("Clicou no módulo 'Curto Prazo' com sucesso.")
        except TimeoutException:
            raise AssertionError("Erro ao clicar no módulo 'Curto Prazo'.")

    def validar_tela_produtos_curto_prazo(self):
        """Valida se o usuário foi direcionado para a tela de visualização dos dados do módulo 'Produtos Curto Prazo'."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(AplicacaoBaseLocators.ELEMENTO_TELA_PRODUTOS_CURTO_PRAZO)
            )
            logging.info("Tela de visualização dos dados do módulo 'Produtos Curto Prazo' validada com sucesso.")
        except TimeoutException:
            raise AssertionError("Erro ao validar a tela de visualização dos dados do módulo 'Produtos Curto Prazo'.")

    def consultar_lista_produtos(self):
        """Consulta e retorna a lista de produtos cadastrados na tela de produtos."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(AplicacaoBaseLocators.LISTA_PRODUTOS)
            )
            elementos_produtos = self.driver.find_elements(*AplicacaoBaseLocators.LISTA_PRODUTOS)
            produtos = [elemento.text for elemento in elementos_produtos]
            logging.info(f"Produtos encontrados: {produtos}")
            return produtos
        except TimeoutException:
            raise AssertionError("Erro ao consultar a lista de produtos cadastrados.")

    def clicar_botao_novo_item(self):
        """Clica no botão 'Adicionar Novo Item'."""
        try:
            botao_novo_item = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(AplicacaoBaseLocators.BOTAO_NOVO_ITEM)
            )
            botao_novo_item.click()
            logging.info('Botão "Adicionar Novo Item" clicado com sucesso.')
        except TimeoutException:
            raise AssertionError('Erro ao clicar no botão "Adicionar Novo Item".')

    def validar_formulario_e_voltar(self):
        """Valida a existência do formulário e clica no botão 'Voltar'."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(AplicacaoBaseLocators.FORMULARIO_VALIDACAO)
            )
            logging.info("Formulário validado com sucesso.")
            botao_voltar = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(AplicacaoBaseLocators.BOTAO_VOLTAR)
            )
            botao_voltar.click()
            logging.info("Botão 'Voltar' clicado com sucesso.")
        except TimeoutException:
            raise AssertionError("Erro ao validar o formulário ou clicar no botão 'Voltar'.")
