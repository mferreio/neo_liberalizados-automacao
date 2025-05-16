from behave import given, when, then
from pages.diretriz_irec_pages import DiretrizIrecPage
from credentials import DATA_FIM_DIRETRIZ_IREC, VALOR_CAMPO_TABELA, DESCRICAO_DIRETRIZ_IREC

@given("que o usuário está na tela de diretriz I-REC")
@when("retorna para a tela de diretriz I-REC")
def step_retornar_tela_listar(context):
    context.diretriz_irec_page = DiretrizIrecPage(context.driver)
    context.diretriz_irec_page.validar_redirecionamento_listar()

@when("o usuário acessa ao módulo de diretrizes I-REC")
def step_acessar_aba_diretriz_irec(context):
    context.diretriz_irec_page = DiretrizIrecPage(context.driver)
    context.diretriz_irec_page.acessar_aba_diretriz_irec()

@when('o usuário clica no botão "Nova Diretriz"')
def step_clicar_nova_diretriz(context):
    context.diretriz_irec_page.clicar_nova_diretriz()

@when("que o usuário está na tela de cadastro de nova diretriz I-REC")
@then("o usuário deve ser direcionado para a tela de cadastro de diretriz I-REC")
def step_validar_tela_cadastro_nova_diretriz(context):
    context.diretriz_irec_page.validar_tela_cadastro_nova_diretriz()

@when("o usuário informa os dados da nova diretriz I-REC")
def step_preencher_dados_nova_diretriz(context):
    context.diretriz_irec_page.preencher_dados_nova_diretriz(
        data_fim=DATA_FIM_DIRETRIZ_IREC,
        valor_tabela=VALOR_CAMPO_TABELA,
        descricao=DESCRICAO_DIRETRIZ_IREC
    )

@when('clica no botão Salvar')
@then('clica no botão Salvar')
def step_clicar_botao_salvar(context):
    context.diretriz_irec_page.clicar_botao_salvar()

@when("o sistema exibe uma mensagem de sucesso")
@then("o sistema exibe uma mensagem de sucesso")
def step_validar_mensagem_cadastro(context):
    context.diretriz_irec_page.validar_mensagem_cadastro()

@when("não há diretrizes cadastradas no sistema")
def step_nao_ha_diretrizes(context):
    context.diretriz_irec_page = DiretrizIrecPage(context.driver)
    context.nenhuma_diretriz = context.diretriz_irec_page.consultar_e_verificar_ausencia_diretrizes()

@then('uma mensagem "Nenhuma diretriz cadastrada" deve ser exibida')
def step_mensagem_ausencia_diretrizes(context):
    context.diretriz_irec_page.exibir_mensagem_ausencia_diretrizes(context.nenhuma_diretriz)

@when("há mais de uma página de diretrizes")
def step_ha_mais_de_uma_pagina(context):
    context.diretriz_irec_page = DiretrizIrecPage(context.driver)
    context.pode_avancar_pagina = context.diretriz_irec_page.validar_mais_de_uma_pagina()

@when("o usuário navega para a próxima página")
def step_navega_proxima_pagina(context):
    context.diretriz_irec_page.avancar_para_proxima_pagina(getattr(context, 'pode_avancar_pagina', False))

@then("as diretrizes da próxima página devem ser exibidas")
def step_exibir_diretrizes_proxima_pagina(context):
    context.diretriz_irec_page.exibir_diretrizes_proxima_pagina(getattr(context, 'pode_avancar_pagina', False))

@when("o usuário deve ser capaz de retornar à página anterior")
def step_retornar_pagina_anterior(context):
    context.diretriz_irec_page.retornar_pagina_anterior(getattr(context, 'pode_avancar_pagina', False))

@when("o usuário insere um intervalo de data inválido")
def step_inserir_intervalo_data_invalido(context):
    context.diretriz_irec_page = DiretrizIrecPage(context.driver)
    context.diretriz_irec_page.inserir_intervalo_data_invalido()

@then("sistema exibe mensagem de erro")
def step_exibir_mensagem_erro_data_invalida(context):
    context.diretriz_irec_page.exibir_mensagem_erro_data_invalida()

@when("o usuário abre o detalhamento de uma diretriz")
def step_abrir_detalhamento_diretriz(context):
    context.diretriz_irec_page = DiretrizIrecPage(context.driver)
    context.diretriz_irec_page.abrir_detalhamento_diretriz()

@then("o usuário valida que existem arquivos anexados")
def step_validar_arquivos_anexados(context):
    context.diretriz_irec_page.validar_arquivos_anexados()

@when("o usuário não preenche os campos obrigatórios")
def step_nao_preenche_campos_obrigatorios(context):
    context.diretriz_irec_page.exibir_mensagem_campos_obrigatorios_nao_preenchidos()

@then("uma mensagem de erro deve ser exibida informando os campos que precisam ser preenchidos")
def step_validar_mensagem_erro_campos_obrigatorios(context):
    context.diretriz_irec_page.validar_mensagem_erro_campos_obrigatorios()

@when("o usuário não preenche os campos de preço obrigatório")
def step_nao_preenche_campos_preco_obrigatorio(context):
    from credentials import DATA_FIM_DIRETRIZ_IREC, DESCRICAO_DIRETRIZ_IREC
    context.diretriz_irec_page.preencher_apenas_campos_obrigatorios_sem_preco(DATA_FIM_DIRETRIZ_IREC, DESCRICAO_DIRETRIZ_IREC)

# @when('o usuário faz o upload de um arquivo de evidência "{nome_arquivo}"')
# def step_upload_evidencia(context, nome_arquivo):
#     context.diretriz_irec_page.fazer_upload_evidencia(nome_arquivo)

@when("existe uma diretriz I-REC vigente no sistema")
def step_existe_diretriz_vigente(context):
    context.diretriz_irec_page = DiretrizIrecPage(context.driver)
    context.diretriz_irec_page.exibir_info_diretrizes_vigentes()

@then("a nova diretriz deve invalidar a anterior")
def step_invalidar_anterior(context):
    context.diretriz_irec_page.validar_invalida_anterior()

@when("o sistema deve garantir que apenas uma diretriz esteja vigente")
def step_garantir_uma_vigente(context):
    context.diretriz_irec_page.garantir_apenas_uma_vigente()

@given("que uma diretriz I-REC foi invalidada")
@given("que uma diretriz Curto Prazo foi invalidada")
@when("o usuário consulta as diretrizes cadastradas")
def step_consulta_diretrizes(context):
    context.diretriz_irec_page = DiretrizIrecPage(context.driver)
    context.diretriz_irec_page.consultar_todas_diretrizes()

@then("a diretriz invalidada deve estar disponível na base de dados para histórico")
def step_diretriz_invalida_historico(context):
    context.diretriz_irec_page.exibir_diretrizes_invalidas_para_historico()

@when("a informação sobre sua vigência deve estar acessível")
def step_info_vigencia_acessivel(context):
    context.diretriz_irec_page.exibir_fim_prematuro_vigencia_todas()

@then("todas as diretrizes cadastradas devem ser exibidas")
def step_exibir_todas_diretrizes(context):
    context.diretriz_irec_page = DiretrizIrecPage(context.driver)
    context.diretriz_irec_page.exibir_todas_diretrizes()

@when("a diretriz vigente deve ser claramente identificável")
def step_identificar_diretriz_vigente_visual(context):
    context.diretriz_irec_page = DiretrizIrecPage(context.driver)
    context.diretriz_irec_page.identificar_diretriz_vigente_visual()

@then("sistema exibe a data de inicio e fim de vigência")
def step_exibir_datas_inicio_fim_vigencia(context):
    context.diretriz_irec_page = DiretrizIrecPage(context.driver)
    context.diretriz_irec_page.exibir_datas_inicio_fim_vigencia()

@when("as datas devem estar formatadas corretamente")
def step_validar_formato_datas_vigencia(context):
    context.diretriz_irec_page = DiretrizIrecPage(context.driver)
    context.diretriz_irec_page.validar_formato_datas_vigencia()

# @then('o sistema deve validar que o arquivo "evidencia_imagem.jpg" foi anexado')
# def step_validar_upload_imagem(context):
#     context.diretriz_irec_page.validar_arquivos_anexados()

@then("todos os produtos cadastrados devem estar visíveis")
def step_todos_produtos_visiveis(context):
    context.diretriz_irec_page.exibir_produtos_visiveis()

@then("valida se a data de inicio da vigência é igual a data atual")
def step_validar_data_inicio_vigencia_atual(context):
    context.diretriz_irec_page.validar_data_inicio_vigencia_atual()

@then('deve exibir a mensagem "Arquivo enviado com sucesso"')
@when('deve exibir a mensagem "Arquivo enviado com sucesso"')
def step_validar_mensagem_sucesso_upload(context):
    context.diretriz_irec_page.validar_mensagem_sucesso_upload()

@when("o usuário faz upload acima de 10 arquivos de evidência")
def step_upload_mais_de_10_evidencias(context):
    context.diretriz_irec_page.fazer_upload_mais_de_10_evidencias()

@then("o sistema deve validar que o limite de anexos foi atingido")
def step_validar_limite_de_evidencia(context):
    mensagem = context.diretriz_irec_page.validar_mensagem_limite_de_evidencia()
    assert mensagem is not None, "Mensagem de limite de anexos não foi exibida."

@given('que o usuário cadastrou uma nova diretriz I-Rec')
def step_validar_cadastro_nova_diretriz(context):
    context.diretriz_irec_page.validar_cadastro_nova_diretriz()

@then('todos os campos da tela de cadastro de diretriz I-REC estar vazios')
def step_validar_campos_cadastro_vazios(context):
    context.diretriz_irec_page.validar_campos_cadastro_vazios()
