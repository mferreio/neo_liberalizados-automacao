Feature: Cadastro de Usuários com Perfil, Fonte e Submercado

    Scenario: Escolha de perfil durante o cadastro
        Given que o usuário está logado no sistema
        When eu devo ter acesso aos módulos de produtos
        When Usuário acessa o produto Diario Semanal na aba produtos
        When Usuário clica em cadastrar produto
	    When eu escolho o perfil "I50"
	    And as opções disponíveis de perfil devem incluir: CONV, I50, I0, I100 e CQI5


    Scenario: Escolha de fonte durante o cadastro
        Given que o usuário está logado no sistema
        When eu devo ter acesso aos módulos de produtos
        When Usuário acessa o produto Diario Semanal na aba produtos
        When Usuário clica em cadastrar produto
	#     When eu escolho a fonte "Eólica"
	#     Then a fonte selecionada deve ser "Eólica"
	#     And as opções disponíveis de fonte devem incluir: Eólica e Solar


    Scenario: Escolha de submercado durante o cadastro
       Given que o usuário está logado no sistema
        When eu devo ter acesso aos módulos de produtos
        When Usuário acessa o produto Diario Semanal na aba produtos
        When Usuário clica em cadastrar produto
	    When eu escolho o submercado "NE"
	    Then as opções disponíveis de submercado devem incluir: SE, NE, S e N


     Scenario: Tentativa de escolher um perfil inválido
        Given que o usuário está logado no sistema
        When eu devo ter acesso aos módulos de produtos
        When Usuário acessa o produto Diario Semanal na aba produtos
        When Usuário clica em cadastrar produto
	    When eu escolho o perfil "XXX"
	    And as opções disponíveis de perfil devem incluir: CONV, I50, I0, I100 e CQI5


    # Scenario: Tentativa de escolher uma fonte inválida
        Given que o usuário está logado no sistema
        When eu devo ter acesso aos módulos de produtos
        When Usuário acessa o produto Diario Semanal na aba produtos
        When Usuário clica em cadastrar produto
	#     When eu escolho a fonte "XXX"
	#     Then a fonte selecionada deve ser "Eólica"
	#     And as opções disponíveis de fonte devem incluir: Eólica e Solar


     Scenario: Tentativa de escolher um submercado inválido
        Given que o usuário está logado no sistema
        When eu devo ter acesso aos módulos de produtos
        When Usuário acessa o produto Diario Semanal na aba produtos
        When Usuário clica em cadastrar produto
	    When eu escolho o submercado "XXX"
	    Then as opções disponíveis de submercado devem incluir: SE, NE, S e N