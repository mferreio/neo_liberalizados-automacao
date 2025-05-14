Feature: Tela de cadastro de Diretriz Curto Prazo

  Background:
    Given que o usuário está logado no sistema

  @tela_cadastro_diretriz_curto_prazo

Scenario: Acesso à tela de cadastro de diretriz curto prazo
    When o usuário acessa a aba "diretriz Curto Prazo"
    When o usuário clica no botão "Nova Diretriz"
 	Then o usuário deve ser direcionado para a tela de cadastro de diretriz Curto Prazo
    When retorna para a tela de diretriz Curto Prazo


Scenario: Inserção de data de início da vigência
    Given Que  o usuário está na tela de cadastro de diretriz curto prazo
	When  o o usuário insere uma data de início da vigência "01/01/2023"
	Then a data de início da vigência é válida
	And a data de início da vigência não pode ser menor Que  a data atual


Scenario: Preenchimento de preços dos produtos cadastrados
    Given Que  o usuário está na tela de cadastro de diretriz curto prazo
	And existem produtos cadastrados para diretrizes de curto prazo
	When  o o usuário insere os preços dos produtos
	Then os preços são armazenados corretamente para os produtos correspondentes


Scenario: Anexação de arquivos de evidência
    Given Que  o usuário está na tela de cadastro de diretriz curto prazo
	When  o o usuário anexa arquivos de evidência para a precificação
	Then os arquivos são recebidos e podem ser visualizados


Scenario: Salvar diretriz curto prazo com sucesso
    Given Que  o usuário preencheu todos os campos necessários
	When  o o usuário clica no botão "Salvar"
	Then os dados da diretriz são persistidos na base de dados
	And o usuário é redirecionado para a tela de diretriz curto prazo
	And uma notificação de sucesso é exibida


Scenario: Falha ao salvar diretriz curto prazo
    Given Que  o usuário preencheu os campos incorretamente
	When  o o usuário clica no botão "Salvar"
	Then uma notificação de falha é exibida
	And os dados não são persistidos na base de dados
	And o usuário permanece na tela de cadastro de diretriz curto prazo


Scenario: Tentativa de salvar diretriz sem preencher todos os campos
    Given Que  o usuário está na tela de cadastro de diretriz curto prazo
	When  o o usuário tenta clicar no botão "Salvar" sem preencher todos os campos obrigatórios
	Then uma notificação de erro é exibida
	And o usuário é informado sobre quais campos precisam ser preenchidos


Scenario: Validação de formato de data
    Given Que  o usuário está na tela de cadastro de diretriz curto prazo
	When  o o usuário insere uma data de início da vigência com formato inválido "31-02-2023"
	Then uma mensagem de erro é exibida indicEo Que  o formato da data é inválido
	And o usuário deve corrigir a data antes de prosseguir


Scenario: Limitação no tamanho dos arquivos anexados
    Given Que  o usuário está na tela de cadastro de diretriz curto prazo
	When  o o usuário tenta anexar um arquivo Que  excede o limite de tamanho
	Then uma notificação de erro é exibida
	And o arquivo não é anexado com sucesso


Scenario: Exibição de diretriz cadastrada após o salvamento
    Given Que  uma diretriz foi cadastrada com sucesso
	When  o o usuário é redirecionado para a tela de diretriz curto prazo
	Then a nova diretriz é exibida na lista de diretrizes cadastradas
	And os dados da diretriz, incluindo a data de início da vigência e os preços dos produtos, estão corretos


Scenario: Cancelamento do cadastro de diretriz curto prazo
    Given Que  o usuário está na tela de cadastro de diretriz curto prazo
	When  o o usuário clica no botão "Cancelar"
	Then o usuário é redirecionado para a tela de diretriz curto prazo
	And nenhuma diretriz é cadastrada


Scenario: Verificação da lista de produtos cadastrados
    Given Que  o usuário está na tela de cadastro de diretriz curto prazo
	When  o o usuário observa a lista de produtos cadastrados
	Then todos os produtos devem estar visíveis
	And deve haver um campo para inserir o preço ao lado de cada produto


Scenario: Visualização de mensagens de notificação após ação
    Given Que  o usuário executou uma ação Que  pode gerar uma notificação
	When  o a ação é concluída, seja com sucesso ou falha
	Then uma mensagem de notificação apropriada é exibida para o usuário
	And a mensagem deve ser clara sobre o resultado da ação realizada
