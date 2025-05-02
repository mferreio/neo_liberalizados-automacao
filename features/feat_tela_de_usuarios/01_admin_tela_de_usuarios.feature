Feature: Acessar a página de login e testar fluxo de tela de usuários

  Scenario: Administrador acessa a tela de usuários
    Given que o usuário está logado como "Administrador"
    When navega até a tela de usuários - Perfil
    Then a tela de usuários deve ser exibida

  Scenario: Visualizar usuários cadastrados
    Given que o usuário está logado como "Administrador"
    When navega até a tela de usuários - Perfil
    Then valida os usuarios cadastrados exibindo nome, email e perfil

  Scenario: Cancelar processo para adicionar um novo usuário
    Given que o usuário está logado como "Administrador"
    When navega até a tela de usuários - Perfil
    When o usuário clica no botão "Novo" para adicionar usuario
    Then o usuário fecha a tela de cadastro e é direcionado para a tela de usuários
    When navega até a tela de usuários - Perfil

  Scenario: Adicionar um novo usuário administrador
    Given que o usuário está logado como "Administrador"
    When navega até a tela de usuários - Perfil
    When o usuário clica no botão "Novo" para adicionar usuario
    When clica no dropdown de perfil
    When o usuário seleciona o perfil de administrador, escreve o nome e email
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
    When clica em excluir
    When clica em nao e cancela a exclusao
    Then navega até a tela de usuários - Perfil

  Scenario: Excluir um usuário existente
    Given que o usuário está logado como "Administrador"
    When navega até a tela de usuários - Perfil
    When pesquisa um usuario cadastrado
    When clica em excluir
    When clica em sim para confirmar a exclusao
    Then navega até a tela de usuários - Perfil