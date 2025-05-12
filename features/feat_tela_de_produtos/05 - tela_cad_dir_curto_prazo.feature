Feature: Tela cadastro de diretrizes curto prazo

Scenario: Cadastro de um produto com sucesso
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Curto Prazo"
    When Usuário clica em novo produto
    When o usuário é direcionado para a tela de cadastros
    When Usuário preenche os campos obrigatórios
    When Usuário clica em cadastrar produto
    Then eu devo conseguir criar dados


# Scenario: Falha no cadastro devido a dados inválidos
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Curto Prazo"
    When Usuário clica em novo produto
    When o usuário é direcionado para a tela de cadastros
    When Usuário preenche os campos obrigatórios com dados inválidos
    When Usuário clica em cadastrar produto
    Then eu devo conseguir criar dados


 Scenario: Cadastro sem preenchimento de campos obrigatórios
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Curto Prazo"
    When Usuário clica em novo produto
    When o usuário é direcionado para a tela de cadastros
    When Usuário não preenche os campos obrigatórios
    When Usuário clica em cadastrar produto
    Then eu devo conseguir criar dados


Scenario: Cadastro com campos preenchidos parcialmente
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Curto Prazo"
    When Usuário clica em novo produto
    When o usuário é direcionado para a tela de cadastros
    When Usuário preenche parcialmente os campos obrigatórios
    When Usuário clica em cadastrar produto
    Then eu devo conseguir criar dados
    Then os dados não devem ser persistidos
    When uma notificação de erro deve ser exibida informWheno que todos os campos devem ser preenchidos


 Scenario: Direcionamento após cadastro com sucesso
    Given que o usuário está logado no sistema
    When o módulo "Produtos" está visível no menu lateral
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Curto Prazo"
    Then o usuário deve ser direcionado para a tela de visualização dos dados do módulo "Produtos Curto Prazo"
    When Usuário clica em novo produto
    When Usuário preenche os campos obrigatórios
    When Usuário clica em cadastrar produto
    Then o usuário deve ser direcionado para a tela de visualização dos dados do módulo "Produtos Curto Prazo"
