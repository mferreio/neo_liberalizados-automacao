# Feature: Validação de Usuário
#   Como um administrador do sistema
#   Eu quero validar o cadastro de usuários no Active Directory
#   Para garantir que apenas usuários válidos possam acessar o sistema

#   Background:
#     Given que o usuário está logado no sistema

#   @diretriz_curto_prazo


# Scenario: Usuário autenticado e associado ao perfil	  Given que o usuário "usuario@exemplo.com" está registrado no Active Directory
# 	  And o usuário tem um perfil previamente cadastrado no sistema
# 	  When o usuário faz login no sistema usando suas credenciais
# 	  Then o sistema deve exibir o perfil registrado do usuário
# 	  And o sistema deve mostrar "Bem-vindo, [nome do usuário]"

# Scenario: Usuário autenticado sem perfil cadastrado	Given que o usuário "usuario@exemplo.com" está registrado no Active Directory
# 	And o usuário não possui um perfil cadastrado no sistema
# 	When o usuário faz login no sistema usando suas credenciais
# 	Then o sistema deve exibir uma mensagem para contato com o administrador
# 	And a mensagem deve ser "Perfil não encontrado. Por favor, entre em contato com o administrador."

# Scenario: Administrador cadastra um novo usuário	  Given que o administrador está logado no sistema
# 	  When o administrador acessa a seção de gerenciamento de usuários
# 	  And ele insere o e-mail "novousuario@exemplo.com" e o perfil "Usuario Padrão"
# 	  And o administrador clica no botão "Cadastrar"
# 	  Then o sistema deve confirmar que o usuário foi cadastrado com sucesso
# 	  And deve exibir a mensagem "Usuário cadastrado com sucesso!"

# Scenario: Administrador tenta cadastrar um usuário já existente	Given que o administrador está logado no sistema
# 	And o usuário "usuario@exemplo.com" já está cadastrado
# 	When o administrador acessa a seção de gerenciamento de usuários
# 	And ele insere o e-mail "usuario@exemplo.com" e o perfil "Usuario Padrão"
# 	And o administrador clica no botão "Cadastrar"
# 	Then o sistema deve exibir uma mensagem de erro
# 	And deve exibir a mensagem "O usuário já está cadastrado."

# Scenario: Falha na autenticação do Active Directory	Given que o serviço do Active Directory está indisponível
# 	When o usuário tenta fazer login no sistema
# 	Then o sistema deve exibir uma mensagem de erro
# 	And deve mostrar "Não foi possível autenticar, por favor, tente novamente mais tarde."