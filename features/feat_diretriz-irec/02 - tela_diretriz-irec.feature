# Feature: Tela de Diretriz I-REC

# Scenario: Mensagem de ausência de diretrizes	Given que o usuário acessou a tela de diretriz I-REC
# 	And não há diretrizes cadastradas no sistema
# 	When a tela é carregada
# 	Then uma mensagem "Nenhuma diretriz cadastrada" deve ser exibida

# Scenario: Navegação entre páginas de diretrizes	Given que o usuário está na tela de diretriz I-REC
# 	And há mais de uma página de diretrizes
# 	When o usuário navega para a próxima página
# 	Then as diretrizes da próxima página devem ser exibidas
# 	And o usuário deve ser capaz de retornar à página anterior

# Scenario: Limite de caracteres na busca por intervalo de data	Given que o usuário está na tela de diretriz I-REC
# 	When o usuário insere um intervalo de data inválido (por exemplo, data de início maior que data de fim)
# 	Then uma mensagem de erro deve ser exibida informando que o intervalo é inválido
# 	And a busca não deve ser realizada

# Scenario: Visualização dos arquivos anexados	Given que o usuário está na tela de detalhes da diretriz
# 	And a diretriz possui arquivos anexados
# 	When o usuário seleciona um arquivo anexado
# 	Then o arquivo deve ser baixado ou aberto para visualização

# Scenario: Acesso ao histórico de alterações da diretriz	Given que o usuário está na tela de detalhes da diretriz
# 	When o usuário clica no botão "Ver histórico de alterações"
# 	Then a tela deve exibir o histórico de alterações realizadas na diretriz, incluindo data e responsável

# Scenario: Filtragem adicional das diretrizes	Given que o usuário está na tela de diretriz I-REC
# 	When o usuário aplica um filtro adicional como categoria ou status
# 	Then apenas as diretrizes que correspondem ao filtro aplicado devem ser exibidas

# Scenario: Validação de campos obrigatórios ao cadastrar nova diretriz	Given que o usuário está na tela de cadastro de nova diretriz
# 	When o usuário tenta salvar a diretriz sem preencher os campos obrigatórios
# 	Then uma mensagem de erro deve ser exibida informando os campos que precisam ser preenchidos

# Scenario: Edição de uma diretriz existente	Given que o usuário está na tela de diretriz I-REC
# 	And o usuário selecionou uma diretriz existente
# 	When o usuário clica no botão de editar
# 	Then o usuário deve ser direcionado para a tela de edição da diretriz escolhida
