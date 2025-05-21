Feature: Validação de Usuário
  Como um administrador do sistema
  Eu quero validar o cadastro de usuários no Active Directory
  Para garantir que apenas usuários válidos possam acessar o sistema

  Background:
    Given que o usuário está logado no sistema

# Scenario: Usuário autenticado sem perfil cadastrado
#     Given que o usuário "usuario@exemplo.com" está registrado no Active Directory
#  	And o usuário não possui um perfil cadastrado no sistema
#  	When o usuário faz login no sistema usando suas credenciais
#  	Then o sistema deve exibir uma mensagem para contato com o administrador
#  	And a mensagem deve ser "Perfil não encontrado. Por favor, entre em contato com o administrador."

Scenario: Administrador cadastra um novo usuário
    Given que o usuário está logado como "Administrador"
    When navega até a tela de usuários - Perfil
    When o usuário clica no botão "Novo" para adicionar usuario
    When clica no dropdown de perfil
    When o usuário seleciona o perfil de administrador, escreve o nome e email
    When o usuário clica em "Salvar" para salvar o novo usuário
    Then navega até a tela de usuários - Perfil

Scenario: Usuário autenticado e associado ao perfil
    Given que o usuário foi cadastrado no sistema
    Then o usuário deve ser exibido na tela de usuários

Scenario: Administrador tenta cadastrar um usuário já existente
    Given que o usuário está logado como "Administrador"
    When navega até a tela de usuários - Perfil
    When clica no botão "Editar"
    When edita o tipo de perfil do usuário
    When edita o nome e email do usuário
    When clica em Salvar para salvar as alterações
    Then a notificação "Usuário já existe" deve ser exibida
    Then navega até a tela de usuários - Perfil

# Scenario: Falha na autenticação do Active Directory
#    Given que o serviço do Active Directory está indisponível
# 	When o usuário tenta fazer login no sistema
# 	Then o sistema deve exibir uma mensagem de erro
# 	And deve mostrar "Não foi possível autenticar, por favor, tente novamente mais tarde."