Feature: Tela cadastro de produtos I-REC

Scenario: Cadastro de produto de diretriz I-REC com sucesso
    Given que eu estou na tela de cadastro de produtos de diretriz I-REC
    When eu preencho o campo período com "2024"
    When eu preencho o campo fonte com "Fonte A"
    When eu clico no botão salvar
    Then os dados do produto devem ser persistidos no sistema
    When uma notificação de sucesso deve ser exibida
    When eu devo ser direcionado para a tela de produtos


Scenario: Cadastro de produto de diretriz I-REC sem preencher campos obrigatórios
    Given que eu estou na tela de cadastro de produtos de diretriz I-REC
    When eu deixo o campo período vazio
    When eu clico no botão salvar
    Then uma notificação de erro deve ser exibida
    When eu devo permanecer na tela de cadastro de produtos de diretriz I-REC


Scenario: Cadastro de produto de diretriz I-REC com falha no sistema
    Given que eu estou na tela de cadastro de produtos de diretriz I-REC
    When eu preencho todos os campos corretamente
    When eu clico no botão salvar
    When ocorre uma falha no sistema durante a persistência dos dados
    Then uma notificação de falha deve ser exibida
    When eu devo permanecer na tela de cadastro de produtos de diretriz I-REC
