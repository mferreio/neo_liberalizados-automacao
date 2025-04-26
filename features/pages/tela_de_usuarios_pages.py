from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
from credentials import NOME, EMAIL
from credentials import EDITAR_PERFIL, EDITAR_NOME, EDITAR_EMAIL, PESQUISAR_NOME_CADASTRADO, EXCLUIR_NOME
import logging
from pages.perfil_de_acesso_pages import PerfilDeAcessoPageLocators

class TeladeUsuariosPageLocators:
    VALIDAR_ADMINISTRADOR = (By.XPATH, "//div[@class='flex align-items-center justify-content-between']//span[text()='Administrador']")
    VALIDAR_TELA_PERFIL = (By.XPATH, "/html/body/app-root/app-layout/div/div[2]/div/ng-component/div/div/div/p-toolbar/div/div/div/button")
    VALIDAR_TELA_CADASTRO_USUARIO = (By.XPATH, "//*[@id='pn_id_70_header']")
    BOTAO_PERFIL = (By.XPATH, "/html/body/app-root/app-layout/div/div[1]/app-sidebar/app-menu/ul/li[2]/ul/li[1]")
    BOTAO_NOVO = (By.XPATH, "/html/body/app-root/app-layout/div/div[2]/div/ng-component/div/div/div/p-toolbar/div/div/div/button")
    BTN_FECHAR_TELA_CADASTRO = (By.XPATH, "//button[contains(@class, 'p-dialog-header-close')]")
    BTN_SALVAR_NOVO_CADASTRO = (By.XPATH, "/html/body/app-root/app-layout/div/div[2]/div/ng-component/div/div/p-dialog[1]/div/div/div[4]/button[2]")
    LINHAS_TABELA_USUARIOS = (By.XPATH, "//div[@class='card px-6 py-6']//div[@class='p-datatable-wrapper']//tbody[@class='p-element p-datatable-tbody']//tr[@class='ng-star-inserted']")
    COLUNA_NOME = ".//td[contains(@class, 'nome-coluna')]"
    DROPDOWN_PERFIL = (By.XPATH, "//span[@role='combobox' and @aria-label='Selecione']")
    PERFIL_ADMINISTRADOR = (By.XPATH, "//li[contains(@class, 'p-dropdown-item') and contains(@class, 'p-focus')]")
    PERFIL_PORTFOLIO_TRADING = (By.XPATH, "//*[@id='pn_id_25_1']")
    INPUT_NOME = (By.XPATH, "/html/body/app-root/app-layout/div/div[2]/div/ng-component/div/div/p-dialog[1]/div/div/div[3]/div[2]/input")
    INPUT_EMAIL = (By.XPATH, "/html/body/app-root/app-layout/div/div[2]/div/ng-component/div/div/p-dialog[1]/div/div/div[3]/div[3]/input")
    BOTAO_EDITAR = (By.XPATH, "//tbody[@class='p-element p-datatable-tbody']//button[@icon='pi pi-pencil']")
    FILTRO_NOME = (By.XPATH, "/html/body/app-root/app-layout/div/div[2]/div/ng-component/div/div/div/p-table/div/div[2]/table/thead/tr[2]/th[1]/span/input")
    DROPDOWN_EDITAR_PERFIL = (By.CSS_SELECTOR, "#perfis")
    EDITAR_PERFIL_ADMINISTRADOR = (By.CSS_SELECTOR, "li[role='option'][aria-label='ADMINISTRADOR'].p-dropdown-item")
    EDITAR_PERFIL_PORTFOLIO_TRADING = (By.CSS_SELECTOR, "#li[role='option'][aria-label='PORTFÓLIO E TRADING'].p-dropdown-item")
    INPUT_EDITAR_NOME = (By.CSS_SELECTOR, "#nome")
    INPUT_EDITAR_EMAIL = (By.CSS_SELECTOR, "#email")
    BTN_SALVAR_EDICAO = (By.CSS_SELECTOR, "button[label='Salvar'][icon='pi pi-check'].p-button.p-component")
    BOTAO_EXCLUIR_USUARIO = (By.CSS_SELECTOR, "tbody.p-element.p-datatable-tbody tr.ng-star-inserted td button[icon='pi pi-trash'].p-button-warning")
    BOTAO_CANCELAR_EXCLUSAO = (By.CSS_SELECTOR, "button[label='Não'][icon='pi pi-times'].p-button.p-component")
    BOTAO_CONFIRMAR_EXCLUSAO = (By.CSS_SELECTOR, "button[label='Sim'][icon='pi pi-check'].p-button.p-component")
    BTN_DASHBOARD = (By.XPATH, "//li[@class='ng-tns-c183498709-6 ng-tns-c183498709-5 ng-star-inserted']")
    MENSAGEM_SUCESSO = (By.XPATH, "//div[@data-pc-section='summary' and text()='Sucesso']")
    LINHAS_TABELA_USUARIOS = (By.CSS_SELECTOR, "table tbody tr")
    COLUNA_NOME = (By.CSS_SELECTOR, "td:nth-child(1)")
    COLUNA_EMAIL = (By.CSS_SELECTOR, "td:nth-child(2)")
    COLUNA_PERFIL = (By.CSS_SELECTOR, "td:nth-child(3)")

class TelaDeUsuariosPage:
    def __init__(self, driver):
        self.driver = driver

    def clicar_botao_perfil(self):
        try:
            # Adicionada espera explícita para garantir que o botão esteja visível
            botao_perfil = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TeladeUsuariosPageLocators.BOTAO_PERFIL)
            )
            botao_perfil.click()
            sleep(2)  # Pequena pausa para garantir que a ação seja concluída
        except TimeoutException:
            raise AssertionError("O botão de perfil não foi encontrado ou não está clicável.")

    def clicar_botao_dashboardl(self):
        try:
            # Adicionada espera explícita para garantir que o botão esteja visível
            botao_perfil = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TeladeUsuariosPageLocators.BTN_DASHBOARD)
            )
            botao_perfil.click()
            sleep(2)  # Pequena pausa para garantir que a ação seja concluída
        except TimeoutException:
            raise AssertionError("O botão dashboard não foi encontrado ou não está clicável.")

    def validar_tela_de_usuarios(self):
        try:
            elemento = self.driver.find_element(*TeladeUsuariosPageLocators.VALIDAR_TELA_PERFIL)
            assert elemento is not None, "Usuário não está na tela de Perfil."
            print("Usuário está na tela de Perfil.")
        except NoSuchElementException:
            raise AssertionError("Elemento de validação da tela de Perfil não encontrado.")

    def obter_nomes_usuarios(self):
        try:
            # Localiza todas as células que contêm os nomes usando XPath
            celulas_nome = self.driver.find_elements(By.XPATH, "//table[@role='table']//thead//th[@psortablecolumn='nome']/following::tbody//td[1]")

            # Extrai o texto de cada célula e remove espaços em branco
            nomes = [celula.text.strip() for celula in celulas_nome if celula.text.strip()]

            if not nomes:
                raise AssertionError("Nenhum nome foi encontrado na tabela de usuários.")

            return nomes
        except NoSuchElementException:
            raise AssertionError("Não foi possível encontrar os nomes cadastrados na tabela.")

    def obter_usuarios_cadastrados(self):
        """Obtém a lista de usuários cadastrados exibindo nome, email e perfil."""
        try:
            logging.info("Obtendo a lista de usuários cadastrados.")
            linhas_tabela = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(TeladeUsuariosPageLocators.LINHAS_TABELA_USUARIOS)
            )
            usuarios = []
            for linha in linhas_tabela:
                nome = linha.find_element(*TeladeUsuariosPageLocators.COLUNA_NOME).text.strip()
                email = linha.find_element(*TeladeUsuariosPageLocators.COLUNA_EMAIL).text.strip()
                perfil = linha.find_element(*TeladeUsuariosPageLocators.COLUNA_PERFIL).text.strip()
                usuarios.append({"nome": nome, "email": email, "perfil": perfil})
            logging.info(f"Usuários cadastrados encontrados: {usuarios}")
            return usuarios
        except Exception as e:
            logging.error(f"Erro ao obter a lista de usuários cadastrados: {e}")
            return []

    def clicar_botao_novo(self):
        try:
            # Adicionada espera explícita para garantir que o botão esteja visível
            botao_novo = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TeladeUsuariosPageLocators.BOTAO_NOVO)
            )
            botao_novo.click()
            sleep(2)  # Pequena pausa para garantir que a ação seja concluída
        except TimeoutException:
            raise AssertionError("O botão 'Novo' não foi encontrado ou não está clicável.")

    def validar_tela_cadastro_usuario(self):
        try:
            # Adicionada espera explícita para garantir que o elemento esteja visível
            elemento = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(TeladeUsuariosPageLocators.VALIDAR_TELA_CADASTRO_USUARIO)
            )
            assert elemento is not None, "Usuário não está na tela de cadastro de usuário."
            print("Usuário está na tela de cadastro de usuário.")
        except TimeoutException:
            raise AssertionError("Elemento de validação da tela de cadastro de usuário não encontrado.")

    def clicar_fechar_tela_cadastro(self):
        try:
            # Adicionada espera explícita para garantir que o botão esteja visível
            botao_fechar_tela_cadastro = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TeladeUsuariosPageLocators.BTN_FECHAR_TELA_CADASTRO)
            )
            botao_fechar_tela_cadastro.click()
            sleep(2)  # Pequena pausa para garantir que a ação seja concluída
        except TimeoutException:
            raise AssertionError("O botão 'Novo' não foi encontrado ou não está clicável.")

    def clicar_dropdown_perfil(self):
        try:
            # Adicionada espera explícita para garantir que o dropdown esteja visível
            dropdown_perfil = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(TeladeUsuariosPageLocators.DROPDOWN_PERFIL)
            )
            # Força o clique no elemento usando JavaScript
            self.driver.execute_script("arguments[0].click();", dropdown_perfil)
            sleep(2)  # Pequena pausa para garantir que a ação seja concluída
        except TimeoutException:
            raise AssertionError("O dropdown de perfil não foi encontrado ou não está clicável.")

    def selecionar_perfil_usuario(self, tipo_perfil):
        """Seleciona o perfil de usuário utilizando JavaScript para garantir a interação."""
        try:
            if tipo_perfil == "ADMINISTRADOR":
                perfil = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(TeladeUsuariosPageLocators.PERFIL_ADMINISTRADOR)
                )
            elif tipo_perfil == "PORTFÓLIO E TRADING":
                perfil = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(TeladeUsuariosPageLocators.PERFIL_PORTFOLIO_TRADING)
                )
            else:
                raise ValueError(f"Tipo de perfil desconhecido: {tipo_perfil}")
            # Força o clique no elemento usando JavaScript
            self.driver.execute_script("arguments[0].click();", perfil)
            logging.info(f"Perfil '{tipo_perfil}' selecionado com sucesso.")
            sleep(2)  # Pequena pausa para garantir que a ação seja concluída
        except TimeoutException:
            raise AssertionError(f"O perfil '{tipo_perfil}' não foi encontrado ou não está clicável.")
        except Exception as e:
            logging.error(f"Erro ao selecionar o perfil '{tipo_perfil}'. Detalhes: {e}")
            raise

    def inserir_nome_email(self):
        try:
            # Insere o nome
            input_nome = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(TeladeUsuariosPageLocators.INPUT_NOME)
            )
            input_nome.clear()
            input_nome.send_keys(NOME)

            # Insere o email
            input_email = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(TeladeUsuariosPageLocators.INPUT_EMAIL)
            )
            input_email.clear()
            input_email.send_keys(EMAIL)

            print(f"Nome '{NOME}' e email '{EMAIL}' inseridos com sucesso.")
        except TimeoutException:
            raise AssertionError("Não foi possível localizar os campos de nome ou email.")

    def clicar_botao_salvar(self):
        try:
            # Adicionada espera explícita para garantir que o botão esteja visível
            botao_salvar_cadastro = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TeladeUsuariosPageLocators.BTN_SALVAR_NOVO_CADASTRO)
            )
            botao_salvar_cadastro.click()
            sleep(2)  # Pequena pausa para garantir que a ação seja concluída
        except TimeoutException:
            raise AssertionError("O botão 'Novo' não foi encontrado ou não está clicável.")

    def validar_mensagem_sucesso(self):
        """Valida se a mensagem de sucesso foi exibida."""
        try:
            mensagem_sucesso = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(TeladeUsuariosPageLocators.MENSAGEM_SUCESSO)
            )
            return mensagem_sucesso.is_displayed()
        except TimeoutException:
            logging.error("Mensagem de sucesso não foi exibida.")
            return False

    def validar_usuario_presente(self, nome_usuario):
        """Valida se o usuário está presente na tabela."""
        try:
            filtro_nome = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(TeladeUsuariosPageLocators.FILTRO_NOME)
            )
            filtro_nome.clear()
            filtro_nome.send_keys(nome_usuario)
            sleep(2)  # Aguarda o filtro ser aplicado

            linhas_tabela = self.driver.find_elements(*TeladeUsuariosPageLocators.LINHAS_TABELA_USUARIOS)
            for linha in linhas_tabela:
                nome = linha.find_element(*TeladeUsuariosPageLocators.COLUNA_NOME).text.strip()
                if nome == nome_usuario:
                    return True
            return False
        except TimeoutException:
            logging.error(f"Erro ao validar a presença do usuário '{nome_usuario}'.")
            return False

    def pesquisar_e_clicar_editar(self, pesquisar_nome_Cadastrado):
        try:
            # Insere o nome no filtro
            filtro_nome = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(TeladeUsuariosPageLocators.FILTRO_NOME)
            )
            filtro_nome.clear()
            filtro_nome.send_keys(pesquisar_nome_Cadastrado)
            sleep(2)  # Aguarda o filtro ser aplicado

            botao_editar = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TeladeUsuariosPageLocators.BOTAO_EDITAR)
            )
            botao_editar.click()
            sleep(2)
            print(f"Usuário '{pesquisar_nome_Cadastrado}' encontrado e botão 'Editar' clicado.")
        except TimeoutException:
            raise AssertionError(f"Usuário '{pesquisar_nome_Cadastrado}' não encontrado ou botão 'Editar' não clicável.")
        sleep(2)

    def editar_perfil_usuario(self):
        try:
            # Adicionada espera explícita para garantir que o dropdown esteja visível
            dropdown_editar_perfil = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(TeladeUsuariosPageLocators.DROPDOWN_EDITAR_PERFIL)
            )
            # Força o clique no elemento usando JavaScript
            self.driver.execute_script("arguments[0].click();", dropdown_editar_perfil)
            sleep(2)

            # Seleciona o perfil com base no EDITAR_PERFIL
            if EDITAR_PERFIL == "ADMINISTRADOR":
                perfil = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(TeladeUsuariosPageLocators.EDITAR_PERFIL_ADMINISTRADOR)
                )
            elif EDITAR_PERFIL == "PORTFOLIO_TRADING":
                perfil = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(TeladeUsuariosPageLocators.EDITAR_PERFIL_PORTFOLIO_TRADING)
                )
            else:
                raise ValueError(f"Perfil desconhecido: {EDITAR_PERFIL}")
            perfil.click()
            print(f"Dados do usuário editados: Perfil='{EDITAR_PERFIL}'.")
            sleep(2)
        except TimeoutException:
            raise AssertionError("Erro ao editar o perfil do usuário: elemento não encontrado ou não clicável.")

    def editar_nome_e_email_usuario(self):
        try:
            # Edita o nome
            input_nome = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(TeladeUsuariosPageLocators.INPUT_EDITAR_NOME)
            )
            input_nome.clear()
            input_nome.send_keys(EDITAR_NOME)

            # Edita o email
            input_email = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(TeladeUsuariosPageLocators.INPUT_EDITAR_EMAIL)
            )
            input_email.clear()
            input_email.send_keys(EDITAR_EMAIL)
            print(f"Dados do usuário editados: Perfil= Nome='{EDITAR_NOME}', Email='{EDITAR_EMAIL}'.")
        except TimeoutException:
            raise AssertionError("O botão 'Salvar' não foi encontrado ou não está clicável.")

    def clicar_botao_salvar_edicao(self):
        try:
            # Adicionada espera explícita para garantir que o botão esteja visível
            botao_salvar_edicao = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TeladeUsuariosPageLocators.BTN_SALVAR_EDICAO)
            )
            # Força o clique no botão usando JavaScript, caso esteja bloqueado
            self.driver.execute_script("arguments[0].click();", botao_salvar_edicao)
            sleep(2)  # Pequena pausa para garantir que a ação seja concluída
            print("Botão 'Salvar' clicado com sucesso.")
        except TimeoutException:
            raise AssertionError("O botão 'Salvar' não foi encontrado ou não está clicável.")

    def pesquisa_usuario_cadastrado(self, excluir_nome):
        try:
            # Insere o nome no filtro
            filtro_nome_para_excluir = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(TeladeUsuariosPageLocators.FILTRO_NOME)
            )
            filtro_nome_para_excluir.clear()
            filtro_nome_para_excluir.send_keys(excluir_nome)
            sleep(2)  # Aguarda o filtro ser aplicado
        except TimeoutException:
            raise AssertionError(f"Usuário '{excluir_nome}' não encontrado.")
        sleep(2)

    def cancelar_exclusao_de_usuario(self, excluir_nome):
        try:
            # Insere o nome no filtro
            filtro_nome_para_excluir = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(TeladeUsuariosPageLocators.FILTRO_NOME)
            )
            filtro_nome_para_excluir.clear()
            filtro_nome_para_excluir.send_keys(excluir_nome)
            sleep(2)  # Aguarda o filtro ser aplicado

            # Clica no botão "Excluir" do usuário
            botao_excluir_usuario = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TeladeUsuariosPageLocators.BOTAO_EXCLUIR_USUARIO)
            )
            botao_excluir_usuario.click()
            sleep(2)  # Aguarda 2 segundos

            # Clica no botão "Não" para cancelar a exclusão
            botao_cancelar_exclusao = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TeladeUsuariosPageLocators.BOTAO_CANCELAR_EXCLUSAO)
            )
            botao_cancelar_exclusao.click()
            print(f"Exclusão do usuário '{excluir_nome}' foi cancelada com sucesso.")
        except TimeoutException:
            raise AssertionError(f"Erro ao cancelar a exclusão do usuário '{excluir_nome}': elemento não encontrado ou não clicável.")

    def excluir_usuario_cadastrado(self):
        try:
            # Clica no botão "Excluir" do usuário
            botao_excluir_usuario = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TeladeUsuariosPageLocators.BOTAO_EXCLUIR_USUARIO)
            )
            botao_excluir_usuario.click()
            # Clica no botão "Sim" para confirmar a exclusão
            botao_confirmar_exclusao = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TeladeUsuariosPageLocators.BOTAO_CONFIRMAR_EXCLUSAO)
            )
            botao_confirmar_exclusao.click()
            sleep(2)
            print("Usuário encontrado e botão 'excluir' clicado.")
        except TimeoutException:
            raise AssertionError("Usuário não encontrado ou botão 'excluir' não clicável.")
        sleep(2)
