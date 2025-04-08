from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
import logging
from time import sleep

class PerfilDeAcessoPageLocators:
    """Locators for the Perfil de Acesso Page."""
    VALIDAR_ADMINISTRADOR = (By.XPATH, "//div[@class='admin']")  # Exemplo de locator para validar administrador
    VALIDAR_TRADING_E_PORTIFOLIO = (By.XPATH, "//div[@class='portifolio']")  # Exemplo de locator para validar portfólio
    
    #Acessar a barra de navegação lateral
    DASHBOARD = (By.XPATH, '/html/body/app-root/app-layout/div/div[1]/app-sidebar/app-menu/ul/li[1]/ul/li/a')
    PERFIL = (By.XPATH, "/html/body/app-root/app-layout/div/div[1]/app-sidebar/app-menu/ul/li[2]/ul/li[1]/a")
    DIRETRIZ_CURTO_PRAZO = (By.XPATH, '/html/body/app-root/app-layout/div/div[1]/app-sidebar/app-menu/ul/li[2]/ul/li[3]/a')
    DIRETRIZ_I_REC = (By.XPATH, '/html/body/app-root/app-layout/div/div[1]/app-sidebar/app-menu/ul/li[2]/ul/li[4]/a')
    DIRETRIZ_SEMANAL = (By.XPATH, '/html/body/app-root/app-layout/div/div[1]/app-sidebar/app-menu/ul/li[2]/ul/li[5]/a')
    DIRETRIZ_DIARIA = (By.XPATH, '/html/body/app-root/app-layout/div/div[1]/app-sidebar/app-menu/ul/li[2]/ul/li[3]/a')
    PRECOS_MERCADO_DIRETRIZ = (By.XPATH, '/html/body/app-root/app-layout/div/div[1]/app-sidebar/app-menu/ul/li[2]/ul/li[6]/a')
    BBCE = (By.XPATH, '/html/body/app-root/app-layout/div/div[1]/app-sidebar/app-menu/ul/li[2]/ul/li[7]/a')
    CNAE = (By.XPATH, '/html/body/app-root/app-layout/div/div[1]/app-sidebar/app-menu/ul/li[2]/ul/li[8]/a')
    SHAPE_DETERMINISTICO = (By.XPATH, '/html/body/app-root/app-layout/div/div[1]/app-sidebar/app-menu/ul/li[2]/ul/li[9]/a')
    PRODUTOS = (By.XPATH, '/html/body/app-root/app-layout/div/div[1]/app-sidebar/app-menu/ul/li[2]/ul/li[10]/a')
    
    
    #Botões de ação e subações
    CADASTRO_USUARIOS = (By.CSS_SELECTOR, 'button.p-element.p-ripple.p-button-success.mr-2.w-8rem.p-button.p-component')
    NOVO = (By.CSS_SELECTOR, 'button.p-element.p-ripple.p-button-success.mr-2.w-8rem.p-button.p-component')
    PRODUTOS_DIARIO_SEMANAL = (By.CSS_SELECTOR, 'li[app-menuitem].ng-tns-c183498709-14.ng-star-inserted')
    PRODUTOS_I_REC = (By.CSS_SELECTOR, 'a.p-ripple.p-element.ng-tns-c183498709-15.ng-star-inserted')
    PRODUTOS_CURTO_PRAZO = (By.CSS_SELECTOR, 'a[href="/pages/short-products"]')
    
    #Assertivas de telas
    DASHBOARD_TELA = (By.CSS_SELECTOR, 'h5.text-primary.text-center.text-2xl.font-semibold.mb-4')
    CADASTRO_USUARIOS_TELA = (By.CSS_SELECTOR, 'div.p-dialog-header.ng-tns-c131382906-131.ng-star-inserted')
    CADASTRO_DIRETRIZ_CURTO_PRAZO_TELA = (By.CSS_SELECTOR, 'p.text-3xl.font-bold.text-green-500')
    CADASTRO_DIRETRIZ_I_REC_TELA = (By.CSS_SELECTOR, 'p.text-3xl.font-bold.text-green-500')
    CADASTRO_DIRETRIZ_SEMANAL_TELA = (By.CSS_SELECTOR, 'div.card.px-6.py-6 > p.text-3xl.font-bold.text-green-500')
    CADASTRO_DIRETRIZ_DIARIA_TELA = (By.CSS_SELECTOR, 'p.text-3xl.font-bold.text-green-500')
    PRECOS_MERCADO_DIRETRIZ_TELA  = (By.CSS_SELECTOR, 'div.card.px-6.py-6 > p.text-3xl.font-bold')
    BBCE_TELA = (By.CSS_SELECTOR, 'div.card > p.text-3xl.font-bold')
    CNAE_TELA = (By.CSS_SELECTOR, 'div.col-12 > p.text-3xl.font-bold')
    SHAPE_DETERMINISTICO_TELA  = (By.CSS_SELECTOR, 'div.card.px-6.py-6 > p.text-3xl.font-bold') 
    CADASTRO_PRODUTOS_DIARIO_SEMANAL_TELA = (By.CSS_SELECTOR, 'div.p-fluid > p.text-3xl.font-bold.text-green-500')
    CADASTRO_PRODUTOS_I_REC_TELA = (By.CSS_SELECTOR, 'div.card.px-6.py-6 > div.p-fluid > p.text-3xl.font-bold.text-green-500')
    CADASTRO_PRODUTOS_CURTO_PRAZO_TELA = (By.CSS_SELECTOR, 'div.p-fluid > p.text-3xl.font-bold.text-green-500') 
    
    
class PerfilDeAcessoPage:
    def __init__(self, driver):
        self.driver = driver
        self.perfil = None
        
    def validar_usuario_administrador(self):
        try:
            elemento = self.driver.find_element(*PerfilDeAcessoPageLocators.VALIDAR_ADMINISTRADOR)
            assert elemento is not None, "Usuário não está logado como Administrador."
            print("Usuário validado como Administrador.")
        except NoSuchElementException:
            raise AssertionError("Elemento de validação de Administrador não encontrado.")
    
    

    def possui_acesso_total(self):
        """Valida se o usuário tem acesso total ao sistema clicando e verificando várias telas."""
        acoes = [
            {"botao": PerfilDeAcessoPageLocators.DASHBOARD, "validacao": PerfilDeAcessoPageLocators.DASHBOARD_TELA, "mensagem": "Tela do Dashboard não está acessível."},
            {"botao": PerfilDeAcessoPageLocators.PERFIL, "subacao": PerfilDeAcessoPageLocators.NOVO, "validacao": PerfilDeAcessoPageLocators.CADASTRO_USUARIOS_TELA, "mensagem": "Página do Cadastro de Usuários não está acessível."},
            {"botao": PerfilDeAcessoPageLocators.DIRETRIZ_CURTO_PRAZO, "subacao": PerfilDeAcessoPageLocators.NOVO, "validacao": PerfilDeAcessoPageLocators.CADASTRO_DIRETRIZ_CURTO_PRAZO_TELA, "mensagem": "Página do Cadastro de Diretriz Curto Prazo não está acessível."},
            {"botao": PerfilDeAcessoPageLocators.DIRETRIZ_I_REC, "subacao": PerfilDeAcessoPageLocators.NOVO, "validacao": PerfilDeAcessoPageLocators.CADASTRO_DIRETRIZ_I_REC_TELA, "mensagem": "Página do Cadastro de Diretriz I-REC não está acessível."},
            {"botao": PerfilDeAcessoPageLocators.DIRETRIZ_SEMANAL, "subacao": PerfilDeAcessoPageLocators.NOVO, "validacao": PerfilDeAcessoPageLocators.CADASTRO_DIRETRIZ_SEMANAL_TELA, "mensagem": "Página do Cadastro de Diretriz Semanal não está acessível."},
            {"botao": PerfilDeAcessoPageLocators.DIRETRIZ_DIARIA, "subacao": PerfilDeAcessoPageLocators.NOVO, "validacao": PerfilDeAcessoPageLocators.CADASTRO_DIRETRIZ_DIARIA_TELA, "mensagem": "Página do Cadastro de Diretriz Diária não está acessível."},
            {"botao": PerfilDeAcessoPageLocators.PRECOS_MERCADO_DIRETRIZ, "validacao": PerfilDeAcessoPageLocators.PRECOS_MERCADO_DIRETRIZ_TELA, "mensagem": "Tela de Preços de Mercado e Diretriz não está acessível."},
            {"botao": PerfilDeAcessoPageLocators.BBCE, "validacao": PerfilDeAcessoPageLocators.BBCE_TELA, "mensagem": "Tela do BBCE não está acessível."},
            {"botao": PerfilDeAcessoPageLocators.CNAE, "validacao": PerfilDeAcessoPageLocators.CNAE_TELA, "mensagem": "Tela do CNAE não está acessível."},
            {"botao": PerfilDeAcessoPageLocators.SHAPE_DETERMINISTICO, "validacao": PerfilDeAcessoPageLocators.SHAPE_DETERMINISTICO_TELA, "mensagem": "Tela do Shape Determinístico não está acessível."},
            {"botao": PerfilDeAcessoPageLocators.PRODUTOS, "subacao": PerfilDeAcessoPageLocators.PRODUTOS_DIARIO_SEMANAL, "subacao2": PerfilDeAcessoPageLocators.NOVO, "validacao": PerfilDeAcessoPageLocators.CADASTRO_PRODUTOS_DIARIO_SEMANAL_TELA, "mensagem": "Página do Cadastro de produtos Diário/Semanal não está acessível."},
            {"botao": PerfilDeAcessoPageLocators.PRODUTOS, "subacao": PerfilDeAcessoPageLocators.PRODUTOS_I_REC, "subacao2": PerfilDeAcessoPageLocators.NOVO, "validacao": PerfilDeAcessoPageLocators.CADASTRO_PRODUTOS_I_REC_TELA, "mensagem": "Página do Cadastro de produtos I-REC não está acessível."},
            {"botao": PerfilDeAcessoPageLocators.PRODUTOS, "subacao": PerfilDeAcessoPageLocators.PRODUTOS_CURTO_PRAZO, "subacao2": PerfilDeAcessoPageLocators.NOVO, "validacao": PerfilDeAcessoPageLocators.CADASTRO_PRODUTOS_CURTO_PRAZO_TELA, "mensagem": "Página do Cadastro de produtos Curto Prazo não está acessível."}
            ]

        for acao in acoes:
            try:
                logging.info(f"Clicando no botão: {acao['botao']}")
                self.driver.find_element(*acao["botao"]).click()
                sleep(3)  # Aguarda 3 segundos após clicar no botão
                logging.info("Confirmação: botão clicado com sucesso.")
                
                if "subacao" in acao:
                    logging.info(f"Executando subação: {acao['subacao']}")
                    self.driver.find_element(*acao["subacao"]).click()
                    sleep(3)  # Aguarda 3 segundos após a subação
                    logging.info("Confirmação: subação executada com sucesso.")
                
                if "subacao2" in acao:
                    logging.info(f"Executando subação2: {acao['subacao2']}")
                    self.driver.find_element(*acao["subacao2"]).click()
                    sleep(3)  # Aguarda 3 segundos após a subação2
                    logging.info("Confirmação: subação2 executada com sucesso.")
                
                logging.info(f"Validando elemento: {acao['validacao']}")
                assert self.driver.find_element(*acao["validacao"]).is_displayed(), acao["mensagem"]
                logging.info("Confirmação: validação bem-sucedida.")
                sleep(3)  # Aguarda 3 segundos após a validação
            except Exception as e:
                logging.error(f"Erro ao executar ação: {acao}. Detalhes do erro: {e}")
                raise AssertionError(f"Erro ao validar acesso total ao sistema: {acao['mensagem']}. Detalhes: {e}")

    # def acessar_diretrizes(self):
    #     """Verifica se o usuário tem acesso às diretrizes."""
    #     # Implementação para verificar acesso às diretrizes
    #     pass

    # def acessar_premios_padrao(self):
    #     """Verifica se o usuário tem acesso aos prêmios padrão."""
    #     # Implementação para verificar acesso aos prêmios padrão
    #     pass

    # def editar_dados(self):
    #     """Verifica se o usuário pode editar dados."""
    #     # Implementação para verificar permissão de edição
    #     pass

    # def criar_dados(self):
    #     """Verifica se o usuário pode criar dados."""
    #     # Implementação para verificar permissão de criação
    #     pass

    # def menu_apresenta_opcoes(self, opcoes):
    #     """Verifica se o menu apresenta as opções esperadas."""
    #     # Implementação para verificar opções no menu
    #     pass

    # def nao_visualizar_nada(self):
    #     """Verifica se o usuário não visualiza nada ao acessar sem login."""
    #     # Implementação para verificar visualização vazia
    #     pass

    # def redirecionado_para_login(self):
    #     """Verifica se o usuário é redirecionado para a tela de login."""
    #     # Implementação para verificar redirecionamento
    #     pass

    # def acessar_modulos_produtos(self):
    #     """Verifica se o usuário tem acesso aos módulos de produtos."""
    #     # Implementação para verificar acesso aos módulos de produtos
    #     pass

    # def acessar_premios(self):
    #     """Verifica se o usuário tem acesso aos prêmios."""
    #     # Implementação para verificar acesso aos prêmios
    #     pass

    # def acessar_premio_proposta_diretrizes(self):
    #     """Verifica se o usuário tem acesso ao prêmio de proposta de diretrizes."""
    #     # Implementação para verificar acesso ao prêmio de proposta de diretrizes
    #     pass

    # def visualizar(self):
    #     """Verifica se o usuário pode visualizar informações."""
    #     # Implementação para verificar permissão de visualização
    #     pass

    # def editar(self):
    #     """Verifica se o usuário pode editar informações."""
    #     # Implementação para verificar permissão de edição
    #     pass

    # def excluir(self):
    #     """Verifica se o usuário pode excluir informações."""
    #     # Implementação para verificar permissão de exclusão
    #     pass

    # def excluir_produto(self):
    #     """Verifica se o usuário pode excluir um produto."""
    #     # Implementação para verificar exclusão de um produto
    #     pass

    # def menu_apresenta_todas_opcoes(self):
    #     """Verifica se o menu apresenta todas as opções disponíveis."""
    #     # Implementação para verificar opções completas no menu
    #     pass

    # def menu_apresenta_opcoes_limitadas(self):
    #     """Verifica se o menu apresenta apenas opções limitadas."""
    #     # Implementação para verificar opções limitadas no menu
    #     pass

    # def visualizar_modulo_produtos(self):
    #     """Verifica se o usuário pode visualizar o módulo de produtos."""
    #     # Implementação para verificar visualização do módulo de produtos
    #     pass

