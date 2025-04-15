from behave import given, when, then
from pages.perfil_de_acesso_portfolio_trading_pages import PerfilDeAcessoPage
import logging

@given('que o usuário está logado como "Trading Portifólio"')
def step_usuario_logado_trading_portfolio(context):
    context.perfil_de_acesso_page = PerfilDeAcessoPage(context.driver)
    context.perfil_de_acesso_page.realizar_login_com_perfil("Trading/Portifólio")
    logging.info("Usuário logado como 'Trading Portifólio'.")

@then('eu devo ter acesso aos módulos de produtos')
def step_verificar_acesso_modulos_produtos(context):
    context.perfil_de_acesso_page.verificar_acesso_modulos_produtos()

@when('eu devo ter acesso aos diretrizes')
def step_verificar_acesso_diretrizes(context):
    context.perfil_de_acesso_page.verificar_acesso_modulo_especifico("Diretrizes")

@when('eu devo ter acesso aos prêmio de proposta de diretrizes')
def step_verificar_acesso_proposta_diretrizes(context):
    context.perfil_de_acesso_page.verificar_acesso_modulo_especifico("Prêmio de Proposta de Diretrizes")

@when('eu devo ter acesso aos prêmios padrão')
def step_verificar_acesso_premios_padrao(context):
    context.perfil_de_acesso_page.verificar_acesso_modulo_especifico("Prêmios Padrão")

@when('eu devo conseguir visualizar o modulo de produtos')
def step_visualizar_modulo_produtos(context):
    context.perfil_de_acesso_page.visualizar_modulo_produtos()

@when('eu devo conseguir editar')
def step_editar_modulo_produtos(context):
    context.perfil_de_acesso_page.editar_modulo_produtos()

@when('eu devo conseguir excluir um produto')
def step_excluir_produto(context):
    context.perfil_de_acesso_page.excluir_produto()

@when('eu devo conseguir criar dados')
def step_criar_dados(context):
    context.perfil_de_acesso_page.criar_dados()

@when('eu devo ter acesso aos prêmios')
def step_verificar_acesso_premios(context):
    context.perfil_de_acesso_page.verificar_acesso_modulo_especifico("Prêmios")

@then('o menu deve apresentar apenas as opções de produtos, prêmios, e diretrizes')
def step_verificar_opcoes_menu(context):
    context.perfil_de_acesso_page.verificar_opcoes_menu()
