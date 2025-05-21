import logging
import time

import ipdb
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AplicacaoBaseLocators:
    """Locators para a página base da aplicação."""

    MENU_LATERAL = (
        By.XPATH,
        "(/html/body/app-root[1]/app-layout[1]/div[1]/div[1]/app-sidebar[1]/app-menu[1]/ul[1]/li[1]/div[1])",
    )
    MODULO_PRODUTOS = (
        By.XPATH,
        "//li[@app-menuitem]//a[span[text()='Produtos']]",
    )
    LISTA_ITENS_CADASTRADOS = (By.XPATH, "//div[@class='lista-itens']")
    BOTAO_ADICIONAR_NOVO_ITEM = (By.XPATH, "//button[text()='Adicionar Novo Item']")
    FORMULARIO_NOVO_ITEM = (By.XPATH, "//form[@id='form-novo-item']")
    MODULO_RELATORIO_VENDAS = (By.XPATH, "//div[text()='Relatório de Vendas']")
    BOTAO_ADMINISTRADOR = (By.XPATH, "//button[text()='Administrador']")
    BOTAO_TRADING_PORTFOLIO = (By.XPATH, "//button[text()='Trading/Portifólio']")
    URL_PAGINA_PRINCIPAL = "https://diretrizes.dev.neoenergia.net/"
    MODULO_SEMANAL_DIARIO = (
        By.XPATH,
        "//li[@app-menuitem]//a[span[text()='Diário/Semanal']]",
    )
    ELEMENTO_TELA_PRODUTOS_SEMANAL_DIARIO = (
        By.XPATH,
        "//h5[text()='Gerenciar Produtos (Diário/Semanal)']",
    )
    MODULO_IREC = (
        By.XPATH,
        "//li[@app-menuitem]//a[span[text()='I-REC']]",
    )
    MODULO_CURTO_PRAZO = (By.XPATH, "//span[text()='Curto Prazo']")
    ELEMENTO_TELA_PRODUTOS_IREC = (
        By.XPATH,
        "//span[text()='Curto Prazo']",
    )
    ELEMENTO_TELA_PRODUTOS_CURTO_PRAZO = (
        By.XPATH,
        "//h5[text()='Gerenciar Produtos (Curto Prazo)']",
    )
    LISTA_PRODUTOS = (
        By.XPATH,
        "//tr[@class='ng-star-inserted']/td[position()=1][span[text()='Mês']]",
    )
    BOTAO_NOVO_ITEM = (By.XPATH, "//button[span[text()='Novo']]")
    FORMULARIO_VALIDACAO = (
        By.XPATH,
        "//p[text()=' Cadastro de Produto - Curto Prazo ']",
    )
    BOTAO_VOLTAR = (By.XPATH, "//button[span[text()='Voltar']]")
    URL_PAGINA_INICIAL = "https://diretrizes.dev.neoenergia.net/"



logger = logging.getLogger(__name__)

class AplicacaoBasePage:
    def __init__(self, driver):
        self.driver = driver
        logger.info("Instanciando page object: AplicacaoBasePage")

    def verificar_menu_lateral(self):
        """Verifica se o menu lateral está presente na página."""
        logger.info("Verificando se o menu lateral está presente na página.")
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(AplicacaoBaseLocators.MENU_LATERAL)
            )
            logger.info("Menu lateral encontrado na página.")
        except TimeoutException:
            logger.error("Menu lateral não está presente na página.")
            raise AssertionError("Menu lateral não está presente na página.")

    def selecionar_modulo(self, modulo_locator):
        """Seleciona um módulo no menu lateral."""
        logger.info(f"Selecionando módulo no menu lateral: {modulo_locator}")
        time.sleep(1)
        try:
            modulo = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(modulo_locator)
            )
            modulo.click()
            logger.info(f"Módulo selecionado com sucesso: {modulo_locator}")
        except TimeoutException:
            logger.error("Erro ao selecionar o módulo no menu lateral.")
            raise AssertionError("Erro ao selecionar o módulo no menu lateral.")

    def verificar_lista_itens_cadastrados(self):
        """Verifica se a lista de itens cadastrados está visível."""
        logger.info("Verificando se a lista de itens cadastrados está visível.")
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    AplicacaoBaseLocators.LISTA_ITENS_CADASTRADOS
                )
            )
            logger.info("Lista de itens cadastrados visível.")
        except TimeoutException:
            logger.error("Lista de itens cadastrados não está visível.")
            raise AssertionError("Lista de itens cadastrados não está visível.")

    def clicar_botao_adicionar_novo_item(self):
        """Clica no botão 'Adicionar Novo Item'."""
        logger.info("Clicando no botão 'Adicionar Novo Item'.")
        time.sleep(1)
        try:
            botao = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    AplicacaoBaseLocators.BOTAO_ADICIONAR_NOVO_ITEM
                )
            )
            botao.click()
            logger.info("Botão 'Adicionar Novo Item' clicado com sucesso.")
        except TimeoutException:
            logger.error("Erro ao clicar no botão 'Adicionar Novo Item'.")
            raise AssertionError("Erro ao clicar no botão 'Adicionar Novo Item'.")

    def verificar_formulario_novo_item(self):
        """Verifica se o formulário para adicionar um novo item está visível."""
        logger.info("Verificando se o formulário para adicionar novo item está visível.")
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    AplicacaoBaseLocators.FORMULARIO_NOVO_ITEM
                )
            )
            logger.info("Formulário para adicionar novo item visível.")
        except TimeoutException:
            logger.error("Formulário para adicionar novo item não está visível.")
            raise AssertionError("Formulário para adicionar novo item não está visível.")


    def verificar_modulo_invisivel(self, modulo_locator):
        """Verifica se um módulo está invisível no menu lateral."""
        logger.info(f"Verificando se o módulo está invisível: {modulo_locator}")
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 10).until_not(
                EC.presence_of_element_located(modulo_locator)
            )
            logger.info(f"Módulo está invisível: {modulo_locator}")
        except TimeoutException:
            logger.error("Módulo está visível no menu lateral.")
            raise AssertionError("Módulo está visível no menu lateral.")

    def verificar_botoes_por_permissao(self, perfil):
        """Verifica os botões visíveis com base no perfil do usuário."""
        logger.info(f"Verificando botões por permissão para o perfil: {perfil}")
        time.sleep(1)
        try:
            if perfil == "Administrador":
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        AplicacaoBaseLocators.BOTAO_ADMINISTRADOR
                    )
                )
                WebDriverWait(self.driver, 10).until_not(
                    EC.presence_of_element_located(
                        AplicacaoBaseLocators.BOTAO_ADICIONAR_NOVO_ITEM
                    )
                )
                logger.info("Botões para Administrador verificados.")
            elif perfil == "Trading/Portifólio":
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        AplicacaoBaseLocators.BOTAO_TRADING_PORTFOLIO
                    )
                )
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        AplicacaoBaseLocators.BOTAO_ADICIONAR_NOVO_ITEM
                    )
                )
                logger.info("Botões para Trading/Portifólio verificados.")
            else:
                logger.error(f"Perfil desconhecido: {perfil}")
                raise ValueError(f"Perfil desconhecido: {perfil}")
        except TimeoutException:
            logger.error(f"Erro ao verificar botões para o perfil {perfil}.")
            raise AssertionError(f"Erro ao verificar botões para o perfil {perfil}.")

    def verificar_botao_trading_portfolio(self):
        """Verifica se o botão 'Trading/Portifólio' está visível."""
        logger.info("Verificando se o botão 'Trading/Portifólio' está visível.")
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    AplicacaoBaseLocators.BOTAO_TRADING_PORTFOLIO
                )
            )
            logger.info("Botão 'Trading/Portifólio' visível.")
        except TimeoutException:
            logger.error("Botão 'Trading/Portifólio' não está visível.")
            raise AssertionError("Botão 'Trading/Portifólio' não está visível.")

    def verificar_botoes_trading_portfolio(self):
        """Verifica se os botões 'Trading/Portifólio' e 'Adicionar Novo Item' estão visíveis."""
        logger.info("Verificando se os botões 'Trading/Portifólio' e 'Adicionar Novo Item' estão visíveis.")
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    AplicacaoBaseLocators.BOTAO_TRADING_PORTFOLIO
                )
            )
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    AplicacaoBaseLocators.BOTAO_ADICIONAR_NOVO_ITEM
                )
            )
            logger.info("Botões 'Trading/Portifólio' e 'Adicionar Novo Item' visíveis.")
        except TimeoutException:
            logger.error("Os botões 'Trading/Portifólio' ou 'Adicionar Novo Item' não estão visíveis.")
            raise AssertionError(
                "Os botões 'Trading/Portifólio' ou 'Adicionar Novo Item' não estão visíveis."
            )

    def validar_pagina_principal(self):
        """Valida se o sistema está na página principal."""
        logger.info("Validando se o sistema está na página principal.")
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.current_url
                == AplicacaoBaseLocators.URL_PAGINA_PRINCIPAL
            )
            logger.info("Usuário está na página principal.")
        except TimeoutException:
            logger.error(f"Usuário não está na página principal. URL atual: {self.driver.current_url}")
            raise AssertionError(
                f"Usuário não está na página principal. URL atual: {self.driver.current_url}"
            )

    def validar_modulo_visivel(self):
        """Valida se o módulo 'Produtos' está visível no menu lateral."""
        logger.info("Validando se o módulo 'Produtos' está visível no menu lateral.")
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    AplicacaoBaseLocators.MODULO_PRODUTOS
                )
            )
            logger.info("Módulo 'Produtos' visível no menu lateral.")
        except TimeoutException:
            logger.error("O módulo 'Produtos' não está visível no menu lateral.")
            raise AssertionError(
                "O módulo 'Produtos' não está visível no menu lateral."
            )

    def clicar_modulo_produtos(self):
        """Clica no módulo 'Produtos' no menu lateral."""
        logger.info("Clicando no módulo 'Produtos' no menu lateral.")
        time.sleep(1)
        try:
            modulo_produtos = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,"//li[@app-menuitem]//a[span[text()='Produtos']]"))
            )
            modulo_produtos.click()
            logger.info("Módulo 'Produtos' clicado com sucesso.")
        except TimeoutException:
            logger.error("Erro ao clicar no módulo 'Produtos'.")
            raise AssertionError("Erro ao clicar no módulo 'Produtos'.")

    def clicar_modulo_semanal_diario(self):
        """Clica no módulo 'Semanal Diario' no menu lateral."""
        logger.info("Clicando no módulo 'Semanal Diario' no menu lateral.")
        time.sleep(1)
        try:
            modulo_semanal_diario = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//li[@app-menuitem]//a[span[text()='Diário/Semanal']]",
                    )
                )
            )
            modulo_semanal_diario.click()
            logger.info("Módulo 'Semanal Diario' clicado com sucesso.")
        except TimeoutException:
            logger.error("Erro ao clicar no módulo 'Semanal Diario'.")
            raise AssertionError("Erro ao clicar no módulo 'Semanal Diario'.")

    def validar_tela_produtos_semanal_diario(self):
        """Valida se o usuário foi direcionado para a tela de visualização dos dados do módulo 'Produtos Semanal Diario'."""
        logger.info("Validando tela de visualização dos dados do módulo 'Produtos Semanal Diario'.")
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    AplicacaoBaseLocators.ELEMENTO_TELA_PRODUTOS_SEMANAL_DIARIO
                )
            )
            logger.info("Tela de visualização dos dados do módulo 'Produtos Semanal Diario' validada.")
        except TimeoutException:
            logger.error("Erro ao validar a tela de visualização dos dados do módulo 'Produtos Semanal Diario'.")
            raise AssertionError(
                "Erro ao validar a tela de visualização dos dados do módulo 'Produtos Semanal Diario'."
            )

    def clicar_modulo_irec(self):
        """Clica no módulo 'IREC' no menu lateral."""
        logger.info("Clicando no módulo 'IREC' no menu lateral.")
        time.sleep(1)
        try:
            modulo_irec = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(AplicacaoBaseLocators.MODULO_IREC)
            )
            modulo_irec.click()
            logger.info("Módulo 'IREC' clicado com sucesso.")
        except TimeoutException:
            logger.error("Erro ao clicar no módulo 'IREC'.")
            raise AssertionError("Erro ao clicar no módulo 'IREC'.")

    def validar_tela_produtos_irec(self):
        """Valida se o usuário foi direcionado para a tela de visualização dos dados do módulo 'Produtos IREC'."""
        logger.info("Validando tela de visualização dos dados do módulo 'Produtos IREC'.")
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    AplicacaoBaseLocators.ELEMENTO_TELA_PRODUTOS_IREC
                )
            )
            logger.info("Tela de visualização dos dados do módulo 'Produtos IREC' validada.")
        except TimeoutException:
            logger.error("Erro ao validar a tela de visualização dos dados do módulo 'Produtos IREC'.")
            raise AssertionError(
                "Erro ao validar a tela de visualização dos dados do módulo 'Produtos IREC'."
            )

    def clicar_modulo_curto_prazo(self):
        """Clica no módulo 'Curto Prazo' no menu lateral."""
        logger.info("Clicando no módulo 'Curto Prazo' no menu lateral.")
        try:
            modulo_curto_prazo = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(AplicacaoBaseLocators.MODULO_CURTO_PRAZO)
            )
            modulo_curto_prazo.click()
            logger.info("Módulo 'Curto Prazo' clicado com sucesso.")
        except TimeoutException:
            logger.error("Erro ao clicar no módulo 'Curto Prazo'.")
            raise AssertionError("Erro ao clicar no módulo 'Curto Prazo'.")

    def validar_tela_produtos_curto_prazo(self):
        """Valida se o usuário foi direcionado para a tela de visualização dos dados do módulo 'Produtos Curto Prazo'."""
        logger.info("Validando tela de visualização dos dados do módulo 'Produtos Curto Prazo'.")
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    AplicacaoBaseLocators.ELEMENTO_TELA_PRODUTOS_CURTO_PRAZO
                )
            )
            logger.info("Tela de visualização dos dados do módulo 'Produtos Curto Prazo' validada.")
        except TimeoutException:
            logger.error("Erro ao validar a tela de visualização dos dados do módulo 'Produtos Curto Prazo'.")
            raise AssertionError(
                "Erro ao validar a tela de visualização dos dados do módulo 'Produtos Curto Prazo'."
            )

    def consultar_lista_produtos(self):
        """Consulta e retorna a lista de produtos cadastrados na tela de produtos."""
        logger.info("Consultando lista de produtos cadastrados na tela de produtos.")
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    AplicacaoBaseLocators.LISTA_PRODUTOS
                )
            )
            elementos_produtos = self.driver.find_elements(
                *AplicacaoBaseLocators.LISTA_PRODUTOS
            )
            produtos = [elemento.text for elemento in elementos_produtos]
            logger.info(f"Produtos encontrados: {produtos}")
            return produtos
        except TimeoutException:
            logger.error("Erro ao consultar a lista de produtos cadastrados.")
            raise AssertionError("Erro ao consultar a lista de produtos cadastrados.")

    def clicar_botao_novo_item(self):
        """Clica no botão 'Adicionar Novo Item'."""
        logger.info("Clicando no botão 'Adicionar Novo Item'.")
        time.sleep(1)
        try:
            botao_novo_item = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(AplicacaoBaseLocators.BOTAO_NOVO_ITEM)
            )
            botao_novo_item.click()
            logger.info("Botão 'Adicionar Novo Item' clicado com sucesso.")
        except TimeoutException:
            logger.error('Erro ao clicar no botão "Adicionar Novo Item".')
            raise AssertionError('Erro ao clicar no botão "Adicionar Novo Item".')

    def validar_formulario_e_voltar(self):
        """Valida a existência do formulário e clica no botão 'Voltar'."""
        logger.info("Validando existência do formulário e clicando no botão 'Voltar'.")
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    AplicacaoBaseLocators.FORMULARIO_VALIDACAO
                )
            )
            logger.info("Formulário validado. Clicando no botão 'Voltar'.")
            botao_voltar = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(AplicacaoBaseLocators.BOTAO_VOLTAR)
            )
            botao_voltar.click()
            logger.info("Botão 'Voltar' clicado com sucesso.")
        except TimeoutException:
            logger.error("Erro ao validar o formulário ou clicar no botão 'Voltar'.")
            raise AssertionError(
                "Erro ao validar o formulário ou clicar no botão 'Voltar'."
            )

    def retornar_pagina_inicial(self):
        """Navega de volta para a página inicial."""
        logger.info("Navegando de volta para a página inicial.")
        time.sleep(1)
        try:
            self.driver.get(AplicacaoBaseLocators.URL_PAGINA_INICIAL)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.current_url
                == AplicacaoBaseLocators.URL_PAGINA_INICIAL
            )
            logger.info("Retorno para a página inicial realizado com sucesso.")
        except TimeoutException:
            logger.error("Erro ao retornar para a página inicial.")
            raise AssertionError("Erro ao retornar para a página inicial.")
