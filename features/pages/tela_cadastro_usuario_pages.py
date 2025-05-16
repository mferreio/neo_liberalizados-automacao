from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class TelaCadastroUsuarioPage:
    FORMATO_EMAIL_INVALIDO = "//small[text()='Formato de e-mail inválido.']"
    USUARIO_JA_EXISTE = ".//div[@data-pc-section='text']/div[text()='Usuário já existe!']"
    MSG_PERFIL_OBRIGATORIO = "//small[text()='Perfil é obrigatório.']"
    MSG_NOME_OBRIGATORIO = "//small[text()='Nome é obrigatório.']"
    MSG_EMAIL_OBRIGATORIO = "//small[text()='E-mail é obrigatório.']"
    VALIDAR_DASH_TABELA_DIR_DIARIA = "//app-diretriz-diaria-dashboard/h5"
    DASHBOARD_DIARIA = "//app-diretriz-diaria-dashboard"
    VALIDAR_DASH_TABELA_DIR_SEMANAL = "app-diretriz-semanal-dashboard"
    VALIDAR_DASH_TABELA_DIR_IREC = "//app-diretriz-irec-dashboard/h5"
    VALIDAR_DASH_TABELA_DIR_CURTO_PRAZO = "//app-diretriz-short-dashboard/h5"
    BTN_VER_HISTORICO_DIR_DIARIA = "//app-diretriz-diaria-dashboard//h5[contains(text(), 'Diretriz Diária')]/following-sibling::div//button[@label='Ver Histórico' and span[text()='Ver Histórico']]"
    BTN_VER_HISTORICO_DIR_SEMANAL = "//app-diretriz-semanal-dashboard//h5[contains(text(), ' Diretriz Semanal')]/following-sibling::div//button[@label='Ver Histórico' and span[text()='Ver Histórico']]"
    XPATH_GRAFICO_COMPARATIVO = "//historico-comparativo-chart//h5[contains(text(), 'Comparativo')]"
    XPATH_GRAFICO_HISTORICO = "//historico-diretriz-diaria-chart//h5[contains(text(), 'Histórico Diretrizes')]"
    XPATH_GRAFICO_BBCE = "//historico-bbce-chart//h5[contains(text(), 'Negociações BBCE')]"
    BTN_EXPORTAR_DIR_DIARIA = "//app-diretriz-diaria-dashboard//h5[contains(text(), 'Diretriz Diária')]/following-sibling::div//button[@label='Exportar' and span[text()='Exportar']]"
    BTN_EXPORTAR_DIR_SEMANAL = "//app-diretriz-semanal-dashboard//h5[contains(text(), 'Diretriz Semanal')]/following-sibling::div//button[@label='Exportar' and span[text()='Exportar']]"
    BTN_EXPORTAR_DIR_IREC = "//app-diretriz-irec-dashboard//h5[contains(text(), ' Diretriz I-REC')]/following-sibling::div//button[@label='Exportar' and span[text()='Exportar']]"
    BTN_EXPORTAR_DIR_CURTO_PRAZO = "//app-diretriz-short-dashboard//h5[contains(text(), ' Diretriz Curto Prazo')]/following-sibling::div//button[@label='Exportar' and span[text()='Exportar']]"
    ABA_PREMIO_SAZO = "//li[@app-menuitem]//a[span[text()='Prêmio Sazo']]"
    ABA_PREMIO_FLEX = "//li[@app-menuitem]//a[span[text()='Prêmio Flex']]"

    def __init__(self, driver):
        self.driver = driver

    def preencher_nome_email_admin_email_invalido(self, nome="Usuário Teste", email="teste"):
        # Seleciona perfil de administrador (exemplo, ajuste conforme necessário)
        perfil_admin = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='perfil']"))
        )
        perfil_admin.click()
        perfil_admin.send_keys("Administrador")
        # Preenche nome
        campo_nome = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='nome']"))
        )
        campo_nome.clear()
        campo_nome.send_keys(nome)
        # Preenche email inválido
        campo_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))
        )
        campo_email.clear()
        campo_email.send_keys(email)
        campo_email.send_keys(Keys.TAB)

    def validar_mensagem_email_invalido(self):
        try:
            elemento = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.FORMATO_EMAIL_INVALIDO))
            )
            print(f"Mensagem exibida: {elemento.text}")
            return elemento.text
        except Exception:
            print("Mensagem de formato de e-mail inválido não foi exibida!")
            return None

    def validar_mensagem_usuario_ja_existe(self):
        try:
            elemento = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.USUARIO_JA_EXISTE))
            )
            print(f"Mensagem exibida: {elemento.text}")
            return elemento.text
        except Exception:
            print("Mensagem de usuário já existe não foi exibida!")
            return None

    def validar_mensagens_campos_obrigatorios(self):
        mensagens = []
        try:
            perfil = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.MSG_PERFIL_OBRIGATORIO))
            )
            mensagens.append(perfil.text)
        except Exception:
            print("Mensagem de perfil obrigatório não exibida.")
        try:
            nome = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.MSG_NOME_OBRIGATORIO))
            )
            mensagens.append(nome.text)
        except Exception:
            print("Mensagem de nome obrigatório não exibida.")
        try:
            email = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.MSG_EMAIL_OBRIGATORIO))
            )
            mensagens.append(email.text)
        except Exception:
            print("Mensagem de e-mail obrigatório não exibida.")
        for msg in mensagens:
            print(f"Mensagem exibida: {msg}")
        return mensagens

    def validar_usuario_cadastrado(self, context):
        """
        Valida se o cenário de cadastro de usuário foi executado com sucesso.
        """
        assert hasattr(context, "usuario_cadastrado") and context.usuario_cadastrado is True, (
            "O cenário de cadastro de usuário não foi executado com sucesso antes deste passo."
        )

    def validar_pagina_inicial(self):
        url_esperada = "https://diretrizes.dev.neoenergia.net/"
        if self.driver.current_url != url_esperada:
            print(f"Usuário NÃO está na página inicial. Redirecionando para: {url_esperada}")
            self.driver.get(url_esperada)
        else:
            print(f"Usuário já está na página inicial: {url_esperada}")

    def validar_tabela_diretrizes_diarias(self):
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        # Valida existência do título
        titulos = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.VALIDAR_DASH_TABELA_DIR_DIARIA))
        )

    def validar_tabela_diretrizes_semanais(self):
        tabelas = self.driver.find_elements(By.XPATH, self.VALIDAR_DASH_TABELA_DIR_SEMANAL)
        if not tabelas:
            print("Tabela de diretrizes semanais não encontrada!")
        for idx, tabela in enumerate(tabelas, 1):
            print(f"Conteúdo da tabela semanal {idx}:")
            print(tabela.text)

    def validar_tabela_diretrizes_irec(self):
        titulos = self.driver.find_elements(By.XPATH, self.VALIDAR_DASH_TABELA_DIR_IREC)
        if not titulos:
            print("Tabela de diretrizes I-REC não encontrada!")
        for idx, titulo in enumerate(titulos, 1):
            print(f"Título da tabela I-REC {idx}: {titulo.text}")

    def validar_tabela_diretrizes_curto_prazo(self):
        titulos = self.driver.find_elements(By.XPATH, self.VALIDAR_DASH_TABELA_DIR_CURTO_PRAZO)
        if not titulos:
            print("Tabela de diretrizes de curto prazo não encontrada!")
        for idx, titulo in enumerate(titulos, 1):
            print(f"Título da tabela Curto Prazo {idx}: {titulo.text}")

    def exibir_dados_diretrizes_diarias(self):
        tabelas = self.driver.find_elements(By.XPATH, "//app-diretriz-diaria-dashboard")
        for idx, tabela in enumerate(tabelas, 1):
            print(f"Conteúdo da tabela de diretrizes diárias {idx}:")
            print(tabela.text)

    def exibir_dados_diretrizes_semanais(self):
        tabelas = self.driver.find_elements(By.XPATH, "//app-diretriz-semanal-dashboard")
        for idx, tabela in enumerate(tabelas, 1):
            print(f"Conteúdo da tabela de diretrizes semanais {idx}:")
            print(tabela.text)

    def clicar_ver_historico_diretriz_diaria(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.BTN_VER_HISTORICO_DIR_DIARIA))
        )
        btn.click()
        print("Botão 'Ver Histórico' da Diretriz Diária clicado.")

    def validar_redirecionamento_historico_diaria(self):
        url_esperada = "https://diretrizes.dev.neoenergia.net/pages/diretriz-diaria/historico"
        WebDriverWait(self.driver, 10).until(lambda d: d.current_url == url_esperada)
        if self.driver.current_url == url_esperada:
            print(f"Usuário foi redirecionado corretamente para: {url_esperada}")
        else:
            print(f"Usuário NÃO foi redirecionado corretamente. URL atual: {self.driver.current_url}")

    def clicar_ver_historico_diretriz_semanal(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.BTN_VER_HISTORICO_DIR_SEMANAL))
        )
        btn.click()
        print("Botão 'Ver Histórico' da Diretriz Semanal clicado.")

    def validar_redirecionamento_historico_semanal(self):
        url_esperada = "https://diretrizes.dev.neoenergia.net/pages/diretriz-semanal/historico"
        WebDriverWait(self.driver, 10).until(lambda d: d.current_url == url_esperada)
        if self.driver.current_url == url_esperada:
            print(f"Usuário foi redirecionado corretamente para: {url_esperada}")
        else:
            print(f"Usuário NÃO foi redirecionado corretamente. URL atual: {self.driver.current_url}")

    def validar_graficos_historico_diaria(self):
        # Valida existência do gráfico Comparativo
        comparativo = self.driver.find_elements(By.XPATH, self.XPATH_GRAFICO_COMPARATIVO)
        assert comparativo, "Gráfico 'Comparativo' não encontrado."
        print("Gráfico 'Comparativo' encontrado.")
        # Valida existência do gráfico Histórico Diretrizes
        historico = self.driver.find_elements(By.XPATH, self.XPATH_GRAFICO_HISTORICO)
        assert historico, "Gráfico 'Histórico Diretrizes' não encontrado."
        print("Gráfico 'Histórico Diretrizes' encontrado.")
        # Valida existência do gráfico Negociações BBCE
        bbce = self.driver.find_elements(By.XPATH, self.XPATH_GRAFICO_BBCE)
        assert bbce, "Gráfico 'Negociações BBCE' não encontrado."
        print("Gráfico 'Negociações BBCE' encontrado.")
    def clicar_exportar_diretriz_diaria(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.BTN_EXPORTAR_DIR_DIARIA))
        )
        btn.click()
        print("Botão 'Exportar' da Diretriz Diária clicado.")

    def clicar_exportar_diretriz_semanal(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.BTN_EXPORTAR_DIR_SEMANAL))
        )
        btn.click()
        print("Botão 'Exportar' da Diretriz Semanal clicado.")

    def clicar_exportar_diretriz_irec(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.BTN_EXPORTAR_DIR_IREC))
        )
        btn.click()
        print("Botão 'Exportar' da Diretriz I-REC clicado.")

    def clicar_exportar_diretriz_curto_prazo(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.BTN_EXPORTAR_DIR_CURTO_PRAZO))
        )
        btn.click()
        print("Botão 'Exportar' da Diretriz Curto Prazo clicado.")

    def acessar_barra_lateral(self):
        print("Acessando a barra de navegação, buscando Prêmio Sazo e Prêmio Flex")

    def validar_abas_premios(self):
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        aba_sazo = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ABA_PREMIO_SAZO))
        )
        aba_flex = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ABA_PREMIO_FLEX))
        )
        assert aba_sazo is not None, "Aba Prêmio Sazo não encontrada."
        assert aba_flex is not None, "Aba Prêmio Flex não encontrada."
        print("Abas 'Prêmio Sazo' e 'Prêmio Flex' encontradas.")
