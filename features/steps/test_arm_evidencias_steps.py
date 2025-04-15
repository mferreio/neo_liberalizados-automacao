from behave import given, when, then
from pages.arm_evidencias_pages import ArmEvidenciasPage
import logging

@given('que o usuário está logado com perfil "Trading"')
def step_usuario_logado_trading(context):
    logging.info("Usuário logado com perfil 'Trading'.")

@when('o usuário faz o upload de um arquivo de evidência "evidencia_imagem.jpg"')
def step_realizar_upload_arquivo(context):
    context.arm_evidencias_page = ArmEvidenciasPage(context.driver)
    context.arm_evidencias_page.realizar_upload_arquivo("caminho/para/evidencia_imagem.jpg")

@then('o sistema deve armazenar o arquivo no bucket do S3')
def step_verificar_upload_sucesso(context):
    context.arm_evidencias_page.verificar_mensagem_sucesso_upload()

@when('deve exibir a mensagem "Arquivo enviado com sucesso"')
def step_verificar_mensagem_sucesso(context):
    context.arm_evidencias_page.verificar_mensagem_sucesso_upload()

@given('que o usuário está logado com perfil "Usuário Comum"')
def step_usuario_logado_usuario_comum(context):
    logging.info("Usuário logado com perfil 'Usuário Comum'.")

@when('o usuário tenta fazer o upload de um arquivo de evidência "evidencia_texto.txt"')
def step_realizar_upload_sem_permissao(context):
    context.arm_evidencias_page.realizar_upload_arquivo("caminho/para/evidencia_texto.txt")

@then('o sistema deve exibir a mensagem "Acesso negado. Você não tem permissão para enviar arquivos."')
def step_verificar_mensagem_acesso_negado(context):
    context.arm_evidencias_page.verificar_mensagem_acesso_negado()

@given('que o usuário está logado com perfil "Administrador"')
def step_usuario_logado_administrador(context):
    logging.info("Usuário logado com perfil 'Administrador'.")

@when('um arquivo de evidência "evidencia_imagem.jpg" foi enviado e está armazenado no S3')
def step_arquivo_enviado(context):
    logging.info("Arquivo 'evidencia_imagem.jpg' foi enviado e está armazenado no S3.")

@when('o usuário solicita o download do arquivo "evidencia_imagem.jpg"')
def step_realizar_download_arquivo(context):
    context.arm_evidencias_page.realizar_download_arquivo("evidencia_imagem.jpg")

@then('o sistema deve buscar o arquivo no bucket do S3')
def step_verificar_download_sucesso(context):
    context.arm_evidencias_page.verificar_mensagem_download_sucesso()

@when('deve retornar o arquivo para o usuário')
def step_verificar_arquivo_retornado(context):
    context.arm_evidencias_page.verificar_mensagem_download_sucesso()

@when('o usuário tenta solicitar o download do arquivo "evidencia_texto.txt"')
def step_realizar_download_sem_permissao(context):
    context.arm_evidencias_page.realizar_download_arquivo("evidencia_texto.txt")

@then('o sistema deve exibir a mensagem "Acesso negado. Você não tem permissão para consultar arquivos."')
def step_verificar_mensagem_acesso_negado_download(context):
    context.arm_evidencias_page.verificar_mensagem_acesso_negado()

@when('o usuário solicita o download do arquivo "arquivo_inexistente.txt"')
def step_realizar_download_arquivo_inexistente(context):
    context.arm_evidencias_page.realizar_download_arquivo("arquivo_inexistente.txt")

@then('o sistema deve exibir a mensagem "Arquivo não encontrado."')
def step_verificar_mensagem_arquivo_nao_encontrado(context):
    context.arm_evidencias_page.verificar_mensagem_arquivo_nao_encontrado()
