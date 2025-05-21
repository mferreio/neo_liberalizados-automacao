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
    When clica no botão Novo
    When o usuário preenche o campo Data Fim
    When o usuário preenche os campos obrigatórios
    When o usuário faz o upload de um arquivo de evidência "evidencia_imagem.jpg"
    When o sistema deve validar que o arquivo "evidencia_imagem.jpg" foi anexado
    When usuário clica em salvar
    Then o sistema exibe uma mensagem de sucesso
    When retorna para a tela de diretriz Curto Prazo


Scenario: Preenchimento de preços dos produtos cadastrados
    When clica no botão Novo
    When o usuário preenche o campo Data Fim
    When o usuário preenche os campos obrigatórios
    When o usuário faz o upload de um arquivo de evidência "evidencia_imagem.jpg"
    When o sistema deve validar que o arquivo "evidencia_imagem.jpg" foi anexado
    When usuário clica em salvar
    Then o sistema exibe uma mensagem de sucesso
    When retorna para a tela de diretriz Curto Prazo


Scenario: Anexação de arquivos de evidência
	When clica no botão Novo
    When o usuário preenche o campo Data Fim
    When o usuário preenche os campos obrigatórios
    When o usuário faz o upload de um arquivo de evidência "evidencia_imagem.jpg"
    When o sistema deve validar que o arquivo "evidencia_imagem.jpg" foi anexado
    When usuário clica em salvar
    Then o sistema exibe uma mensagem de sucesso
    When retorna para a tela de diretriz Curto Prazo


Scenario: Salvar diretriz curto prazo com sucesso
    When clica no botão Novo
    When o usuário preenche o campo Data Fim
    When o usuário preenche os campos obrigatórios
    When o usuário faz o upload de um arquivo de evidência "evidencia_imagem.jpg"
    When o sistema deve validar que o arquivo "evidencia_imagem.jpg" foi anexado
    When usuário clica em salvar
    Then o sistema exibe uma mensagem de sucesso
    When retorna para a tela de diretriz Curto Prazo


# Scenario: Falha ao salvar diretriz curto prazo
#   Given Que  o usuário preencheu os campos incorretamente
# 	When  o o usuário clica no botão "Salvar"
# 	Then uma notificação de falha é exibida
# 	And os dados não são persistidos na base de dados
# 	And o usuário permanece na tela de cadastro de diretriz curto prazo


Scenario: Tentativa de salvar diretriz sem preencher todos os campos
    When clica no botão Novo
    When o usuário preenche o campo Data Fim
    When o usuário não preenche os campos obrigatórios
    When o usuário faz o upload de um arquivo de evidência "evidencia_imagem.jpg"
    When o sistema deve validar que o arquivo "evidencia_imagem.jpg" foi anexado
    When usuário clica em salvar
    Then o sistema exibe uma mensagem de sucesso
    When retorna para a tela de diretriz Curto Prazo


Scenario: Validação de formato de data
    When clica no botão Novo
    When o usuário preenche o campo Data Fim
    When o usuário preenche os campos obrigatórios com data inválida
	Then uma mensagem de erro é exibida

Scenario: Limitação no tamanho dos arquivos anexados
    When o usuário acessa a aba "diretriz Curto Prazo"
    When clica no botão Novo
    When o usuário preenche o campo Data Fim
    When o usuário preenche os campos obrigatórios
    When o usuário faz o upload de um arquivo de evidência "limitedetamanho.pdf"
    Then o sistema deve exibir uma mensagem de limite de tamanho


Scenario: Exibição de diretriz cadastrada após o salvamento
	When o usuário acessa a aba "diretriz Curto Prazo"
    Then todas as diretrizes cadastradas devem ser exibidas
 	When a diretriz vigente deve ser claramente identificável

Scenario: Cancelamento do cadastro de diretriz curto prazo
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



Scenario: Verificação da lista de produtos cadastrados
    Given o usuário clica no botão "Nova Diretriz"
 	Then todos os produtos cadastrados devem estar visíveis
    When retorna para a tela de diretriz I-REC


Scenario: Visualização de mensagens de notificação após ação
    When o usuário acessa a aba "diretriz Curto Prazo"
    When clica no botão Novo
    When o usuário preenche o campo Data Fim
    When o usuário preenche os campos obrigatórios
    When o usuário faz o upload de um arquivo de evidência "evidencia_imagem.jpg"
    When usuário clica em salvar
    Then o sistema exibe uma mensagem de sucesso
	When deve exibir a mensagem "Arquivo enviado com sucesso"
    When retorna para a tela de diretriz Curto Prazo
