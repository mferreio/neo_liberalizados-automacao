from behave import given, then, when
from pages.arm_evidencias_pages import ArmEvidenciasPage

from credentials import DATA_FIM_DIRETRIZ

@when("o sistema exibe uma mensagem de upload concluido com sucesso")
def step_verifica_mensagem_upload_sucesso(context):
    evidencias_page = ArmEvidenciasPage(context.driver)
    assert evidencias_page.validar_mensagem_upload_sucesso(), "Mensagem de upload concluído com sucesso NÃO foi exibida."

# Step para validar ausência de arquivo anexo
@then('o sistema deve validar que não existe nenhum arquivo anexado')
def step_validar_ausencia_arquivo_anexado(context):
    evidencias_page = ArmEvidenciasPage(context.driver)
    assert evidencias_page.validar_ausencia_arquivo_anexado(), "Foi encontrado um arquivo anexo, mas não deveria haver nenhum."
from time import sleep


@when('o usuário acessa a aba "diretriz Curto Prazo"')
@then('usuário é encaminhado para a tela de diretriz curto prazo')
def step_acessar_diretriz_curto_prazo(context):
    try:
        evidencias_page = ArmEvidenciasPage(context.driver)
        evidencias_page.clicar_diretriz_curto_prazo()
        sleep(4)
    except Exception as e:
        print(f"Erro ao acessar a aba 'diretriz Curto Prazo': {e}")
        raise


@when("clica no botão Novo")
def step_clicar_botao_novo(context):
    try:
        evidencias_page = ArmEvidenciasPage(context.driver)
        evidencias_page.clicar_botao_novo()
        sleep(4)
    except Exception as e:
        print(f"Erro ao clicar no botão 'Novo': {e}")
        raise


@when("o usuário preenche o campo Data Fim")
def step_preencher_campo_data_fim(context):
    try:
        evidencias_page = ArmEvidenciasPage(context.driver)
        evidencias_page.preencher_campo_data_fim(DATA_FIM_DIRETRIZ)
        sleep(4)
    except Exception as e:
        print(f"Erro ao preencher o campo 'Data Fim': {e}")
        raise


@when('o usuário faz o upload de um arquivo de evidência "evidencia_imagem.jpg"')
def step_fazer_upload_evidencia(context):
    try:
        evidencias_page = ArmEvidenciasPage(context.driver)
        evidencias_page.fazer_upload_evidencia("evidencia_imagem.jpg")
        sleep(4)
    except Exception as e:
        print(f"Erro ao fazer upload do arquivo 'evidencia_imagem.jpg': {e}")
        raise


@when('o usuário faz o upload de um arquivo de evidência "limitedetamanho.pdf"')
def step_fazer_upload_limitedetamanho(context):
    try:
        evidencias_page = ArmEvidenciasPage(context.driver)
        evidencias_page.fazer_upload_limitedetamanho()
        sleep(4)
    except Exception as e:
        print(f"Erro ao fazer upload do arquivo 'limitedetamanho.pdf': {e}")
        raise


@when('o sistema deve validar que o arquivo "evidencia_imagem.jpg" foi anexado')
@then('o sistema deve validar que o arquivo "evidencia_imagem.jpg" foi anexado')
def step_validar_arquivo_anexado(context):
    try:
        evidencias_page = ArmEvidenciasPage(context.driver)
        assert (
            evidencias_page.validar_arquivo_anexado_no_elemento()
        ), "Não foi encontrado nenhum arquivo anexo."
        sleep(4)
    except Exception as e:
        print(f"Erro ao validar o armazenamento do arquivo 'evidencia_imagem.jpg': {e}")
        raise


@then('o sistema deve exibir uma mensagem de limite de tamanho')
def step_validar_mensagem_limite_tamanho(context):
    evidencias_page = ArmEvidenciasPage(context.driver)
    mensagem = evidencias_page.validar_mensagem_limite_tamanho_arquivo()
    assert mensagem is not None and "Tamanho de arquivo inválido" in mensagem, "Mensagem de limite de tamanho não foi exibida corretamente."


@when("usuário clica em salvar")
@then("usuário clica em salvar")
def step_clicar_em_salvar(context):
    evidencias_page = ArmEvidenciasPage(context.driver)
    evidencias_page.clicar_em_salvar()


@when("o usuário preenche os campos obrigatórios")
def step_preencher_campos_obrigatorios(context):
    try:
        evidencias_page = ArmEvidenciasPage(context.driver)
        import os
        from dotenv import load_dotenv
        load_dotenv()
        descricao = os.getenv("DESCRICAO")
        evidencias_page.preencher_campo_premio("10")
        evidencias_page.preencher_campo_descricao(descricao)
        sleep(4)
    except Exception as e:
        print(f"Erro ao preencher os campos obrigatórios: {e}")
        raise



@when("usuário retorna a tela inicial")
def step_retorna_tela_inicial(context):
    """Retorna para a página inicial, se necessário."""
    try:
        evidencias_page = ArmEvidenciasPage(context.driver)
        evidencias_page.retorna_tela_inicial()
        sleep(4)
    except Exception as e:
        print(f"Erro ao retornar para a página inicial: {e}")
        raise

