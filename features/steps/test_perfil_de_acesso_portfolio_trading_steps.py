from behave import given, when, then
from pages.perfil_de_acesso_portfolio_trading_pages import PerfilDeAcessoPage
import logging
from time import sleep

@given('que o usuário está logado como "Trading Portifólio"')
def step_usuario_logado_trading_portfolio(context):
    context.perfil_de_acesso_portfolio_trading_pages = PerfilDeAcessoPage(context.driver)
    context.perfil_de_acesso_page = PerfilDeAcessoPage(context.driver)
    context.perfil_de_acesso_page.realizar_login_com_perfil("Trading/Portifólio")
    assert context.perfil_de_acesso_page.validar_texto_perfil("Portfólio e Trading"), \
        "O texto do perfil não corresponde a 'Portfólio e Trading'."
    logging.info("Usuário logado como 'Trading Portifólio'.")
    sleep(2)

@then('eu devo conseguir visualizar o modulo de produtos')
@when('eu devo ter acesso aos módulos de produtos')
def step_verificar_acesso_modulos_produtos(context):
    """Valida se o elemento VALIDAR_MODULOS_PRODUTOS existe na tela."""
    context.perfil_de_acesso_page = PerfilDeAcessoPage(context.driver)
    assert context.perfil_de_acesso_page.validar_modulos_produtos_existe(), \
        "Usuário sem acesso ao modulo Produtos."
    logging.info("Usuário com acesso ao Modulo Produtos.")

@then('eu devo ter acesso aos diretrizes')
def step_verificar_acesso_diretrizes(context):
    """Valida se o usuário tem acesso aos módulos especificados."""
    context.perfil_de_acesso_page = PerfilDeAcessoPage(context.driver)  # Certifique-se de inicializar o atributo correto
    assert context.perfil_de_acesso_page.validar_acesso_diretrizes(), \
        "Usuário não tem acesso aos produtos Semanal/Diário, I-Rec e Curto Prazo."
    logging.info("Usuário com acesso aos produtos Semanal/Diário, I-Rec e Curto Prazo.")
    sleep(2)

@when('eu devo conseguir editar')
def step_editar_modulo_produtos(context):
    context.perfil_de_acesso_page.editar_modulo_produtos()

@when('Usuário acessa o produto Diario Semanal na aba produtos')
@then('eu devo ter acesso aos prêmio de proposta de diretrizes')
def step_verificar_acesso_proposta_diretrizes(context):
    """Clica nos elementos necessários e valida a existência do título 'Gerenciar Produtos Diário/Semanal'."""
    context.perfil_de_acesso_page = PerfilDeAcessoPage(context.driver)
    context.perfil_de_acesso_page.acessar_premio_proposta_diretrizes()
    logging.info("Acesso ao prêmio de proposta de diretrizes validado com sucesso.")

@when('eu devo conseguir excluir um produto')
def step_excluir_produto(context):
    context.perfil_de_acesso_page.excluir_produto()

@when('eu devo conseguir criar dados')
def step_criar_dados(context):
    context.perfil_de_acesso_page.criar_dados()

@then('o menu deve apresentar apenas as opções de produtos, prêmios, e diretrizes')
def step_verificar_opcoes_menu(context):
    context.perfil_de_acesso_page.verificar_opcoes_menu()

@then('os produtos "Diário/Semanal", "I-REC" e "Curto Prazo" devem estar visíveis na tela')
def step_validar_produtos_visiveis(context):
    """Valida que os produtos 'Diário/Semanal', 'I-REC' e 'Curto Prazo' estão visíveis na tela."""
    context.perfil_de_acesso_page = PerfilDeAcessoPage(context.driver)
    assert context.perfil_de_acesso_page.validar_produtos_visiveis(), \
        "Um ou mais produtos não estão visíveis na tela."
    logging.info("Os produtos 'Diário/Semanal', 'I-REC' e 'Curto Prazo' estão visíveis na tela.")

@when('Usuário pesquisa pelo ano')
def step_pesquisar_por_ano(context):
    """Pesquisa pelo ano utilizando o valor de CONS_PROD_ANO."""
    context.perfil_de_acesso_page.pesquisar_por_ano()
    logging.info("Usuário pesquisou pelo ano estipulado.")

@when('Usuário seleciona o produto de acordo com o que for estipulado')
def step_selecionar_produto_estipulado(context):
    """Seleciona o produto de acordo com os valores estipulados no arquivo credentials."""
    context.perfil_de_acesso_page.selecionar_produto_estipulado()
    logging.info("Usuário selecionou o produto de acordo com as especificações.")

@when('Usuário clica no botão editar')
def step_clicar_botao_editar(context):
    """Clica no botão editar."""
    context.perfil_de_acesso_page.clicar_botao_editar()
    logging.info("Usuário clicou no botão editar.")

@then('o sistema exibe a pagina de edição do produto')
def step_validar_pagina_edicao_produto(context):
    """Valida que o usuário está na tela de edição do produto através do título da página."""
    context.perfil_de_acesso_page = PerfilDeAcessoPage(context.driver)
    assert context.perfil_de_acesso_page.validar_pagina_edicao_produto(), \
        "O título da página de edição do produto não foi encontrado."
    logging.info("Usuário está na página de edição do produto.")

@when('Usuário clica no botão excluir')
def step_clicar_botao_excluir(context):
    """Clica no botão excluir."""
    context.perfil_de_acesso_page = PerfilDeAcessoPage(context.driver)
    context.perfil_de_acesso_page.clicar_botao_excluir()
    logging.info("Usuário clicou no botão excluir.")

@then('eu devo acessar a tela para excluir um produto')
def step_validar_tela_exclusao_produto(context):
    """Valida que o sistema exibiu a tela de exclusão do produto."""
    context.perfil_de_acesso_page = PerfilDeAcessoPage(context.driver)
    assert context.perfil_de_acesso_page.validar_tela_exclusao_produto(), \
        "A tela de exclusão do produto não foi exibida."
    logging.info("Tela de exclusão do produto exibida com sucesso.")

@when('Usuário clica em novo produto')
def step_clicar_em_novo_produto(context):
    """Clica no botão 'Novo Produto'."""
    context.perfil_de_acesso_page = PerfilDeAcessoPage(context.driver)
    context.perfil_de_acesso_page.clicar_em_novo_produto()
    logging.info("Usuário clicou no botão 'Novo Produto'.")

@when('Usuário preenche os campos obrigatórios')
def step_preencher_campos_obrigatorios(context):
    """Preenche os campos obrigatórios para criar um novo produto."""
    context.perfil_de_acesso_page = PerfilDeAcessoPage(context.driver)
    context.perfil_de_acesso_page.preencher_campos_obrigatorios()
    logging.info("Usuário preencheu os campos obrigatórios.")

@when('Usuário clica em cadastrar')
def step_clicar_em_cadastrar(context):
    """Clica no botão 'Cadastrar Produto'."""
    context.perfil_de_acesso_page = PerfilDeAcessoPage(context.driver)
    context.perfil_de_acesso_page.clicar_em_cadastrar_produto()
    logging.info("Usuário clicou no botão 'Cadastrar Produto'.")
