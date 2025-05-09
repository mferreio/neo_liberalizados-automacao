Feature: Tela cadastro de diretrizes curto prazo

Scenario: Cadastro de um produto Curto Prazo com sucesso
    Given que o usuário está logado no sistema
    When o módulo "Produtos" está visível no menu lateral
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Curto Prazo"
    Then o usuário deve ser direcionado para a tela de visualização dos dados do módulo "Produtos Curto Prazo"
    When Usuário clica em novo produto
    When Usuário preenche os campos obrigatórios
    When Usuário clica em cadastrar produto
    Then eu devo conseguir criar dados


Scenario: Falha no cadastro de um produto Curto Prazo devido a dados inválidos
    Given que o usuário está logado no sistema
    When o módulo "Produtos" está visível no menu lateral
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Curto Prazo"
    Then o usuário deve ser direcionado para a tela de visualização dos dados do módulo "Produtos Curto Prazo"
    When Usuário clica em novo produto
    When o usuário preenche o campo perfil com "Incentivada 50%", o tipo com "Venda PLD", o período com "Fevereiro - 2024" e o volume em MWh com "-10"
    When Usuário clica em cadastrar produto
    Then eu devo conseguir criar dados


Scenario: Cadastro de um produto Curto Prazo sem preencher campos obrigatórios
    Given que o usuário está logado no sistema
    When o módulo "Produtos" está visível no menu lateral
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Curto Prazo"
    Then o usuário deve ser direcionado para a tela de visualização dos dados do módulo "Produtos Curto Prazo"
    When Usuário clica em novo produto
    When Usuário não preenche os campos obrigatórios
    When Usuário clica em cadastrar produto
    Then eu devo conseguir criar dados


Scenario: Cadastro com campos preenchidos parcialmente
    Given que o usuário está logado no sistema
    When o módulo "Produtos" está visível no menu lateral
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Curto Prazo"
    Then o usuário deve ser direcionado para a tela de visualização dos dados do módulo "Produtos Curto Prazo"
    When Usuário clica em novo produto
    When Usuário preenche parte dos campos obrigatórios
    When Usuário clica em cadastrar produto
    Then eu devo conseguir criar dados


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
