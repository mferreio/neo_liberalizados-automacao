from behave import given, when, then
import allure
import logging
from pages.perfil_de_acesso_pages import PerfilDeAcessoPage

@then('eu devo ter acesso total ao sistema')
def step_then_acesso_total(context):
    logging.info("Validando acesso total ao sistema.")
    try:
        assert context.perfil_de_acesso_pages.possui_acesso_total(), "Usuário não possui acesso total ao sistema."
    except AssertionError as e:
        context.failed_steps.append(f"Erro no passo 'eu devo ter acesso total ao sistema': {e}")
    except Exception as e:
        context.failed_steps.append(f"Erro inesperado no passo 'eu devo ter acesso total ao sistema': {e}")

# @then('eu devo conseguir cadastrar usuários com perfis')
# def step_then_cadastrar_usuarios_com_perfis(context):
#     logging.info("Validando cadastro de usuários com perfis.")
#     try:
#         if not hasattr(context, 'perfil_de_acesso_pages'):
#             context.perfil_de_acesso_pages = PerfilDeAcessoPage(context.driver)
#         assert context.perfil_de_acesso_pages.cadastrar_usuarios_com_perfis(), "Não foi possível cadastrar usuários com perfis."
#     except AssertionError as e:
#         logging.error(f"Erro ao validar cadastro de usuários com perfis: {e}")
#         context.failed_steps.append(f"Erro no passo 'eu devo conseguir cadastrar usuários com perfis': {e}")
#     except Exception as e:
#         logging.error(f"Erro inesperado ao validar cadastro de usuários com perfis: {e}")
#         context.failed_steps.append(f"Erro inesperado no passo 'eu devo conseguir cadastrar usuários com perfis': {e}")

# @then('eu devo conseguir visualizar todas as telas')
# def step_then_visualizar_todas_as_telas(context):
#     logging.info("Validando visualização de todas as telas.")
#     try:
#         assert context.perfil_de_acesso_pages.visualizar_todas_as_telas(), "Não foi possível visualizar todas as telas."
#     except AssertionError as e:
#         logging.error(f"Erro ao validar visualização de todas as telas: {e}")
#         context.failed_steps.append(f"Erro no passo 'eu devo conseguir visualizar todas as telas': {e}")
#     except Exception as e:
#         logging.error(f"Erro inesperado ao validar visualização de todas as telas: {e}")
#         context.failed_steps.append(f"Erro inesperado no passo 'eu devo conseguir visualizar todas as telas': {e}")

# @when("eu devo conseguir realizar todas as operações de 'Trading Portifólio'")
# def step_then_operacoes_trading_portfolio(context):
#     logging.info("Validando operações de Trading/Portfólio.")
#     try:
#         assert context.perfil_de_acesso_pages.realizar_operacoes_trading_portfolio(), "Não foi possível realizar operações de Trading/Portfólio."
#     except AssertionError as e:
#         logging.error(f"Erro ao validar operações de Trading/Portfólio: {e}")
#         context.failed_steps.append(f"Erro no passo 'eu devo conseguir realizar todas as operações de Trading Portifólio': {e}")
#     except Exception as e:
#         logging.error(f"Erro inesperado ao validar operações de Trading/Portfólio: {e}")
#         context.failed_steps.append(f"Erro inesperado no passo 'eu devo conseguir realizar todas as operações de Trading Portifólio': {e}")

# @then('eu devo conseguir realizar todas as operações do módulo Comercial')
# def step_then_operacoes_modulo_comercial(context):
#     logging.info("Validando operações do módulo Comercial.")
#     try:
#         assert context.perfil_de_acesso_pages.realizar_operacoes_modulo_comercial(), "Não foi possível realizar operações do módulo Comercial."
#     except AssertionError as e:
#         logging.error(f"Erro ao validar operações do módulo Comercial: {e}")
#         context.failed_steps.append(f"Erro no passo 'eu devo conseguir realizar todas as operações do módulo Comercial': {e}")
#     except Exception as e:
#         logging.error(f"Erro inesperado ao validar operações do módulo Comercial: {e}")
#         context.failed_steps.append(f"Erro inesperado no passo 'eu devo conseguir realizar todas as operações do módulo Comercial': {e}")

# @then('eu devo ter acesso aos módulos de produtos')
# def step_then_acesso_modulos_produtos(context):
#     logging.info("Validando acesso aos módulos de produtos.")
#     try:
#         assert context.perfil_de_acesso_pages.acessar_modulos_produtos(), "Não foi possível acessar os módulos de produtos."
#     except AssertionError as e:
#         logging.error(f"Erro ao validar acesso aos módulos de produtos: {e}")
#         context.failed_steps.append(f"Erro no passo 'eu devo ter acesso aos módulos de produtos': {e}")
#     except Exception as e:
#         logging.error(f"Erro inesperado ao validar acesso aos módulos de produtos: {e}")
#         context.failed_steps.append(f"Erro inesperado no passo 'eu devo ter acesso aos módulos de produtos': {e}")

# @then('eu devo ter acesso aos prêmios')
# def step_then_acesso_premios(context):
#     logging.info("Validando acesso aos prêmios.")
#     try:
#         assert context.perfil_de_acesso_pages.acessar_premios(), "Não foi possível acessar os prêmios."
#     except AssertionError as e:
#         logging.error(f"Erro ao validar acesso aos prêmios: {e}")
#         context.failed_steps.append(f"Erro no passo 'eu devo ter acesso aos prêmios': {e}")
#     except Exception as e:
#         logging.error(f"Erro inesperado ao validar acesso aos prêmios: {e}")
#         context.failed_steps.append(f"Erro inesperado no passo 'eu devo ter acesso aos prêmios': {e}")

# @then('eu devo ter acesso aos diretrizes')
# def step_then_acesso_diretrizes(context):
#     logging.info("Validando acesso às diretrizes.")
#     try:
#         assert context.perfil_de_acesso_pages.acessar_diretrizes(), "Não foi possível acessar as diretrizes."
#     except AssertionError as e:
#         logging.error(f"Erro ao validar acesso às diretrizes: {e}")
#         context.failed_steps.append(f"Erro no passo 'eu devo ter acesso aos diretrizes': {e}")
#     except Exception as e:
#         logging.error(f"Erro inesperado ao validar acesso às diretrizes: {e}")
#         context.failed_steps.append(f"Erro inesperado no passo 'eu devo ter acesso aos diretrizes': {e}")

# @then('eu devo ter acesso aos prêmio de proposta de diretrizes')
# def step_then_acesso_premio_proposta_diretrizes(context):
#     logging.info("Validando acesso ao prêmio de proposta de diretrizes.")
#     try:
#         assert context.perfil_de_acesso_pages.acessar_premio_proposta_diretrizes(), "Não foi possível acessar o prêmio de proposta de diretrizes."
#     except AssertionError as e:
#         logging.error(f"Erro ao validar acesso ao prêmio de proposta de diretrizes: {e}")
#         context.failed_steps.append(f"Erro no passo 'eu devo ter acesso aos prêmio de proposta de diretrizes': {e}")
#     except Exception as e:
#         logging.error(f"Erro inesperado ao validar acesso ao prêmio de proposta de diretrizes: {e}")
#         context.failed_steps.append(f"Erro inesperado no passo 'eu devo ter acesso aos prêmio de proposta de diretrizes': {e}")

# @then('eu devo ter acesso aos prêmios padrão')
# def step_then_acesso_premios_padrao(context):
#     logging.info("Validando acesso aos prêmios padrão.")
#     try:
#         assert context.perfil_de_acesso_pages.acessar_premios_padrao(), "Não foi possível acessar os prêmios padrão."
#     except AssertionError as e:
#         logging.error(f"Erro ao validar acesso aos prêmios padrão: {e}")
#         context.failed_steps.append(f"Erro no passo 'eu devo ter acesso aos prêmios padrão': {e}")
#     except Exception as e:
#         logging.error(f"Erro inesperado ao validar acesso aos prêmios padrão: {e}")
#         context.failed_steps.append(f"Erro inesperado no passo 'eu devo ter acesso aos prêmios padrão': {e}")

# @then('eu devo conseguir editar')
# def step_then_editar_dados(context):
#     logging.info("Validando permissão para editar dados.")
#     try:
#         assert context.perfil_de_acesso_pages.editar_dados(), "Não foi possível editar os dados."
#     except AssertionError as e:
#         logging.error(f"Erro ao validar permissão para editar dados: {e}")
#         context.failed_steps.append(f"Erro no passo 'eu devo conseguir editar': {e}")
#     except Exception as e:
#         logging.error(f"Erro inesperado ao validar permissão para editar dados: {e}")
#         context.failed_steps.append(f"Erro inesperado no passo 'eu devo conseguir editar': {e}")

# @then('eu devo conseguir criar dados')
# def step_then_criar_dados(context):
#     logging.info("Validando permissão para criar dados.")
#     try:
#         assert context.perfil_de_acesso_pages.criar_dados(), "Não foi possível criar os dados."
#     except AssertionError as e:
#         logging.error(f"Erro ao validar permissão para criar dados: {e}")
#         context.failed_steps.append(f"Erro no passo 'eu devo conseguir criar dados': {e}")
#     except Exception as e:
#         logging.error(f"Erro inesperado ao validar permissão para criar dados: {e}")
#         context.failed_steps.append(f"Erro inesperado no passo 'eu devo conseguir criar dados': {e}")

# @then('o menu deve apresentar todas as opções disponíveis')
# def step_then_menu_todas_opcoes(context):
#     logging.info("Validando que o menu apresenta todas as opções disponíveis.")
#     try:
#         assert context.perfil_de_acesso_pages.menu_apresenta_opcoes("todas"), "O menu não apresenta todas as opções disponíveis."
#     except AssertionError as e:
#         logging.error(f"Erro ao validar que o menu apresenta todas as opções disponíveis: {e}")
#         context.failed_steps.append(f"Erro no passo 'o menu deve apresentar todas as opções disponíveis': {e}")
#     except Exception as e:
#         logging.error(f"Erro inesperado ao validar que o menu apresenta todas as opções disponíveis: {e}")
#         context.failed_steps.append(f"Erro inesperado no passo 'o menu deve apresentar todas as opções disponíveis': {e}")

# @then('o menu deve apresentar apenas as opções de produtos, prêmios, e diretrizes')
# def step_then_menu_opcoes_limitadas(context):
#     logging.info("Validando que o menu apresenta apenas opções limitadas.")
#     try:
#         assert context.perfil_de_acesso_pages.menu_apresenta_opcoes("produtos, prêmios, diretrizes"), "O menu não apresenta as opções esperadas."
#     except AssertionError as e:
#         logging.error(f"Erro ao validar que o menu apresenta apenas opções limitadas: {e}")
#         context.failed_steps.append(f"Erro no passo 'o menu deve apresentar apenas as opções de produtos, prêmios, e diretrizes': {e}")
#     except Exception as e:
#         logging.error(f"Erro inesperado ao validar que o menu apresenta apenas opções limitadas: {e}")
#         context.failed_steps.append(f"Erro inesperado no passo 'o menu deve apresentar apenas as opções de produtos, prêmios, e diretrizes': {e}")

# @given('que eu não estou logado na aplicação')
# def step_given_nao_logado(context):
#     logging.info("Validando que o usuário não está logado na aplicação.")
#     context.perfil_de_acesso_pages.logout()

# @when('eu tento acessar a aplicação')
# def step_when_tento_acessar(context):
#     logging.info("Tentando acessar a aplicação sem estar logado.")
#     context.perfil_de_acesso_pages.tentar_acessar()

# @then('eu não devo visualizar nada')
# def step_then_nao_visualizar_nada(context):
#     logging.info("Validando que o usuário não visualiza nada ao acessar sem login.")
#     try:
#         assert context.perfil_de_acesso_pages.nao_visualizar_nada(), "Usuário conseguiu visualizar algo, mas não deveria."
#     except AssertionError as e:
#         logging.error(f"Erro ao validar que o usuário não visualiza nada ao acessar sem login: {e}")
#         context.failed_steps.append(f"Erro no passo 'eu não devo visualizar nada': {e}")
#     except Exception as e:
#         logging.error(f"Erro inesperado ao validar que o usuário não visualiza nada ao acessar sem login: {e}")
#         context.failed_steps.append(f"Erro inesperado no passo 'eu não devo visualizar nada': {e}")

# @given('que eu não sou um usuário autenticado')
# def step_given_nao_autenticado(context):
#     logging.info("Validando que o usuário não é autenticado.")
#     context.perfil_de_acesso_pages.logout()

# @when('eu tento acessar qualquer recurso da aplicação')
# def step_when_tento_acessar_recurso(context):
#     logging.info("Tentando acessar recursos da aplicação sem autenticação.")
#     context.perfil_de_acesso_pages.tentar_acessar_recurso()

# @then('eu devo ser redirecionado para a tela de login')
# def step_then_redirecionado_login(context):
#     logging.info("Validando redirecionamento para a tela de login.")
#     try:
#         assert context.perfil_de_acesso_pages.redirecionado_para_login(), "Usuário não foi redirecionado para a tela de login."
#     except AssertionError as e:
#         logging.error(f"Erro ao validar redirecionamento para a tela de login: {e}")
#         context.failed_steps.append(f"Erro no passo 'eu devo ser redirecionado para a tela de login': {e}")
#     except Exception as e:
#         logging.error(f"Erro inesperado ao validar redirecionamento para a tela de login: {e}")
#         context.failed_steps.append(f"Erro inesperado no passo 'eu devo ser redirecionado para a tela de login': {e}")

# @then('eu não devo conseguir visualizar informações de qualquer perfil')
# def step_then_nao_visualizar_informacoes(context):
#     logging.info("Validando que o usuário não visualiza informações de qualquer perfil.")
#     try:
#         assert context.perfil_de_acesso_pages.nao_visualizar_nada(), "Usuário conseguiu visualizar informações, mas não deveria."
#     except AssertionError as e:
#         logging.error(f"Erro ao validar que o usuário não visualiza informações de qualquer perfil: {e}")
#         context.failed_steps.append(f"Erro no passo 'eu não devo conseguir visualizar informações de qualquer perfil': {e}")
#     except Exception as e:
#         logging.error(f"Erro inesperado ao validar que o usuário não visualiza informações de qualquer perfil: {e}")
#         context.failed_steps.append(f"Erro inesperado no passo 'eu não devo conseguir visualizar informações de qualquer perfil': {e}")

# @then('eu devo conseguir visualizar o modulo de produtos')
# def step_then_visualizar_modulo_produtos(context):
#     logging.info("Validando visualização do módulo de produtos.")
#     try:
#         assert context.perfil_de_acesso_pages.visualizar_modulo_produtos(), "Não foi possível visualizar o módulo de produtos."
#     except AssertionError as e:
#         logging.error(f"Erro ao validar visualização do módulo de produtos: {e}")
#         context.failed_steps.append(f"Erro no passo 'eu devo conseguir visualizar o modulo de produtos': {e}")
#     except Exception as e:
#         logging.error(f"Erro inesperado ao validar visualização do módulo de produtos: {e}")
#         context.failed_steps.append(f"Erro inesperado no passo 'eu devo conseguir visualizar o modulo de produtos': {e}")

# @then('eu devo conseguir excluir um produto')
# def step_then_excluir_produto(context):
#     logging.info("Validando exclusão de um produto.")
#     try:
#         assert context.perfil_de_acesso_pages.excluir_produto(), "Não foi possível excluir o produto."
#     except AssertionError as e:
#         logging.error(f"Erro ao validar exclusão de um produto: {e}")
#         context.failed_steps.append(f"Erro no passo 'eu devo conseguir excluir um produto': {e}")
#     except Exception as e:
#         logging.error(f"Erro inesperado ao validar exclusão de um produto: {e}")
#         context.failed_steps.append(f"Erro inesperado no passo 'eu devo conseguir excluir um produto': {e}")

