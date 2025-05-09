Feature: Perfil de acesso Administrador
  Como administrador
  Quero acessar a aplicação com permissões específicas
  Para realizar operações de acordo com meu perfil

  Scenario: Administrador acessa a aplicação cadastro de usuário com perfis
    Given que o usuário está logado como "Administrador"
    When eu devo ter acesso total ao sistema
    When navega até a tela de usuários - Perfil
    When o usuário clica no botão "Novo" para adicionar usuario
    When clica no dropdown de perfil
    #When o usuário seleciona o perfil de usuário, escreve o nome e email
    When o usuário clica em "Salvar" para salvar o novo usuário
    #Then o sistema exibe uma mensagem de sucesso
    Then navega até a tela inicial

   Scenario: Administrador acessa a aplicação visualização das telas
    Given que o usuário está logado como "Administrador"
    When eu devo ter acesso total ao sistema
    Then eu devo conseguir visualizar todas as telas

   Scenario: Administrador acessa a aplicação operações Trading/Portifólio
    Given que o usuário está logado como "Administrador"
    When eu devo ter acesso total ao sistema
    Then eu devo conseguir realizar todas as operações de 'Trading Portifólio'

   Scenario: Administrador acessa a aplicação operações módulo Comercial
    Given que o usuário está logado como "Administrador"
    Then eu devo ter acesso total ao sistema
    # And eu devo conseguir realizar todas as operações do módulo Comercial

   Scenario: Acesso ao menu pelo Administrador
    Given que o usuário está logado como "Administrador"
    Then o menu deve apresentar todas as opções disponíveis