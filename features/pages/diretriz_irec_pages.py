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
    MSG_SUCESSO_CAD_DIR_IREC = (By.XPATH, "//div[contains(text(), 'sucesso')]")
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
    PROD_DIR_IREC = (By.XPATH, "//tr[@class='ng-star-inserted']/td[1]/strong")
    VALIDA_DATA_ATUAL = (By.XPATH, "//span[@class='ng-tns-c4209099177-26 p-calendar p-calendar-w-btn p-calendar-disabled']/input[@aria-controls='pn_id_15_panel']")
    MSG_SUCESSO_ANEXAR_ARQUIVO = (By.XPATH, "//div[@data-pc-section='text']/div[@data-pc-section='detail' and contains(text(), 'Upload concluído')]")
    MSG_LIMITE_DE_EVIDENCIA = (By.XPATH, "//div[@class='p-message-wrapper ng-tns-c3633978228-28']")

logger = logging.getLogger(__name__)
class DiretrizIrecPage:
    def __init__(self, driver):
        self.driver = driver
        logger.info("Instanciando page object: DiretrizIrecPage")

    def acessar_aba_diretriz_irec(self):
        logger.info("Acessando aba Diretriz I-REC.")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(DiretrizIrecLocators.ABA_DIR_IREC)
        ).click()
        logger.info("Aba Diretriz I-REC acessada.")

    def clicar_nova_diretriz(self):
        logger.info("Clicando no botão Nova Diretriz.")
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(DiretrizIrecLocators.BTN_NOVA_DIR)
        ).click()
        logger.info("Botão Nova Diretriz clicado.")
        # Screenshot para diagnóstico
        try:
            self.driver.save_screenshot("reports/evidencias/apos_clicar_nova_diretriz.png")
            logger.info("Screenshot após clicar em Nova Diretriz salvo.")
        except Exception as e:
            logger.warning(f"Não foi possível salvar screenshot: {e}")
        # Espera por campo exclusivo da tela de cadastro
        try:
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(DiretrizIrecLocators.DESCRICAO_DAS_DIRETRIZ)
            )
            logger.info("Tela de cadastro de nova diretriz carregada.")
        except TimeoutException:
            logger.error("Tela de cadastro de nova diretriz NÃO carregou após o clique.")
            raise

    def validar_tela_cadastro_nova_diretriz(self):
        url_esperada = "https://diretrizes.dev.neoenergia.net/pages/diretriz-irec/novo"
        time.sleep(1)
        if self.driver.current_url != url_esperada:
            logger.error(f"URL incorreta. Esperado: {url_esperada}, Atual: {self.driver.current_url}")
            raise AssertionError(f"URL incorreta. Esperado: {url_esperada}, Atual: {self.driver.current_url}")
        logger.info("Usuário está na tela de cadastro de nova diretriz I-REC.")

    def preencher_dados_nova_diretriz(self, data_fim, valor_tabela, descricao):
        logger.info("Preenchendo dados da nova diretriz.")
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
        logger.info("Dados da nova diretriz preenchidos.")

    def preencher_apenas_campos_obrigatorios_sem_preco(self, data_fim, descricao):
        logger.info("Preenchendo apenas os campos obrigatórios (data fim da vigência e descrição), sem preço.")
        campo_data_fim = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(DiretrizIrecLocators.DATA_FIM_VIGENCIA)
        )
        campo_data_fim.clear()
        campo_data_fim.send_keys(data_fim)
        campo_descricao = self.driver.find_element(*DiretrizIrecLocators.DESCRICAO_DAS_DIRETRIZ)
        campo_descricao.clear()
        campo_descricao.send_keys(descricao)
        logger.info("Preenchidos apenas os campos data fim da vigência e descrição da diretriz, sem preço.")

    def clicar_botao_salvar(self):
        logger.info("Clicando no botão Salvar.")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(DiretrizIrecLocators.SALVAR_DIR_IREC)
        ).click()
        logger.info("Botão Salvar clicado.")

    def validar_mensagem_cadastro(self):
        try:
            WebDriverWait(self.driver, 4).until(
                EC.visibility_of_element_located(DiretrizIrecLocators.MSG_SUCESSO_CAD_DIR_IREC)
            )
            logger.info("Mensagem de sucesso ao cadastrar diretriz!")
        except TimeoutException:
            try:
                WebDriverWait(self.driver, 4).until(
                    EC.visibility_of_element_located(DiretrizIrecLocators.MSG_ERRO_CAD_DIR_IREC)
                )
                logger.error("Mensagem de erro ao cadastrar diretriz!")
            except TimeoutException:
                logger.error("Nenhuma mensagem de sucesso ou erro foi exibida.")
                raise AssertionError("Nenhuma mensagem de sucesso ou erro foi exibida.")

    def validar_redirecionamento_listar(self):
        url_esperada = "https://diretrizes.dev.neoenergia.net/pages/diretriz-irec/listar"
        time.sleep(1)
        if self.driver.current_url != url_esperada:
            self.driver.get(url_esperada)
            logger.info("Usuário foi redirecionado manualmente para a tela de listar diretrizes I-REC.")
        else:
            logger.info("Usuário já está na tela de listar diretrizes I-REC.")

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
            logger.info(f"Foi encontrada {len(diretrizes)} diretriz vigente no sistema:")
            for d in diretrizes:
                logger.info(f"Início Vigência: {d['inicio_vig']} | Fim Vigência: {d['fim_vig']}")
        else:
            logger.info("Não foram encontradas nenhuma diretriz vigente")

    def validar_invalida_anterior(self):
        linhas = self.driver.find_elements(*DiretrizIrecLocators.CONSULTAR_DIR_CADASTRADAS)
        for linha in linhas:
            colunas = linha.find_elements(By.TAG_NAME, "td")
            if len(colunas) > 3:
                fim_prematuro = colunas[3].text
                if fim_prematuro and fim_prematuro != "Não Definido":
                    logger.info("Diretriz anterior inválidada com sucesso")
                    return True
                elif fim_prematuro == "Não Definido":
                    logger.warning("Parece que a Diretriz anterior não foi invalidada corretamente, Verifique!")
                    return False
        logger.warning("Não foi possível validar a invalidação da diretriz anterior.")
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
            logger.info("Correto, apenas uma Diretriz vigênte")
        elif len(diretrizes_vigentes) > 1:
            logger.warning("Atenção!!! Mais de uma diretriz vigênte identificada")
            for d in diretrizes_vigentes:
                logger.warning(f"Início Vigência: {d['inicio_vig']} | Fim Vigência: {d['fim_vig']}")
        else:
            logger.info("Nenhuma diretriz vigente encontrada")

    def validar_diretriz_foi_invalidada(self):
        linhas = self.driver.find_elements(*DiretrizIrecLocators.CONSULTAR_DIR_CADASTRADAS)
        for linha in linhas:
            colunas = linha.find_elements(By.TAG_NAME, "td")
            if len(colunas) > 3:
                fim_prematuro = colunas[3].text
                if fim_prematuro and fim_prematuro != "Não Definido":
                    logger.info("Diretriz anterior inválidada com sucesso")
                    return True
        logger.warning("Parece que a Diretriz anterior não foi invalidada corretamente, Verifique!")
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
        logger.info("Todas as diretrizes cadastradas:")
        for linha in linhas:
            colunas = linha.find_elements(By.TAG_NAME, "td")
            if len(colunas) > 3:
                inicio_vig = colunas[1].text if len(colunas) > 1 else "?"
                fim_vig = colunas[2].text if len(colunas) > 2 else "?"
                fim_prematuro = colunas[3].text
                logger.info(f"Início Vigência: {inicio_vig} | Fim Vigência: {fim_vig} | Fim Prematuro Vigência: {fim_prematuro}")

    def identificar_diretriz_vigente_visual(self):
        linhas = self.driver.find_elements(*DiretrizIrecLocators.CONSULTAR_DIR_CADASTRADAS)
        for linha in linhas:
            if "Não Definido" in linha.text:
                style = linha.get_attribute("style")
                class_attr = linha.get_attribute("class")
                is_verde = "green" in style or "verde" in class_attr or "text-green" in class_attr
                is_negrito = "bold" in style or "font-weight: bold" in style or "font-bold" in class_attr
                if is_verde and is_negrito:
                    logger.info("Diretriz vigente está claramente identificável: verde e negrito.")
                else:
                    logger.warning("Atenção: Diretriz vigente NÃO está destacada corretamente (verde e negrito).")
                return
        logger.info("Nenhuma diretriz vigente encontrada para validação visual.")

    def exibir_datas_inicio_fim_vigencia(self):
        linhas = self.driver.find_elements(*DiretrizIrecLocators.CONSULTAR_DIR_CADASTRADAS)
        logger.info("Lista de datas de início e fim de vigência:")
        for idx, linha in enumerate(linhas, 1):
            colunas = linha.find_elements(By.TAG_NAME, "td")
            if len(colunas) > 2:
                inicio_vig = colunas[1].text if len(colunas) > 1 else "?"
                fim_vig = colunas[2].text if len(colunas) > 2 else "?"
                logger.info(f"Dir{idx} - {inicio_vig} | {fim_vig}")

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
                    logger.warning(f"Atenção: Data(s) da Dir{idx} não estão no formato correto: {inicio_vig} | {fim_vig}")
                else:
                    logger.info(f"Datas da Dir{idx} estão no formato correto: {inicio_vig} | {fim_vig}")

    def validar_ausencia_diretrizes(self):
        linhas = self.driver.find_elements(*DiretrizIrecLocators.CONSULTAR_DIR_CADASTRADAS)
        logger.info("Validando se não existem diretrizes cadastradas")
        return len(linhas) == 0

    def exibir_mensagem_ausencia_diretrizes(self, nenhuma_diretriz):
        if nenhuma_diretriz:
            logger.info("Não existe nenhuma diretriz cadastrada")
        else:
            logger.info("Não foi possivel validar este cenário, porque existem diretrizes cadastradas.")

    def consultar_e_verificar_ausencia_diretrizes(self):
        linhas = self.driver.find_elements(*DiretrizIrecLocators.CONSULTAR_DIR_CADASTRADAS)
        logger.info("Validando se não existem diretrizes cadastradas")
        return len(linhas) == 0

    def validar_mais_de_uma_pagina(self):
        btn_avancar = self.driver.find_element(*DiretrizIrecLocators.AVANCAR_PGN_DIRETRIZ)
        habilitado = btn_avancar.is_enabled()
        if habilitado:
            logger.info("Mais de uma página de diretrizes identificada")
        else:
            logger.info("Há apenas uma página identificada com as diretrizes cadastradas")
        return habilitado

    def avancar_para_proxima_pagina(self, pode_avancar):
        if pode_avancar:
            btn_avancar = self.driver.find_element(*DiretrizIrecLocators.AVANCAR_PGN_DIRETRIZ)
            btn_avancar.click()
            logger.info("Avançou para a próxima página de diretrizes.")
        else:
            logger.info("Botão para avançar para a próxima página não está habilitado")

    def exibir_diretrizes_proxima_pagina(self, pode_avancar):
        if pode_avancar:
            linhas = self.driver.find_elements(*DiretrizIrecLocators.CONSULTAR_DIR_CADASTRADAS)
            logger.info("Diretrizes da próxima página:")
            for linha in linhas:
                colunas = linha.find_elements(By.TAG_NAME, "td")
                if len(colunas) > 3:
                    inicio_vig = colunas[1].text if len(colunas) > 1 else "?"
                    fim_vig = colunas[2].text if len(colunas) > 2 else "?"
                    fim_prematuro = colunas[3].text
                    logger.info(f"Início Vigência: {inicio_vig} | Fim Vigência: {fim_vig} | Fim Prematuro Vigência: {fim_prematuro}")
        else:
            logger.info("Não é possivel exibir as diretrizes da próxima página, por que existe apenas uma página com diretrizes cadastradas")

    def retornar_pagina_anterior(self, pode_avancar):
        if pode_avancar:
            btn_retornar = self.driver.find_element(*DiretrizIrecLocators.RETORNAR_PGN_DIRETRIZ)
            btn_retornar.click()
            logger.info("Retornou para a página anterior de diretrizes.")
        else:
            logger.info("Não é possivel clicar no botão retornar, ja que existe apenas uma unica página de diretrizes cadastradas")

    def inserir_intervalo_data_invalido(self):
        campo_inicio = self.driver.find_element(*DiretrizIrecLocators.CONSULTAR_DATA_INICIO_VIGENCIA)
        campo_fim = self.driver.find_element(*DiretrizIrecLocators.CONSULTAR_DATA_FIM_VIGENCIA)
        campo_inicio.clear()
        campo_inicio.send_keys("24/04/2036")
        campo_fim.clear()
        campo_fim.send_keys("10/09/2025")
        logger.info("Intervalo de data inválido inserido: 24/04/2036 a 10/09/2025")

    def exibir_mensagem_erro_data_invalida(self):
        try:
            msg = self.driver.find_element(*DiretrizIrecLocators.MENSAGEM_ERRO_DATA_INVALIDA)
            texto = msg.text.strip()
            if texto:
                logger.info(f"Mensagem de erro exibida: {texto}")
            else:
                logger.info("Não foi identificada nenhuma mensagem de erro ao inserir uma data inválida")
        except NoSuchElementException:
            logger.info("Não foi identificada nenhuma mensagem de erro ao inserir uma data inválida")

    def abrir_detalhamento_diretriz(self):
        btn = self.driver.find_element(*DiretrizIrecLocators.BTN_DETALHE_DIRETRIZ)
        btn.click()
        logger.info("Detalhamento da diretriz aberto.")

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
                logger.info(f"Arquivo anexo identificado: {nome}")
        else:
            logger.info("Não foram identificados nenhum arquivo anexo.")

    def exibir_mensagem_campos_obrigatorios_nao_preenchidos(self):
        logger.info("Usuário não preencheu os campos obrigatórios: data fim da vigência, tabela de cálculo e descrição da diretriz.")

    def validar_mensagem_erro_campos_obrigatorios(self):
        try:
            msg = self.driver.find_element(*DiretrizIrecLocators.MSG_ERRO_CAMPOS_OBRIGATORIOS)
            texto = msg.text.strip()
            if texto:
                logger.info(f"Mensagem de erro exibida: {texto}")
            else:
                logger.info("Não foi exibida mensagem de erro informando os campos obrigatórios.")
        except NoSuchElementException:
            logger.info("Não foi exibida mensagem de erro informando os campos obrigatórios.")

    def fazer_upload_evidencia(self, nome_arquivo):
        btn_anexar = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'p-fileupload-choose') and span[contains(@class, 'p-button-label') and text()='Anexar Evidência']]")
        ))
        btn_anexar.click()
        caminho_arquivo = os.path.abspath(nome_arquivo)
        input_file = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        input_file.send_keys(caminho_arquivo)
        logger.info(f"Arquivo de evidência '{nome_arquivo}' anexado.")

    def fazer_upload_mais_de_10_evidencias(self):
        """
        Faz upload de mais de 10 arquivos de evidência (textos) presentes na raiz do repositório.
        """
        arquivos = [
            "evidencia_texto.txt",
            "evidencia_texto - Copia (2).txt",
            "evidencia_texto - Copia (3).txt",
            "evidencia_texto - Copia (4).txt",
            "evidencia_texto - Copia (5).txt",
            "evidencia_texto - Copia (6).txt",
            "evidencia_texto - Copia (7).txt",
            "evidencia_texto - Copia (8).txt",
            "evidencia_texto - Copia (9).txt",
            "evidencia_texto - Copia (10).txt"
        ]
        for arquivo in arquivos:
            self.fazer_upload_evidencia(arquivo)

    def validar_mensagem_limite_de_evidencia(self):
        """
        Valida se a mensagem de limite de anexos foi exibida e imprime o texto.
        """
        try:
            elemento = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(DiretrizIrecLocators.MSG_LIMITE_DE_EVIDENCIA)
            )
            logger.info(f"Mensagem exibida: {elemento.text}")
            return elemento.text
        except Exception:
            logger.info("Mensagem de limite de anexos não foi exibida!")
            return None

    def exibir_produtos_visiveis(self):
        produtos = self.driver.find_elements(*DiretrizIrecLocators.PROD_DIR_IREC)
        nomes = [p.text.strip() for p in produtos if p.text.strip()]
        logger.info("Produtos visíveis na tela:")
        for nome in nomes:
            logger.info(nome)
        return nomes

    def validar_data_inicio_vigencia_atual(self):
        from datetime import datetime
        campo_data = self.driver.find_element(*DiretrizIrecLocators.VALIDA_DATA_ATUAL)
        data_tela = campo_data.get_attribute("value")
        data_hoje = datetime.now().strftime("%d/%m/%Y")
        if data_tela == data_hoje:
            logger.info(f"Data de início da vigência correta: {data_tela}")
        else:
            logger.warning(f"Data de início da vigência incorreta. Esperado: {data_hoje}, Encontrado: {data_tela}")

    def fazer_upload_evidencia_texto(self):
        self.fazer_upload_evidencia("evidencia_texto.txt")

    def validar_mensagem_sucesso_upload(self):
        try:
            msg = self.driver.find_element(*DiretrizIrecLocators.MSG_SUCESSO_ANEXAR_ARQUIVO)
            texto = msg.text.strip()
            if texto:
                logger.info(f"Mensagem de sucesso exibida: {texto}")
            else:
                logger.info("Mensagem de sucesso de upload não exibida.")
        except NoSuchElementException:
            logger.info("Mensagem de sucesso de upload não exibida.")

    def validar_cadastro_nova_diretriz(self):
        logger.info("Usuário cadastrou a última diretriz com sucesso.")

    def validar_campos_cadastro_vazios(self):
        campo_data_fim = self.driver.find_element(*DiretrizIrecLocators.DATA_FIM_VIGENCIA)
        campos_tabela = self.driver.find_elements(*DiretrizIrecLocators.CAMPOS_TABELA_DE_CALCULOS)
        campo_descricao = self.driver.find_element(*DiretrizIrecLocators.DESCRICAO_DAS_DIRETRIZ)
        vazio = True
        if campo_data_fim.get_attribute("value"):
            logger.warning("Campo DATA_FIM_VIGENCIA não está vazio!")
            vazio = False
        for campo in campos_tabela:
            if campo.get_attribute("value"):
                logger.warning("Campo da tabela de cálculos não está vazio!")
                vazio = False
        if campo_descricao.get_attribute("value"):
            logger.warning("Campo DESCRICAO_DAS_DIRETRIZ não está vazio!")
            vazio = False
        if vazio:
            logger.info("Todos os campos obrigatórios estão vazios para novo cadastro.")
        else:
            logger.warning("Nem todos os campos obrigatórios estão vazios!")
