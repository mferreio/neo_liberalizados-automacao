from behave import given, then, when

@given("que o usuário está logado como Portifolio Trading")
def step_usuario_logado(context):
    context.perfil_de_acesso_pages.realizar_login_com_perfil("Portifolio Trading")

@then("eu devo ter acesso aos módulos de produtos")
def step_acesso_modulos_produtos(context):
    assert context.perfil_de_acesso_pages.verificar_acesso_modulos_produtos(), "Usuário não tem acesso aos módulos de produtos."

@then("eu devo ter acesso aos diretrizes")
def step_acesso_modulo_especifico(context):
    assert context.perfil_de_acesso_pages.verificar_acesso_modulo_especifico("diretrizes"), "Usuário não tem acesso ao módulo diretrizes."

@then("eu devo conseguir visualizar o modulo de produtos")
def step_visualizar_modulo_produtos(context):
    assert context.perfil_de_acesso_pages.visualizar_modulo_produtos(), "Usuário não conseguiu visualizar o módulo de produtos."

@then("eu devo conseguir editar")
def step_editar(context):
    assert context.perfil_de_acesso_pages.editar_modulo_produtos(), "Usuário não conseguiu editar o módulo de produtos."

@then("eu devo conseguir excluir um produto")
def step_excluir_produto(context):
    assert context.perfil_de_acesso_pages.excluir_produto(), "Usuário não conseguiu excluir um produto."

@then("eu devo conseguir criar dados")
def step_criar_dados(context):
    assert context.perfil_de_acesso_pages.criar_dados(), "Usuário não conseguiu criar dados."

@then("o menu deve apresentar apenas as opções de produtos, prêmios, e diretrizes")
def step_verificar_menu(context):
    assert context.perfil_de_acesso_pages.verificar_opcoes_menu(), "O menu não apresenta as opções corretas."

@when("eu devo ter acesso aos prêmio de proposta de diretrizes")
def step_acesso_modulo_especifico(context):
    assert context.perfil_de_acesso_pages.verificar_acesso_modulo_especifico("prêmio de proposta de diretrizes"), "Usuário não tem acesso ao módulo prêmio de proposta de diretrizes."

@when("eu devo ter acesso aos prêmios padrão")
def step_acesso_modulo_especifico(context):
    assert context.perfil_de_acesso_pages.verificar_acesso_modulo_especifico("prêmios padrão"), "Usuário não tem acesso ao módulo prêmios padrão."

@when("eu devo ter acesso aos prêmios")
def step_acesso_modulo_especifico(context):
    assert context.perfil_de_acesso_pages.verificar_acesso_modulo_especifico("prêmios"), "Usuário não tem acesso ao módulo prêmios."
