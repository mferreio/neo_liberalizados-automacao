from behave import When
from pages.arm_evidencias_pages import ArmEvidenciasPage

@When('o usuário acessa a aba "diretriz Curto Prazo"')
def step_acessar_diretriz_curto_prazo(context):
    evidencias_page = ArmEvidenciasPage(context.driver)
    evidencias_page.clicar_diretriz_curto_prazo()

@When('o sistema clica no botão Novo')
def step_clicar_botao_novo(context):
    evidencias_page = ArmEvidenciasPage(context.driver)
    evidencias_page.clicar_botao_novo()

@When('o usuário preenche o campo Data Fim')
def step_preencher_campo_data_fim(context):
    evidencias_page = ArmEvidenciasPage(context.driver)
    evidencias_page.preencher_campo_data_fim(context.config.userdata.get("DATA_FIM_DIRETRIZ"))

@When('o usuário faz o upload de um arquivo de evidência "evidencia_imagem.jpg"')
def step_fazer_upload_evidencia(context, arquivo):
    evidencias_page = ArmEvidenciasPage(context.driver)
    evidencias_page.fazer_upload_evidencia("evidencia_imagem.jpg")