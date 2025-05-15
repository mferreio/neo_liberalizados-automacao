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