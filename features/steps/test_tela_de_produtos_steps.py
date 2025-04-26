from behave import when, then
from pages.tela_deprodutos_pages import TelaDeProdutosPage
import logging

@when('eu escolho o perfil "{perfil}"')
def step_escolher_perfil(context, perfil):
    """Abre o dropdown de perfil e seleciona o perfil especificado."""
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    context.tela_de_produtos_page.escolher_perfil()
    logging.info(f"Perfil '{perfil}' selecionado com sucesso.")

@then('as opções disponíveis de perfil devem incluir: CONV, I50, I0, I100 e CQI5')
def step_verificar_opcoes_disponiveis(context):
    """Verifica se as opções disponíveis no dropdown de perfil incluem as esperadas."""
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    opcoes_disponiveis = context.tela_de_produtos_page.obter_opcoes_disponiveis_no_dropdown()

    # Opções esperadas
    opcoes_esperadas = ["CONV", "I50", "I0", "I100", "CQI5"]

    # Verifica se todas as opções esperadas estão presentes
    for opcao in opcoes_esperadas:
        assert opcao in opcoes_disponiveis, f"A opção '{opcao}' não está disponível no dropdown."

    logging.info("Todas as opções esperadas estão disponíveis no dropdown de perfil.")

@when('eu escolho o submercado "{submercado}"')
def step_escolher_submercado(context, submercado):
    """Abre o dropdown de submercado e seleciona o submercado especificado."""
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    context.tela_de_produtos_page.escolher_submercado()
    logging.info(f"Submercado '{submercado}' selecionado com sucesso.")

@then('as opções disponíveis de submercado devem incluir: SE, NE, S e N')
def step_verificar_opcoes_disponiveis_submercado(context):
    """Verifica se as opções disponíveis no dropdown de submercado incluem as esperadas."""
    context.tela_de_produtos_page = TelaDeProdutosPage(context.driver)
    opcoes_disponiveis = context.tela_de_produtos_page.obter_opcoes_disponiveis_submercado()

    # Opções esperadas
    opcoes_esperadas = ["SE", "NE", "S", "N"]

    # Verifica se todas as opções esperadas estão presentes
    for opcao in opcoes_esperadas:
        assert opcao in opcoes_disponiveis, f"A opção '{opcao}' não está disponível no dropdown."

    logging.info("Todas as opções esperadas estão disponíveis no dropdown de submercado.")