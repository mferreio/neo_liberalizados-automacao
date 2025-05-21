import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from datetime import datetime

# Carrega variáveis do .env
load_dotenv()


REMETENTE = os.getenv('REMETENTE_DE_EMAIL')
DESTINATARIO = os.getenv('DESTINATARIO')
SENHADEAPP = os.getenv('SENHADEAPP')

# Garante que todos os destinatários recebam o e-mail
destinatarios = [email.strip() for email in DESTINATARIO.split(',')]

# Lê métricas das variáveis de ambiente

report_url = os.getenv('ALLURE_REPORT_URL', 'N/A')
data_execucao = os.getenv('DATA_EXECUCAO', 'N/A')
total_testes = int(os.getenv('TOTAL_TESTES', '0'))
testes_aprovados = int(os.getenv('TESTES_APROVADOS', '0'))
testes_falhados = int(os.getenv('TESTES_FALHADOS', '0'))
testes_ignorados = int(os.getenv('TESTES_IGNORADOS', '0'))
percentual_falhas = (testes_falhados / total_testes * 100) if total_testes > 0 else 0

# Tempo de execução do teste (em minutos e segundos)
tempo_execucao = os.getenv('TEMPO_EXECUCAO', None)
if tempo_execucao is None:
    tempo_execucao = '-'  # fallback caso não esteja definido

# UI/UX aprimorado para e-mail de relatório
html = f"""
<html>
  <body style="font-family: Arial, sans-serif; background: #f7f7f7; margin:0; padding:0;">
    <table width="600" align="center" cellpadding="0" cellspacing="0" style="background:#fff; border-radius:8px; box-shadow:0 2px 8px #0001; padding:0; border:0;">
      <tr>
        <td align="center" style="padding:32px 32px 0 32px;">
          <img src="cid:logo_neoenergia" alt="Neoenergia" width="180" height="48" style="display:block; margin-bottom:16px;">
          <h2 style="color:#43a047;margin-bottom:8px;">Relatório de Automação - Neoenergia</h2>
          <p style="color:#888;margin-top:0;font-size:15px;">Diretrizes Liberalizados</p>
        </td>
      </tr>
      <tr><td><hr style="border:none;border-top:1px solid #e0e0e0;margin:24px 0;"></td></tr>
      <tr>
        <td style="padding:0 32px;">
          <h3 style="color:#222;text-align:left;">Resumo da Execução</h3>
          <table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom:24px;">
            <tr>
              <td style="padding:8px 0;color:#666;text-align:left;width:180px;">Tempo de Execução:</td>
              <td style="padding:8px 0;color:#222;text-align:left;"><b>{tempo_execucao}</b></td>
            </tr>
            <tr>
              <td style="padding:8px 0;color:#666;text-align:left;width:180px;">Data de Execução:</td>
              <td style="padding:8px 0;color:#222;text-align:left;"><b>{data_execucao}</b></td>
            </tr>
            <tr>
              <td style="padding:8px 0;color:#666;text-align:left;">Total de Testes:</td>
              <td style="padding:8px 0;color:#222;text-align:left;"><b>{total_testes}</b></td>
            </tr>
            <tr>
              <td style="padding:8px 0;color:#43a047;text-align:left;">Testes Aprovados:</td>
              <td style="padding:8px 0;text-align:left;">
                <span style="color:#388e3c;font-weight:bold;">{testes_aprovados}</span>
              </td>
            </tr>
            <tr>
              <td style="padding:8px 0;color:#d32f2f;text-align:left;">Testes Falhados:</td>
              <td style="padding:8px 0;text-align:left;">
                <span style="color:#d32f2f;font-weight:bold;">{testes_falhados}</span>
                <span style="color:#d32f2f;font-size:13px;">({percentual_falhas:.2f}% falhas)</span>
              </td>
            </tr>
            <tr>
              <td style="padding:8px 0;color:#ffa000;text-align:left;">Testes Ignorados:</td>
              <td style="padding:8px 0;text-align:left;">
                <span style="color:#ffa000;font-weight:bold;">{testes_ignorados}</span>
              </td>
            </tr>
          </table>
        </td>
      </tr>
      <tr>
        <td align="center" style="padding:0 32px 32px 32px;">
          <!-- Botão compatível com Outlook -->
          <table cellpadding="0" cellspacing="0" border="0" align="center" style="margin:32px auto;">
            <tr>
              <td align="center" bgcolor="#43a047" style="border-radius:24px;">
                <a href="{report_url}" target="_blank" style="display:inline-block; color:#fff; background:#43a047; text-decoration:none; font-weight:bold; padding:14px 32px; border-radius:24px; font-size:16px;">Visualizar Relatório Allure</a>
              </td>
            </tr>
          </table>
        </td>
      </tr>
      <tr>
        <td align="center" style="padding:0 32px 24px 32px;">
          <table width="100%" cellpadding="0" cellspacing="0">
            <tr>
              <td align="center" bgcolor="#f1f8e9" style="border-radius:6px; padding:16px 20px; color:#222;">
                Este é o resultado dos testes automatizados que foram executados no projeto.
              </td>
            </tr>
          </table>
        </td>
      </tr>
      <tr><td><hr style="border:none;border-top:1px solid #e0e0e0;margin:24px 0;"></td></tr>
      <tr>
        <td align="center" style="color:#888;font-size:13px;">
          Este é um e-mail automático. Por favor, não responda.<br>
          &copy; {datetime.now().year} Neoenergia - Automação QA
        </td>
      </tr>
    </table>
  </body>
</html>
"""



msg = EmailMessage()
msg['Subject'] = '[Neoenergia - Liberalizados Diretrizes] Report de automação ' + data_execucao
msg['From'] = REMETENTE
# Define o campo 'To' apenas com o remetente (ou um destinatário principal)
msg['To'] = REMETENTE
# Todos os destinatários reais vão em BCC
msg['Bcc'] = ', '.join(destinatarios)
msg.set_content("Seu cliente de e-mail não suporta HTML.")
msg.add_alternative(html, subtype="html")

# Anexa a logo como imagem embutida (inline)
logo_path = os.path.join(os.getcwd(), "neoenergia.png")
if os.path.exists(logo_path):
    with open(logo_path, "rb") as img:
        msg.get_payload()[1].add_related(img.read(), 'image', 'png', cid='logo_neoenergia')
else:
    print("Logo não encontrada em:", logo_path)


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(REMETENTE, SENHADEAPP)
    smtp.send_message(msg, to_addrs=destinatarios)

print('E-mail de notificação enviado com sucesso!')
