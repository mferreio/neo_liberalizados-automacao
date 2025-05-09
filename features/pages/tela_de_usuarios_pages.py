import logging
import os
from time import sleep

from pages.perfil_de_acesso_pages import PerfilDeAcessoPageLocators
from selenium.common.exceptions import (NoSuchElementException,
                                        StaleElementReferenceException,
                                        TimeoutException)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from credentials import (EDITAR_EMAIL, EDITAR_NOME, EDITAR_PERFIL, EMAIL,
                         EXCLUIR_NOME, NOME, PESQUISAR_NOME_CADASTRADO)


class TeladeUsuariosPageLocators:
    VALIDAR_ADMINISTRADOR = (
        By.XPATH,
        "//div[@class='flex align-items-center justify-content-between']//span[text()='Administrador']",
    )
    VALIDAR_TELA_CADASTRO_USUARIO = (By.XPATH, "//*[@id='pn_id_70_header']")
    BOTAO_PERFIL = (
        By.XPATH,
        "/html/body/app-root/app-layout/div/div[1]/app-sidebar/app-menu/ul/li[2]/ul/li[1]",
    )
    BOTAO_NOVO = (
        By.XPATH,
        "/html/body/app-root/app-layout/div/div[2]/div/ng-component/div/div/div/p-toolbar/div/div/div/button",
    )
    BTN_FECHAR_TELA_CADASTRO = (
        By.XPATH,
        "//button[contains(@class, 'p-dialog-header-close')]",
    )
    BTN_SALVAR_NOVO_CADASTRO = (
        By.XPATH,
        "/html/body/app-root/app-layout/div/div[2]/div/ng-component/div/div/p-dialog[1]/div/div/div[4]/button[2]",
    )
    LINHAS_TABELA_USUARIOS = (
        By.XPATH,
        "//div[@class='card px-6 py-6']//div[@class='p-datatable-wrapper']//tbody[@class='p-element p-datatable-tbody']//tr[@class='ng-star-inserted']",
    )
    COLUNA_NOME = ".//td[contains(@class, 'nome-coluna')]"
    DROPDOWN_PERFIL = (By.XPATH, "//span[@role='combobox' and @aria-label='Selecione']")
    PERFIL_ADMINISTRADOR = (
        By.XPATH,
        "//div[@class='p-dropdown-items-wrapper']//li[contains(., 'ADMINISTRADOR') and @role='option' and @aria-label='ADMINISTRADOR']",
    )
    PERFIL_PORTFOLIO_TRADING = (
        By.XPATH,
        "//div[@class='p-dropdown-items-wrapper']//li[contains(., 'PORTFÓLIO E TRADING') and @role='option' and @aria-label='PORTFÓLIO E TRADING']",
    )
    INPUT_NOME = (
        By.XPATH,
        "//div[@role='dialog']//input[1][@type='text' and @id='nome']",
    )
    INPUT_EMAIL = (
        By.XPATH,
        "//div[@role='dialog']//input[1][@type='email' and @id='email']",
    )
    BOTAO_EDITAR = (By.XPATH, "//button[.//span[contains(@class, 'pi-pencil')]]")
    FILTRO_NOME = (
        By.XPATH,
        "/html/body/app-root/app-layout/div/div[2]/div/ng-component/div/div/div/p-table/div/div[2]/table/thead/tr[2]/th[1]/span/input",
    )
    DROPDOWN_EDITAR_PERFIL = (By.CSS_SELECTOR, "#perfis")
    INPUT_EDITAR_NOME = (By.CSS_SELECTOR, "#nome")
    INPUT_EDITAR_EMAIL = (By.CSS_SELECTOR, "#email")
    BTN_SALVAR_EDICAO = (
        By.CSS_SELECTOR,
        "button[label='Salvar'][icon='pi pi-check'].p-button.p-component",
    )
    BOTAO_EXCLUIR_USUARIO = (
        By.XPATH,
        "//span[contains(@class, 'p-button-icon') and contains(@class, 'pi') and contains(@class, 'pi-trash')]",
    )
    BOTAO_CONFIRMAR_EXCLUSAO = (
        By.XPATH,
        "/html/body/app-root/app-layout/div/div[2]/div/ng-component/div/div/p-dialog[2]/div/div/div[4]/button[2]",
    )
    BOTAO_NAO_CONFIRMAR_EXCLUSAO = (
        By.XPATH,
        "//div[@role='dialog']//button[contains(@class, 'p-button-text') and @label='Não']",
    )
    BTN_DASHBOARD = (
        By.XPATH,
        "//li[@class='ng-tns-c183498709-6 ng-tns-c183498709-5 ng-star-inserted']",
    )
    LINHAS_TABELA_USUARIOS = (By.CSS_SELECTOR, "table tbody tr")
    COLUNA_NOME = (By.CSS_SELECTOR, "td:nth-child(1)")
    COLUNA_EMAIL = (By.CSS_SELECTOR, "td:nth-child(2)")
    COLUNA_PERFIL = (By.CSS_SELECTOR, "td:nth-child(3)")


class TelaDeUsuariosPage:
    def __init__(self, driver):
        self.driver = driver

    def clicar_botao_perfil(self):
        try:
            botao_perfil = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TeladeUsuariosPageLocators.BOTAO_PERFIL)
            )
            botao_perfil.click()
        except TimeoutException:
            raise AssertionError(
                "O botão de perfil não foi encontrado ou não está clicável."
            )

    def clicar_botao_dashboardl(self):
        try:
            botao_dashboard = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TeladeUsuariosPageLocators.BTN_DASHBOARD)
            )
            botao_dashboard.click()
        except TimeoutException:
            raise AssertionError(
                "O botão dashboard não foi encontrado ou não está clicável."
            )

    def obter_nomes_usuarios(self):
        try:
            celulas_nome = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    (
                        By.XPATH,
                        "//table[@role='table']//thead//th[@psortablecolumn='nome']/following::tbody//td[1]",
                    )
                )
            )
            nomes = [
                celula.text.strip() for celula in celulas_nome if celula.text.strip()
            ]
            if not nomes:
                raise AssertionError(
                    "Nenhum nome foi encontrado na tabela de usuários."
                )
            return nomes
        except TimeoutException:
            raise AssertionError(
                "Não foi possível encontrar os nomes cadastrados na tabela."
            )

    def obter_usuarios_cadastrados(self):
        try:
            linhas = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table tbody tr"))
            )
            usuarios = []
            for linha in linhas:
                nome = linha.find_element(
                    By.CSS_SELECTOR, "td:nth-child(1)"
                ).text.strip()
                email = linha.find_element(
                    By.CSS_SELECTOR, "td:nth-child(2)"
                ).text.strip()
                perfil = linha.find_element(
                    By.CSS_SELECTOR, "td:nth-child(3)"
                ).text.strip()
                usuarios.append({"nome": nome, "email": email, "perfil": perfil})
            return usuarios
        except TimeoutException:
            return []

    def clicar_botao_novo(self):
        try:
            botao_novo = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TeladeUsuariosPageLocators.BOTAO_NOVO)
            )
            botao_novo.click()
        except TimeoutException:
            raise AssertionError(
                "O botão 'Novo' não foi encontrado ou não está clicável."
            )

    def validar_tela_cadastro_usuario(self):
        try:
            elemento = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    TeladeUsuariosPageLocators.VALIDAR_TELA_CADASTRO_USUARIO
                )
            )
            assert (
                elemento is not None
            ), "Usuário não está na tela de cadastro de usuário."
        except TimeoutException:
            raise AssertionError(
                "Elemento de validação da tela de cadastro de usuário não encontrado."
            )

    def clicar_fechar_tela_cadastro(self):
        try:
            botao_fechar_tela_cadastro = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    TeladeUsuariosPageLocators.BTN_FECHAR_TELA_CADASTRO
                )
            )
            botao_fechar_tela_cadastro.click()
        except TimeoutException:
            raise AssertionError(
                "O botão 'Fechar' não foi encontrado ou não está clicável."
            )

    def clicar_dropdown_perfil(self):
        try:
            dropdown_perfil = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    TeladeUsuariosPageLocators.DROPDOWN_PERFIL
                )
            )
            self.driver.execute_script("arguments[0].click();", dropdown_perfil)
        except TimeoutException:
            raise AssertionError(
                "O dropdown de perfil não foi encontrado ou não está clicável."
            )

    def selecionar_perfil_usuario(self, tipo_perfil):
        try:
            if tipo_perfil == "ADMINISTRADOR":
                perfil = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        TeladeUsuariosPageLocators.PERFIL_ADMINISTRADOR
                    )
                )
            elif tipo_perfil == "PORTFÓLIO E TRADING":
                perfil = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        TeladeUsuariosPageLocators.PERFIL_PORTFOLIO_TRADING
                    )
                )
            else:
                raise ValueError(f"Tipo de perfil desconhecido: {tipo_perfil}")
            self.driver.execute_script("arguments[0].click();", perfil)
        except TimeoutException:
            raise AssertionError(
                f"O perfil '{tipo_perfil}' não foi encontrado ou não está clicável."
            )

    def inserir_nome_email(self):
        try:
            input_nome = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(TeladeUsuariosPageLocators.INPUT_NOME)
            )
            input_nome.clear()
            input_nome.send_keys(NOME)

            input_email = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(TeladeUsuariosPageLocators.INPUT_EMAIL)
            )
            input_email.clear()
            input_email.send_keys(EMAIL)
        except TimeoutException:
            raise AssertionError(
                "Não foi possível localizar os campos de nome ou email."
            )

    def clicar_botao_salvar(self):
        try:
            botao_salvar_cadastro = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    TeladeUsuariosPageLocators.BTN_SALVAR_NOVO_CADASTRO
                )
            )
            botao_salvar_cadastro.click()
        except TimeoutException:
            raise AssertionError(
                "O botão 'Salvar' não foi encontrado ou não está clicável."
            )

    def validar_usuario_presente(self, nome_usuario):
        try:
            filtro_nome = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(TeladeUsuariosPageLocators.FILTRO_NOME)
            )
            filtro_nome.clear()
            filtro_nome.send_keys(nome_usuario)

            linhas_tabela = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    TeladeUsuariosPageLocators.LINHAS_TABELA_USUARIOS
                )
            )
            for linha in linhas_tabela:
                nome = linha.find_element(
                    *TeladeUsuariosPageLocators.COLUNA_NOME
                ).text.strip()
                if nome == nome_usuario:
                    return True
            return False
        except TimeoutException:
            return False

    def pesquisar_e_clicar_editar(self, pesquisar_nome_Cadastrado):
        try:
            filtro_nome = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(TeladeUsuariosPageLocators.FILTRO_NOME)
            )
            filtro_nome.clear()
            filtro_nome.send_keys(pesquisar_nome_Cadastrado)
            sleep(2)  # Espera a tabela atualizar após a pesquisa
            # Localizar o botão "Editar" novamente antes de clicar
            botao_editar = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TeladeUsuariosPageLocators.BOTAO_EDITAR)
            )
            botao_editar.click()
        except StaleElementReferenceException:
            # Re-localizar o botão "Editar" em caso de StaleElementReferenceException
            botao_editar = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TeladeUsuariosPageLocators.BOTAO_EDITAR)
            )
            botao_editar.click()
        except TimeoutException:
            raise AssertionError(
                f"Usuário '{pesquisar_nome_Cadastrado}' não encontrado ou botão 'Editar' não clicável."
            )

    def editar_perfil_usuario(self):
        try:
            dropdown_editar_perfil = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    TeladeUsuariosPageLocators.DROPDOWN_EDITAR_PERFIL
                )
            )
            self.driver.execute_script("arguments[0].click();", dropdown_editar_perfil)

            if EDITAR_PERFIL == "ADMINISTRADOR":
                perfil = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(
                        TeladeUsuariosPageLocators.PERFIL_ADMINISTRADOR
                    )
                )
            elif EDITAR_PERFIL == "PORTFÓLIO E TRADING":
                perfil = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(
                        TeladeUsuariosPageLocators.PERFIL_PORTFOLIO_TRADING
                    )
                )
            else:
                raise ValueError(f"Perfil desconhecido: {EDITAR_PERFIL}")
            perfil.click()
        except TimeoutException:
            raise AssertionError(
                "Erro ao editar o perfil do usuário: elemento não encontrado ou não clicável."
            )

    def editar_nome_e_email_usuario(self):
        try:
            input_nome = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    TeladeUsuariosPageLocators.INPUT_EDITAR_NOME
                )
            )
            input_nome.clear()
            input_nome.send_keys(EDITAR_NOME)

            input_email = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    TeladeUsuariosPageLocators.INPUT_EDITAR_EMAIL
                )
            )
            input_email.clear()
            input_email.send_keys(EDITAR_EMAIL)
        except TimeoutException:
            raise AssertionError(
                "Não foi possível localizar os campos de edição de nome ou email."
            )

    def clicar_botao_salvar_edicao(self):
        try:
            botao_salvar_edicao = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TeladeUsuariosPageLocators.BTN_SALVAR_EDICAO)
            )
            self.driver.execute_script("arguments[0].click();", botao_salvar_edicao)
        except TimeoutException:
            raise AssertionError(
                "O botão 'Salvar' não foi encontrado ou não está clicável."
            )

    def pesquisa_usuario_cadastrado(self, editar_nome):
        try:
            filtro_nome_para_excluir = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(TeladeUsuariosPageLocators.FILTRO_NOME)
            )
            filtro_nome_para_excluir.clear()
            filtro_nome_para_excluir.send_keys(editar_nome)
        except TimeoutException:
            raise AssertionError(f"Usuário '{editar_nome}' não encontrado.")
        sleep(2)

    def clicar_botao_excluir_usuario(self):
        try:
            botao_excluir_usuario = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    TeladeUsuariosPageLocators.BOTAO_EXCLUIR_USUARIO
                )
            )
            botao_excluir_usuario.click()
        except StaleElementReferenceException:
            # Re-localizar o botão "Excluir" em caso de StaleElementReferenceException
            botao_excluir_usuario = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    TeladeUsuariosPageLocators.BOTAO_EXCLUIR_USUARIO
                )
            )
            botao_excluir_usuario.click()
            sleep(1)  # Espera a tabela atualizar após a pesquisa
        except TimeoutException:
            raise AssertionError("Erro ao localizar ou clicar no botão 'Excluir'.")

    def clicar_cancelar_exclusao_usuario(self):
        try:
            botao_nao_confirmar_exclusao = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    TeladeUsuariosPageLocators.BOTAO_NAO_CONFIRMAR_EXCLUSAO
                )
            )
            botao_nao_confirmar_exclusao.click()
        except TimeoutException:
            raise AssertionError(
                "Erro ao clicar em não excluir usuario: elemento não encontrado ou não clicável."
            )

    def clicar_confirmar_exclusao_usuario(self):
        try:
            botao_nao_confirmar_exclusao = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    TeladeUsuariosPageLocators.BOTAO_CONFIRMAR_EXCLUSAO
                )
            )
            botao_nao_confirmar_exclusao.click()
        except TimeoutException:
            raise AssertionError(
                "Erro ao clicar em sim para excluir usuario: elemento não encontrado ou não clicável."
            )

    def validar_tela_de_usuarios(self):
        try:
            current_url = WebDriverWait(self.driver, 10).until(
                lambda driver: driver.current_url
            )
            expected_url = "https://diretrizes.dev.neoenergia.net/pages/perfil/listar"
            return current_url == expected_url
        except Exception:
            return False

    def selecionar_perfil_administrador_e_inserir_dados(self):
        try:
            WebDriverWait(self.driver, 10).until(
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
            email.send_keys(os.getenv("EMAIL"))
        except TimeoutException:
            raise AssertionError(
                "Erro ao selecionar o perfil de administrador ou inserir os dados."
            )
