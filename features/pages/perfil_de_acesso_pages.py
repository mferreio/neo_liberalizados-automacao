import logging
import traceback  # Import necessário para capturar detalhes do erro

# Logger padronizado para o módulo
logger = logging.getLogger(__name__)
from time import sleep

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PerfilDeAcessoPageLocators:
    """Locators for the Perfil de Acesso Page."""

    VALIDAR_ADMINISTRADOR = (
        By.XPATH,
        "//div[@class='admin']",
    )  # Exemplo de locator para validar administrador
    VALIDAR_TRADING_E_PORTIFOLIO = (
        By.XPATH,
        "//div[@class='portifolio']",
    )  # Exemplo de locator para validar portfólio

    # Acessar a barra de navegação lateral
    DASHBOARD = (By.XPATH, "//a[@routerlinkactive='active-route']")
    PERFIL = (By.XPATH, "//a[@href='/pages/perfil']")
    DIRETRIZ_CURTO_PRAZO = (
        By.XPATH,
        "/html/body/app-root/app-layout/div/div[1]/app-sidebar/app-menu/ul/li[2]/ul/li[3]/a",
    )
    DIRETRIZ_I_REC = (
        By.XPATH,
        "/html/body/app-root/app-layout/div/div[1]/app-sidebar/app-menu/ul/li[2]/ul/li[4]/a",
    )
    DIRETRIZ_SEMANAL = (
        By.XPATH,
        "/html/body/app-root/app-layout/div/div[1]/app-sidebar/app-menu/ul/li[2]/ul/li[5]/a",
    )
    DIRETRIZ_DIARIA = (
        By.XPATH,
        "/html/body/app-root/app-layout/div/div[1]/app-sidebar/app-menu/ul/li[2]/ul/li[3]/a",
    )
    PRECOS_MERCADO_DIRETRIZ = (
        By.XPATH,
        "/html/body/app-root/app-layout/div/div[1]/app-sidebar/app-menu/ul/li[2]/ul/li[6]/a",
    )
    BBCE = (
        By.XPATH,
        "/html/body/app-root/app-layout/div/div[1]/app-sidebar/app-menu/ul/li[2]/ul/li[7]/a",
    )
    CNAE = (
        By.XPATH,
        "/html/body/app-root/app-layout/div/div[1]/app-sidebar/app-menu/ul/li[2]/ul/li[8]/a",
    )
    SHAPE_DETERMINISTICO = (
        By.XPATH,
        "/html/body/app-root/app-layout/div/div[1]/app-sidebar/app-menu/ul/li[2]/ul/li[9]/a",
    )
    PRODUTOS = (
        By.XPATH,
        "/html/body/app-root/app-layout/div/div[1]/app-sidebar/app-menu/ul/li[2]/ul/li[10]/a",
    )

    # Botões de ação e subações
    CADASTRO_USUARIOS = (
        By.CSS_SELECTOR,
        "button.p-element.p-ripple.p-button-success.mr-2.w-8rem.p-button.p-component",
    )
    NOVO = (
        By.CSS_SELECTOR,
        "//button[span[@class='p-button-label' and text()='Novo']]",
    )
    PRODUTOS_DIARIO_SEMANAL = (
        By.CSS_SELECTOR,
        "li[app-menuitem].ng-tns-c183498709-14.ng-star-inserted",
    )
    PRODUTOS_I_REC = (
        By.CSS_SELECTOR,
        "a.p-ripple.p-element.ng-tns-c183498709-15.ng-star-inserted",
    )
    PRODUTOS_CURTO_PRAZO = (By.CSS_SELECTOR, 'a[href="/pages/short-products"]')
    BOTAO_FECHAR = (By.XPATH, "//button[contains(@class, 'p-dialog-header-close')]")

    # Assertivas de telas
    PERFIL_TELA = (By.XPATH, "//h5[text()='Gerenciar Usuários']")
    TELA_DIRETRIZ_CURTO_PRAZO = (By.XPATH, "//h5[text()='Diretrizes Curto Prazo']")
    TELA_DIRETRIZ_I_REC = (By.XPATH, "//h5[text()='Diretrizes I-REC']")
    TELA_DIRETRIZ_SEMANAL = (By.XPATH, "//h5[text()='Diretrizes Semanal']")
    TELA_DIRETRIZ_DIARIA = (By.XPATH, "//h5[text()='Diretrizes Diária']")
    PRECOS_MERCADO_DIRETRIZ_TELA = (By.XPATH, "//p[text()=' Preço do Mercado ']")
    BBCE_TELA = (By.CSS_SELECTOR, "div.card > p.text-3xl.font-bold")
    CNAE_TELA = (By.CSS_SELECTOR, "div.col-12 > p.text-3xl.font-bold")
    SHAPE_DETERMINISTICO_TELA = (
        By.CSS_SELECTOR,
        "div.card.px-6.py-6 > p.text-3xl.font-bold",
    )
    CADASTRO_PRODUTOS_DIARIO_SEMANAL_TELA = (
        By.CSS_SELECTOR,
        "div.p-fluid > p.text-3xl.font-bold.text-green-500",
    )
    CADASTRO_PRODUTOS_I_REC_TELA = (
        By.CSS_SELECTOR,
        "div.card.px-6.py-6 > div.p-fluid > p.text-3xl.font-bold.text-green-500",
    )
    CADASTRO_PRODUTOS_CURTO_PRAZO_TELA = (
        By.CSS_SELECTOR,
        "//span[text()='Curto Prazo']",
    )


class PerfilDeAcessoPage:
    def __init__(self, driver):
        self.driver = driver
        self.perfil = None

    def executar_com_erro_controlado(self, funcao, *args, **kwargs):
        """Executa uma função, captura erros e continua a execução."""
        try:
            logger.info(f"Executando função '{funcao.__name__}' com args={args}, kwargs={kwargs}")
            funcao(*args, **kwargs)
        except Exception as e:
            logger.error(f"Erro ao executar {funcao.__name__}: {e}")
            logger.debug(traceback.format_exc())  # Log detalhado do erro

    def validar_usuario_administrador(self):
        self.executar_com_erro_controlado(self._validar_usuario_administrador)

    def _validar_usuario_administrador(self):
        logger.info("Validando se o usuário está logado como Administrador.")
        elemento = self.driver.find_element(
            *PerfilDeAcessoPageLocators.VALIDAR_ADMINISTRADOR
        )
        assert elemento is not None, "Usuário não está logado como Administrador."
        logger.info("Usuário validado como Administrador.")

    def visualizar_todas_as_telas(self):
        """Valida se os acessos especificados estão sendo exibidos na tela."""
        acessos = [
            {"nome": "DashBoard", "locator": PerfilDeAcessoPageLocators.DASHBOARD},
            {"nome": "Perfil", "locator": PerfilDeAcessoPageLocators.PERFIL},
            {
                "nome": "Diretriz Curto Prazo",
                "locator": PerfilDeAcessoPageLocators.DIRETRIZ_CURTO_PRAZO,
            },
            {
                "nome": "Diretriz I-REC",
                "locator": PerfilDeAcessoPageLocators.DIRETRIZ_I_REC,
            },
            {
                "nome": "Diretriz Semanal",
                "locator": PerfilDeAcessoPageLocators.DIRETRIZ_SEMANAL,
            },
            {
                "nome": "Diretriz Diária",
                "locator": PerfilDeAcessoPageLocators.DIRETRIZ_DIARIA,
            },
            {
                "nome": "Preços de Mercado e Diretriz",
                "locator": PerfilDeAcessoPageLocators.PRECOS_MERCADO_DIRETRIZ,
            },
            {"nome": "BBCE", "locator": PerfilDeAcessoPageLocators.BBCE},
            {"nome": "CNAE", "locator": PerfilDeAcessoPageLocators.CNAE},
            {
                "nome": "Shape Deterministico",
                "locator": PerfilDeAcessoPageLocators.SHAPE_DETERMINISTICO,
            },
            {"nome": "Produtos", "locator": PerfilDeAcessoPageLocators.PRODUTOS},
        ]

        for acesso in acessos:
            self.executar_com_erro_controlado(self._validar_acesso, acesso)

    def _validar_acesso(self, acesso):
        logger.info(f"Validando exibição do acesso: {acesso['nome']}")
        elemento = WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located(acesso["locator"])
        )
        assert (
            elemento.is_displayed()
        ), f"O acesso '{acesso['nome']}' não está sendo exibido na tela."
        logger.info(f"Confirmação: o acesso '{acesso['nome']}' está sendo exibido.")

    def possui_acesso_total(self):
        """Clica e valida a exibição das telas especificadas."""
        telas = [
            {
                "nome": "DashBoard",
                "botao": PerfilDeAcessoPageLocators.DASHBOARD,
                "validacao": lambda driver: driver.current_url
                == "https://diretrizes.dev.neoenergia.net/",
            },
            {
                "nome": "Perfil",
                "botao": PerfilDeAcessoPageLocators.PERFIL,
                "validacao": PerfilDeAcessoPageLocators.PERFIL_TELA,
            },
            {
                "nome": "Diretriz Curto Prazo",
                "botao": PerfilDeAcessoPageLocators.DIRETRIZ_CURTO_PRAZO,
                "validacao": PerfilDeAcessoPageLocators.TELA_DIRETRIZ_CURTO_PRAZO,
            },
            {
                "nome": "Diretriz I-REC",
                "botao": PerfilDeAcessoPageLocators.DIRETRIZ_I_REC,
                "validacao": PerfilDeAcessoPageLocators.TELA_DIRETRIZ_I_REC,
            },
            {
                "nome": "Diretriz Semanal",
                "botao": PerfilDeAcessoPageLocators.DIRETRIZ_SEMANAL,
                "validacao": PerfilDeAcessoPageLocators.TELA_DIRETRIZ_SEMANAL,
            },
            {
                "nome": "Diretriz Diária",
                "botao": PerfilDeAcessoPageLocators.DIRETRIZ_DIARIA,
                "validacao": PerfilDeAcessoPageLocators.TELA_DIRETRIZ_DIARIA,
            },
            {
                "nome": "Preços de Mercado e Diretriz",
                "botao": PerfilDeAcessoPageLocators.PRECOS_MERCADO_DIRETRIZ,
                "validacao": PerfilDeAcessoPageLocators.PRECOS_MERCADO_DIRETRIZ_TELA,
            },
            {
                "nome": "BBCE",
                "botao": PerfilDeAcessoPageLocators.BBCE,
                "validacao": PerfilDeAcessoPageLocators.BBCE_TELA,
            },
            {
                "nome": "CNAE",
                "botao": PerfilDeAcessoPageLocators.CNAE,
                "validacao": PerfilDeAcessoPageLocators.CNAE_TELA,
            },
            {
                "nome": "Shape Deterministico",
                "botao": PerfilDeAcessoPageLocators.SHAPE_DETERMINISTICO,
                "validacao": PerfilDeAcessoPageLocators.SHAPE_DETERMINISTICO_TELA,
            },
            {
                "nome": "Produtos",
                "botao": PerfilDeAcessoPageLocators.PRODUTOS,
                "validacao": PerfilDeAcessoPageLocators.CADASTRO_PRODUTOS_CURTO_PRAZO_TELA,
            },
        ]

        for tela in telas:
            self.executar_com_erro_controlado(self._visualizar_tela, tela)

    def _visualizar_tela(self, tela):
        logger.info(f"Clicando na tela: {tela['nome']}")
        try:
            WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable(tela["botao"])
            ).click()
            logger.info(f"Validando exibição da tela: {tela['nome']}")

            # Corrige a validação para lidar com diferentes tipos de validação
            if callable(tela["validacao"]):
                assert tela["validacao"](
                    self.driver
                ), f"A tela '{tela['nome']}' não está sendo exibida."
            else:
                elemento = WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located(tela["validacao"])
                )
                assert (
                    elemento.is_displayed()
                ), f"A tela '{tela['nome']}' não está sendo exibida."

            logger.info(f"A tela '{tela['nome']}' está sendo exibida.")
        except Exception as e:
            logger.error(f"Erro ao visualizar a tela '{tela['nome']}': {e}")
            logger.debug(traceback.format_exc())

    def validar_exibicao_telas(self):
        """Valida se os elementos das telas estão sendo exibidos sem realizar cliques."""
        telas = [
            {"nome": "DashBoard", "locator": PerfilDeAcessoPageLocators.DASHBOARD},
            {"nome": "Perfil", "locator": PerfilDeAcessoPageLocators.PERFIL},
            {
                "nome": "Diretriz Curto Prazo",
                "locator": PerfilDeAcessoPageLocators.DIRETRIZ_CURTO_PRAZO,
            },
            {
                "nome": "Diretriz I-REC",
                "locator": PerfilDeAcessoPageLocators.DIRETRIZ_I_REC,
            },
            {
                "nome": "Diretriz Semanal",
                "locator": PerfilDeAcessoPageLocators.DIRETRIZ_SEMANAL,
            },
            {
                "nome": "Diretriz Diária",
                "locator": PerfilDeAcessoPageLocators.DIRETRIZ_DIARIA,
            },
            {
                "nome": "Preços de Mercado e Diretriz",
                "locator": PerfilDeAcessoPageLocators.PRECOS_MERCADO_DIRETRIZ,
            },
            {"nome": "BBCE", "locator": PerfilDeAcessoPageLocators.BBCE},
            {"nome": "CNAE", "locator": PerfilDeAcessoPageLocators.CNAE},
            {
                "nome": "Shape Deterministico",
                "locator": PerfilDeAcessoPageLocators.SHAPE_DETERMINISTICO,
            },
            {"nome": "Produtos", "locator": PerfilDeAcessoPageLocators.PRODUTOS},
        ]

        for tela in telas:
            self.executar_com_erro_controlado(self._validar_exibicao, tela)

    def _validar_exibicao(self, tela):
        logger.info(f"Validando exibição do elemento: {tela['nome']}")
        try:
            elemento = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(tela["locator"])
            )
            assert (
                elemento.is_displayed()
            ), f"O elemento '{tela['nome']}' não está sendo exibido na tela."
            logger.info(f"Confirmação: o elemento '{tela['nome']}' está sendo exibido.")
        except Exception as e:
            logger.error(f"Erro ao validar exibição do elemento '{tela['nome']}': {e}")
            logger.debug(traceback.format_exc())

    def realizar_operacoes_trading_portfolio(self):
        """Valida os acessos necessários para operações de Trading/Portifólio, excluindo o elemento 'Perfil'."""
        acessos = [
            {"nome": "DashBoard", "locator": PerfilDeAcessoPageLocators.DASHBOARD},
            {
                "nome": "Diretriz Curto Prazo",
                "locator": PerfilDeAcessoPageLocators.DIRETRIZ_CURTO_PRAZO,
            },
            {
                "nome": "Diretriz I-REC",
                "locator": PerfilDeAcessoPageLocators.DIRETRIZ_I_REC,
            },
            {
                "nome": "Diretriz Semanal",
                "locator": PerfilDeAcessoPageLocators.DIRETRIZ_SEMANAL,
            },
            {
                "nome": "Diretriz Diária",
                "locator": PerfilDeAcessoPageLocators.DIRETRIZ_DIARIA,
            },
            {
                "nome": "Preços de Mercado e Diretriz",
                "locator": PerfilDeAcessoPageLocators.PRECOS_MERCADO_DIRETRIZ,
            },
            {"nome": "BBCE", "locator": PerfilDeAcessoPageLocators.BBCE},
            {"nome": "CNAE", "locator": PerfilDeAcessoPageLocators.CNAE},
            {
                "nome": "Shape Deterministico",
                "locator": PerfilDeAcessoPageLocators.SHAPE_DETERMINISTICO,
            },
            {"nome": "Produtos", "locator": PerfilDeAcessoPageLocators.PRODUTOS},
        ]

        for acesso in acessos:
            self.executar_com_erro_controlado(self._validar_acesso, acesso)

    def validar_menu_apresenta_opcoes_administrador(self):
        """Valida se o menu apresenta todas as opções disponíveis."""
        opcoes_menu = [
            {"nome": "DashBoard", "locator": PerfilDeAcessoPageLocators.DASHBOARD},
            {
                "nome": "Diretriz Curto Prazo",
                "locator": PerfilDeAcessoPageLocators.DIRETRIZ_CURTO_PRAZO,
            },
            {
                "nome": "Diretriz I-REC",
                "locator": PerfilDeAcessoPageLocators.DIRETRIZ_I_REC,
            },
            {
                "nome": "Diretriz Semanal",
                "locator": PerfilDeAcessoPageLocators.DIRETRIZ_SEMANAL,
            },
            {
                "nome": "Diretriz Diária",
                "locator": PerfilDeAcessoPageLocators.DIRETRIZ_DIARIA,
            },
            {
                "nome": "Preços de Mercado e Diretriz",
                "locator": PerfilDeAcessoPageLocators.PRECOS_MERCADO_DIRETRIZ,
            },
            {"nome": "BBCE", "locator": PerfilDeAcessoPageLocators.BBCE},
            {"nome": "CNAE", "locator": PerfilDeAcessoPageLocators.CNAE},
            {
                "nome": "Shape Deterministico",
                "locator": PerfilDeAcessoPageLocators.SHAPE_DETERMINISTICO,
            },
            {"nome": "Produtos", "locator": PerfilDeAcessoPageLocators.PRODUTOS},
        ]

        for opcao in opcoes_menu:
            self.executar_com_erro_controlado(self._validar_acesso, opcao)
