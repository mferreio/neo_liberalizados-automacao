from behave import given, when, then
from features.pages.perfil_de_acesso_pages import PerfilDeAcessoPage

@given('que eu sou um usuário com perfil {perfil}')
def step_given_usuario_com_perfil(context, perfil):
    context.perfil_page = PerfilDeAcessoPage(context.driver)
    context.perfil_page.set_user_profile(perfil)

@when('eu faço login na aplicação')
def step_when_faco_login(context):
    context.perfil_page.login()

@then('eu devo ter acesso total ao sistema')
def step_then_acesso_total(context):
    assert context.perfil_page.has_full_access(), "Usuário não tem acesso total ao sistema."

@then('eu devo conseguir {acao}')
def step_then_conseguir_acao(context, acao):
    assert context.perfil_page.can_perform_action(acao), f"Usuário não conseguiu realizar a ação: {acao}"

@then('o menu deve apresentar {opcoes}')
def step_then_menu_apresenta(context, opcoes):
    assert context.perfil_page.menu_has_options(opcoes), f"O menu não apresenta as opções esperadas: {opcoes}"

@then('eu não devo visualizar nada')
def step_then_nao_visualizar_nada(context):
    assert context.perfil_page.is_empty_view(), "Usuário conseguiu visualizar algo, mas não deveria."

@then('eu devo ser redirecionado para a tela de login')
def step_then_redirecionado_login(context):
    assert context.perfil_page.is_redirected_to_login(), "Usuário não foi redirecionado para a tela de login."
