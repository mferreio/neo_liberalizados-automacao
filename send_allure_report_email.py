import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import shutil
from git import Repo

# Carrega variáveis do .env
load_dotenv()

REMETENTE = os.getenv('REMETENTE_DE_EMAIL')
DESTINATARIO = os.getenv('DESTINATARIO')
SENHADEAPP = os.getenv('SENHADEAPP')

# Compacta a pasta allure-report em um zip
dir_relatorio = os.path.join('reports', 'allure-report')

# --- NOVO: Copia allure-report para docs/ e faz commit/push na main ---
docs_path = os.path.join('docs')
if os.path.exists(docs_path):
    shutil.rmtree(docs_path)
shutil.copytree(dir_relatorio, docs_path)

repo = Repo(os.getcwd())
repo.git.add('docs')
repo.index.commit('Atualiza relatório Allure em docs para GitHub Pages (branch main)')
repo.git.push('origin', 'main')
# --- FIM NOVO ---

# Cria a mensagem de e-mail
msg = EmailMessage()
msg['Subject'] = 'Relatório de Testes Automatizados - Allure'
msg['From'] = REMETENTE
msg['To'] = DESTINATARIO
msg.set_content(
    'Olá,\n\nO relatório Allure dos testes automatizados foi publicado na branch main (GitHub Pages).\n'
    'Acesse o relatório atualizado pelo link do GitHub Pages configurado para este repositório.\n\n'
    'Dica UI/UX: O relatório Allure é interativo e responsivo, facilitando a navegação entre cenários, evidências e gráficos.\n\n'
    'Atenciosamente,\nAutomação QA'
)

# Envia o e-mail
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(REMETENTE, SENHADEAPP)
    smtp.send_message(msg)

print('E-mail de notificação enviado com sucesso!')
print('Relatório Allure publicado em docs/ e enviado para a branch main (GitHub Pages).')
