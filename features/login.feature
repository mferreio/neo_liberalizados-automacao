Feature: Testar o login no site da Neoenergia

  Scenario: Verificar o login com sucesso
    Given que eu acesso a página de login
    When eu clico no botão Entrar
    When eu insiro o email de usuario
    When eu clico no botão Seguinte
    When eu preencho o ADFS com usuário e senha
    Then eu verifico que o usuário acessou o sistema
