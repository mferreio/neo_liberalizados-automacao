@tela_de_usuarios
Feature: Tela Inicial

Scenario: Visualizar dashboard com diretrizes
    Given que eu estou na Página Inicial
	Then eu devo ver um campo para diretrizes diárias

Scenario: Visualizar dashboard com diretrizes semanais
    Given que eu estou na Página Inicial
	Then eu devo ver um campo para diretrizes semanais

Scenario: Visualizar dashboard para I-REC
    Given que eu estou na Página Inicial
 	Then eu devo ver um campo para I-REC

Scenario: Visualizar dashboard com diretrizes de curto prazo
    Given que eu estou na Página Inicial
	Then eu devo ver um campo para diretrizes de curto prazo

Scenario: Verificar apresentação dos dados de diretrizes diárias
   Given que eu estou na Página Inicial
 	When eu devo ver um campo para diretrizes diárias
 	Then exibe os dados de diretrizes diárias

Scenario: Verificar apresentação dos dados de diretrizes semanais
    Given que eu estou na Página Inicial
    When eu devo ver um campo para diretrizes semanais
    Then exibe os dados de diretrizes semanais

Scenario: Verificar apresentação do histórico dos dados de diretrizes diárias
    Given que eu estou na Página Inicial
 	When eu clico no botão "Ver Histórico" para diretrizes diárias
  	Then eu sou direcionado para a tela de histórico da diretriz diária
  	When eu devo poder visualizar dados históricos de maneira gráfica
    When usuário retorna a tela inicial

Scenario: Verificar apresentação do histórico dos dados de diretrizes semanais
    Given que eu estou na Página Inicial
 	When eu clico no botão "Ver Histórico" para diretrizes semanais
 	Then eu sou direcionado para a tela de histórico da diretriz semanal
 	When eu devo poder visualizar dado histórico de maneira gráfica
    When usuário retorna a tela inicial

Scenario: Verificar apresentação de dados BBCE do histórico dos dados de diretrizes diárias
    Given que eu estou na Página Inicial
 	When eu clico no botão "Ver Histórico" para diretrizes diárias
 	Then eu sou direcionado para a tela de dados BBCE do histórico dos dados de diretrizes diárias
 	When eu devo poder visualizar dados históricos de maneira gráfica
    When usuário retorna a tela inicial

 Scenario: Verificar apresentação de dados BBCE do histórico dos dados de diretrizes semanais
    Given que eu estou na Página Inicial
 	When eu clico no botão "Ver Histórico" para diretrizes semanais
 	Then eu sou direcionado para a tela de dados BBCE do histórico dos dados de diretrizes semanal
 	When eu devo poder visualizar dado histórico de maneira gráfica
    When usuário retorna a tela inicial

Scenario: Verificar apresentação de dados DCIDE do histórico dos dados de diretrizes diárias
     Given que eu estou na Página Inicial
 	When eu clico no botão "Ver Histórico" para diretrizes diárias
 	Then eu sou direcionado para a tela de dados DCIDE do histórico dos dados de diretrizes diárias
 	When eu devo poder visualizar dados históricos de maneira gráfica
    When usuário retorna a tela inicial

Scenario: Verificar apresentação de dados DCIDE do histórico dos dados de diretrizes semanais
    Given que eu estou na Página Inicial
	When eu clico no botão "Ver Histórico" para diretrizes semanais
 	Then eu sou direcionado para a tela de dados DCIDE do histórico dos dados de diretrizes semanal
 	When eu devo poder visualizar dado histórico de maneira gráfica
    When usuário retorna a tela inicial

Scenario: Exportar dados da diretriz diária apresentados em XLSX
    Given que eu estou na Página Inicial
 	When eu clico no botão "Exportar" da diretriz diária
 	Then os dados apresentados devem ser baixados no formato XLSX
 	When o nome do arquivo deve ter "relatorio_diretriz_diaria"

Scenario: Exportar dados da diretriz Semanal apresentados em XLSX
    Given que eu estou na Página Inicial
 	When eu clico no botão "Exportar" da diretriz semanal
 	Then os dados apresentados devem ser baixados no formato XLSX
 	When o nome do arquivo deve ter "relatorio_diretriz_semanal"

Scenario: Exportar dados da diretriz I-REC apresentados em XLSX
    Given que eu estou na Página Inicial
 	When eu clico no botão "Exportar" da diretriz I-REC
 	Then os dados apresentados devem ser baixados no formato XLSX
 	When o nome do arquivo deve ter "relatorio_diretriz_irec"

Scenario: Exportar dados da diretriz curto prazo apresentados em XLSX
    Given que eu estou na Página Inicial
 	When eu clico no botão "Exportar" da diretriz curto prazo
 	Then os dados apresentados devem ser baixados no formato XLSX
 	When o nome do arquivo deve ter "relatorio_diretriz_curto_prazo"


Scenario: Visualizar prêmios padrões
    Given que eu estou na Página Inicial
    When eu visualizo a barra de lateral
 	Then eu devo ver os prêmios para "prêmio Sazo" e "prêmio Flex"
	When usuário retorna a tela inicial
