Feature: Tela de cadastro de usuário
  Como administrador
  Quero cadastrar usuários com perfis específicos
  Para gerenciar o acesso à aplicação

Background: Given que eu estou na Página Inicial
    Given que o usuário está logado como "Administrador"
    When navega até a tela de usuários - Perfil


Scenario: Cadastro de usuário com sucesso
    When o usuário clica no botão "Novo" para adicionar usuario
    When clica no dropdown de perfil
    When o usuário seleciona o perfil de administrador, escreve o nome e email
    When o usuário clica em "Salvar" para salvar o novo usuário
    Then navega até a tela de usuários - Perfil

Scenario: Cadastro de usuário com e-mail inválido
    When o usuário clica no botão "Novo" para adicionar usuario
    When clica no dropdown de perfil
    When o usuário seleciona o perfil de administrador, escreve o nome e email invalido
    When o usuário clica em "Salvar" para salvar o novo usuário
    Then a notificação "E-mail inválido" deve ser exibida
    When o usuário clica em "Salvar" para salvar o novo usuário

 Scenario: Alteração de dados do usuário com sucesso
    When clica no botão "Editar"
    When edita o tipo de perfil do usuário
    When edita o nome e email do usuário
    When clica em Salvar para salvar as alterações
    Then navega até a tela de usuários - Perfil

Scenario: Erro ao tentar cadastrar usuário que já existe
    When clica no botão "Editar"
    When edita o tipo de perfil do usuário
    When edita o nome e email do usuário
    When clica em Salvar para salvar as alterações
    Then a notificação "Usuário já existe" deve ser exibida
    Then navega até a tela de usuários - Perfil

Scenario: Campos obrigatórios não preenchidos
    When o usuário clica no botão "Novo" para adicionar usuario
    When clica no dropdown de perfil
    When o usuário não preenche os campos obrigatórios
    When o usuário clica em "Salvar" para salvar o novo usuário
    Then a notificação 'Campos obrigatórios não preenchidos' deve ser exibida
    When navega até a tela de usuários - Perfil