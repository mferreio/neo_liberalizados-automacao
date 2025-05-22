
import logging
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from features.pages.tela_de_usuarios_pages import TeladeUsuariosPageLocators
from selenium.common.exceptions import TimeoutException
from credentials import (EDITAR_EMAIL, EDITAR_NOME, EDITAR_PERFIL, EMAIL,
                         EXCLUIR_NOME, NOME, PESQUISAR_NOME_CADASTRADO, EMAIL_INVALIDO)

logger = logging.getLogger(__name__)
class TelaCadastroUsuarioPage:
    BTN_FECHAR = "//div[@role='dialog']//button[contains(@class, 'p-dialog-header-close')]"
    FORMATO_EMAIL_INVALIDO = "//small[text()='Formato de e-mail inválido.']"
    USUARIO_JA_EXISTE = "//div[text()='Usuário já existe!']"
    MSG_PERFIL_OBRIGATORIO = "//small[text()='Perfil é obrigatório.']"
    MSG_NOME_OBRIGATORIO = "//small[text()='Nome é obrigatório.']"
    MSG_EMAIL_OBRIGATORIO = "//small[text()='E-mail é obrigatório.']"
    VALIDAR_DASH_TABELA_DIR_DIARIA = "//app-diretriz-diaria-dashboard/h5"
    DASHBOARD_DIARIA = "//app-diretriz-diaria-dashboard"
    VALIDAR_DASH_TABELA_DIR_SEMANAL = "app-diretriz-semanal-dashboard"
    VALIDAR_DASH_TABELA_DIR_IREC = "//app-diretriz-irec-dashboard/h5"
    VALIDAR_DASH_TABELA_DIR_CURTO_PRAZO = "//app-diretriz-short-dashboard/h5"
    BTN_VER_HISTORICO_DIR_DIARIA = "//app-diretriz-diaria-dashboard//h5[contains(text(), 'Diretriz Diária')]/following-sibling::div//button[@label='Ver Histórico' and span[text()='Ver Histórico']]"
    BTN_VER_HISTORICO_DIR_SEMANAL = "//app-diretriz-semanal-dashboard//h5[contains(text(), ' Diretriz Semanal')]/following-sibling::div//button[@label='Ver Histórico' and span[text()='Ver Histórico']]"
    XPATH_GRAFICO_COMPARATIVO = "//historico-comparativo-chart//h5[contains(text(), 'Comparativo')]"
    XPATH_GRAFICO_HISTORICO = "//historico-diretriz-diaria-chart//h5[contains(text(), 'Histórico Diretrizes')]"
    XPATH_GRAFICOS_HISTORICOS = "//historico-diretriz-chart//h5[contains(text(), 'Histórico Diretrizes')]"
    XPATH_GRAFICO_BBCE = "//historico-bbce-chart//h5[contains(text(), 'Negociações BBCE')]"
    BTN_EXPORTAR_DIR_DIARIA = "//app-diretriz-diaria-dashboard//h5[contains(text(), 'Diretriz Diária')]/following-sibling::div//button[@label='Exportar' and span[text()='Exportar']]"
    BTN_EXPORTAR_DIR_SEMANAL = "//app-diretriz-semanal-dashboard//h5[contains(text(), 'Diretriz Semanal')]/following-sibling::div//button[@label='Exportar' and span[text()='Exportar']]"
    BTN_EXPORTAR_DIR_IREC = "//app-diretriz-irec-dashboard//h5[contains(text(), ' Diretriz I-REC')]/following-sibling::div//button[@label='Exportar' and span[text()='Exportar']]"
    BTN_EXPORTAR_DIR_CURTO_PRAZO = "//app-diretriz-short-dashboard//h5[contains(text(), ' Diretriz Curto Prazo')]/following-sibling::div//button[@label='Exportar' and span[text()='Exportar']]"
    ABA_PREMIO_SAZO = "//li[@app-menuitem]//a[span[text()='Prêmio Sazo']]"
    ABA_PREMIO_FLEX = "//li[@app-menuitem]//a[span[text()='Prêmio Flex']]"

    def __init__(self, driver):
        self.driver = driver

    def selecionar_perfil_administrador_e_inserir_dados_invalidos(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(
                    TeladeUsuariosPageLocators.PERFIL_ADMINISTRADOR
                )
            ).click()

            nome = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TeladeUsuariosPageLocators.INPUT_NOME)
            )
            nome.send_keys(os.getenv("NOME"))

            email = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TeladeUsuariosPageLocators.INPUT_EMAIL)
            )
            email.send_keys(os.getenv("EMAIL_INVALIDO"))
        except TimeoutException:
            raise AssertionError(
                "Erro ao selecionar o perfil de administrador ou inserir os dados."
            )


    def validar_mensagem_email_invalido(self):
        try:
            elemento = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.FORMATO_EMAIL_INVALIDO))
            )
            logger.info("Mensagem exibida: %s", elemento.text)
            return elemento.text
        except Exception:
            logger.warning("Mensagem de formato de e-mail inválido não foi exibida!")
            return None

    def validar_mensagem_usuario_ja_existe(self):
        try:
            elemento = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.USUARIO_JA_EXISTE))
            )
            logger.info("Mensagem exibida: %s", elemento.text)
            return elemento.text
        except Exception:
            logger.warning("Mensagem de usuário já existe não foi exibida!")
            return None

    def validar_mensagens_campos_obrigatorios(self):
        mensagens = []
        try:
            perfil = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.MSG_PERFIL_OBRIGATORIO))
            )
            mensagens.append(perfil.text)
        except Exception:
            logger.warning("Mensagem de perfil obrigatório não exibida.")
        try:
            nome = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.MSG_NOME_OBRIGATORIO))
            )
            mensagens.append(nome.text)
        except Exception:
            logger.warning("Mensagem de nome obrigatório não exibida.")
        try:
            email = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.MSG_EMAIL_OBRIGATORIO))
            )
            mensagens.append(email.text)
        except Exception:
            logger.warning("Mensagem de e-mail obrigatório não exibida.")
        for msg in mensagens:
            logger.info("Mensagem exibida: %s", msg)
        return mensagens

    def validar_usuario_cadastrado(self, context):
        """
        Valida se o cenário de cadastro de usuário foi executado com sucesso.
        """
        if hasattr(context, "usuario_cadastrado") and context.usuario_cadastrado is True:
            logger.info("Usuário cadastrado com sucesso no contexto.")
        else:
            logger.error("O cenário de cadastro de usuário não foi executado com sucesso antes deste passo.")
            assert False, (
                "O cenário de cadastro de usuário não foi executado com sucesso antes deste passo."
            )

    def validar_pagina_inicial(self):
        url_esperada = "https://diretrizes.dev.neoenergia.net/"
        if self.driver.current_url != url_esperada:
            logger.warning("Usuário NÃO está na página inicial. Redirecionando para: %s", url_esperada)
            self.driver.get(url_esperada)
        else:
            logger.info("Usuário já está na página inicial: %s", url_esperada)

    def validar_tabela_diretrizes_diarias(self):
        # Valida existência do título
        titulos = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.VALIDAR_DASH_TABELA_DIR_DIARIA))
        )
        logger.info("Títulos de diretrizes diárias encontrados: %s", [t.text for t in titulos])

    def validar_tabela_diretrizes_semanais(self):
        tabelas = self.driver.find_elements(By.XPATH, self.VALIDAR_DASH_TABELA_DIR_SEMANAL)
        if not tabelas:
            logger.warning("Tabela de diretrizes semanais não encontrada!")
        for idx, tabela in enumerate(tabelas, 1):
            logger.info("Conteúdo da tabela semanal %d: %s", idx, tabela.text)

    def validar_tabela_diretrizes_irec(self):
        titulos = self.driver.find_elements(By.XPATH, self.VALIDAR_DASH_TABELA_DIR_IREC)
        if not titulos:
            logger.warning("Tabela de diretrizes I-REC não encontrada!")
        for idx, titulo in enumerate(titulos, 1):
            logger.info("Título da tabela I-REC %d: %s", idx, titulo.text)

    def validar_tabela_diretrizes_curto_prazo(self):
        titulos = self.driver.find_elements(By.XPATH, self.VALIDAR_DASH_TABELA_DIR_CURTO_PRAZO)
        if not titulos:
            logger.warning("Tabela de diretrizes de curto prazo não encontrada!")
        for idx, titulo in enumerate(titulos, 1):
            logger.info("Título da tabela Curto Prazo %d: %s", idx, titulo.text)

    def exibir_dados_diretrizes_diarias(self):
        tabelas = self.driver.find_elements(By.XPATH, "//app-diretriz-diaria-dashboard")
        for idx, tabela in enumerate(tabelas, 1):
            logger.info("Conteúdo da tabela de diretrizes diárias %d: %s", idx, tabela.text)

    def exibir_dados_diretrizes_semanais(self):
        tabelas = self.driver.find_elements(By.XPATH, "//app-diretriz-semanal-dashboard")
        for idx, tabela in enumerate(tabelas, 1):
            logger.info("Conteúdo da tabela de diretrizes semanais %d: %s", idx, tabela.text)

    def clicar_ver_historico_diretriz_diaria(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.BTN_VER_HISTORICO_DIR_DIARIA))
        )
        btn.click()
        logger.info("Botão 'Ver Histórico' da Diretriz Diária clicado.")

    def validar_redirecionamento_historico_diaria(self):
        url_esperada = "https://diretrizes.dev.neoenergia.net/pages/diretriz-diaria/historico"
        WebDriverWait(self.driver, 10).until(lambda d: d.current_url == url_esperada)
        if self.driver.current_url == url_esperada:
            logger.info("Usuário foi redirecionado corretamente para: %s", url_esperada)
        else:
            logger.error("Usuário NÃO foi redirecionado corretamente. URL atual: %s", self.driver.current_url)

    def clicar_ver_historico_diretriz_semanal(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.BTN_VER_HISTORICO_DIR_SEMANAL))
        )
        btn.click()
        logger.info("Botão 'Ver Histórico' da Diretriz Semanal clicado.")

    def validar_redirecionamento_historico_semanal(self):
        url_esperada = "https://diretrizes.dev.neoenergia.net/pages/diretriz-semanal/historico"
        WebDriverWait(self.driver, 10).until(lambda d: d.current_url == url_esperada)
        if self.driver.current_url == url_esperada:
            logger.info("Usuário foi redirecionado corretamente para: %s", url_esperada)
        else:
            logger.error("Usuário NÃO foi redirecionado corretamente. URL atual: %s", self.driver.current_url)

    def validar_graficos_historico_diretriz(self):
        # Valida existência do gráfico Comparativo
        comparativo = self.driver.find_elements(By.XPATH, self.XPATH_GRAFICO_COMPARATIVO)
        assert comparativo, "Gráfico 'Comparativo' não encontrado."
        logger.info("Gráfico 'Comparativo' encontrado.")
        # Valida existência do gráfico Histórico Diretrizes
        historico = self.driver.find_elements(By.XPATH, self.XPATH_GRAFICO_HISTORICO)
        assert historico, "Gráfico 'Histórico Diretrizes' não encontrado."
        logger.info("Gráfico 'Histórico Diretrizes' encontrado.")
        # Valida existência do gráfico Negociações BBCE
        bbce = self.driver.find_elements(By.XPATH, self.XPATH_GRAFICO_BBCE)
        assert bbce, "Gráfico 'Negociações BBCE' não encontrado."
        logger.info("Gráfico 'Negociações BBCE' encontrado.")

    def validar_grafico_historico_diretriz(self):
        # Valida existência do gráfico Comparativo
        comparativo = self.driver.find_elements(By.XPATH, self.XPATH_GRAFICO_COMPARATIVO)
        assert comparativo, "Gráfico 'Comparativo' não encontrado."
        logger.info("Gráfico 'Comparativo' encontrado.")
        # Valida existência do gráfico Histórico Diretrizes
        historico = self.driver.find_elements(By.XPATH, self.XPATH_GRAFICOS_HISTORICOS)
        assert historico, "Gráfico 'Histórico Diretrizes' não encontrado."
        logger.info("Gráfico 'Histórico Diretrizes' encontrado.")
        # Valida existência do gráfico Negociações BBCE
        bbce = self.driver.find_elements(By.XPATH, self.XPATH_GRAFICO_BBCE)
        assert bbce, "Gráfico 'Negociações BBCE' não encontrado."
        logger.info("Gráfico 'Negociações BBCE' encontrado.")

    def clicar_exportar_diretriz_diaria(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.BTN_EXPORTAR_DIR_DIARIA))
        )
        btn.click()
        logger.info("Botão 'Exportar' da Diretriz Diária clicado.")

    def clicar_exportar_diretriz_semanal(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.BTN_EXPORTAR_DIR_SEMANAL))
        )
        btn.click()
        logger.info("Botão 'Exportar' da Diretriz Semanal clicado.")

    def clicar_exportar_diretriz_irec(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.BTN_EXPORTAR_DIR_IREC))
        )
        btn.click()
        logger.info("Botão 'Exportar' da Diretriz I-REC clicado.")

    def clicar_exportar_diretriz_curto_prazo(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.BTN_EXPORTAR_DIR_CURTO_PRAZO))
        )
        btn.click()
        logger.info("Botão 'Exportar' da Diretriz Curto Prazo clicado.")

    def acessar_barra_lateral(self):
        logger.info("Acessando a barra de navegação, buscando Prêmio Sazo e Prêmio Flex")

    def validar_abas_premios(self):
        aba_sazo = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ABA_PREMIO_SAZO))
        )
        aba_flex = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ABA_PREMIO_FLEX))
        )
        assert aba_sazo is not None, "Aba Prêmio Sazo não encontrada."
        assert aba_flex is not None, "Aba Prêmio Flex não encontrada."
        logger.info("Abas 'Prêmio Sazo' e 'Prêmio Flex' encontradas.")

    def clicar_fechar_janela_cadastro(self):
        """Clica no botão de fechar (X) da janela de cadastro."""
        try:
            btn_fechar = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.BTN_FECHAR))
            )
            btn_fechar.click()
            logger.info("Botão de fechar janela de cadastro clicado.")
        except Exception as e:
            logger.error(f"Erro ao clicar no botão de fechar janela de cadastro: {e}")
            raise AssertionError("Não foi possível clicar no botão de fechar a janela de cadastro.")
