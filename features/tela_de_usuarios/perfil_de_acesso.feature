Feature: Gerenciamento de Perfis de Acesso
  Como administrador ou usuário Trading/Portifólio
  Quero acessar a aplicação com permissões específicas
  Para realizar operações de acordo com meu perfil

  Scenario: Administrador acessa a aplicação cadastro de usuário com perfis
    Given que o usuário está logado como "Administrador"
    And eu devo conseguir cadastrar usuários com perfis

  Scenario: Administrador acessa a aplicação visualização das telas
    Given que o usuário está logado como "Administrador"
    Then eu devo ter acesso total ao sistema
    And eu devo conseguir visualizar todas as telas

  Scenario: Administrador acessa a aplicação operações Trading/Portifólio
    Given que o usuário está logado como "Administrador"
    Then eu devo ter acesso total ao sistema
    And eu devo conseguir realizar todas as operações de Trading/Portifólio

  Scenario: Administrador acessa a aplicação operações módulo Comercial
    Given que o usuário está logado como "Administrador"
    Then eu devo ter acesso total ao sistema
    And eu devo conseguir realizar todas as operações do módulo Comercial

  Scenario: Usuário Trading/Portifólio acessa a aplicação prêmios
    Given que o usuário está logado como "Administrador"
    Then eu devo ter acesso aos módulos de produtos
    And eu devo ter acesso aos prêmios

  Scenario: Usuário Trading/Portifólio acessa a aplicação diretrizes
    Given que o usuário está logado como "Trading/Portifólio"
    When eu faço login na aplicação
    Then eu devo ter acesso aos módulos de produtos
    And eu devo ter acesso aos diretrizes

  Scenario: Usuário Trading/Portifólio acessa a aplicação prêmio de proposta de diretrizes
    Given que o usuário está logado como "Trading/Portifólio"
    Then eu devo ter acesso aos módulos de produtos
    And eu devo ter acesso aos prêmio de proposta de diretrizes

  Scenario: Usuário Trading/Portifólio acessa a aplicação prêmios padrão
    Given que o usuário está logado como "Trading/Portifólio"
    Then eu devo ter acesso aos módulos de produtos
    And eu devo ter acesso aos prêmios padrão

  Scenario: Usuário Trading/Portifólio acessa a aplicação visualizar
    Given que o usuário está logado como "Trading/Portifólio"
    Then eu devo ter acesso aos módulos de produtos
    And eu devo conseguir visualizar

  Scenario: Usuário Trading/Portifólio acessa a aplicação editar
    Given que o usuário está logado como "Trading/Portifólio"
    Then eu devo ter acesso aos módulos de produtos
    And eu devo conseguir editar

  Scenario: Usuário Trading/Portifólio acessa a aplicação excluir
    Given que o usuário está logado como "Trading/Portifólio"
    Then eu devo ter acesso aos módulos de produtos
    And eu devo conseguir excluir

  Scenario: Usuário Trading/Portifólio acessa a aplicação criar dados
    Given que o usuário está logado como "Trading/Portifólio"
    Then eu devo ter acesso aos módulos de produtos
    And eu devo conseguir criar dados

  Scenario: Acesso ao menu pelo Administrador
    Given que o usuário está logado como "Administrador"
    Then o menu deve apresentar todas as opções disponíveis

  Scenario: Acesso ao menu pelo Trading/Portifólio
    Given que o usuário está logado como "Trading/Portifólio"
    Then o menu deve apresentar apenas as opções de produtos, prêmios, e diretrizes

  Scenario: Acesso não logado
    Given que eu não estou logado na aplicação
    When eu tento acessar a aplicação
    Then eu não devo visualizar nada

  Scenario: Tentativa de acesso não logado
    Given que eu não sou um usuário autenticado
    When eu tento acessar qualquer recurso da aplicação
    Then eu devo ser redirecionado para a tela de login
    And eu não devo conseguir visualizar informações de qualquer perfil
