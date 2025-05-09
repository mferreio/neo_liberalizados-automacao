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


@when('eu escolho o perfil "{perfil}"')
def step_escolher_perfil(context, perfil):
    """Abre o dropdown de perfil e seleciona o perfil especificado."""
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    context.tela_de_produtos_page.escolher_perfil()
    logging.info(f"Perfil '{perfil}' selecionado com sucesso.")


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


@when("o usuário tiver um produto inativo")
def step_usuario_tiver_produto_inativo(context):
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    context.produto_inativo = context.tela_de_produtos_page.consultar_produto_inativo()


@then("esse produto deve ser exibido na lista de produtos")
def step_produto_exibido_na_lista(context):
    if context.produto_inativo:
        print(
            f"Produto Inativo - Mês: {context.produto_inativo['mes']}, Ano: {context.produto_inativo['ano']}"
        )
    else:
        print("Não foram identificados produtos inativos cadastrados")


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


@when("Usuário não preenche os campos obrigatórios")
def step_nao_preenche_campos_obrigatorios(context):
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    context.tela_de_produtos_page.nao_preencher_campos_obrigatorios()


@when("Usuário preenche os campos obrigatórios com dados inválidos")
def step_preencher_campos_obrigatorios_invalidos(context):
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    context.tela_de_produtos_page.preencher_campos_obrigatorios_invalidos()


@when("consultar os produtos cadastrados")
def step_consultar_produtos_cadastrados(context):
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    context.produtos_com_submercado = (
        context.tela_de_produtos_page.consultar_produtos_cadastrados()
    )


@when("o usuário visualizar um produto com diretriz diária e semanal")
def step_visualizar_produto_diretriz_diaria_semanal(context):
    # Apenas garante que os dados já estão disponíveis no context
    assert hasattr(context, "produtos_com_submercado"), "Produtos não foram coletados."


@then("o submercado associado ao produto deve ser exibido corretamente na lista")
def step_exibir_lista_produtos_com_submercado(context):
    produtos = getattr(context, "produtos_com_submercado", [])
    if produtos:
        print("Segue a relação de cada produto cadastrado com o Submercado")
        print("Mês | Ano | Perfil | Submercado | Tipo de Produto | Produto Ativo")
        for p in produtos:
            print(
                f"{p['mes']} | {p['ano']} | {p['perfil']} | {p['submercado']} | {p['tipo']} | {p['ativo']}"
            )
    else:
        print("Nenhum produto cadastrado encontrado.")


@then("o novo produto deve estar visível na lista de produtos")
def step_novo_produto_visivel_na_lista(context):
    # Exemplo: context.produto_cadastrado deve ser um dicionário com as chaves: mes, ano, perfil, submercado, tipo
    produto = getattr(context, "produto_cadastrado", None)
    if not produto:
        raise AssertionError("Dados do novo produto não encontrados no contexto.")
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    if context.tela_de_produtos_page.produto_esta_visivel_na_lista(produto):
        print("Novo produto está visível na lista de produtos.")
    else:
        raise AssertionError("Novo produto NÃO está visível na lista de produtos.")


@when("o usuário clica em voltar")
def step_clicar_em_voltar(context):
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    context.tela_de_produtos_page.clicar_botao_voltar()


@then("o usuário deve ser redirecionado para a tela de produtos")
def step_validar_redirecionamento_tela_produtos(context):
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    if context.tela_de_produtos_page.validar_redirecionamento_tela_produtos():
        print("Usuário foi redirecionado para a tela de produtos.")
    else:
        raise AssertionError("Usuário NÃO foi redirecionado para a tela de produtos.")


@when("o usuário consulta um produto inativo")
def step_consulta_produto_inativo(context):
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    context.produtos_inativos_detalhados = (
        context.tela_de_produtos_page.consultar_produtos_inativos_detalhados()
    )


@then("todos os detalhes do produto inativo devem ser exibidos na tela")
def step_exibe_detalhes_produto_inativo(context):
    produtos = getattr(context, "produtos_inativos_detalhados", [])
    if produtos:
        print("Segue a relação de produtos inativos")
        print("Mês | Ano | Perfil | Submercado | Tipo de Produto | Produto Ativo")
        for p in produtos:
            print(
                f"{p['mes']} | {p['ano']} | {p['perfil']} | {p['submercado']} | {p['tipo']} | {p['ativo']}"
            )
    else:
        print("Nenhum produto inativo foi encontrado.")
