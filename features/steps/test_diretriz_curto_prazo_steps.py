from behave import given, when, then
from features.pages.diretriz_curto_prazo_pages import DiretrizCurtoPrazoPage

@given("retorna para a tela de diretriz Curto Prazo")
@when("retorna para a tela de diretriz Curto Prazo")
def step_retornar_tela_diretriz_curto_prazo(context):
    page = DiretrizCurtoPrazoPage(context.driver)
    page.validar_ou_redirecionar_tela_diretriz_curto_prazo()

@given("que o usuário está na tela de diretriz Curto Prazo")
def step_usuario_na_tela_diretriz_curto_prazo(context):
    page = DiretrizCurtoPrazoPage(context.driver)
    page.validar_ou_redirecionar_tela_diretriz_curto_prazo_curto()

@then("o usuário deve ser direcionado para a tela de cadastro de diretriz Curto Prazo")
def step_usuario_direcionado_tela_cadastro_curto_prazo(context):
    page = DiretrizCurtoPrazoPage(context.driver)
    page.validar_ou_redirecionar_tela_cadastro_diretriz_curto_prazo()
