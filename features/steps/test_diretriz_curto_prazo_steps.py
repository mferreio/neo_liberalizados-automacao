from behave import given, when, then
from features.pages.diretriz_curto_prazo_pages import DiretrizCurtoPrazoPage

@given("retorna para a tela de diretriz Curto Prazo")
@when("retorna para a tela de diretriz Curto Prazo")
def step_retornar_tela_diretriz_curto_prazo(context):
    page = DiretrizCurtoPrazoPage(context.driver)
    page.validar_ou_redirecionar_tela_diretriz_curto_prazo()

@given("que o usuário está na tela de diretriz Curto Prazo")
def step_usuario_na_tela_diretriz_curto_prazo(context):
    page = DiretrizCurtoPrazoPage(context.driver)
    page.validar_ou_redirecionar_tela_diretriz_curto_prazo_curto()

@then("o usuário deve ser direcionado para a tela de cadastro de diretriz Curto Prazo")
def step_usuario_direcionado_tela_cadastro_curto_prazo(context):
    page = DiretrizCurtoPrazoPage(context.driver)
    page.validar_ou_redirecionar_tela_cadastro_diretriz_curto_prazo()

@when("o usuário preenche os campos obrigatórios com data inválida")
def step_preencher_campos_obrigatorios_data_invalida(context):
    page = DiretrizCurtoPrazoPage(context.driver)
    page.preencher_campos_obrigatorios_com_data_invalida()

@then("uma mensagem de erro é exibida")
def step_validar_mensagem_erro_data_invalida(context):
    page = DiretrizCurtoPrazoPage(context.driver)
    mensagem = page.validar_mensagem_erro_data_invalida()
    assert mensagem is not None, "Mensagem de erro de data inválida não foi exibida."

@when("o usuário insere um intervalo de data para busca")
def step_inserir_intervalo_data_para_busca(context):
    page = DiretrizCurtoPrazoPage(context.driver)
    page.inserir_intervalo_data_para_busca()

@then("apenas as diretrizes que estão dentro do intervalo de data devem ser exibidas")
def step_validar_diretrizes_no_intervalo(context):
    page = DiretrizCurtoPrazoPage(context.driver)
    page.validar_diretrizes_exibidas_no_intervalo()

@when("o usuário clica no botão para ver mais detalhes de uma diretriz")
def step_clicar_botao_detalhamento_diretriz(context):
    page = DiretrizCurtoPrazoPage(context.driver)
    page.clicar_botao_detalhamento_diretriz()

@then("todos os dados da diretriz escolhida devem ser exibidos")
def step_exibir_detalhes_diretriz(context):
    page = DiretrizCurtoPrazoPage(context.driver)
    page.exibir_detalhes_diretriz()

@when("os arquivos anexados também devem ser acessíveis")
def step_exibir_arquivos_anexados(context):
    page = DiretrizCurtoPrazoPage(context.driver)
    page.exibir_arquivos_anexados()
