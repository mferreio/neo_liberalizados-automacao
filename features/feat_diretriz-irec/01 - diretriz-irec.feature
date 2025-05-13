Feature: Diretrizes I-REC

Scenario: Cadastro de uma nova diretriz I-REC
    Given que o usuário está logado no sistema
    When o usuário acessa ao módulo de diretrizes I-REC
    When o usuário clica no botão "Nova Diretriz"
    When que o usuário está na tela de cadastro de nova diretriz I-REC
    When o usuário informa os dados da nova diretriz I-REC
    When clica no botão Salvar
    Then o sistema exibe uma mensagem de sucesso
    When retorna para a tela de diretriz I-REC

Scenario: Tentativa de cadastrar múltiplas diretrizes vigentes
   Given que o usuário está na tela de diretriz I-REC
   When o usuário clica no botão "Nova Diretriz"
   When existe uma diretriz I-REC vigente no sistema
   When o usuário informa os dados da nova diretriz I-REC
   When clica no botão Salvar
   Then a nova diretriz deve invalidar a anterior
   When o sistema deve garantir que apenas uma diretriz esteja vigente
   When retorna para a tela de diretriz I-REC

Scenario: Mantendo diretrizes invalidas para histórico
    Given que uma diretriz I-REC foi invalidada
	When o usuário consulta as diretrizes cadastradas
	Then a diretriz invalidada deve estar disponível na base de dados para histórico
	When a informação sobre sua vigência deve estar acessível

Scenario: Visualização de diretrizes cadastradas
    Given que o usuário está na tela de diretriz I-REC
    Then todas as diretrizes cadastradas devem ser exibidas
 	When a diretriz vigente deve ser claramente identificável

Scenario: Anexação de arquivos durante o cadastro
    Given que o usuário está na tela de diretriz I-REC
    When o usuário clica no botão "Nova Diretriz"
    When que o usuário está na tela de cadastro de nova diretriz I-REC
    When o usuário preenche os campos obrigatórios
    When o usuário faz o upload de um arquivo de evidência "evidencia_imagem.jpg"
    Then o sistema deve validar que o arquivo "evidencia_imagem.jpg" foi anexado


Scenario: Exibição de data de vigência da diretriz
    Given que o usuário está na tela de diretriz I-REC
    When o usuário consulta as diretrizes cadastradas
 	Then sistema exibe a data de inicio e fim de vigência
 	When as datas devem estar formatadas corretamente
