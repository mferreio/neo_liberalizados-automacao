Feature: Perfil de acesso não logado
  Como administrador
  Quero acessar a aplicação com permissões específicas
  Para realizar operações de acordo com meu perfil

   Scenario: Acesso não logado
    Given que o usuário não está logado
    When eu tento acessar a aplicação
    Then eu não devo visualizar nada

   Scenario: Tentativa de acesso não logado
    Given que o usuário não está logado
    When eu tento acessar qualquer recurso da aplicação
    Then eu devo ser redirecionado para a tela de login
    When eu não devo conseguir visualizar informações de qualquer perfil