# Feature: Tela cadastro de produtos diaria/semanal

# Scenario: Cadastro de produto com sucesso
#     Given que eu estou na tela de cadastro de produtos
#     When eu preencho o campo nome do produto com "Produto A"
#     When eu preencho o campo período com "01/01/2024 a 07/01/2024"
#     When eu preencho o campo perfil com "Perfil X"
#     When eu preencho o campo submercado com "Submercado Y"
#     When eu escolho o tipo de diretriz como "semanal"
#     When eu clico no botão salvar
#     Then os dados do produto devem ser persistidos no sistema
#     When uma notificação de sucesso deve ser exibida
#     When eu devo ser direcionado para a tela de produtos


# Scenario: Cadastro de produto sem preencher campos obrigatórios
#     Given que eu estou na tela de cadastro de produtos
#     When eu deixo o campo nome do produto vazio
#     When eu clico no botão salvar
#     Then uma notificação de erro deve ser exibida
#     When eu devo permanecer na tela de cadastro de produtos


# Scenario: Cadastro de produto com falha no sistema
#     Given que eu estou na tela de cadastro de produtos
#     When eu preencho todos os campos corretamente
#     When eu clico no botão salvar
#     When ocorre uma falha no sistema durante a persistência dos dados
#     Then uma notificação de falha deve ser exibida
#     When eu devo permanecer na tela de cadastro de produtos


# Scenario: Cadastro de produto com diretriz diária
#     Given que eu estou na tela de cadastro de produtos
#     When eu preencho o campo nome do produto com "Produto B"
#     When eu preencho o campo período com "01/01/2024 a 01/01/2024"
#     When eu preencho o campo perfil com "Perfil Z"
#     When eu preencho o campo submercado com "Submercado W"
#     When eu escolho o tipo de diretriz como "diária"
#     When eu clico no botão salvar
#     Then os dados do produto devem ser persistidos no sistema
#     When uma notificação de sucesso deve ser exibida
#     When eu devo ser direcionado para a tela de produtos
