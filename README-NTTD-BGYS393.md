# neo_liberalizados-automacao

Automação de testes para o sistema Neo Liberalizados.

## Sumário
- [Setup do Ambiente](#setup-do-ambiente)
- [Execução dos Testes](#execução-dos-testes)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Padrão para Steps](#padrão-para-steps)
- [Padrão para Pages](#padrão-para-pages)
- [Relatórios e Evidências](#relatórios-e-evidências)
- [Dicas e Boas Práticas](#dicas-e-boas-práticas)

## Setup do Ambiente

1. Crie e ative um ambiente virtual Python:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # Windows
   # ou
   source venv/bin/activate  # Linux/Mac
   ```
2. Instale as dependências do projeto:
   ```sh
   pip install -r requirements.txt
   ```
3. Configure as variáveis de ambiente no arquivo `.env` (veja o exemplo em `credentials.py`).

## Execução dos Testes

- Para rodar todos os testes com Behave:
  ```sh
  behave
  ```
- Para rodar os testes e gerar relatório Allure e publicar no GitHub Pages:
  ```sh
  python run_tests_with_allure.py
  ```
  O relatório será gerado em `reports/allure-report` e publicado em: https://mferreio.github.io/neo_liberalizados-automacao/

## Estrutura do Projeto

- `features/` - Cenários BDD (.feature), steps e pages:
  - `feat_tela_de_produtos/` - Features relacionadas à tela de produtos.
  - `feat_tela_de_usuarios/` - Features relacionadas à tela de usuários.
  - `pages/` - Page Objects (ex: `tela_deprodutos_pages.py`, `login_page.py`).
  - `steps/` - Steps do Behave (ex: `test_tela_de_produtos_steps.py`).
  - `environment.py` - Configuração global do Behave.
- `utils/` - Funções utilitárias gerais.
- `docs/` - Relatórios Allure HTML, histórico e widgets.
- `reports/` - Resultados, evidências e screenshots dos testes.
- `modelos de evidencias/` - Modelos de documentos para evidências e relatórios.
- `requirements.txt` - Dependências do projeto.
- `run_tests_with_allure.py` - Script para execução automatizada dos testes e publicação do relatório.
- `credentials.py`/`.json` - Configuração de credenciais e variáveis sensíveis.

## Padrão para Steps
- Use nomes descritivos e em português.
- Utilize os decoradores @given, @when, @then do Behave.
- Mantenha os steps organizados por contexto de tela ou funcionalidade.
- Exemplo:
  ```python
  @when('Usuário clica em cadastrar produto')
  def step_clicar_em_cadastrar(context):
      context.tela_de_produtos_page.clicar_em_cadastrar_produto()
  ```

## Padrão para Pages
- Crie uma classe para cada tela ou contexto.
- Métodos devem representar ações ou validações da tela.
- Utilize nomes claros e objetivos.
- Exemplo:
  ```python
  class TelaDeProdutosPage:
      def clicar_em_cadastrar_produto(self):
          # implementação Selenium
          pass
  ```

## Relatórios e Evidências
- Relatórios Allure são gerados em `reports/allure-report`.
- Evidências (prints, documentos) ficam em `reports/evidencias/` e `reports/screenshots/`.
- Modelos de evidências disponíveis em `modelos de evidencias/`.
- O relatório pode ser publicado automaticamente no GitHub Pages.

## Dicas e Boas Práticas
- Use variáveis de ambiente para dados sensíveis.
- Mantenha o requirements.txt atualizado (use pip-tools se desejar).
- Organize os arquivos de steps e pages conforme o contexto das features.
- Documente sempre que criar novos padrões ou fluxos.
- Consulte os exemplos de steps e pages para manter a padronização.

---

Dúvidas ou sugestões? Abra uma issue ou entre em contato com o responsável pelo repositório.