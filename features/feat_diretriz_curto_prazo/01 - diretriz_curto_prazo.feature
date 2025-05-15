Feature: diretriz de curto prazo

  Background:
    Given que o usuário está logado no sistema

  @diretriz_curto_prazo

Scenario: Cadastro de uma nova diretriz de curto prazo
    When o usuário acessa a aba "diretriz Curto Prazo"
    When clica no botão Novo
    When o usuário preenche o campo Data Fim
    When o usuário preenche os campos obrigatórios
    When o usuário faz o upload de um arquivo de evidência "evidencia_imagem.jpg"
    When o sistema deve validar que o arquivo "evidencia_imagem.jpg" foi anexado
    When usuário clica em salvar
    Then o sistema exibe uma mensagem de sucesso
    When retorna para a tela de diretriz Curto Prazo


Scenario: Validação de vigência única da diretriz
    When o usuário acessa a aba "diretriz Curto Prazo"
    When clica no botão Novo
    When o usuário preenche o campo Data Fim
    When o usuário preenche os campos obrigatórios
    When clica no botão Salvar
    Then a nova diretriz deve invalidar a anterior
    When o sistema deve garantir que apenas uma diretriz esteja vigente
    When retorna para a tela de diretriz Curto Prazo


Scenario: Armazenamento de diretrizes invalidadas para histórico
    Given que uma diretriz Curto Prazo foi invalidada
	When o usuário consulta as diretrizes cadastradas
	Then a diretriz invalidada deve estar disponível na base de dados para histórico
	When a informação sobre sua vigência deve estar acessível


Scenario: Exibição de data de vigência da diretriz de curto prazo
    Given o usuário acessa a aba "diretriz Curto Prazo"
    When o usuário consulta as diretrizes cadastradas
 	Then sistema exibe a data de inicio e fim de vigência
 	When as datas devem estar formatadas corretamente


#Scenario: Edição de preço de produto na diretriz de curto prazo //adicionar informação de edição de preço
    When o usuário acessa a aba "diretriz Curto Prazo"
    When clica no botão Novo
    When o usuário preenche o campo Data Fim
    When o usuário preenche os campos obrigatórios
    When o usuário faz o upload de um arquivo de evidência "evidencia_imagem.jpg"
    When o sistema deve validar que o arquivo "evidencia_imagem.jpg" foi anexado
    When usuário clica em salvar
    Then o sistema exibe uma mensagem de sucesso
    When retorna para a tela de diretriz Curto Prazo


Scenario: Envio de arquivos anexados na diretriz de curto prazo
    When o usuário acessa a aba "diretriz Curto Prazo"
    When clica no botão Novo
    When o usuário preenche o campo Data Fim
    When o usuário preenche os campos obrigatórios
    When o usuário faz o upload de um arquivo de evidência "evidencia_imagem.jpg"
    When o sistema deve validar que o arquivo "evidencia_imagem.jpg" foi anexado
    When usuário clica em salvar
    Then deve exibir a mensagem "Arquivo enviado com sucesso"
    When o sistema exibe uma mensagem de sucesso
    When retorna para a tela de diretriz Curto Prazo


#Scenario: Cancelamento do cadastro de nova diretriz de curto prazo // não é exibido um modal para confirmar o cancelamento
    When o usuário acessa a aba "diretriz Curto Prazo"
    When clica no botão Novo
    When o usuário preenche o campo Data Fim
    When o usuário preenche os campos obrigatórios
    When o usuário faz o upload de um arquivo de evidência "evidencia_imagem.jpg"
    When o sistema deve validar que o arquivo "evidencia_imagem.jpg" foi anexado
    When usuário clica em salvar
    # When deve exibir um modal para confirmar ou cancelar o cadastro
    # When o usuário clica em "Cancelar"
    # Then o sistema deve retornar para a tela de diretriz Curto Prazo
    # When nenhuma diretriz é cadastrada