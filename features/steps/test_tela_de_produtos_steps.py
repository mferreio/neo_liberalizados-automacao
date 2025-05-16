import logging

from behave import given, then, when
from pages.tela_deprodutos_pages import TelaDeProdutosPage


@when("o usuário é direcionado para a tela de cadastros")
def step_validar_tela_cadastro(context):
    """Valida se o usuário está na tela de cadastro de produtos."""
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    if context.tela_de_produtos_page.validar_tela_cadastro():
        logging.info("Tela de cadastro de produtos validada com sucesso.")
        print("Tela de cadastro de produtos validada com sucesso")
    else:
        logging.error("Não foi possivel validar tela de cadastro de produtos.")
        print("Não foi possivel validar tela de cadastro de produtos")


@when('eu escolho o perfil convencional')
def step_escolher_perfil(context, perfil):
    """Abre o dropdown de perfil e seleciona o perfil especificado."""
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    context.tela_de_produtos_page.escolher_perfil()
    logging.info(f"Perfil '{perfil}' selecionado com sucesso.")


# @when("eu escolho o perfil")
# def step_escolher_perfil_de_energia(context):
#     context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
#     context.tela_de_produtos_page.escolher_perfil_de_energia()


@when('eu escolho o perfil "XXX"')
def step_escolher_perfil_invalido(context):
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    context.tela_de_produtos_page.escolher_perfil_invalido()


@then("as opções disponíveis de perfil devem incluir: CONV, I50, I0, I100 e CQI5")
def step_verificar_opcoes_disponiveis(context):
    """Verifica se as opções disponíveis no dropdown de perfil incluem as esperadas."""
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    opcoes_disponiveis = (
        context.tela_de_produtos_page.obter_opcoes_disponiveis_no_dropdown()
    )

    # Opções esperadas
    opcoes_esperadas = ["CONV", "I50", "I0", "I100", "CQI5"]

    # Verifica se todas as opções esperadas estão presentes
    for opcao in opcoes_esperadas:
        assert (
            opcao in opcoes_disponiveis
        ), f"A opção '{opcao}' não está disponível no dropdown."

    logging.info("Todas as opções esperadas estão disponíveis no dropdown de perfil.")


@when('eu escolho o submercado "{submercado}"')
def step_escolher_submercado(context, submercado):
    """Abre o dropdown de submercado e seleciona o submercado especificado."""
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    context.tela_de_produtos_page.escolher_submercado()
    logging.info(f"Submercado '{submercado}' selecionado com sucesso.")


@when("eu escolho o submercado")
def step_escolher_submercado_dropdown(context):
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    context.tela_de_produtos_page.escolher_submercado_dropdown()


@when("eu escolho o submercado inválido")
def step_escolher_submercado_invalido(context):
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    context.tela_de_produtos_page.escolher_submercado_invalido()


@then("as opções disponíveis de submercado devem incluir: SE, NE, S e N")
def step_verificar_opcoes_disponiveis_submercado(context):
    """Verifica se as opções disponíveis no dropdown de submercado incluem as esperadas."""
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    opcoes_disponiveis = (
        context.tela_de_produtos_page.obter_opcoes_disponiveis_submercado()
    )

    # Opções esperadas
    opcoes_esperadas = ["SE", "NE", "S", "N"]

    # Verifica se todas as opções esperadas estão presentes
    for opcao in opcoes_esperadas:
        assert (
            opcao in opcoes_disponiveis
        ), f"A opção '{opcao}' não está disponível no dropdown."

    logging.info(
        "Todas as opções esperadas estão disponíveis no dropdown de submercado."
    )


@then("exibe os produtos com perfil, submercado e tipo de diretriz")
def step_exibir_produtos(context):
    """Coleta e exibe os dados dos produtos listados na tabela."""
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    produtos = context.tela_de_produtos_page.obter_dados_produtos()

    for produto in produtos:
        logging.info(
            f"Mês: {produto['mes']}, Ano: {produto['ano']}, Perfil: {produto['perfil']}, Submercado: {produto['submercado']}, Tipo de Produto: {produto['tipo']}"
        )

    # Exibe os produtos no console
    for produto in produtos:
        print(
            f"Mês: {produto['mes']}, Ano: {produto['ano']}, Perfil: {produto['perfil']}, Submercado: {produto['submercado']}, Tipo de Produto: {produto['tipo']}"
        )


@given("exibe os produtos com perfil, submercado e tipo de diretriz atualizados")
@when("exibe os produtos com perfil, submercado e tipo de diretriz atualizados")
@then("exibe os produtos com perfil, submercado e tipo de diretriz atualizados")
def step_exibir_produtos_atualizados(context):
    """Compara e exibe apenas os novos produtos cadastrados."""
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    novos_produtos = context.tela_de_produtos_page.obter_novos_produtos(
        context.produtos_anteriores
    )

    if novos_produtos:
        print("Os novos produtos cadastrados são:")
        for produto in novos_produtos:
            print(
                f"Mês: {produto['mes']}, Ano: {produto['ano']}, Perfil: {produto['perfil']}, Submercado: {produto['submercado']}, Tipo de Produto: {produto['tipo']}"
            )
    else:
        print("Não existem novos produtos cadastrados")


@when("o usuário marcar o checkbox de inativação de um produto e clica em sim")
def step_inativar_produto(context):
    """Marca o checkbox de inativação de um produto e confirma a ação."""
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    context.tela_de_produtos_page.inativar_produto()


@then("o sistema exibe uma mensagem de produto inativado com sucesso")
def step_validar_mensagem_inativacao(context):
    """Valida a exibição da mensagem de produto inativado com sucesso."""
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    mensagem = context.tela_de_produtos_page.validar_mensagem_inativacao()
    if mensagem:
        print(f"Mensagem exibida: {mensagem}")
    else:
        print("Mensagem de inativação não foi exibida.")


@then("o usuário consegue visualizar os produtos inativos")
def step_visualizar_produtos_inativos(context):
    """Valida e exibe os produtos inativos encontrados."""
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    produtos_inativos = context.tela_de_produtos_page.obter_produtos_inativos()

    if produtos_inativos:
        print("Foram encontrados os seguintes produtos inativos:")
        for produto in produtos_inativos:
            print(f"Mês: {produto['mes']}, Ano: {produto['ano']}")
    else:
        print("Nenhum produto inativo foi encontrado.")


@when("Usuário confirma exclusão de produto cadastrado")
def step_confirmar_exclusao_produto(context):
    """Confirma a exclusão de um produto clicando no botão 'Sim'."""
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    context.tela_de_produtos_page.confirmar_exclusao_produto()


@then("Sistema exibe mensagem de produto excluido com sucesso")
def step_validar_mensagem_confirmacao_exclusao(context):
    """Valida se a mensagem de confirmação da exclusão do produto é exibida."""
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    mensagem = context.tela_de_produtos_page.validar_mensagem_confirmacao_exclusao()
    if mensagem:
        print(f"Mensagem exibida: {mensagem}")
    else:
        print("Mensagem de confirmação da exclusão do produto não foi exibida.")


@when("Usuário não confirma exclusão de produto cadastrado")
def step_nao_confirmar_exclusao_produto(context):
    """Não confirma a exclusão de um produto clicando no botão 'Não'."""
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    context.tela_de_produtos_page.nao_confirmar_exclusao_produto


@then("Sistema retorna a página de produtos")
def step_validar_retorno_tela_produtos(context):
    """Valida que o usuário retornou à tela de produtos."""
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    if context.tela_de_produtos_page.validar_tela_produtos():
        print("Usuário retornou a tela de produtos")
    else:
        raise AssertionError("Usuário não retornou à tela de produtos.")


@then("uma mensagem de erro deve ser exibida")
def step_mensagem_erro_exibida(context):
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    mensagens = (
        context.tela_de_produtos_page.consultar_mensagens_erro_campos_obrigatorios()
    )
    if mensagens:
        print("Mensagens de erro exibidas:")
        for msg in mensagens:
            print(f"- {msg}")
    else:
        print("Nenhuma mensagem de erro foi exibida.")


@then("o sistema exibe apenas os produtos correspondentes ao filtro aplicado")
def step_valida_produtos_filtrados_por_ano(context):
    ano_pesquisado = getattr(context, "ano_pesquisado", None)
    if not ano_pesquisado:
        raise AssertionError(
            "Ano pesquisado não encontrado no contexto. Certifique-se de armazenar o ano ao pesquisar."
        )
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    if context.tela_de_produtos_page.validar_produtos_filtrados_por_ano(ano_pesquisado):
        print(f"Todos os produtos exibidos possuem o ano filtrado: {ano_pesquisado}")
    else:
        raise AssertionError(
            f"Foram encontrados produtos com ano diferente do filtrado: {ano_pesquisado}"
        )
