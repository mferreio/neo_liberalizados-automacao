from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DiretrizCurtoPrazoPage:
    BTN_DETALHAMENTO_DIRETRIZ = "//button[@class='p-ripple p-element p-button p-component p-button-icon-only p-button-rounded p-button-text p-button-plain']"
    DETALHAMENTO_INICIO_VIGENCIA = "//form[@class='ng-untouched ng-pristine ng-star-inserted']//span[@class='ng-tns-c4209099177-32 p-calendar p-calendar-w-btn p-calendar-disabled']"
    DETALHAMENTO_FIM_VIGENCIA = "//form[@class='ng-untouched ng-pristine ng-star-inserted']//span[@class='ng-tns-c4209099177-33 p-calendar p-calendar-w-btn p-calendar-disabled']"
    DETALHAMENTO_PRODUTOS = "//div[@class='card mb-4 ng-untouched ng-pristine']//tbody[@class='p-element p-datatable-tbody']//tr[@class='ng-untouched ng-pristine ng-star-inserted']"
    DETALHAMENTO_DESCRICAO = "//div[@class='col-12 md:col-6 lg:col-6']//textarea[@id='descricao']"
    DETALHAMENTO_ARQUIVOS_ANEXADOS = "//table[@id='pn_id_43-table']//tbody[@role='rowgroup']"

    def __init__(self, driver):
        self.driver = driver

    def validar_ou_redirecionar_tela_diretriz_curto_prazo(self):
        url_esperada = "https://diretrizes.dev.neoenergia.net/pages/diretriz-irec/listar"
        if self.driver.current_url != url_esperada:
            print(f"Usuário NÃO foi encaminhado para a página correta. Redirecionando para: {url_esperada}")
            self.driver.get(url_esperada)
        else:
            print(f"Usuário já está na página correta: {url_esperada}")

    def validar_ou_redirecionar_tela_diretriz_curto_prazo_curto(self):
        url_esperada = "https://diretrizes.dev.neoenergia.net/pages/diretriz-curto-prazo/listar"
        if self.driver.current_url != url_esperada:
            print(f"Usuário NÃO foi encaminhado para a página correta. Redirecionando para: {url_esperada}")
            self.driver.get(url_esperada)
        else:
            print(f"Usuário já está na página correta: {url_esperada}")

    def validar_ou_redirecionar_tela_cadastro_diretriz_curto_prazo(self):
        url_esperada = "https://diretrizes.dev.neoenergia.net/pages/diretriz-curto-prazo/novo"
        if self.driver.current_url != url_esperada:
            print(f"Usuário NÃO foi encaminhado para a tela de cadastro correta. Redirecionando para: {url_esperada}")
            self.driver.get(url_esperada)
        else:
            print(f"Usuário já está na tela de cadastro correta: {url_esperada}")

    def preencher_campos_obrigatorios(self, premio="10", descricao="Teste automatizado", data_inicio=None):
        """
        Preenche os campos obrigatórios do cadastro de diretriz curto prazo.
        Se data_inicio for passado, preenche com o valor informado.
        """
        # Campo prêmio
        campo_premio = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@role='spinbutton']"))
        )
        campo_premio.clear()
        campo_premio.send_keys(premio)
        # Campo descrição
        campo_descricao = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@id='descricao']"))
        )
        campo_descricao.clear()
        campo_descricao.send_keys(descricao)
        # Campo data início (opcional)
        if data_inicio:
            campo_data_inicio = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@aria-controls and contains(@id,'dataInicio')]"))
            )
            campo_data_inicio.clear()
            campo_data_inicio.send_keys(data_inicio)
            campo_data_inicio.send_keys(Keys.TAB)

    def preencher_campos_obrigatorios_com_data_invalida(self):
        """
        Preenche os campos obrigatórios usando uma data inválida no campo de início.
        """
        self.preencher_campos_obrigatorios(data_inicio="2025/10/13")

    def validar_mensagem_erro_data_invalida(self):
        """
        Valida se a mensagem de erro de data inválida é exibida e imprime o texto.
        """
        xpath = "//small[text()=' A data não pode ser menor que a atual ']"
        try:
            elemento = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            print(f"Mensagem exibida: {elemento.text}")
            return elemento.text
        except Exception:
            print("Mensagem de erro de data inválida não foi exibida!")
            return None

    def inserir_intervalo_data_para_busca(self):
        """
        Insere o intervalo de data para busca nos campos de filtro.
        """
        campo_inicio = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@aria-controls='pn_id_25_panel']"))
        )
        campo_inicio.clear()
        campo_inicio.send_keys("01/03/2025")
        campo_inicio.send_keys(Keys.TAB)
        campo_fim = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@aria-controls='pn_id_26_panel']"))
        )
        campo_fim.clear()
        campo_fim.send_keys("15/05/2025")
        campo_fim.send_keys(Keys.TAB)

    def validar_diretrizes_exibidas_no_intervalo(self):
        """
        Valida se todas as diretrizes exibidas estão dentro do intervalo de 01/03 a 15/05.
        """
        from datetime import datetime
        linhas = self.driver.find_elements(By.XPATH, "//tbody/tr[contains(@class, 'ng-star-inserted')]")
        fora_periodo = []
        data_inicio_periodo = datetime.strptime("01/03/2025", "%d/%m/%Y")
        data_fim_periodo = datetime.strptime("15/05/2025", "%d/%m/%Y")
        for linha in linhas:
            colunas = linha.find_elements(By.TAG_NAME, "td")
            if len(colunas) > 2:
                inicio_vig = colunas[1].text.strip()
                fim_vig = colunas[2].text.strip()
                try:
                    data_inicio = datetime.strptime(inicio_vig, "%d/%m/%Y")
                    data_fim = datetime.strptime(fim_vig, "%d/%m/%Y")
                except Exception:
                    fora_periodo.append({"inicio": inicio_vig, "fim": fim_vig, "motivo": "formato inválido"})
                    continue
                if not (data_inicio_periodo <= data_inicio <= data_fim_periodo and data_inicio_periodo <= data_fim <= data_fim_periodo):
                    fora_periodo.append({"inicio": inicio_vig, "fim": fim_vig, "motivo": "fora do período"})
        if fora_periodo:
            print("Diretrizes fora do período 01/03/2025 a 15/05/2025:")
            for d in fora_periodo:
                print(f"Início Vigência: {d['inicio']} | Fim Vigência: {d['fim']} | Motivo: {d['motivo']}")
        else:
            print("Todas as diretrizes exibidas estão dentro do período 01/03/2025 a 15/05/2025.")

    def clicar_botao_detalhamento_diretriz(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.BTN_DETALHAMENTO_DIRETRIZ))
        )
        btn.click()
        print("Botão de detalhamento da diretriz clicado.")

    def exibir_detalhes_diretriz(self):
        # Início Vigência
        spans_inicio = self.driver.find_elements(By.XPATH, self.DETALHAMENTO_INICIO_VIGENCIA)
        for idx, span in enumerate(spans_inicio, 1):
            print(f"Início Vigência {idx}: {span.text}")
        # Fim Vigência
        spans_fim = self.driver.find_elements(By.XPATH, self.DETALHAMENTO_FIM_VIGENCIA)
        for idx, span in enumerate(spans_fim, 1):
            print(f"Fim Vigência {idx}: {span.text}")
        # Produtos
        linhas_produtos = self.driver.find_elements(By.XPATH, self.DETALHAMENTO_PRODUTOS)
        for idx, linha in enumerate(linhas_produtos, 1):
            colunas = linha.find_elements(By.TAG_NAME, "td")
            valores = [col.text for col in colunas]
            print(f"Produto {idx}: {valores}")
        # Descrição
        try:
            descricao = self.driver.find_element(By.XPATH, self.DETALHAMENTO_DESCRICAO)
            print(f"Descrição: {descricao.get_attribute('value')}")
        except Exception:
            print("Descrição não encontrada.")

    def exibir_arquivos_anexados(self):
        linhas = self.driver.find_elements(By.XPATH, self.DETALHAMENTO_ARQUIVOS_ANEXADOS)
        for idx, linha in enumerate(linhas, 1):
            colunas = linha.find_elements(By.TAG_NAME, "td")
            for col in colunas:
                texto = col.text.strip()
                if texto:
                    print(f"Arquivo anexo {idx}: {texto}")
