Feature: Tela de Cadastro de Diretriz I-REC

Scenario: Acesso à tela de cadastro de nova diretriz
    Given que o usuário está logado no sistema
    When o usuário acessa ao módulo de diretrizes I-REC
    When o usuário clica no botão "Nova Diretriz"
 	Then o usuário deve ser direcionado para a tela de cadastro de diretriz I-REC
    When retorna para a tela de diretriz I-REC

Scenario: Exibição dos produtos cadastrados na tela de cadastro
    Given o usuário clica no botão "Nova Diretriz"
 	Then o usuário deve ser direcionado para a tela de cadastro de diretriz I-REC
 	Then todos os produtos cadastrados devem estar visíveis
    When retorna para a tela de diretriz I-REC

Scenario: Data de início da vigência válida
    Given o usuário clica no botão "Nova Diretriz"
 	Then o usuário deve ser direcionado para a tela de cadastro de diretriz I-REC
 	Then valida se a data de inicio da vigência é igual a data atual
    When retorna para a tela de diretriz I-REC

Scenario: Anexação de arquivos durante o cadastro
    Given que o usuário está na tela de diretriz I-REC
    When o usuário clica no botão "Nova Diretriz"
    When que o usuário está na tela de cadastro de nova diretriz I-REC
    When o usuário preenche os campos obrigatórios
    When o usuário faz o upload de um arquivo de evidência "evidencia_imagem.jpg"
    Then o sistema deve validar que o arquivo "evidencia_imagem.jpg" foi anexado

Scenario: Salvar nova diretriz com sucesso
    Given que o usuário está logado no sistema
    When o usuário acessa ao módulo de diretrizes I-REC
    When o usuário clica no botão "Nova Diretriz"
    When que o usuário está na tela de cadastro de nova diretriz I-REC
    When o usuário informa os dados da nova diretriz I-REC
    When clica no botão Salvar
    Then o sistema exibe uma mensagem de sucesso
    When retorna para a tela de diretriz I-REC

# Scenario: Salvar nova diretriz com falha
#   Given que o usuário preencheu os campos obrigatórios, mas ocorreu um erro ao salvar
# 	When o usuário clica no botão "Salvar"
# 	Then uma notificação de falha deve ser exibida
# 	When o usuário deve permanecer na tela de cadastro de diretriz I-REC

# Scenario: Campo de preço obrigatório
    Given que o usuário está na tela de diretriz I-REC
    When o usuário clica no botão "Nova Diretriz"
    When que o usuário está na tela de cadastro de nova diretriz I-REC
    When o usuário não preenche os campos de preço obrigatório
    When clica no botão Salvar
 	Then uma mensagem de erro deve ser exibida informando os campos que precisam ser preenchidos

# Scenario: Edição de preço de produto
# Given que o usuário está na tela de cadastro de diretriz I-REC
# 	When o usuário altera o preço de um dos produtos
# 	When clica no botão "Salvar"
# 	Then o novo preço deve ser persistido na base de dados
# 	When o usuário deve ser notificado sobre a atualização bem-sucedida

Scenario: Limite de anexos
    Given que o usuário está na tela de diretriz I-REC
    When o usuário clica no botão "Nova Diretriz"
    When que o usuário está na tela de cadastro de nova diretriz I-REC
    When o usuário preenche os campos obrigatórios
    When o usuário faz o upload de um arquivo de evidência "evidencia_imagem.jpg"
    When o usuário faz o upload de um arquivo de evidência "evidencia_texto.txt"

# Scenario: Validação de formato de arquivos anexados
#   Given que o usuário está na tela de cadastro de diretriz I-REC
# 	When o usuário tenta anexar um arquivo em um formato inválido
# 	Then uma mensagem de erro deve ser exibida informando que o formato do arquivo não é suportado
# 	When o arquivo não deve ser anexado

# Scenario: Cancelamento do cadastro de nova diretriz // não é exibido um modal para confirmar o cancelamento
    Given que o usuário está logado no sistema
    When o usuário acessa ao módulo de diretrizes I-REC
    When o usuário clica no botão "Nova Diretriz"
    When que o usuário está na tela de cadastro de nova diretriz I-REC
    When o usuário preenche os campos obrigatórios
    When clica no botão Salvar
    When deve exibir um modal para confirmar ou cancelar o cadastro
    When o usuário clica em "Cancelar"
    Then o sistema deve retornar para a tela de diretriz Curto Prazo
    When nenhuma diretriz é cadastrada

# Não é possivel executar este cenário, documentação foi alterada.
# Scenario: Data de fim da vigência opcional
# Given que o usuário está na tela de cadastro de diretriz I-REC
# 	When o usuário não preenche um campo para a data de fim da vigência
# 	Then a diretriz deve ser salva com a data de fim como indefinida
# 	And o sistema deve permitir que essa informação seja atualizada posteriormente

Scenario: Visualização de mensagem de sucesso ao anexar arquivos
    Given que o usuário está logado no sistema
    When o usuário acessa ao módulo de diretrizes I-REC
    When o usuário clica no botão "Nova Diretriz"
    When que o usuário está na tela de cadastro de nova diretriz I-REC
    When o usuário informa os dados da nova diretriz I-REC
    When o usuário faz o upload de um arquivo de evidência "evidencia_imagem.jpg"
    When clica no botão Salvar
    When deve exibir a mensagem "Arquivo enviado com sucesso"
    When retorna para a tela de diretriz I-REC

# Scenario: Limpeza dos campos após cadastro bem-sucedido
    Given que o usuário cadastrou uma nova diretriz I-Rec
    When o usuário clica no botão "Nova Diretriz"
 	Then todos os campos da tela de cadastro de diretriz I-REC estar vazios
