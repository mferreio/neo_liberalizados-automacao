import logging
logger = logging.getLogger(__name__)
import os

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ArmEvidenciasSelectors:
    """Classe para armazenar os seletores da página de evidências."""

    DIRETRIZ_CURTO_PRAZO = "//a[span[text()='Diretriz Curto Prazo']]"
    BOTAO_NOVO = "//button[span[text()='Novo']]"
    CAMPO_DATA_FIM = "//p-calendar[@id='fimVigencia']//input[@type='text' and @role='combobox']"
    BOTAO_ANEXAR = "//span[contains(@class, 'p-fileupload-choose') and span[contains(@class, 'p-button-label') and text()='Anexar Evidência']]"
    INPUT_ARQUIVO = "input[type='file']"
    BOTAO_ANEXAR_XPATH = "/html/body/app-root[1]/app-layout[1]/div[1]/div[2]/div[1]/ng-component[1]/div[1]/div[1]/div[1]/div[3]/div[1]/p-fileupload[1]/div[1]/div[1]/span[1]/span[1]"
    ARQUIVO_JPG_ANEXADO_ELEMENTO = "//div[text()='evidencia_imagem.jpg']"
    BOTAO_SALVAR_DIRETRIZ = "//button[span[text()='Salvar']]"
    MENSAGEM_TIPO = "/html/body/app-root[1]/app-layout[1]/div[1]/p-toast[1]/div[1]/p-toastitem[1]/div[1]/div[1]/span[1]/checkicon[1]/svg[1]"
    MENSAGEM_TEXTO = "/html/body/app-root[1]/app-layout[1]/div[1]/p-toast[1]/div[1]/p-toastitem[1]/div[1]/div[1]/div[1]/div[2]"
    CAMPO_DESCRICAO = "//textarea[@id='descricao']"
    CAMPO_PREMIO = "//input[@role='spinbutton']"
    MENSAGEM_ERRO_FIM_VIGENCIA_OBRIGATORIO = "//div[@data-pc-section='text']//div[@data-pc-section='detail' and text()='Fim da vigência é obrigatório.']"
    MENSAGEM_ERRO_FIM_VIGENCIA_MESMO_DIA = (
        "/html/body/app-root/app-layout/div/p-toast/div/p-toastitem/div/div/div/div[2]"
    )
    MENSAGEM_SUCESSO_DIRETRIZ_CADASTRADA = (
        "/html/body/app-root/app-layout/div/p-toast/div/p-toastitem/div/div/div/div[1]"
    )
    MSG_LIMITE_TAMANHO_ARQUIVO = "//span[@class='p-message-summary ng-tns-c3633978228-28 ng-star-inserted']"
    # XPATH para mensagem de upload concluído com sucesso
    MG_UPLOAD_ARQUIVO_SUCESSO = "//div[text()='Upload concluído com sucesso.']"


class ArmEvidenciasPage:
    def validar_mensagem_upload_sucesso(self):
        """Valida se a mensagem de upload concluído com sucesso foi exibida na tela."""
        logger.info("Validando se a mensagem de upload concluído com sucesso está visível.")
        try:
            elemento = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, ArmEvidenciasSelectors.MG_UPLOAD_ARQUIVO_SUCESSO))
            )
            logger.info("Mensagem de upload concluído com sucesso exibida.")
            return elemento.is_displayed()
        except Exception:
            logger.error("Mensagem de upload concluído com sucesso NÃO foi exibida!")
            return False
    def validar_ausencia_arquivo_anexado(self):
        """
        Valida que não existe nenhum arquivo anexo na tela.
        Se não houver, exibe mensagem de sucesso.
        """
        logger.info("Validando ausência de arquivo anexo na tela.")
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, ArmEvidenciasSelectors.ARQUIVO_JPG_ANEXADO_ELEMENTO))
            )
            logger.error("Foi encontrado um arquivo anexo, mas não deveria haver nenhum.")
            raise AssertionError("Foi encontrado um arquivo anexo, mas não deveria haver nenhum.")
        except TimeoutException:
            logger.info("Não existem arquivos anexados na tela (OK)")
            return True
    def __init__(self, driver):
        self.driver = driver

    def clicar_diretriz_curto_prazo(self):
        try:
            logging.info("Clicando no botão 'Diretriz Curto Prazo'.")
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, ArmEvidenciasSelectors.DIRETRIZ_CURTO_PRAZO)
                )
            ).click()
        except Exception as e:
            logging.error(f"Erro ao clicar no botão 'Diretriz Curto Prazo': {e}")
            raise

    def clicar_botao_novo(self):
        try:
            logging.info("Clicando no botão 'Novo'.")
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, ArmEvidenciasSelectors.BOTAO_NOVO)
                )
            ).click()
        except Exception as e:
            logging.error(f"Erro ao clicar no botão 'Novo': {e}")
            raise

    def preencher_campo_data_fim(self, data_fim):
        try:
            logging.info(f"Preenchendo o campo 'Data Fim' com a data: {data_fim}.")
            campo_data_fim = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, ArmEvidenciasSelectors.CAMPO_DATA_FIM)
                )
            )
            campo_data_fim.click()
            campo_data_fim.clear()
            campo_data_fim.send_keys(data_fim)
            campo_data_fim.send_keys(Keys.TAB)
        except Exception as e:
            logging.error(f"Erro ao preencher o campo 'Data Fim': {e}")
            raise

    def fazer_upload_evidencia(self, arquivo):
        """Faz o upload de um arquivo de evidência."""
        # Define o novo local do arquivo na raiz do projeto
        caminho_arquivo = os.path.join(os.getcwd(), arquivo)

        if not os.path.exists(caminho_arquivo):
            raise FileNotFoundError(
                f"O arquivo '{caminho_arquivo}' não foi encontrado."
            )

        try:
            logging.info(f"Fazendo upload do arquivo: {arquivo}.")
            # Envia o caminho do arquivo diretamente para o seletor de arquivo
            input_arquivo = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ArmEvidenciasSelectors.INPUT_ARQUIVO)
                )
            )
            input_arquivo.send_keys(caminho_arquivo)
        except Exception as e:
            logging.error(f"Erro ao fazer upload do arquivo '{arquivo}': {e}")
            raise

    def fazer_upload_limitedetamanho(self):
        """
        Faz o upload do arquivo 'limitedetamanho.pdf' que está na raiz do repositório.
        """
        self.fazer_upload_evidencia("limitedetamanho.pdf")

    def validar_arquivo_anexado_no_elemento(self):
        try:
            logging.info("Validando se o arquivo foi anexado.")
            elemento = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, ArmEvidenciasSelectors.ARQUIVO_JPG_ANEXADO_ELEMENTO)
                )
            )
            logging.info("Arquivo anexo encontrado.")
            return elemento.is_displayed()
        except Exception as e:
            logging.error("Não foi encontrado nenhum arquivo anexo")
            raise

    def validar_mensagem_limite_tamanho_arquivo(self):
        """
        Valida se a mensagem de limite de tamanho do arquivo foi exibida e imprime o texto.
        """
        logger.info("Validando mensagem de limite de tamanho do arquivo.")
        xpath = ArmEvidenciasSelectors.MSG_LIMITE_TAMANHO_ARQUIVO
        try:
            elemento = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            logger.info(f"Mensagem exibida: {elemento.text}")
            return elemento.text
        except Exception:
            logger.warning("Mensagem de limite de tamanho de arquivo não foi exibida!")
            return None

    def clicar_em_salvar(self):
        try:
            logging.info("Clicando no botão 'Salvar'.")
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, ArmEvidenciasSelectors.BOTAO_SALVAR_DIRETRIZ)
                )
            ).click()
        except Exception as e:
            logging.error(f"Erro ao clicar no botão 'Salvar': {e}")
            raise

    def verificar_mensagem_sistema(self):
        try:
            logging.info("Verificando mensagem exibida pelo sistema.")
            if self._elemento_existe(
                ArmEvidenciasSelectors.MENSAGEM_ERRO_FIM_VIGENCIA_OBRIGATORIO
            ):
                mensagem = "Fim da vigência é obrigatório"
            elif self._elemento_existe(
                ArmEvidenciasSelectors.MENSAGEM_ERRO_FIM_VIGENCIA_MESMO_DIA
            ):
                mensagem = "Não é possível cadastrar a diretriz com o fim da vigência no mesmo dia após as 14:00"
            elif self._elemento_existe(
                ArmEvidenciasSelectors.MENSAGEM_SUCESSO_DIRETRIZ_CADASTRADA
            ):
                mensagem = "Diretriz cadastrada com sucesso"
            else:
                mensagem = "Nenhuma mensagem identificada"
            logging.info(f"Mensagem exibida: {mensagem}")
            return mensagem
        except Exception as e:
            logging.error(f"Erro ao verificar a mensagem do sistema: {e}")
            raise

    def _elemento_existe(self, xpath):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return True
        except:
            return False

    def preencher_campo_descricao(self, descricao):
        try:
            logging.info(f"Preenchendo o campo 'Descrição' com: {descricao}.")
            campo_descricao = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, ArmEvidenciasSelectors.CAMPO_DESCRICAO)
                )
            )
            campo_descricao.click()
            campo_descricao.clear()
            campo_descricao.send_keys(descricao)
        except Exception as e:
            logging.error(f"Erro ao preencher o campo 'Descrição': {e}")
            raise

    def preencher_campo_premio(self, premio):
        try:
            logging.info(f"Preenchendo todos os campos 'Prêmio' com: {premio}.")
            campos_premio = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, ArmEvidenciasSelectors.CAMPO_PREMIO)
                )
            )
            for campo in campos_premio:
                campo.click()
                campo.clear()
                campo.send_keys(premio)
        except Exception as e:
            logging.error(f"Erro ao preencher os campos 'Prêmio': {e}")
            raise

    def retorna_tela_inicial(self):
        """Verifica se está na página inicial, se não estiver, navega para ela."""
        url_inicial = "https://diretrizes.dev.neoenergia.net/"
        try:
            if self.driver.current_url != url_inicial:
                logger.info("Navegando para a página inicial.")
                self.driver.get(url_inicial)
                WebDriverWait(self.driver, 10).until(
                    EC.url_to_be(url_inicial)
                )
                logger.info("Usuário retornou para a página inicial com sucesso.")
            else:
                logger.info("Usuário já está na página inicial.")
        except TimeoutException:
            logger.error("Erro ao retornar para a página inicial.")
            raise

    def validar_pagina_inicial(self):
        """Valida se o usuário está na página inicial."""
        url_inicial = "https://diretrizes.dev.neoenergia.net/"
        if self.driver.current_url != url_inicial:
            raise AssertionError(f"Usuário não está na página inicial. URL atual: {self.driver.current_url}")
