Feature: Tela cadastro de produtos I-REC

Scenario: Cadastro de produto de diretriz I-REC com sucesso
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "IREC"
    When Usuário clica em novo produto
    When o usuário é direcionado para a tela de cadastros
    When Usuário preenche os campos obrigatórios
    When Usuário clica em cadastrar produto
    Then eu devo conseguir criar dados


Scenario: Cadastro de produto de diretriz I-REC sem preencher campos obrigatórios
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "IREC"
    When Usuário clica em novo produto
    When o usuário é direcionado para a tela de cadastros
    When Usuário não preenche os campos obrigatórios
    When Usuário clica em cadastrar produto
    Then eu devo conseguir criar dados


Scenario: Cadastro de produto de diretriz I-REC com falha no sistema
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "IREC"
    When Usuário clica em novo produto
    When o usuário é direcionado para a tela de cadastros
    When Usuário não preenche os campos obrigatórios
    When Usuário clica em cadastrar produto
#     When ocorre uma falha no sistema durante a persistência dos dados
#     Then uma notificação de falha deve ser exibida
#     When eu devo permanecer na tela de cadastro de produtos de diretriz I-REC
