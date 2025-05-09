# Feature: Tela cadastro de diretrizes curto prazo

# Scenario: Cadastro de um produto com sucesso
#     Given que o usuário está na tela de cadastro de produtos de diretriz curto prazo
#     When o usuário preenche o campo perfil com "Convencional", o tipo com "Compra PLD", o período com "Janeiro - 2024" e o volume em MWh com "100"
#     When o usuário seleciona a opção de salvar
#     Then os dados devem ser persistidos
#     When uma notificação de sucesso deve ser exibida
#     When o usuário deve ser direcionado à tela de produtos


# Scenario: Falha no cadastro devido a dados inválidos
#     Given que o usuário está na tela de cadastro de produtos de diretriz curto prazo
#     When o usuário preenche o campo perfil com "Incentivada 50%", o tipo com "Venda PLD", o período com "Fevereiro - 2024" e o volume em MWh com "-10"
#     When o usuário seleciona a opção de salvar
#     Then os dados não devem ser persistidos
#     When uma notificação de erro deve ser exibida


# Scenario: Cadastro sem preenchimento de campos obrigatórios
#     Given que o usuário está na tela de cadastro de produtos de diretriz curto prazo
#     When o usuário não preenche nenhum campo do formulário
#     When o usuário seleciona a opção de salvar
#     Then os dados não devem ser persistidos
#     When uma notificação de erro deve ser exibida informWheno sobre campos obrigatórios


# Scenario: Cadastro com campos preenchidos parcialmente
#     Given que o usuário está na tela de cadastro de produtos de diretriz curto prazo
#     When o usuário preenche o campo perfil com "Convencional" e o volume em MWh com "50"
#     When o usuário seleciona a opção de salvar
#     Then os dados não devem ser persistidos
#     When uma notificação de erro deve ser exibida informWheno que todos os campos devem ser preenchidos


# Scenario: Direcionamento após cadastro com sucesso
#     Given que o usuário acabou de cadastrar um produto com sucesso
#     When a notificação de sucesso é exibida
#     Then o usuário deve ser direcionado automaticamente à tela de produtos
