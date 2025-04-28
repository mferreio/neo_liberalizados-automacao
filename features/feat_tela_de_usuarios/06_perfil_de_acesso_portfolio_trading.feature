Feature: Perfil de acesso Portifólio/Trading
  Como usuário Trading/Portifólio
  Quero acessar a aplicação com permissões específicas
  Para realizar operações de acordo com meu perfil

    Scenario: Usuário Trading/Portifólio acessa a aplicação diretrizes
        Given que o usuário está logado como 'Trading Portifólio'
        When eu devo ter acesso aos módulos de produtos
        Then eu devo ter acesso aos diretrizes

     Scenario: Usuário Trading/Portifólio acessa a aplicação prêmio de proposta de diretrizes
        Given que o usuário está logado como 'Trading Portifólio'
        When eu devo ter acesso aos módulos de produtos
        Then eu devo ter acesso aos prêmio de proposta de diretrizes
        When usuário retorna a tela inicial

     Scenario: Usuário Trading/Portifólio acessa a aplicação prêmios padrão
        Given que o usuário está logado como 'Trading Portifólio'
        When eu devo ter acesso aos módulos de produtos
    #     Then eu devo ter acesso aos prêmios padrão // "Produto está sendo desenvolvido, não existe prêmio padrão ainda"
        When usuário retorna a tela inicial

     Scenario: Usuário Trading/Portifólio acessa a aplicação visualizar
        Given que o usuário está logado como 'Trading Portifólio'
        When eu devo ter acesso aos módulos de produtos
        Then eu devo conseguir visualizar o modulo de produtos

     Scenario: Usuário Trading/Portifólio acessa a aplicação editar
        Given que o usuário está logado como 'Trading Portifólio'
        When eu devo ter acesso aos módulos de produtos
        When Usuário acessa o produto Diario Semanal na aba produtos
        When Usuário pesquisa pelo ano
        When Usuário seleciona o produto
        When Usuário clica no botão editar
        Then o sistema exibe a pagina de edição do produto
        When usuário retorna a tela inicial

     Scenario: Usuário Trading/Portifólio acessa a aplicação excluir
        Given que o usuário está logado como 'Trading Portifólio'
        When eu devo ter acesso aos módulos de produtos
        When Usuário acessa o produto Diario Semanal na aba produtos
        When Usuário pesquisa pelo ano
        When Usuário seleciona o produto
        When Usuário clica no botão excluir
        Then eu devo acessar a tela para excluir um produto
        When usuário retorna a tela inicial


     Scenario: Usuário Trading/Portifólio acessa a aplicação criar dados
         Given que o usuário está logado como 'Trading Portifólio'
         When eu devo ter acesso aos módulos de produtos
         When Usuário acessa o produto Diario Semanal na aba produtos
         When Usuário clica em novo produto
         When Usuário preenche os campos obrigatórios
         When Usuário clica em cadastrar produto
         Then eu devo conseguir criar dados

    # Scenario: Usuário Trading/Portifólio acessa a aplicação prêmios
    #     Given que o usuário está logado como 'Trading Portifólio'
    #     When eu devo ter acesso aos módulos de produtos
    #     Then eu devo ter acesso aos prêmios

    Scenario: Acesso ao menu pelo Trading/Portifólio
         Given que o usuário está logado como 'Trading Portifólio'
    #     Then o menu deve apresentar apenas as opções de produtos, prêmios, e diretrizes

