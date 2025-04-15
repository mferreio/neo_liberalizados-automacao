from behave import given, when, then
from pages.aplicacao_base_pages import AplicacaoBasePage, AplicacaoBaseLocators
import logging
import time

@given('que o usuário está logado no sistema')
def step_usuario_logado(context):
    context.aplicacao_base_page = AplicacaoBasePage(context.driver)
    context.aplicacao_base_page.validar_pagina_principal()
    logging.info("Usuário está logado no sistema e na página principal.")

@when('o usuário acessa a tela principal da aplicação')
def step_acessa_tela_principal(context):
    context.aplicacao_base_page = AplicacaoBasePage(context.driver)
    logging.info("usuário acessa a tela principal da aplicação.")

@then('ele deve visualizar o menu lateral na posição esquerda da tela')
def step_verificar_menu_lateral(context):
    context.aplicacao_base_page.verificar_menu_lateral()

@when('o módulo "Produtos" está visível no menu lateral')
def step_modulo_registro_itens_visivel(context):
    context.aplicacao_base_page.validar_modulo_visivel()
    logging.info("O módulo 'Produtos' está visível no menu lateral.")

@when('o usuário seleciona o módulo "Produtos"')
def step_selecionar_modulo_registro_itens(context):
    context.aplicacao_base_page.clicar_modulo_produtos()
    logging.info("Usuário selecionou o módulo 'Produtos'.")

@then('o usuário deve ser direcionado para a tela de visualização dos dados do módulo "Produtos Semanal Diario"')
def step_verificar_tela_visualizacao_produtos_semanal_diario(context):
    context.aplicacao_base_page.validar_tela_produtos_semanal_diario()
    logging.info("Usuário foi direcionado para a tela de visualização dos dados do módulo 'Produtos Semanal Diario'.")

@then('ele deve ver uma lista de todos os itens cadastrados')
def step_verificar_lista_itens(context):
    produtos = context.aplicacao_base_page.consultar_lista_produtos()
    logging.info("Lista de produtos cadastrados:")
    for produto in produtos:
        logging.info(f"- {produto}")
    logging.info("Consulta de produtos cadastrados realizada com sucesso.")

@when('ele deve ver um botão "Adicionar Novo Item"')
def step_verificar_botao_adicionar(context):
    context.aplicacao_base_page.clicar_botao_novo_item()
    logging.info('Botão "Adicionar Novo Item" clicado com sucesso.')

@when('o usuário clica em "Adicionar Novo Item"')
def step_clicar_botao_adicionar(context):
    context.aplicacao_base_page.clicar_botao_novo_item()
    logging.info('Usuário clicou no botão "Adicionar Novo Item".')

@then('deve ser direcionado para um formulário para registrar um novo item')
def step_verificar_formulario(context):
    context.aplicacao_base_page.validar_formulario_e_voltar()
    logging.info("Formulário validado e retornado à tela anterior com sucesso.")

@then('ele deve ver apenas o botão "Trading/Portifólio" e deve ver o botão "Adicionar Novo Item"')
def step_verificar_botoes_trading_portfolio(context):
    context.aplicacao_base_page.verificar_botoes_por_permissao("Trading/Portifólio")

@when('o usuário está na tela de visualização do módulo "Produtos"')
def step_usuario_na_tela_visualizacao_registro_itens(context):
    context.aplicacao_base_page.verificar_lista_itens_cadastrados()
    logging.info("Usuário está na tela de visualização do módulo 'Produtos'.")

@given('que o usuário está na tela de visualização do módulo "Produtos"')
def step_usuario_na_tela_visualizacao_registro_itens_given(context):
    context.aplicacao_base_page.verificar_lista_itens_cadastrados()
    logging.info("Usuário está na tela de visualização do módulo 'Produtos'.")

@when('o usuário acessa a tela de visualização do módulo "Produtos"')
def step_usuario_acessa_tela_visualizacao_registro_itens(context):
    context.aplicacao_base_page.verificar_lista_itens_cadastrados()
    logging.info("Usuário acessou a tela de visualização do módulo 'Produtos'.")

@given('que o usuário tem perfil de "Trading/Portifólio"')
def step_usuario_com_perfil_trading_portfolio(context):
    context.aplicacao_base_page.verificar_botao_trading_portfolio()
    logging.info("Usuário tem perfil de 'Trading/Portifólio'.")

@when('o usuário seleciona o módulo "Semanal Diario"')
def step_selecionar_modulo_semanal_diario(context):
    context.aplicacao_base_page.clicar_modulo_semanal_diario()
    logging.info("Usuário selecionou o módulo 'Semanal Diario'.")

@when('o usuário seleciona o módulo "IREC"')
def step_selecionar_modulo_irec(context):
    context.aplicacao_base_page.clicar_modulo_irec()
    logging.info("Usuário selecionou o módulo 'IREC'.")

@then('o usuário deve ser direcionado para a tela de visualização dos dados do módulo "Produtos IREC"')
def step_verificar_tela_visualizacao_produtos_irec(context):
    context.aplicacao_base_page.validar_tela_produtos_irec()
    logging.info("Usuário foi direcionado para a tela de visualização dos dados do módulo 'Produtos IREC'.")

@when('o usuário seleciona o módulo "Curto Prazo"')
def step_selecionar_modulo_curto_prazo(context):
    context.aplicacao_base_page.clicar_modulo_curto_prazo()
    logging.info("Usuário selecionou o módulo 'Curto Prazo'.")

@then('o usuário deve ser direcionado para a tela de visualização dos dados do módulo "Produtos Curto Prazo"')
def step_verificar_tela_visualizacao_produtos_curto_prazo(context):
    context.aplicacao_base_page.validar_tela_produtos_curto_prazo()
    logging.info("Usuário foi direcionado para a tela de visualização dos dados do módulo 'Produtos Curto Prazo'.")

@when('retorna a pagina inicial')
def step_retorna_pagina_inicial(context):
    context.aplicacao_base_page.retornar_pagina_inicial()
    logging.info("Usuário retornou para a página inicial.")
