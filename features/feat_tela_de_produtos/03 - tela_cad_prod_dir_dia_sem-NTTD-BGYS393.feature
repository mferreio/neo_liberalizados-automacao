Feature: Tela cadastro de produtos diaria/semanal

Scenario: Cadastro de produto com sucesso
    Given que o usuário está logado no sistema
    When eu devo ter acesso aos módulos de produtos
    When Usuário acessa o produto Diario Semanal na aba produtos
    When Usuário clica em novo produto
    When Usuário preenche os campos obrigatórios
    When Usuário clica em cadastrar produto
    Then eu devo conseguir criar dados


Scenario: Cadastro de produto com sucesso
    Given que o usuário está logado no sistema
    When eu devo ter acesso aos módulos de produtos
    When Usuário acessa o produto Diario Semanal na aba produtos
    When Usuário clica em novo produto
    When Usuário não preenche os campos obrigatórios
    When Usuário clica em cadastrar produto
    Then eu devo conseguir criar dados


Scenario: Cadastro de produto com falha no sistema
    Given que o usuário está logado no sistema
    When eu devo ter acesso aos módulos de produtos
    When Usuário acessa o produto Diario Semanal na aba produtos
    When Usuário clica em novo produto
    When Usuário preenche os campos obrigatórios
    When Usuário clica em cadastrar produto
    When ocorre uma falha no sistema durante a persistência dos dados
    Then uma notificação de falha deve ser exibida
    When eu devo permanecer na tela de cadastro de produtos


Scenario: Cadastro de produto com diretriz diária
    Given que o usuário está logado no sistema
    When eu devo ter acesso aos módulos de produtos
    When Usuário acessa o produto Diario Semanal na aba produtos
    When Usuário clica em novo produto
    When Usuário preenche os campos obrigatórios
    When Usuário clica em cadastrar produto
    Then eu devo conseguir criar dados
