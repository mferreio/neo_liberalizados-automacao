from behave import when, then
from features.pages.tela_cadastro_usuario_pages import TelaCadastroUsuarioPage

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