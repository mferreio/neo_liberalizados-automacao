import logging
import time

from behave import given, then, when
from pages.aplicacao_base_pages import AplicacaoBaseLocators, AplicacaoBasePage


@given("que o usuário está logado no sistema")
def step_usuario_logado(context):
    context.aplicacao_base_page = AplicacaoBasePage(context.driver)
    context.aplicacao_base_page.validar_pagina_principal()


@when("o usuário acessa a tela principal da aplicação")
def step_acessa_tela_principal(context):
    context.aplicacao_base_page = AplicacaoBasePage(context.driver)
    logging.info("usuário acessa a tela principal da aplicação.")


@then("ele deve visualizar o menu lateral na posição esquerda da tela")
def step_verificar_menu_lateral(context):
    context.aplicacao_base_page.verificar_menu_lateral()


@when('o módulo "Produtos" está visível no menu lateral')
def step_modulo_registro_itens_visivel(context):
    context.aplicacao_base_page.validar_modulo_visivel()


@when('o usuário seleciona o módulo "Produtos"')
def step_selecionar_modulo_registro_itens(context):
    context.aplicacao_base_page.clicar_modulo_produtos()


@then(
    'o usuário deve ser direcionado para a tela de visualização dos dados do módulo "Produtos Semanal Diario"'
)
def step_verificar_tela_visualizacao_produtos_semanal_diario(context):
    context.aplicacao_base_page.validar_tela_produtos_semanal_diario()


@then("ele deve ver uma lista de todos os itens cadastrados")
def step_verificar_lista_itens(context):
    produtos = context.aplicacao_base_page.consultar_lista_produtos()
    logging.info("Lista de produtos cadastrados:")
    for produto in produtos:
        logging.info(f"- {produto}")
    logging.info("Consulta de produtos cadastrados realizada com sucesso.")


@when('o usuário clica em "Adicionar Novo Item"')
def step_clicar_botao_adicionar(context):
    context.aplicacao_base_page.clicar_botao_novo_item()


@then("deve ser direcionado para um formulário para registrar um novo item")
def step_verificar_formulario(context):
    context.aplicacao_base_page.validar_formulario_e_voltar()


@then(
    'ele deve ver apenas o botão "Trading/Portifólio" e deve ver o botão "Adicionar Novo Item"'
)
def step_verificar_botoes_trading_portfolio(context):
    context.aplicacao_base_page.verificar_botoes_por_permissao("Trading/Portifólio")


@when('o usuário está na tela de visualização do módulo "Produtos"')
def step_usuario_na_tela_visualizacao_registro_itens(context):
    context.aplicacao_base_page.verificar_lista_itens_cadastrados()


@given('que o usuário está na tela de visualização do módulo "Produtos"')
def step_usuario_na_tela_visualizacao_registro_itens_given(context):
    context.aplicacao_base_page.verificar_lista_itens_cadastrados()


@when('o usuário acessa a tela de visualização do módulo "Produtos"')
def step_usuario_acessa_tela_visualizacao_registro_itens(context):
    context.aplicacao_base_page.verificar_lista_itens_cadastrados()


@given('que o usuário tem perfil de "Trading/Portifólio"')
def step_usuario_com_perfil_trading_portfolio(context):
    context.aplicacao_base_page.verificar_botao_trading_portfolio()


@when('o usuário seleciona o módulo "Semanal Diario"')
def step_selecionar_modulo_semanal_diario(context):
    context.aplicacao_base_page.clicar_modulo_semanal_diario()


@when('o usuário seleciona o módulo "IREC"')
def step_selecionar_modulo_irec(context):
    context.aplicacao_base_page.clicar_modulo_irec()


@then(
    'o usuário deve ser direcionado para a tela de visualização dos dados do módulo "Produtos IREC"'
)
def step_verificar_tela_visualizacao_produtos_irec(context):
    context.aplicacao_base_page.validar_tela_produtos_irec()


@when('o usuário seleciona o módulo "Curto Prazo"')
def step_selecionar_modulo_curto_prazo(context):
    context.aplicacao_base_page.clicar_modulo_curto_prazo()


@then(
    'o usuário deve ser direcionado para a tela de visualização dos dados do módulo "Produtos Curto Prazo"'
)
def step_verificar_tela_visualizacao_produtos_curto_prazo(context):
    context.aplicacao_base_page.validar_tela_produtos_curto_prazo()


@when("retorna a pagina inicial")
def step_retorna_pagina_inicial(context):
    context.aplicacao_base_page.retornar_pagina_inicial()
