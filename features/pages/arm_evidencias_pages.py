from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import logging, ipdb
import os
from selenium.common.exceptions import TimeoutException


class ArmEvidenciasSelectors:
    """Classe para armazenar os seletores da página de evidências."""
    DIRETRIZ_CURTO_PRAZO = "//a[span[text()='Diretriz Curto Prazo']]"
    BOTAO_NOVO = "//button[span[text()='Novo']]"
    CAMPO_DATA_FIM = "//input[@aria-controls='pn_id_21_panel']"
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
    MENSAGEM_ERRO_FIM_VIGENCIA_MESMO_DIA = "/html/body/app-root/app-layout/div/p-toast/div/p-toastitem/div/div/div/div[2]"
    MENSAGEM_SUCESSO_DIRETRIZ_CADASTRADA = "/html/body/app-root/app-layout/div/p-toast/div/p-toastitem/div/div/div/div[1]"

class ArmEvidenciasPage:
    def __init__(self, driver):
        self.driver = driver

    def clicar_diretriz_curto_prazo(self):
        try:
            logging.info("Clicando no botão 'Diretriz Curto Prazo'.")
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, ArmEvidenciasSelectors.DIRETRIZ_CURTO_PRAZO))
            ).click()
        except Exception as e:
            logging.error(f"Erro ao clicar no botão 'Diretriz Curto Prazo': {e}")
            raise

    def clicar_botao_novo(self):
        try:
            logging.info("Clicando no botão 'Novo'.")
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, ArmEvidenciasSelectors.BOTAO_NOVO))
            ).click()
        except Exception as e:
            logging.error(f"Erro ao clicar no botão 'Novo': {e}")
            raise

    def preencher_campo_data_fim(self, data_fim):
        try:
            logging.info(f"Preenchendo o campo 'Data Fim' com a data: {data_fim}.")
            campo_data_fim = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ArmEvidenciasSelectors.CAMPO_DATA_FIM))
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
            raise FileNotFoundError(f"O arquivo '{caminho_arquivo}' não foi encontrado.")

        try:
            logging.info(f"Fazendo upload do arquivo: {arquivo}.")
            # Envia o caminho do arquivo diretamente para o seletor de arquivo
            input_arquivo = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ArmEvidenciasSelectors.INPUT_ARQUIVO))
            )
            input_arquivo.send_keys(caminho_arquivo)
        except Exception as e:
            logging.error(f"Erro ao fazer upload do arquivo '{arquivo}': {e}")
            raise

    def validar_arquivo_anexado_no_elemento(self):
        try:
            logging.info("Validando se o arquivo foi anexado.")
            elemento = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ArmEvidenciasSelectors.ARQUIVO_JPG_ANEXADO_ELEMENTO))
            )
            logging.info("Arquivo anexo encontrado.")
            return elemento.is_displayed()
        except Exception as e:
            logging.error("Não foi encontrado nenhum arquivo anexo")
            raise

    def clicar_em_salvar(self):
        try:
            logging.info("Clicando no botão 'Salvar'.")
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, ArmEvidenciasSelectors.BOTAO_SALVAR_DIRETRIZ))
            ).click()
        except Exception as e:
            logging.error(f"Erro ao clicar no botão 'Salvar': {e}")
            raise

    def verificar_mensagem_sistema(self):
        try:
            logging.info("Verificando mensagem exibida pelo sistema.")
            if self._elemento_existe(ArmEvidenciasSelectors.MENSAGEM_ERRO_FIM_VIGENCIA_OBRIGATORIO):
                mensagem = "Fim da vigência é obrigatório"
            elif self._elemento_existe(ArmEvidenciasSelectors.MENSAGEM_ERRO_FIM_VIGENCIA_MESMO_DIA):
                mensagem = "Não é possível cadastrar a diretriz com o fim da vigência no mesmo dia após as 14:00"
            elif self._elemento_existe(ArmEvidenciasSelectors.MENSAGEM_SUCESSO_DIRETRIZ_CADASTRADA):
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
                EC.presence_of_element_located((By.XPATH, ArmEvidenciasSelectors.CAMPO_DESCRICAO))
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
                EC.presence_of_all_elements_located((By.XPATH, ArmEvidenciasSelectors.CAMPO_PREMIO))
            )
            for campo in campos_premio:
                campo.click()
                campo.clear()
                campo.send_keys(premio)
        except Exception as e:
            logging.error(f"Erro ao preencher os campos 'Prêmio': {e}")
            raise

    def retorna_tela_inicial(self):
        """Retorna para a página inicial."""
        try:
            logging.info("Navegando para a página inicial.")
            self.driver.get("https://diretrizes.dev.neoenergia.net/")
            WebDriverWait(self.driver, 10).until(
                EC.url_to_be("https://diretrizes.dev.neoenergia.net/")
            )
            logging.info("Usuário retornou para a página inicial com sucesso.")
        except TimeoutException:
            logging.error("Erro ao retornar para a página inicial.")
            raise
