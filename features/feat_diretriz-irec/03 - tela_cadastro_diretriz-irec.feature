# Feature: Tela de Cadastro de Diretriz I-REC

# Scenario: Acesso à tela de cadastro de nova diretriz	Given que o usuário está na tela de diretriz I-REC
# 	When o usuário clica no botão de adicionar nova diretriz
# 	Then o usuário deve ser direcionado para a tela de cadastro de diretriz I-REC

# Scenario: Exibição dos produtos cadastrados na tela de cadastro	Given que o usuário está na tela de cadastro de diretriz I-REC
# 	When a tela é carregada
# 	Then todos os produtos cadastrados devem estar visíveis
# 	And há campos para o usuário inserir o preço de cada produto

# Scenario: Data de início da vigência válida	Given que o usuário está na tela de cadastro de diretriz I-REC
# 	When o usuário insere uma data de início de vigência
# 	And a data é menor que a data atual
# 	Then uma mensagem de erro deve ser exibida informando que a data não pode ser menor que a data atual

# Scenario: Anexação de arquivos durante o cadastro	Given que o usuário está na tela de cadastro de diretriz I-REC
# 	When o usuário anexa arquivos como evidência da precificação
# 	Then os arquivos devem ser salvos juntamente com os dados da diretriz

# Scenario: Salvar nova diretriz com sucesso	Given que o usuário preencheu todos os campos obrigatórios
# 	And anexou os documentos necessários
# 	When o usuário clica no botão "Salvar"
# 	Then os dados devem ser persistidos na base de dados
# 	And uma notificação de sucesso deve ser exibida
# 	And o usuário deve ser redirecionado para a tela de diretrizes

# Scenario: Salvar nova diretriz com falha	Given que o usuário preencheu os campos obrigatórios, mas ocorreu um erro ao salvar
# 	When o usuário clica no botão "Salvar"
# 	Then uma notificação de falha deve ser exibida
# 	And o usuário deve permanecer na tela de cadastro de diretriz I-REC

# Scenario: Campo de preço obrigatório	Given que o usuário está na tela de cadastro de diretriz I-REC
# 	When o usuário tenta salvar a diretriz sem inserir preços para todos os produtos
# 	Then uma mensagem de erro deve ser exibida informando que todos os preços são obrigatórios

# Scenario: Edição de preço de produto	Given que o usuário está na tela de cadastro de diretriz I-REC
# 	When o usuário altera o preço de um dos produtos
# 	And clica no botão "Salvar"
# 	Then o novo preço deve ser persistido na base de dados
# 	And o usuário deve ser notificado sobre a atualização bem-sucedida

# Scenario: Limite de anexos	Given que o usuário está na tela de cadastro de diretriz I-REC
# 	When o usuário tenta anexar mais do que o limite permitido de arquivos
# 	Then uma mensagem de erro deve ser exibida informando que o limite de anexos foi excedido
# 	And o usuário deve ser impedido de anexar mais arquivos

# Scenario: Validação de formato de arquivos anexados	Given que o usuário está na tela de cadastro de diretriz I-REC
# 	When o usuário tenta anexar um arquivo em um formato inválido
# 	Then uma mensagem de erro deve ser exibida informando que o formato do arquivo não é suportado
# 	And o arquivo não deve ser anexado

# Scenario: Cancelamento do cadastro de nova diretriz	Given que o usuário está na tela de cadastro de diretriz I-REC
# 	When o usuário clica no botão "Cancelar"
# 	Then o usuário deve ser solicitado a confirmar o cancelamento
# 	And se confirmado, o usuário deve ser redirecionado para a tela de diretrizes
# 	And nenhuma alteração deve ser salva na base de dados

# Scenario: Data de fim da vigência opcional	Given que o usuário está na tela de cadastro de diretriz I-REC
# 	When o usuário não preenche um campo para a data de fim da vigência
# 	Then a diretriz deve ser salva com a data de fim como indefinida
# 	And o sistema deve permitir que essa informação seja atualizada posteriormente

# Scenario: Visualização de mensagem de sucesso ao anexar arquivos	Given que o usuário está na tela de cadastro de diretriz I-REC
# 	When o usuário anexa um arquivo com sucesso
# 	Then um feedback deve ser exibido informando que o arquivo foi anexado corretamente

# Scenario: Limpeza dos campos após cadastro bem-sucedido	Given que o usuário preencheu todos os dados e clicou em "Salvar"
# 	And a operação foi bem-sucedida
# 	Then todos os campos da tela de cadastro de diretriz I-REC devem ser limpos
# 	And o usuário deve estar preparado para cadastrar uma nova diretriz se desejar
