Feature: Gerenciamento de Evidências
  Como usuário
  Quero gerenciar arquivos de evidências
  Para garantir o armazenamento e consulta de forma segura

Scenario: Enviar um arquivo de evidências com sucesso
  Given que o usuário está logado no sistema
  When o usuário faz o upload de um arquivo de evidência "evidencia_imagem.jpg"
  Then o sistema deve armazenar o arquivo no bucket do S3
  When deve exibir a mensagem "Arquivo enviado com sucesso"

Scenario: Tentativa de envio de um arquivo por um usuário sem permissão
  Given que o usuário está logado com perfil "Usuário Comum"
  When o usuário tenta fazer o upload de um arquivo de evidência "evidencia_texto.txt"
  Then o sistema deve exibir a mensagem "Acesso negado. Você não tem permissão para enviar arquivos."

Scenario: Consultar um arquivo de evidências com sucesso
  Given que o usuário está logado com perfil "Administrador"
  When um arquivo de evidência "evidencia_imagem.jpg" foi enviado e está armazenado no S3
  When o usuário solicita o download do arquivo "evidencia_imagem.jpg"
  Then o sistema deve buscar o arquivo no bucket do S3
  When deve retornar o arquivo para o usuário

Scenario: Tentativa de consulta de um arquivo por um usuário sem permissão
  Given que o usuário está logado com perfil "Usuário Comum"
  When um arquivo de evidência "evidencia_texto.txt" foi enviado e está armazenado no S3
  When o usuário tenta solicitar o download do arquivo "evidencia_texto.txt"
  Then o sistema deve exibir a mensagem "Acesso negado. Você não tem permissão para consultar arquivos."

Scenario: Consultar um arquivo que não existe
  Given que o usuário está logado com perfil "Trading"
  When o usuário solicita o download do arquivo "arquivo_inexistente.txt"
  Then o sistema deve exibir a mensagem "Arquivo não encontrado."
