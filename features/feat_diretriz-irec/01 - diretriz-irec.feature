# Feature: Diretrizes I-REC

# Scenario: Cadastro de uma nova diretriz I-REC	Given que o usuário está na tela de cadastro de nova diretriz I-REC
# 	When o usuário informa os dados da nova diretriz, incluindo preço e anexa arquivos
# 	And clica no botão "Cadastrar"
# 	Then a nova diretriz deve ser cadastrada
# 	And a diretriz anterior deve ser invalidada
# 	And as datas de início e fim da vigência devem ser geradas e registradas

# Scenario: Tentativa de cadastrar múltiplas diretrizes vigentes	Given que existe uma diretriz I-REC vigente no sistema
# 	When o usuário tenta cadastrar uma nova diretriz I-REC
# 	Then a nova diretriz deve invalidar a anterior
# 	And o sistema deve garantir que apenas uma diretriz esteja vigente

# Scenario: Mantendo diretrizes invalidas para histórico	Given que uma diretriz I-REC foi invalidada
# 	When o usuário consulta as diretrizes cadastradas
# 	Then a diretriz invalidada deve estar disponível na base de dados para histórico
# 	And a informação sobre sua vigência deve estar acessível

# Scenario: Visualização de diretrizes cadastradas	Given que o usuário está na tela de diretriz I-REC
# 	When a tela é carregada
# 	Then todas as diretrizes cadastradas devem ser exibidas
# 	And a diretriz vigente deve ser claramente identificável

# Scenario: Anexação de arquivos durante o cadastro	Given que o usuário está na tela de cadastro de nova diretriz I-REC
# 	When o usuário anexa um arquivo e clica no botão "Cadastrar"
# 	Then o arquivo deve ser salvo junto com as informações da diretriz
# 	And o usuário deve receber uma confirmação da anexação bem-sucedida

# Scenario: Exibição de data de vigência da diretriz	Given que uma nova diretriz I-REC foi cadastrada
# 	When o usuário visualiza a tela de diretriz I-REC
# 	Then a data de início e a data de fim da vigência da diretriz devem ser apresentadas claramente
# 	And as datas devem estar formatadas corretamente
# 	Then o usuário deve ser direcionado para a tela de cadastro de nova diretriz
