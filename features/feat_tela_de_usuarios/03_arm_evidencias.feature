Feature: Armazenamento de evidências
  Como usuário
  Quero gerenciar arquivos de evidências
  Para garantir o armazenamento e consulta de forma segura


Scenario: Enviar um arquivo de evidências com sucesso ao cadastrar a diretriz Curto Prazo
  Given que o usuário está logado no sistema
  When o usuário acessa a aba "diretriz Curto Prazo"
  When clica no botão Novo
  When o usuário preenche o campo Data Fim
  When o usuário preenche os campos obrigatórios
  When o usuário faz o upload de um arquivo de evidência "evidencia_imagem.jpg"
  When o sistema deve validar que o arquivo "evidencia_imagem.jpg" foi anexado
  When usuário clica em salvar
  When o sistema exibe uma mensagem de sucesso
  When retorna a pagina inicial

# Scenario: Tentativa de envio de um arquivo por um usuário sem permissão // "Não existe usuário que não tenha permissão de adicionar arquivos"
#  Given que o usuário está logado com perfil "Usuário Comum"
#   When o usuário tenta fazer o upload de um arquivo de evidência "evidencia_texto.txt"
#   Then o sistema deve exibir a mensagem "Acesso negado. Você não tem permissão para enviar arquivos."

 Scenario: Consultar um arquivo de evidências com sucesso
  Given que o usuário está logado no sistema
  When o usuário acessa a aba "diretriz Curto Prazo"
  When clica no botão Novo
  When o usuário preenche o campo Data Fim
  When o usuário preenche os campos obrigatórios
  When o usuário faz o upload de um arquivo de evidência "evidencia_imagem.jpg"
  Then o sistema deve validar que o arquivo "evidencia_imagem.jpg" foi anexado
  When retorna a pagina inicial

# Scenario: Tentativa de consulta de um arquivo por um usuário sem permissão  // "Não existe usuário que não tenha permissão de consultar arquivos"
#   Given que o usuário está logado com perfil "Usuário Comum"
#   When um arquivo de evidência "evidencia_texto.txt" foi enviado e está armazenado no S3
#   When o usuário tenta solicitar o download do arquivo "evidencia_texto.txt"
#   Then o sistema deve exibir a mensagem "Acesso negado. Você não tem permissão para consultar arquivos."

 Scenario: Consultar um arquivo que não existe
  Given que o usuário está logado no sistema
  When o usuário acessa a aba "diretriz Curto Prazo"
  When clica no botão Novo
  When o usuário preenche o campo Data Fim
  When o usuário preenche os campos obrigatórios
  Then o sistema deve validar que não existe nenhum arquivo anexado
  When retorna a pagina inicial

