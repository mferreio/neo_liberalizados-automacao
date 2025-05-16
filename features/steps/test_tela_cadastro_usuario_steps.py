from behave import when, then, given
from features.pages.tela_cadastro_usuario_pages import TelaCadastroUsuarioPage
import os
import time

@when('o usuário preenche o nome e um e-mail inválido')
def step_preencher_nome_email_invalido(context):
    page = TelaCadastroUsuarioPage(context.driver)
    page.preencher_nome_email_admin_email_invalido()

@then('a notificação "E-mail inválido" deve ser exibida')
def step_validar_mensagem_email_invalido(context):
    page = TelaCadastroUsuarioPage(context.driver)
    mensagem = page.validar_mensagem_email_invalido()
    assert mensagem is not None, "Mensagem de formato de e-mail inválido não foi exibida."

@then('a notificação "Usuário já existe" deve ser exibida')
def step_validar_mensagem_usuario_ja_existe(context):
    page = TelaCadastroUsuarioPage(context.driver)
    mensagem = page.validar_mensagem_usuario_ja_existe()
    assert mensagem is not None, "Mensagem de usuário já existe não foi exibida."

@then("a notificação 'Campos obrigatórios não preenchidos' deve ser exibida")
def step_validar_mensagens_campos_obrigatorios(context):
    page = TelaCadastroUsuarioPage(context.driver)
    mensagens = page.validar_mensagens_campos_obrigatorios()
    assert any([
        "Perfil é obrigatório." in msg or
        "Nome é obrigatório." in msg or
        "E-mail é obrigatório." in msg
        for msg in mensagens
    ]), "Nenhuma mensagem de campo obrigatório foi exibida."

@given("que o usuário foi cadastrado no sistema")
def step_usuario_foi_cadastrado(context):
    page = TelaCadastroUsuarioPage(context.driver)
    page.validar_usuario_cadastrado()

@given("que eu estou na Página Inicial")
def step_estar_na_pagina_inicial(context):
    page = TelaCadastroUsuarioPage(context.driver)
    page.validar_pagina_inicial()

@when("eu devo ver um campo para diretrizes diárias")
@then("eu devo ver um campo para diretrizes diárias")
def step_ver_campo_diretrizes_diarias(context):
    page = TelaCadastroUsuarioPage(context.driver)
    page.validar_tabela_diretrizes_diarias()

@when("eu devo ver um campo para diretrizes semanais")
@then("eu devo ver um campo para diretrizes semanais")
def step_ver_campo_diretrizes_semanais(context):
    page = TelaCadastroUsuarioPage(context.driver)
    page.validar_tabela_diretrizes_semanais()

@when("eu devo ver um campo para I-REC")
@then("eu devo ver um campo para I-REC")
def step_ver_campo_diretrizes_irec(context):
    page = TelaCadastroUsuarioPage(context.driver)
    page.validar_tabela_diretrizes_irec()

@when("eu devo ver um campo para diretrizes de curto prazo")
@then("eu devo ver um campo para diretrizes de curto prazo")
def step_ver_campo_diretrizes_curto_prazo(context):
    page = TelaCadastroUsuarioPage(context.driver)
    page.validar_tabela_diretrizes_curto_prazo()

@then("exibe os dados de diretrizes diárias")
def step_exibir_dados_diretrizes_diarias(context):
    page = TelaCadastroUsuarioPage(context.driver)
    page.exibir_dados_diretrizes_diarias()

@then("exibe os dados de diretrizes semanais")
def step_exibir_dados_diretrizes_semanais(context):
    page = TelaCadastroUsuarioPage(context.driver)
    page.exibir_dados_diretrizes_semanais()

@when('eu clico no botão "Ver Histórico" para diretrizes diárias')
def step_clicar_ver_historico_diretriz_diaria(context):
    page = TelaCadastroUsuarioPage(context.driver)
    page.clicar_ver_historico_diretriz_diaria()

@then('eu sou direcionado para a tela de histórico da diretriz diária')
def step_validar_redirecionamento_historico_diaria(context):
    page = TelaCadastroUsuarioPage(context.driver)
    page.validar_redirecionamento_historico_diaria()

@when('eu clico no botão "Ver Histórico" para diretrizes semanais')
def step_clicar_ver_historico_diretriz_semanal(context):
    page = TelaCadastroUsuarioPage(context.driver)
    page.clicar_ver_historico_diretriz_semanal()

@then('eu sou direcionado para a tela de histórico da diretriz semanal')
def step_validar_redirecionamento_historico_semanal(context):
    page = TelaCadastroUsuarioPage(context.driver)
    page.validar_redirecionamento_historico_semanal()

@then('eu sou direcionado para a tela de dados BBCE do histórico dos dados de diretrizes diárias')
def step_validar_redirecionamento_bbce_historico_diaria(context):
    page = TelaCadastroUsuarioPage(context.driver)
    page.validar_redirecionamento_historico_diaria()

@then('eu sou direcionado para a tela de dados BBCE do histórico dos dados de diretrizes semanal')
def step_validar_redirecionamento_bbce_historico_semanal(context):
    page = TelaCadastroUsuarioPage(context.driver)
    page.validar_redirecionamento_historico_semanal()

@then('eu sou direcionado para a tela de dados DCIDE do histórico dos dados de diretrizes diárias')
def step_validar_redirecionamento_dcide_historico_diaria(context):
    page = TelaCadastroUsuarioPage(context.driver)
    page.validar_redirecionamento_historico_diaria()

@then('eu sou direcionado para a tela de dados DCIDE do histórico dos dados de diretrizes semanal')
def step_validar_redirecionamento_dcide_historico_semanal(context):
    page = TelaCadastroUsuarioPage(context.driver)
    page.validar_redirecionamento_historico_semanal()

@when('eu devo poder visualizar dados históricos de maneira gráfica')
def step_validar_graficos_historico_diaria(context):
    page = TelaCadastroUsuarioPage(context.driver)
    page.validar_graficos_historico_diaria()

@when('eu clico no botão "Exportar" da diretriz diária')
def step_clicar_exportar_diretriz_diaria(context):
    page = TelaCadastroUsuarioPage(context.driver)
    page.clicar_exportar_diretriz_diaria()

@when('eu clico no botão "Exportar" da diretriz semanal')
def step_clicar_exportar_diretriz_semanal(context):
    page = TelaCadastroUsuarioPage(context.driver)
    page.clicar_exportar_diretriz_semanal()

@when('eu clico no botão "Exportar" da diretriz I-REC')
def step_clicar_exportar_diretriz_irec(context):
    page = TelaCadastroUsuarioPage(context.driver)
    page.clicar_exportar_diretriz_irec()

@when('eu clico no botão "Exportar" da diretriz curto prazo')
def step_clicar_exportar_diretriz_curto_prazo(context):
    page = TelaCadastroUsuarioPage(context.driver)
    page.clicar_exportar_diretriz_curto_prazo()

@then('os dados apresentados devem ser baixados no formato XLSX')
def step_validar_download_xlsx(context):
    pasta_download = r"C:\\Users\\mferreio\\Downloads"
    timeout = 10  # segundos
    arquivo_baixado = False
    for _ in range(timeout):
        arquivos = os.listdir(pasta_download)
        if any(arquivo.endswith('.xlsx') for arquivo in arquivos):
            arquivo_baixado = True
            break
        time.sleep(1)
    assert arquivo_baixado, "Arquivo XLSX não foi baixado!"

@when('o nome do arquivo deve ter "relatorio_diretriz_diaria"')
def step_validar_nome_arquivo_relatorio_diaria(context):
    pasta_download = r"C:\\Users\\mferreio\\Downloads"
    arquivos = os.listdir(pasta_download)
    assert any("relatorio_diretriz_diaria" in arquivo for arquivo in arquivos), "Nome do arquivo não contém 'relatorio_diretriz_diaria'"

@when('o nome do arquivo deve ter "relatorio_diretriz_semanal"')
def step_validar_nome_arquivo_relatorio_semanal(context):
    pasta_download = r"C:\\Users\\mferreio\\Downloads"
    arquivos = os.listdir(pasta_download)
    assert any("relatorio_diretriz_semanal" in arquivo for arquivo in arquivos), "Nome do arquivo não contém 'relatorio_diretriz_semanal'"

@when('o nome do arquivo deve ter "relatorio_diretriz_irec"')
def step_validar_nome_arquivo_relatorio_irec(context):
    pasta_download = r"C:\\Users\\mferreio\\Downloads"
    arquivos = os.listdir(pasta_download)
    assert any("relatorio_diretriz_irec" in arquivo for arquivo in arquivos), "Nome do arquivo não contém 'relatorio_diretriz_irec'"

@when('o nome do arquivo deve ter "relatorio_diretriz_curto_prazo"')
def step_validar_nome_arquivo_relatorio_curto_prazo(context):
    pasta_download = r"C:\\Users\\mferreio\\Downloads"
    arquivos = os.listdir(pasta_download)
    assert any("relatorio_diretriz_curto_prazo" in arquivo for arquivo in arquivos), "Nome do arquivo não contém 'relatorio_diretriz_curto_prazo'"

@when('eu visualizo a barra de lateral')
def step_visualizar_barra_lateral(context):
    page = TelaCadastroUsuarioPage(context.driver)
    page.acessar_barra_lateral()

@then('eu devo ver os prêmios para "prêmio Sazo" e "prêmio Flex"')
def step_validar_abas_premios(context):
    page = TelaCadastroUsuarioPage(context.driver)
    page.validar_abas_premios()