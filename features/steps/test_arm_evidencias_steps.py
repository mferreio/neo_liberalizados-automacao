import logging
from time import sleep
from behave import given, when, then
from pages.arm_evidencias_pages import ArmEvidenciasPage
from credentials import DATA_FIM_DIRETRIZ

@when('o usuário acessa a aba "diretriz Curto Prazo"')
def step_acessar_diretriz_curto_prazo(context):
    try:
        logging.info('Acessando a aba "diretriz Curto Prazo".')
        evidencias_page = ArmEvidenciasPage(context.driver)
        evidencias_page.clicar_diretriz_curto_prazo()
        sleep(4)
    except Exception as e:
        logging.error(f"Erro ao acessar a aba 'diretriz Curto Prazo': {e}")
        raise

@when('clica no botão Novo')
def step_clicar_botao_novo(context):
    try:
        logging.info('Clicando no botão "Novo".')
        evidencias_page = ArmEvidenciasPage(context.driver)
        evidencias_page.clicar_botao_novo()
        sleep(4)
    except Exception as e:
        logging.error(f"Erro ao clicar no botão 'Novo': {e}")
        raise

@when('o usuário preenche o campo Data Fim')
def step_preencher_campo_data_fim(context):
    try:
        logging.info('Preenchendo o campo "Data Fim" com a data especificada.')
        evidencias_page = ArmEvidenciasPage(context.driver)
        evidencias_page.preencher_campo_data_fim(DATA_FIM_DIRETRIZ)
        sleep(4)
    except Exception as e:
        logging.error(f"Erro ao preencher o campo 'Data Fim': {e}")
        raise

@when('o usuário faz o upload de um arquivo de evidência "evidencia_imagem.jpg"')
def step_fazer_upload_evidencia(context):
    try:
        logging.info('Fazendo upload do arquivo "evidencia_imagem.jpg".')
        evidencias_page = ArmEvidenciasPage(context.driver)
        evidencias_page.fazer_upload_evidencia("evidencia_imagem.jpg")
        sleep(4)
    except Exception as e:
        logging.error(f"Erro ao fazer upload do arquivo 'evidencia_imagem.jpg': {e}")
        raise

@then('o sistema deve validar que o arquivo "evidencia_imagem.jpg" foi anexado')
def step_validar_arquivo_anexado(context):
    try:
        logging.info('Validando se o arquivo "evidencia_imagem.jpg" foi armazenado.')
        evidencias_page = ArmEvidenciasPage(context.driver)
        assert evidencias_page.validar_arquivo_anexado_no_elemento(), "Não foi encontrado nenhum arquivo anexo."
        sleep(4)
    except Exception as e:
        logging.error(f"Erro ao validar o armazenamento do arquivo 'evidencia_imagem.jpg': {e}")
        raise

@then('usuário clica em cadastrar')
def step_clicar_em_cadastrar(context):
    try:
        logging.info('Clicando no botão "Cadastrar".')
        evidencias_page = ArmEvidenciasPage(context.driver)
        evidencias_page.clicar_em_cadastrar()
        sleep(4)
    except Exception as e:
        logging.error(f"Erro ao clicar no botão 'Cadastrar': {e}")
        raise

@when('sistema exibe mensagem de sucesso ou erro')
def step_verificar_mensagem_sistema(context):
    try:
        logging.info('Verificando mensagem de sucesso ou erro exibida pelo sistema.')
        evidencias_page = ArmEvidenciasPage(context.driver)
        mensagem = evidencias_page.verificar_mensagem_sistema()
        logging.info(f"Mensagem exibida: {mensagem}")
        assert mensagem in [
            "Fim da vigência é obrigatório",
            "Não é possível cadastrar a diretriz com o fim da vigência no mesmo dia após as 14:00",
            "Diretriz cadastrada com sucesso"
        ], f"Mensagem inesperada: {mensagem}"
    except Exception as e:
        logging.error(f"Erro ao verificar a mensagem do sistema: {e}")
        raise

@when('o usuário preenche os campos obrigatórios')
def step_preencher_campos_obrigatorios(context):
    try:
        logging.info('Preenchendo os campos obrigatórios.')
        evidencias_page = ArmEvidenciasPage(context.driver)
        evidencias_page.preencher_campo_descricao("teste")
        evidencias_page.preencher_campo_premio("10")
        sleep(4)
    except Exception as e:
        logging.error(f"Erro ao preencher os campos obrigatórios: {e}")
        raise

@when('usuário retorna a tela inicial')
def step_retorna_tela_inicial(context):
    """Retorna para a página inicial."""
    try:
        logging.info('Retornando para a página inicial.')
        evidencias_page = ArmEvidenciasPage(context.driver)
        evidencias_page.retorna_tela_inicial()
        sleep(4)
    except Exception as e:
        logging.error(f"Erro ao retornar para a página inicial: {e}")
        raise