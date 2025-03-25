Feature: Acessar a página de login e testar fluxo de tela de usuários

  Scenario: Acessar a página de login com sucesso
    Given que eu acesso a página de login
    When eu clico no botão Entrar
    When eu insiro o email de usuario
    When eu clico no botão Seguinte
    When eu preencho o ADFS com usuário e senha
    Then eu verifico que o usuário acessou o sistema

  Scenario: Administrador acessa a tela de usuários
    Given que o usuário está logado como "Administrador"
    When navega até a tela de usuários - Perfil
    Then a tela de usuários deve ser exibida

  Scenario: Visualizar usuários cadastrados
    Given que o usuário está logado como "Administrador"
    When navega até a tela de usuários - Perfil
    Then valida os usuarios cadastrados

  Scenario: Cancelar processo para adicionar um novo usuário
    Given que o usuário está logado como "Administrador"
    When navega até a tela de usuários - Perfil
    When o usuário clica no botão "Novo" para adicionar usuario
  #  When o usuário acessa a tela de cadastro de usuário
    Then o usuário fecha a tela de cadastro e é direcionado para a tela de usuários
    When navega até a tela de usuários - Perfil

  Scenario: Adicionar um novo usuário
    Given que o usuário está logado como "Administrador"
    When navega até a tela de usuários - Perfil
    When o usuário clica no botão "Novo" para adicionar usuario
    #  When o usuário acessa a tela de cadastro de usuário
    When clica no dropdown de perfil
    When o usuário seleciona o perfil de usuário, escreve o nome e email
    When o usuário clica em "Salvar" para salvar o novo usuário
    Then navega até a tela de usuários - Perfil

  Scenario: Editar um usuário existente
    Given que o usuário está logado como "Administrador"
    When navega até a tela de usuários - Perfil
    When clica no botão "Editar"
    When edita o tipo de perfil do usuário
    When edita o nome e email do usuário
    When clica em Salvar para salvar as alterações
    Then navega até a tela de usuários - Perfil

  Scenario: Cancelar exclusão de um usuário
    Given que o usuário está logado como "Administrador"
    When navega até a tela de usuários - Perfil
    When pesquisa um usuario cadastrado
    When clica em excluir e cancela a exclusao
    Then navega até a tela de usuários - Perfil

    Scenario: Excluir um usuário existente
    Given que o usuário está logado como "Administrador"
    When navega até a tela de usuários - Perfil
    When pesquisa um usuario cadastrado
    When clica em excluir e confirma
    Then navega até a tela de usuários - Perfil

  # Scenario: Controle de acesso a módulos do sistema
  #   Given que um usuário tem o e-mail "joao@email.com" e o perfil "Usuário"
  #   When o usuário tenta acessar o módulo "Administração"
  #   Then uma mensagem de erro "Acesso negado. Você não tem permissão para acessar este módulo." deve ser exibida

  # Scenario: Usuário não administrador tenta acessar a tela de usuários
  #   Given que o usuário está logado como "Usuário Comum"
  #   When o usuário navega até a tela de usuários
  #   Then uma mensagem de erro "Acesso negado. Somente administradores podem acessar esta tela." deve ser exibida
