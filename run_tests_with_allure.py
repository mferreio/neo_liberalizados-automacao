import os
import subprocess
import sys
import logging
import shutil
import datetime
import stat
from features.utils_general import send_email, generate_evidence
from features.utils_allure import upload_to_github_pages

def remove_readonly(func, path, excinfo):
    """Remove o atributo somente leitura de arquivos/diretórios."""
    os.chmod(path, stat.S_IWRITE)
    func(path)

def run_tests():
    """Executa os testes com o Behave e gera relatórios para o Allure."""
    try:
        start_time = datetime.datetime.now()

        # Diretórios para relatórios
        allure_results_dir = "reports/allure-results"
        allure_report_dir = "reports/allure-report"
        evidence_dir = "reports/evidencias"

        # Limpa e cria os diretórios necessários
        for directory in [allure_results_dir, allure_report_dir, evidence_dir]:
                shutil.rmtree(directory, onexc=remove_readonly)
                shutil.rmtree(directory, onerror=remove_readonly)
                os.makedirs(directory, exist_ok=True)

        # Caminho do Allure CLI
        allure_executable = r"C:\allure\bin\allure.bat"
        if not os.path.exists(allure_executable):
            raise FileNotFoundError(f"Executável do Allure não encontrado: {allure_executable}")

        # Executa os testes com o Behave
        print("Executando os testes com o Behave...")
        behave_command = ["behave", "--no-capture", "-f", "allure_behave.formatter:AllureFormatter", "-o", allure_results_dir]
        feature_file = sys.argv[1] if len(sys.argv) > 1 else "features/login.feature"
        if feature_file:
            behave_command.append(feature_file)
        subprocess.run(behave_command, check=True)

        end_time = datetime.datetime.now()

        # Gera o relatório do Allure
        print("Gerando o relatório do Allure...")
        subprocess.run([allure_executable, "generate", allure_results_dir, "-o", allure_report_dir, "--clean"], check=True)

        # Envia o relatório para o GitHub Pages
        print("Enviando o relatório para o GitHub Pages...")
        repo_url = "https://github.com/mferreio/neo_liberalizados-automacao.git"
        upload_to_github_pages(allure_report_dir, repo_url)

        # Retorna o contexto necessário para o envio de e-mail
        allure_report_url = "https://mferreio.github.io/neo_liberalizados-automacao/"
        return {
            "allure_report_url": allure_report_url,
            "start_time": start_time,
            "end_time": end_time,
        }

    except Exception as e:
        logging.error(f"Erro durante a execução dos testes: {e}")
        raise

if __name__ == "__main__":
    try:
        email_context = run_tests()
        evidence_path = generate_evidence()

        email_subject = "Relatório de Resultados dos Testes Automatizados"
        email_body = f"""
        <html>
        <body>
            <p>Prezados,</p>
            <p>Segue o relatório detalhado dos testes realizados em {datetime.datetime.now().strftime('%d/%m/%Y')}.</p>
            <ul>
                <li><strong>Tempo total de execução:</strong> {(email_context["end_time"] - email_context["start_time"]).total_seconds() / 60:.2f} minutos</li>
                <li><strong>Link do relatório Allure:</strong> <a href="{email_context["allure_report_url"]}" target="_blank">Clique aqui</a></li>
            </ul>
            <p>Atenciosamente,</p>
            <p><strong>Equipe de Automação de Testes</strong></p>
        </body>
        </html>
        """
        send_email(subject=email_subject, body=email_body, recipient_email="matheus.drens@gmail.com", attachment_path=evidence_path)
        print("E-mail enviado com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao enviar o e-mail: {e}")
