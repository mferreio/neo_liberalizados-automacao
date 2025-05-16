Feature: Aplicação Base - Tela de usuários
  Como administrador
  Quero acessar a aplicação com permissões específicas
  Para realizar operações de acordo com meu perfil


Scenario: O menu lateral deve estar presente na página
    Given que o usuário está logado no sistema
    When o usuário acessa a tela principal da aplicação
    Then ele deve visualizar o menu lateral na posição esquerda da tela

Scenario: O usuário seleciona o modulo Produtos Semanal Diario do menu lateral
    Given que o usuário está logado no sistema
    When o módulo "Produtos" está visível no menu lateral
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Semanal Diario"
    Then o usuário deve ser direcionado para a tela de visualização dos dados do módulo "Produtos Semanal Diario"
    When retorna a pagina inicial

Scenario: O usuário seleciona o modulo Produtos IREC do menu lateral
    Given que o usuário está logado no sistema
    When o módulo "Produtos" está visível no menu lateral
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "IREC"
    Then o usuário deve ser direcionado para a tela de visualização dos dados do módulo "Produtos IREC"
    When retorna a pagina inicial

Scenario: O usuário seleciona o modulo Produtos Curto Prazo do menu lateral
    Given que o usuário está logado no sistema
    When o módulo "Produtos" está visível no menu lateral
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Curto Prazo"
    Then o usuário deve ser direcionado para a tela de visualização dos dados do módulo "Produtos Curto Prazo"
    When retorna a pagina inicial

Scenario: O usuário visualiza dados já cadastrados no módulo
    Given que o usuário está logado no sistema
    When o módulo "Produtos" está visível no menu lateral
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Curto Prazo"
    Then ele deve ver uma lista de todos os itens cadastrados
    When retorna a pagina inicial

Scenario: O usuário acessa o botão para adicionar um novo item
    Given que o usuário está logado no sistema
    When o módulo "Produtos" está visível no menu lateral
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Curto Prazo"
    When o usuário clica em "Adicionar Novo Item"
    Then deve ser direcionado para um formulário para registrar um novo item

# Scenario: O usuário só vê módulos aos quais tem acesso
#     Given que o usuário tem um perfil que não permite o acesso ao módulo "Relatório de Vendas"
#     When o usuário acessa a tela principal da aplicação
#     Then ele não deve visualizar o módulo "Relatório de Vendas" no menu lateral

# Scenario: O usuário Não pode ver botões se tiver permissão Administrador
#     Given que o usuário tem perfil de "Administrador"
#     When o usuário acessa a tela de visualização do módulo "Produtos"
#     Then ele deve ver apenas o botão "Administrador" e não deve ver o botão "Adicionar Novo Item"

# Scenario: O usuário pode ver botões apenas se tiver permissão Trading/Portifólio
#     Given que o usuário tem perfil de "Trading/Portifólio"
#     When o usuário acessa a tela de visualização do módulo "Produtos"
#     Then ele deve ver apenas o botão "Trading/Portifólio" e deve ver o botão "Adicionar Novo Item"

