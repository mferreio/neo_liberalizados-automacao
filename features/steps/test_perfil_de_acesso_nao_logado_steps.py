import logging
from time import sleep

from behave import given, then, when
from pages.perfil_de_acesso_nao_logado_pages import PerfilDeAcessoNaoLogadoPage

from features.steps.test_login_steps import step_click_next_button, step_impl


@given("que o usuário não está logado")
def step_usuario_nao_logado(context):
    context.perfil_nao_logado_page = PerfilDeAcessoNaoLogadoPage(context.driver)
    logging.info("Usuário não está logado.")
    sleep(3)


@when("eu tento acessar qualquer recurso da aplicação")
def step_acessar_recurso(context):
    context.perfil_nao_logado_page.acessar_recurso_direto()
    sleep(3)


@when("eu tento acessar a aplicação")
def step_acessar_aplicacao_com_login(context):
    """Executa os passos de login ao tentar acessar a aplicação."""
    step_impl(context)  # @given('que eu acesso a página de login')
    context.perfil_nao_logado_page.clicar_botao_entrar()  # @when('eu clico no botão Entrar')
    step_click_next_button(context)  # @when('eu clico no botão Seguinte')
    sleep(3)


@then("eu devo ser redirecionado para a tela de login")
def step_redirecionado_tela_login(context):
    assert (
        context.perfil_nao_logado_page.validar_redirecionamento_para_login()
    ), "Usuário não foi redirecionado para a tela de login Microsoft (login.microsoftonline.com)."
    sleep(3)


@then("eu não devo visualizar nada")
def step_validar_tela_login(context):
    mensagem = context.perfil_nao_logado_page.validar_e_capturar_mensagem_erro()
    logging.info(f"Mensagem capturada: {mensagem}")
    assert mensagem, "Nenhuma mensagem foi exibida na tela."
    sleep(3)


@when("eu não devo conseguir visualizar informações de qualquer perfil")
def step_validar_mensagem_acesso_negado(context):
    mensagem = context.perfil_nao_logado_page.exibir_mensagem_acesso_negado()
    logging.info(mensagem)
    assert (
        mensagem
        == "Usuário deve realizar login antes de acessar uma funcionalidade do sistema"
    ), "Mensagem de acesso negado não exibida corretamente."
    sleep(3)


@then("o sistema valida e captura a mensagem de erro exibida")
def step_validar_e_capturar_mensagem_erro(context):
    """Valida e captura o texto do elemento de erro."""
    mensagem = context.perfil_nao_logado_page.validar_e_capturar_mensagem_erro()
    logging.info(f"Mensagem capturada: {mensagem}")
    assert mensagem, "Nenhuma mensagem foi exibida na tela."
    sleep(3)
