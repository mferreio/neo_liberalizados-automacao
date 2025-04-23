Feature: Testar a usabilidade da tela de usuários para o administrador

  Scenario: Administrador acessa a tela de usuários
    Given que o usuário está logado como "Administrador"
    When navega até a tela de usuários - Perfil
    Then a tela de usuários deve ser exibida com todos os elementos visíveis

  Scenario: Visualizar usuários cadastrados
    Given que o usuário está logado como "Administrador"
    When navega até a tela de usuários - Perfil
    Then valida os usuarios cadastrados exibindo nome, email e perfil

  Scenario: Cancelar processo para adicionar um novo usuário
    Given que o usuário está logado como "Administrador"
    When navega até a tela de usuários - Perfil
    When valida os usuarios cadastrados exibindo nome, email e perfil
    When o usuário clica no botão "Novo" para adicionar usuario
    Then o usuário fecha a tela de cadastro e é direcionado para a tela de usuários
    When valida que nenhum novo usuário foi adicionado

  Scenario: Adicionar um novo usuário
    Given que o usuário está logado como "Administrador"
    When navega até a tela de usuários - Perfil
    When o usuário clica no botão "Novo" para adicionar usuario
    When clica no dropdown de perfil
    When o usuário seleciona o perfil de usuário, escreve o nome e email
    When o usuário clica em "Salvar" para salvar o novo usuário
    Then valida que o novo usuário foi adicionado com sucesso

  Scenario: Editar um usuário existente
    Given que o usuário está logado como "Administrador"
    When navega até a tela de usuários - Perfil
    When clica no botão "Editar"
    When edita o tipo de perfil do usuário
    When edita o nome e email do usuário
    When clica em Salvar para salvar as alterações
    Then valida que as alterações foram salvas corretamente

  Scenario: Cancelar exclusão de um usuário
    Given que o usuário está logado como "Administrador"
    When navega até a tela de usuários - Perfil
    When pesquisa um usuario cadastrado
    When clica em excluir e cancela a exclusao
    Then valida que o usuário não foi excluído

  Scenario: Excluir um usuário existente
    Given que o usuário está logado como "Administrador"
    When navega até a tela de usuários - Perfil
    When pesquisa um usuario cadastrado
    When clica em excluir e confirma
    Then valida que o usuário foi excluído com sucesso