Feature: Tela cadastro de produtos diaria/semanal

Scenario: Cadastro de produto com sucesso
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Semanal Diario"
    When Usuário clica em novo produto
    When o usuário é direcionado para a tela de cadastros
    When Usuário preenche os campos obrigatórios
    When Usuário clica em cadastrar produto
    Then eu devo conseguir criar dados


Scenario: Cadastro de produto sem preencher campos obrigatórios
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Semanal Diario"
    When Usuário clica em novo produto
    When o usuário é direcionado para a tela de cadastros
    When Usuário preenche os campos obrigatórios com dados inválidos
    When Usuário clica em cadastrar produto
    Then eu devo conseguir criar dados


# Scenario: Cadastro de produto com falha no sistema
#     Given que eu estou na tela de cadastro de produtos
#     When eu preencho todos os campos corretamente
#     When eu clico no botão salvar
#     When ocorre uma falha no sistema durante a persistência dos dados
#     Then uma notificação de falha deve ser exibida
#     When eu devo permanecer na tela de cadastro de produtos


 Scenario: Cadastro de produto com diretriz diária
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Semanal Diario"
    When Usuário clica em novo produto
    When o usuário é direcionado para a tela de cadastros
    When Usuário preenche os campos obrigatórios
    When Usuário clica em cadastrar produto
    Then eu devo conseguir criar dados
