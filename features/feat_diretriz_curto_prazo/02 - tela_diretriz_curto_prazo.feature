Feature: Tela de Diretriz Curto Prazo

  Background:
    Given que o usuário está logado no sistema

  @tela_diretriz_curto_prazo

Scenario: Acesso ao menu de navegação para Diretriz Curto Prazo
    When o usuário acessa a aba "diretriz Curto Prazo"
	Then usuário é encaminhado para a tela de diretriz curto prazo
	When retorna para a tela de diretriz Curto Prazo


Scenario: Visualização das diretrizes cadastradas
    Given que o usuário está na tela de diretriz Curto Prazo
    Then todas as diretrizes cadastradas devem ser exibidas
 	When a diretriz vigente deve ser claramente identificável


Scenario: Paginação das diretrizes
    Given que o usuário está na tela de diretriz Curto Prazo
 	When há mais de uma página de diretrizes
 	When o usuário navega para a próxima página
 	Then as diretrizes da próxima página devem ser exibidas
 	When o usuário deve ser capaz de retornar à página anterior


Scenario: Busca por intervalo de data
    Given Que  o usuário está na tela de diretriz curto prazo
	When  o o usuário insere um intervalo de data para busca
	And clica no botão de busca
	Then apenas as diretrizes Que  estão dentro do intervalo de data devem ser exibidas


Scenario: Exibição dos detalhes da diretriz
    Given Que  o usuário está na tela de diretriz curto prazo
	When  o o usuário clica no botão para ver mais detalhes de uma diretriz
	Then todos os dados da diretriz escolhida devem ser exibidos
	And os arquivos anexados também devem ser acessíveis


Scenario: Adicionar nova diretriz
    When o usuário acessa a aba "diretriz Curto Prazo"
    When clica no botão Novo
    When o usuário preenche o campo Data Fim
    When o usuário preenche os campos obrigatórios
    When o usuário faz o upload de um arquivo de evidência "evidencia_imagem.jpg"
    When o sistema deve validar que o arquivo "evidencia_imagem.jpg" foi anexado
    When usuário clica em salvar
    Then o sistema exibe uma mensagem de sucesso
    When retorna para a tela de diretriz Curto Prazo
