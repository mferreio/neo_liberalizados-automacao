from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging
import time
import os

class DiretrizIrecLocators:
    ABA_DIR_IREC = (By.XPATH, "//a[span[text()='Diretriz I-REC']]")
    BTN_NOVA_DIR = (By.XPATH, "//button[span[text()='Novo']]")
    DATA_FIM_VIGENCIA = (By.XPATH, "//div[@class='grid my-4']//input[@class='ng-tns-c4209099177-22 p-inputtext p-component ng-star-inserted' and @aria-controls='pn_id_5_panel']")
    CAMPOS_TABELA_DE_CALCULOS = (By.XPATH, "//tbody[@class='p-element p-datatable-tbody']//input[@class='p-inputtext p-component p-element p-inputnumber-input']")
    DESCRICAO_DAS_DIRETRIZ = (By.XPATH, "//textarea[@id='descricao']")
    SALVAR_DIR_IREC = (By.XPATH, "//button[span[text()='Salvar']]")
    MSG_SUCESSO_CAD_DIR_IREC = (By.XPATH, "//div[text()='Diretriz cadastrada com sucesso!']")
    MSG_ERRO_CAD_DIR_IREC = (By.XPATH, "//div[text()='Erro de validação']")
    CONSULTAR_DIR_CADASTRADAS = (By.XPATH, "//tbody/tr[contains(@class, 'ng-star-inserted')]")
    AVANCAR_PGN_DIRETRIZ = (By.XPATH, "//button[@aria-label='Next Page']")
    RETORNAR_PGN_DIRETRIZ = (By.XPATH, "//button[@aria-label='Previous Page']")
    CONSULTAR_DATA_INICIO_VIGENCIA = (By.XPATH, "//input[contains(@aria-controls, 'pn_id_74_panel')]")
    CONSULTAR_DATA_FIM_VIGENCIA = (By.XPATH, "//input[contains(@aria-controls, 'pn_id_75_panel')]")
    MENSAGEM_ERRO_DATA_INVALIDA = (By.XPATH, "//div[@id='pn_id_70']")
    BTN_DETALHE_DIRETRIZ = (By.XPATH, "//button[@data-pc-name='button']")
    ANEXO_TXT = (By.XPATH, "//div[text()='evidencia_texto.txt']")
    ANEXO_JPG = (By.XPATH, "//div[text()='evidencia_imagem.jpg']")
    MSG_ERRO_CAMPOS_OBRIGATORIOS = (By.XPATH, "//div[@data-pc-section='text']")

class DiretrizIrecPage:
    def __init__(self, driver):
        self.driver = driver

    def acessar_aba_diretriz_irec(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(DiretrizIrecLocators.ABA_DIR_IREC)
        ).click()
        logging.info("Aba Diretriz I-REC acessada.")

    def clicar_nova_diretriz(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(DiretrizIrecLocators.BTN_NOVA_DIR)
        ).click()
        logging.info("Botão Nova Diretriz clicado.")

    def validar_tela_cadastro_nova_diretriz(self):
        url_esperada = "https://diretrizes.dev.neoenergia.net/pages/diretriz-irec/novo"
        time.sleep(1)
        if self.driver.current_url != url_esperada:
            raise AssertionError(f"URL incorreta. Esperado: {url_esperada}, Atual: {self.driver.current_url}")
        logging.info("Usuário está na tela de cadastro de nova diretriz I-REC.")

    def preencher_dados_nova_diretriz(self, data_fim, valor_tabela, descricao):
        campo_data_fim = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(DiretrizIrecLocators.DATA_FIM_VIGENCIA)
        )
        campo_data_fim.clear()
        campo_data_fim.send_keys(data_fim)
        campos_tabela = self.driver.find_elements(*DiretrizIrecLocators.CAMPOS_TABELA_DE_CALCULOS)
        for campo in campos_tabela:
            campo.clear()
            campo.send_keys(str(valor_tabela))
        campo_descricao = self.driver.find_element(*DiretrizIrecLocators.DESCRICAO_DAS_DIRETRIZ)
        campo_descricao.clear()
        campo_descricao.send_keys(descricao)
        logging.info("Dados da nova diretriz preenchidos.")

    def preencher_apenas_campos_obrigatorios_sem_preco(self, data_fim, descricao):
        campo_data_fim = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(DiretrizIrecLocators.DATA_FIM_VIGENCIA)
        )
        campo_data_fim.clear()
        campo_data_fim.send_keys(data_fim)
        campo_descricao = self.driver.find_element(*DiretrizIrecLocators.DESCRICAO_DAS_DIRETRIZ)
        campo_descricao.clear()
        campo_descricao.send_keys(descricao)
        print("Preenchidos apenas os campos data fim da vigência e descrição da diretriz, sem preço.")

    def clicar_botao_salvar(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(DiretrizIrecLocators.SALVAR_DIR_IREC)
        ).click()
        logging.info("Botão Salvar clicado.")

    def validar_mensagem_cadastro(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(DiretrizIrecLocators.MSG_SUCESSO_CAD_DIR_IREC)
            )
            logging.info("Mensagem de sucesso exibida ao cadastrar diretriz.")
            print("Mensagem de sucesso ao cadastrar diretriz!")
        except TimeoutException:
            try:
                WebDriverWait(self.driver, 2).until(
                    EC.visibility_of_element_located(DiretrizIrecLocators.MSG_ERRO_CAD_DIR_IREC)
                )
                logging.error("Mensagem de erro exibida ao cadastrar diretriz.")
                print("Mensagem de erro ao cadastrar diretriz!")
            except TimeoutException:
                raise AssertionError("Nenhuma mensagem de sucesso ou erro foi exibida.")

    def validar_redirecionamento_listar(self):
        url_esperada = "https://diretrizes.dev.neoenergia.net/pages/diretriz-irec/listar"
        time.sleep(1)
        if self.driver.current_url != url_esperada:
            self.driver.get(url_esperada)
            logging.info("Usuário foi redirecionado manualmente para a tela de listar diretrizes I-REC.")
        else:
            logging.info("Usuário já está na tela de listar diretrizes I-REC.")

    def consultar_diretrizes_vigentes(self):
        linhas = self.driver.find_elements(*DiretrizIrecLocators.CONSULTAR_DIR_CADASTRADAS)
        diretrizes_vigentes = []
        for linha in linhas:
            if "Não Definido" in linha.text:
                colunas = linha.find_elements(By.TAG_NAME, "td")
                inicio_vig = colunas[1].text if len(colunas) > 1 else "?"
                fim_vig = colunas[2].text if len(colunas) > 2 else "?"
                diretrizes_vigentes.append({
                    "linha": linha,
                    "inicio_vig": inicio_vig,
                    "fim_vig": fim_vig
                })
        return diretrizes_vigentes

    def exibir_info_diretrizes_vigentes(self):
        diretrizes = self.consultar_diretrizes_vigentes()
        if diretrizes:
            print(f"Foi encontrada {len(diretrizes)} diretriz vigente no sistema:")
            for d in diretrizes:
                print(f"Início Vigência: {d['inicio_vig']} | Fim Vigência: {d['fim_vig']}")
        else:
            print("Não foram encontradas nenhuma diretriz vigente")

    def validar_invalida_anterior(self):
        linhas = self.driver.find_elements(*DiretrizIrecLocators.CONSULTAR_DIR_CADASTRADAS)
        for linha in linhas:
            colunas = linha.find_elements(By.TAG_NAME, "td")
            if len(colunas) > 3:
                fim_prematuro = colunas[3].text
                if fim_prematuro and fim_prematuro != "Não Definido":
                    print("Diretriz anterior inválidada com sucesso")
                    return True
                elif fim_prematuro == "Não Definido":
                    print("Parece que a Diretriz anterior não foi invalidada corretamente, Verifique!")
                    return False
        print("Não foi possível validar a invalidação da diretriz anterior.")
        return False

    def garantir_apenas_uma_vigente(self):
        linhas = self.driver.find_elements(*DiretrizIrecLocators.CONSULTAR_DIR_CADASTRADAS)
        diretrizes_vigentes = []
        for linha in linhas:
            if "Não Definido" in linha.text:
                colunas = linha.find_elements(By.TAG_NAME, "td")
                inicio_vig = colunas[1].text if len(colunas) > 1 else "?"
                fim_vig = colunas[2].text if len(colunas) > 2 else "?"
                diretrizes_vigentes.append({
                    "inicio_vig": inicio_vig,
                    "fim_vig": fim_vig
                })
        if len(diretrizes_vigentes) == 1:
            print("Correto, apenas uma Diretriz vigênte")
        elif len(diretrizes_vigentes) > 1:
            print("Atenção!!! Mais de uma diretriz vigênte identificada")
            for d in diretrizes_vigentes:
                print(f"Início Vigência: {d['inicio_vig']} | Fim Vigência: {d['fim_vig']}")
        else:
            print("Nenhuma diretriz vigente encontrada")

    def validar_diretriz_foi_invalidada(self):
        linhas = self.driver.find_elements(*DiretrizIrecLocators.CONSULTAR_DIR_CADASTRADAS)
        for linha in linhas:
            colunas = linha.find_elements(By.TAG_NAME, "td")
            if len(colunas) > 3:
                fim_prematuro = colunas[3].text
                if fim_prematuro and fim_prematuro != "Não Definido":
                    print("Diretriz anterior inválidada com sucesso")
                    return True
        print("Parece que a Diretriz anterior não foi invalidada corretamente, Verifique!")
        return False

    def consultar_todas_diretrizes(self):
        linhas = self.driver.find_elements(*DiretrizIrecLocators.CONSULTAR_DIR_CADASTRADAS)
        diretrizes = []
        for linha in linhas:
            colunas = linha.find_elements(By.TAG_NAME, "td")
            if len(colunas) > 3:
                diretrizes.append({
                    "inicio_vig": colunas[1].text if len(colunas) > 1 else "?",
                    "fim_vig": colunas[2].text if len(colunas) > 2 else "?",
                    "fim_prematuro": colunas[3].text
                })
        return diretrizes

    def exibir_todas_diretrizes(self):
        linhas = self.driver.find_elements(*DiretrizIrecLocators.CONSULTAR_DIR_CADASTRADAS)
        print("Todas as diretrizes cadastradas:")
        for linha in linhas:
            colunas = linha.find_elements(By.TAG_NAME, "td")
            if len(colunas) > 3:
                inicio_vig = colunas[1].text if len(colunas) > 1 else "?"
                fim_vig = colunas[2].text if len(colunas) > 2 else "?"
                fim_prematuro = colunas[3].text
                print(f"Início Vigência: {inicio_vig} | Fim Vigência: {fim_vig} | Fim Prematuro Vigência: {fim_prematuro}")

    def identificar_diretriz_vigente_visual(self):
        linhas = self.driver.find_elements(*DiretrizIrecLocators.CONSULTAR_DIR_CADASTRADAS)
        for linha in linhas:
            if "Não Definido" in linha.text:
                style = linha.get_attribute("style")
                class_attr = linha.get_attribute("class")
                is_verde = "green" in style or "verde" in class_attr or "text-green" in class_attr
                is_negrito = "bold" in style or "font-weight: bold" in style or "font-bold" in class_attr
                if is_verde and is_negrito:
                    print("Diretriz vigente está claramente identificável: verde e negrito.")
                else:
                    print("Atenção: Diretriz vigente NÃO está destacada corretamente (verde e negrito).")
                return
        print("Nenhuma diretriz vigente encontrada para validação visual.")

    def exibir_datas_inicio_fim_vigencia(self):
        linhas = self.driver.find_elements(*DiretrizIrecLocators.CONSULTAR_DIR_CADASTRADAS)
        print("Lista de datas de início e fim de vigência:")
        for idx, linha in enumerate(linhas, 1):
            colunas = linha.find_elements(By.TAG_NAME, "td")
            if len(colunas) > 2:
                inicio_vig = colunas[1].text if len(colunas) > 1 else "?"
                fim_vig = colunas[2].text if len(colunas) > 2 else "?"
                print(f"Dir{idx} - {inicio_vig} | {fim_vig}")

    def validar_formato_datas_vigencia(self):
        import re
        linhas = self.driver.find_elements(*DiretrizIrecLocators.CONSULTAR_DIR_CADASTRADAS)
        formato = re.compile(r"^\d{2}/\d{2}/\d{4}$")
        for idx, linha in enumerate(linhas, 1):
            colunas = linha.find_elements(By.TAG_NAME, "td")
            if len(colunas) > 2:
                inicio_vig = colunas[1].text.strip() if len(colunas) > 1 else ""
                fim_vig = colunas[2].text.strip() if len(colunas) > 2 else ""
                if not (formato.match(inicio_vig) and formato.match(fim_vig)):
                    print(f"Atenção: Data(s) da Dir{idx} não estão no formato correto: {inicio_vig} | {fim_vig}")
                else:
                    print(f"Datas da Dir{idx} estão no formato correto: {inicio_vig} | {fim_vig}")

    def validar_ausencia_diretrizes(self):
        linhas = self.driver.find_elements(*DiretrizIrecLocators.CONSULTAR_DIR_CADASTRADAS)
        print("Validando se não existem diretrizes cadastradas")
        return len(linhas) == 0

    def exibir_mensagem_ausencia_diretrizes(self, nenhuma_diretriz):
        if nenhuma_diretriz:
            print("Não existe nenhuma diretriz cadastrada")
        else:
            print("Não foi possivel validar este cenário, porque existem diretrizes cadastradas.")

    def consultar_e_verificar_ausencia_diretrizes(self):
        linhas = self.driver.find_elements(*DiretrizIrecLocators.CONSULTAR_DIR_CADASTRADAS)
        print("Validando se não existem diretrizes cadastradas")
        return len(linhas) == 0

    def validar_mais_de_uma_pagina(self):
        btn_avancar = self.driver.find_element(*DiretrizIrecLocators.AVANCAR_PGN_DIRETRIZ)
        habilitado = btn_avancar.is_enabled()
        if habilitado:
            print("Mais de uma página de diretrizes identificada")
        else:
            print("Há apenas uma página identificada com as diretrizes cadastradas")
        return habilitado

    def avancar_para_proxima_pagina(self, pode_avancar):
        if pode_avancar:
            btn_avancar = self.driver.find_element(*DiretrizIrecLocators.AVANCAR_PGN_DIRETRIZ)
            btn_avancar.click()
            print("Avançou para a próxima página de diretrizes.")
        else:
            print("Botão para avançar para a próxima página não está habilitado")

    def exibir_diretrizes_proxima_pagina(self, pode_avancar):
        if pode_avancar:
            linhas = self.driver.find_elements(*DiretrizIrecLocators.CONSULTAR_DIR_CADASTRADAS)
            print("Diretrizes da próxima página:")
            for linha in linhas:
                colunas = linha.find_elements(By.TAG_NAME, "td")
                if len(colunas) > 3:
                    inicio_vig = colunas[1].text if len(colunas) > 1 else "?"
                    fim_vig = colunas[2].text if len(colunas) > 2 else "?"
                    fim_prematuro = colunas[3].text
                    print(f"Início Vigência: {inicio_vig} | Fim Vigência: {fim_vig} | Fim Prematuro Vigência: {fim_prematuro}")
        else:
            print("Não é possivel exibir as diretrizes da próxima página, por que existe apenas uma página com diretrizes cadastradas")

    def retornar_pagina_anterior(self, pode_avancar):
        if pode_avancar:
            btn_retornar = self.driver.find_element(*DiretrizIrecLocators.RETORNAR_PGN_DIRETRIZ)
            btn_retornar.click()
            print("Retornou para a página anterior de diretrizes.")
        else:
            print("Não é possivel clicar no botão retornar, ja que existe apenas uma unica página de diretrizes cadastradas")

    def inserir_intervalo_data_invalido(self):
        campo_inicio = self.driver.find_element(*DiretrizIrecLocators.CONSULTAR_DATA_INICIO_VIGENCIA)
        campo_fim = self.driver.find_element(*DiretrizIrecLocators.CONSULTAR_DATA_FIM_VIGENCIA)
        campo_inicio.clear()
        campo_inicio.send_keys("24/04/2036")
        campo_fim.clear()
        campo_fim.send_keys("10/09/2025")
        print("Intervalo de data inválido inserido: 24/04/2036 a 10/09/2025")

    def exibir_mensagem_erro_data_invalida(self):
        try:
            msg = self.driver.find_element(*DiretrizIrecLocators.MENSAGEM_ERRO_DATA_INVALIDA)
            texto = msg.text.strip()
            if texto:
                print(f"Mensagem de erro exibida: {texto}")
            else:
                print("Não foi identificada nenhuma mensagem de erro ao inserir uma data inválida")
        except NoSuchElementException:
            print("Não foi identificada nenhuma mensagem de erro ao inserir uma data inválida")

    def abrir_detalhamento_diretriz(self):
        btn = self.driver.find_element(*DiretrizIrecLocators.BTN_DETALHE_DIRETRIZ)
        btn.click()
        print("Detalhamento da diretriz aberto.")

    def validar_arquivos_anexados(self):
        arquivos = []
        try:
            self.driver.find_element(*DiretrizIrecLocators.ANEXO_TXT)
            arquivos.append("evidencia_texto.txt")
        except NoSuchElementException:
            pass
        try:
            self.driver.find_element(*DiretrizIrecLocators.ANEXO_JPG)
            arquivos.append("evidencia_imagem.jpg")
        except NoSuchElementException:
            pass
        if arquivos:
            for nome in arquivos:
                print(f"Arquivo anexo identificado: {nome}")
        else:
            print("Não foram identificados nenhum arquivo anexo.")

    def exibir_mensagem_campos_obrigatorios_nao_preenchidos(self):
        print("Usuário não preencheu os campos obrigatórios: data fim da vigência, tabela de cálculo e descrição da diretriz.")

    def validar_mensagem_erro_campos_obrigatorios(self):
        try:
            msg = self.driver.find_element(*DiretrizIrecLocators.MSG_ERRO_CAMPOS_OBRIGATORIOS)
            texto = msg.text.strip()
            if texto:
                print(f"Mensagem de erro exibida: {texto}")
            else:
                print("Não foi exibida mensagem de erro informando os campos obrigatórios.")
        except NoSuchElementException:
            print("Não foi exibida mensagem de erro informando os campos obrigatórios.")

    def fazer_upload_evidencia(self, nome_arquivo):
        # Localiza e clica no botão de anexar evidência
        btn_anexar = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'p-fileupload-choose') and span[contains(@class, 'p-button-label') and text()='Anexar Evidência']]")
        ))
        btn_anexar.click()
        # Faz upload do arquivo
        caminho_arquivo = os.path.abspath(nome_arquivo)
        input_file = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        input_file.send_keys(caminho_arquivo)
        print(f"Arquivo de evidência '{nome_arquivo}' anexado.")
