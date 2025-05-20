import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import zipfile

# Carrega variáveis do .env
load_dotenv()

REMETENTE = os.getenv('REMETENTE_DE_EMAIL')
DESTINATARIO = os.getenv('DESTINATARIO')
SENHADEAPP = os.getenv('SENHADEAPP')

# Compacta a pasta allure-report em um zip
dir_relatorio = os.path.join('reports', 'allure-report')
zip_path = os.path.join('reports', 'allure-report.zip')

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, os.path.dirname(path))
            ziph.write(file_path, arcname)

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipdir(dir_relatorio, zipf)

# Cria a mensagem de e-mail
msg = EmailMessage()
msg['Subject'] = 'Relatório de Testes Automatizados - Allure'
msg['From'] = REMETENTE
msg['To'] = DESTINATARIO
msg.set_content(
    'Olá,\n\nSegue em anexo o relatório Allure dos testes automatizados.\n'\
    'Para melhor experiência de visualização:\n'
    '1. Baixe e extraia o arquivo "allure-report.zip" em seu computador.\n'
    '2. Abra o arquivo "index.html" extraído usando o navegador Google Chrome.\n\n'
    'Dica UI/UX: O relatório Allure é interativo e responsivo, facilitando a navegação entre cenários, evidências e gráficos.\n\n'
    'Atenciosamente,\nAutomação QA'
)

# Anexa o zip
with open(zip_path, 'rb') as f:
    msg.add_attachment(f.read(), maintype='application', subtype='zip', filename='allure-report.zip')

# Envia o e-mail
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(REMETENTE, SENHADEAPP)
    smtp.send_message(msg)

print('E-mail com relatório Allure (zip) enviado com sucesso!')
