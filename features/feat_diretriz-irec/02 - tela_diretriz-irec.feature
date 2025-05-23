@diretriz_irec
Feature: Tela de Diretriz I-REC

Scenario: Mensagem de ausência de diretrizes
    Given que o usuário está na tela de diretriz I-REC
	When não há diretrizes cadastradas no sistema
 	Then uma mensagem "Nenhuma diretriz cadastrada" deve ser exibida

Scenario: Navegação entre páginas de diretrizes
    Given que o usuário está na tela de diretriz I-REC
 	When há mais de uma página de diretrizes
 	When o usuário navega para a próxima página
 	Then as diretrizes da próxima página devem ser exibidas
 	When o usuário deve ser capaz de retornar à página anterior

Scenario: Limite de caracteres na busca por intervalo de data
    Given que o usuário está na tela de diretriz I-REC
 	When o usuário insere um intervalo de data inválido
 	Then sistema exibe mensagem de erro

Scenario: Anexação de arquivos durante o cadastro
    Given que o usuário está na tela de diretriz I-REC
    When o usuário clica no botão "Nova Diretriz"
    When que o usuário está na tela de cadastro de nova diretriz I-REC
    When o usuário preenche os campos obrigatórios
    When o usuário faz o upload de um arquivo de evidência "evidencia_imagem.jpg"
    Then o sistema deve validar que o arquivo "evidencia_imagem.jpg" foi anexado

Scenario: Visualização dos arquivos anexados
    Given que o usuário está na tela de diretriz I-REC
 	When o usuário abre o detalhamento de uma diretriz
 	Then o usuário valida que existem arquivos anexados

# O Cenário a seguir não é automatizavel
# Scenario: Acesso ao histórico de alterações da diretriz
#     Given que o usuário está na tela de diretriz I-REC
#     When o usuário abre o detalhamento de uma diretriz
#  	Then a tela deve exibir o histórico de alterações realizadas na diretriz, incluindo data e responsável

# O Cenário a seguir não é automatizavel
# Scenario: Filtragem adicional das diretrizes
#     Given que o usuário está na tela de diretriz I-REC
#  	When o usuário aplica um filtro adicional como categoria ou status
#  	Then apenas as diretrizes que correspondem ao filtro aplicado devem ser exibidas

Scenario: Validação de campos obrigatórios ao cadastrar nova diretriz
    Given que o usuário está na tela de diretriz I-REC
    When o usuário clica no botão "Nova Diretriz"
    When que o usuário está na tela de cadastro de nova diretriz I-REC
    When o usuário não preenche os campos obrigatórios
    When clica no botão Salvar
 	Then uma mensagem de erro deve ser exibida informando os campos que precisam ser preenchidos

# O Cenário a seguir não é automatizavel
# Scenario: Edição de uma diretriz existente
#     Given que o usuário está na tela de diretriz I-REC
#  	When o usuário selecionou uma diretriz existente
#  	When o usuário clica no botão de editar
#  	Then o usuário deve ser direcionado para a tela de edição da diretriz escolhida
