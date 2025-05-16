from behave import given, then, when
from pages.perfil_de_acesso_pages import PerfilDeAcessoPage


@when("eu devo ter acesso total ao sistema")
def step_then_acesso_total(context):
    context.perfil_de_acesso_pages.possui_acesso_total()


@then("eu devo conseguir visualizar todas as telas")
def step_then_visualizar_todas_as_telas(context):
    context.perfil_de_acesso_pages.visualizar_todas_as_telas()


@then("eu devo conseguir realizar todas as operações de 'Trading Portifólio'")
def step_then_operacoes_trading_portfolio(context):
    context.perfil_de_acesso_pages.realizar_operacoes_trading_portfolio()


@then("o menu deve apresentar todas as opções disponíveis")
def step_then_menu_apresenta_opcoes(context):
    context.perfil_de_acesso_pages.validar_menu_apresenta_opcoes_administrador()
