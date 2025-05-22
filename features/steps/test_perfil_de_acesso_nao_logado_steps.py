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
    """Tenta acessar a aplicação e garante que o botão 'Entrar' NÃO está disponível."""
    from selenium.common.exceptions import TimeoutException
    try:
        context.perfil_nao_logado_page.clicar_botao_entrar()
        logging.error("Botão 'Entrar' foi encontrado e clicado, mas não deveria estar disponível!")
        context.passo_acesso_aplicacao_ok = False
        assert False, "Botão 'Entrar' foi encontrado e clicado, mas não deveria estar disponível!"
    except TimeoutException:
        logging.info("Botão 'Entrar' não foi encontrado, comportamento esperado para usuário não logado.")
        context.passo_acesso_aplicacao_ok = True
    sleep(3)


@then("eu devo ser redirecionado para a tela de login")
def step_redirecionado_tela_login(context):
    assert (
        context.perfil_nao_logado_page.validar_redirecionamento_para_login()
    ), "Usuário não foi redirecionado para a tela de login Microsoft (login.microsoftonline.com)."
    sleep(3)


@then("eu não devo visualizar nada")
def step_validar_tela_login(context):
    # Verifica se o passo anterior foi executado com sucesso
    if hasattr(context, 'passo_acesso_aplicacao_ok') and context.passo_acesso_aplicacao_ok:
        print("Usuário não consegue acessar o sistema sem fazer login.")
        logging.info("Usuário não consegue acessar o sistema sem fazer login.")
    else:
        print("Verifique o passo 'When eu tento acessar a aplicação'.")
        logging.warning("Verifique o passo 'When eu tento acessar a aplicação'.")
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
