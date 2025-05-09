Feature: Tela de Produtos

Scenario: Visualização de produtos cadastrados para diretrizes diárias e semanais
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Semanal Diario"
    Then exibe os produtos com perfil, submercado e tipo de diretriz


Scenario: Visualização de produtos cadastrados para diretrizes I-REC
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "IREC"
    Then exibe os produtos com perfil, submercado e tipo de diretriz


Scenario: Visualização de produtos cadastrados para diretrizes de curto prazo
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Curto Prazo"
    Then exibe os produtos com perfil, submercado e tipo de diretriz


Scenario: Adição de um novo produto para diretrizes diárias e semanais
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Semanal Diario"
    When Usuário clica em novo produto
    When o usuário é direcionado para a tela de cadastros
    When Usuário preenche os campos obrigatórios
    When Usuário clica em cadastrar produto
    Then eu devo conseguir criar dados


Scenario: Adição de um novo produto para diretrizes I-REC
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "IREC"
    When Usuário clica em novo produto
    When o usuário é direcionado para a tela de cadastros
    When Usuário preenche os campos obrigatórios
    When Usuário clica em cadastrar produto
    Then eu devo conseguir criar dados

Scenario: Adição de um novo produto para diretrizes de curto prazo
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Curto Prazo"
    When Usuário clica em novo produto
    When o usuário é direcionado para a tela de cadastros
    When Usuário preenche os campos obrigatórios
    When Usuário clica em cadastrar produto
    Then eu devo conseguir criar dados

Scenario: Edição de um produto já cadastrado
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Semanal Diario"
    When Usuário pesquisa pelo ano
    When Usuário seleciona o produto
    When Usuário clica no botão editar
    Then o sistema exibe a pagina de edição do produto
    When usuário retorna a tela inicial

Scenario: Atualização da exibição após edição de um produto
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Semanal Diario"
    Then exibe os produtos com perfil, submercado e tipo de diretriz atualizados

Scenario: Inativação de um produto
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Semanal Diario"
    When o usuário marcar o checkbox de inativação de um produto e clica em sim
    Then o sistema exibe uma mensagem de produto inativado com sucesso

Scenario: Visualização da lista de produtos após inativação
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Semanal Diario"
    Then o usuário consegue visualizar os produtos inativos

Scenario: Verificação da disponibilidade de produtos inativos
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Semanal Diario"
    When o usuário tiver um produto inativo
    Then esse produto deve ser exibido na lista de produtos

Scenario: Exclusão de um produto
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Semanal Diario"
    When Usuário pesquisa pelo ano
    When Usuário seleciona o produto
    When Usuário clica no botão excluir
    When eu devo acessar a tela para excluir um produto
    When Usuário confirma exclusão de produto cadastrado
    Then Sistema exibe mensagem de produto excluido com sucesso


Scenario: Tentativa de exclusão sem confirmação
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Semanal Diario"
    When Usuário pesquisa pelo ano
    When Usuário seleciona o produto
    When Usuário clica no botão excluir
    When eu devo acessar a tela para excluir um produto
    When Usuário não confirma exclusão de produto cadastrado
    Then Sistema retorna a página de produtos


Scenario: Visualização correta do submercado
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Semanal Diario"
    When consultar os produtos cadastrados
    When o usuário visualizar um produto com diretriz diária e semanal
    Then o submercado associado ao produto deve ser exibido corretamente na lista


Scenario: Adição de produto com dados válidos
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Semanal Diario"
    When Usuário clica em novo produto
    When o usuário é direcionado para a tela de cadastros
    When Usuário preenche os campos obrigatórios com dados inválidos
    When Usuário clica em cadastrar produto
    Then eu devo conseguir criar dados

Scenario: Navegação de volta após adicionar um novo produto
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Semanal Diario"
    Then o novo produto deve estar visível na lista de produtos


Scenario: Erro na adição de um produto
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Semanal Diario"
    When Usuário clica em novo produto
    When o usuário é direcionado para a tela de cadastros
    When Usuário não preenche os campos obrigatórios
    When Usuário clica em cadastrar produto
    Then uma mensagem de erro deve ser exibida, informando que todos os campos obrigatórios devem ser preenchidos


Scenario: Verificação da navegação entre telas
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Semanal Diario"
    When Usuário clica em novo produto
    When o usuário é direcionado para a tela de cadastros
    When o usuário clica em voltar
    Then o usuário deve ser redirecionado para a tela de produtos
    When Usuário clica no botão editar
    Then o sistema exibe a pagina de edição do produto


Scenario: Exibição de detalhes de produtos inativos
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Semanal Diario"
    When o usuário consulta um produto inativo
    Then todos os detalhes do produto inativo devem ser exibidos na tela


Scenario: Acesso à funcionalidade de edição sem selecionar um produto
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Semanal Diario"
    When o usuário clicar no botão de editar sem selecionar um produto
    When uma mensagem de erro deve ser exibida, informWheno que é necessário selecionar um produto para edição
    Then o usuário não deve ser redirecionado para a tela de edição


Scenario: Atualização de status em produtos
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Semanal Diario"
    When o usuário ativar um produto anteriormente inativo
    When exibe os produtos com perfil, submercado e tipo de diretriz
    Then o produto deve ser exibido como ativo na lista de produtos


Scenario: Visualização de mensagens de erro em campos obrigatórios
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Semanal Diario"
    When Usuário clica em novo produto
    When o usuário é direcionado para a tela de cadastros
    When Usuário preenche os campos obrigatórios com dados inválidos
    Then uma mensagem de erro deve ser exibida


Scenario: Confirmação visual ao excluir um produto
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Semanal Diario"
    When Usuário pesquisa pelo ano
    When Usuário seleciona o produto
    When Usuário clica no botão excluir
    When eu devo acessar a tela para excluir um produto
    When Usuário confirma exclusão de produto cadastrado
    Then Sistema exibe mensagem de produto excluido com sucesso


Scenario: Efeito de filtro na tela de produtos
    Given que o usuário está logado no sistema
    When o usuário seleciona o módulo "Produtos"
    When o usuário seleciona o módulo "Semanal Diario"
    When Usuário pesquisa pelo ano
    Then o sistema exibe apenas os produtos correspondentes ao filtro aplicado
