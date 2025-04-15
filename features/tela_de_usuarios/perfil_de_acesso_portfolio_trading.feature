Feature: Gerenciamento de Perfis de Acesso
  Como usuário Trading/Portifólio
  Quero acessar a aplicação com permissões específicas
  Para realizar operações de acordo com meu perfil

    Scenario: Usuário Trading/Portifólio acessa a aplicação diretrizes
        Given que o usuário está logado como 'Trading Portifólio'
        Then eu devo ter acesso aos módulos de produtos
        When eu devo ter acesso aos diretrizes

    Scenario: Usuário Trading/Portifólio acessa a aplicação prêmio de proposta de diretrizes
        Given que o usuário está logado como 'Trading Portifólio'
        Then eu devo ter acesso aos módulos de produtos
        When eu devo ter acesso aos prêmio de proposta de diretrizes

    Scenario: Usuário Trading/Portifólio acessa a aplicação prêmios padrão
        Given que o usuário está logado como 'Trading Portifólio'
        Then eu devo ter acesso aos módulos de produtos
        When eu devo ter acesso aos prêmios padrão

    Scenario: Usuário Trading/Portifólio acessa a aplicação visualizar
        Given que o usuário está logado como 'Trading Portifólio'
        Then eu devo ter acesso aos módulos de produtos
        When eu devo conseguir visualizar o modulo de produtos

    Scenario: Usuário Trading/Portifólio acessa a aplicação editar
        Given que o usuário está logado como 'Trading Portifólio'
        Then eu devo ter acesso aos módulos de produtos
        When eu devo conseguir editar

    Scenario: Usuário Trading/Portifólio acessa a aplicação excluir
        Given que o usuário está logado como 'Trading Portifólio'
        Then eu devo ter acesso aos módulos de produtos
        When eu devo conseguir excluir um produto

    Scenario: Usuário Trading/Portifólio acessa a aplicação criar dados
        Given que o usuário está logado como 'Trading Portifólio'
        Then eu devo ter acesso aos módulos de produtos
        When eu devo conseguir criar dados

    Scenario: Usuário Trading/Portifólio acessa a aplicação prêmios
        Given que o usuário está logado como 'Trading Portifólio'
        Then eu devo ter acesso aos módulos de produtos
        When eu devo ter acesso aos prêmios

    Scenario: Acesso ao menu pelo Trading/Portifólio
        Given que o usuário está logado como 'Trading Portifólio'
        Then o menu deve apresentar apenas as opções de produtos, prêmios, e diretrizes

