import os
import subprocess
import sys
from features.environment import send_email_report, generate_pdf_report  # Importa a função para gerar o PDF
import logging
import shutil  # Para limpar diretórios
import stat  # Para redefinir permissões de arquivos/diretórios

def remove_readonly(func, path, excinfo):
    """Remove o atributo somente leitura de arquivos/diretórios."""
    os.chmod(path, stat.S_IWRITE)
    func(path)

def upload_to_github_pages(report_dir, repo_url, branch="main"):
    """Faz o upload do relatório Allure para o GitHub Pages."""
    try:
        # Diretório temporário para o repositório
        temp_repo_dir = "temp_repo"

        # Clona o repositório
        if os.path.exists(temp_repo_dir):
            try:
                shutil.rmtree(temp_repo_dir, onerror=remove_readonly)
            except Exception as e:
                print(f"Erro ao limpar o diretório {temp_repo_dir}: {e}")
                raise
        subprocess.run(["git", "clone", repo_url, temp_repo_dir], check=True)

        # Copia os arquivos do relatório para o diretório allure-report no repositório
        allure_report_dir = os.path.join(temp_repo_dir, "allure-report")
        if os.path.exists(allure_report_dir):
            try:
                shutil.rmtree(allure_report_dir, onerror=remove_readonly)
            except Exception as e:
                print(f"Erro ao limpar o diretório {allure_report_dir}: {e}")
                raise
        shutil.copytree(report_dir, allure_report_dir)

        # Faz o commit e o push para o repositório
        os.chdir(temp_repo_dir)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Atualização do relatório Allure"], check=True)
        subprocess.run(["git", "push", "origin", branch], check=True)
        os.chdir("..")  # Retorna ao diretório original

        # Remove o diretório temporário
        try:
            shutil.rmtree(temp_repo_dir, onerror=remove_readonly)
        except Exception as e:
            print(f"Erro ao remover o diretório {temp_repo_dir}: {e}")
            raise
        print(f"Relatório enviado para o GitHub Pages: {repo_url}/allure-report")
    except Exception as e:
        print(f"Erro ao enviar o relatório para o GitHub Pages: {e}")
        raise

def run_tests():
    """Executa os testes com o behave e gera relatórios para o Allure."""
    try:
        # Diretórios para relatórios
        allure_results_dir = "reports/allure-results"
        allure_report_dir = "reports/allure-report"
        evidence_dir = "reports/evidencias"

        # Limpa o diretório de resultados do Allure antes de executar os testes
        if os.path.exists(allure_results_dir):
            try:
                shutil.rmtree(allure_results_dir, onerror=remove_readonly)
            except Exception as e:
                raise PermissionError(f"Erro ao limpar o diretório {allure_results_dir}: {e}")
        os.makedirs(allure_results_dir, exist_ok=True)
        os.makedirs(allure_report_dir, exist_ok=True)
        os.makedirs(evidence_dir, exist_ok=True)

        # Caminho do Allure CLI
        allure_executable = r"C:\allure\bin\allure.bat"
        if not os.path.exists(allure_executable):
            raise FileNotFoundError(f"Executável do Allure não encontrado: {allure_executable}")

        # Verifica se o Allure CLI está acessível
        try:
            subprocess.run([allure_executable, "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Erro ao verificar o Allure CLI: {e.stderr.decode(errors='replace')}")

        # Executa os testes com o Behave
        print("Executando os testes com o Behave...")
        behave_command = ["behave", "--no-capture", "-f", "allure_behave.formatter:AllureFormatter", "-o", allure_results_dir]
        feature_file = sys.argv[1] if len(sys.argv) > 1 else ""
        if feature_file:
            behave_command.append(feature_file)
        try:
            result = subprocess.run(behave_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(result.stdout.decode(errors='replace'))  # Decodifica a saída ignorando erros
        except subprocess.CalledProcessError as e:
            print("Erro ao executar os testes com o Behave:")
            print(e.stderr.decode(errors='replace'))  # Decodifica a saída de erro ignorando erros
            # Continua o fluxo mesmo que os testes falhem
            test_failed = True
        else:
            test_failed = False

        # Gera o relatório do Allure
        print("Gerando o relatório do Allure...")
        subprocess.run([allure_executable, "generate", allure_results_dir, "-o", allure_report_dir, "--clean"], check=True)

        # Verifica se o relatório foi gerado corretamente
        if not os.path.exists(os.path.join(allure_report_dir, "index.html")):
            raise FileNotFoundError(f"O relatório Allure não foi gerado no diretório: {allure_report_dir}")

        # Gera o relatório PDF
        print("Gerando o relatório PDF...")
        passed_steps = []  # Substitua por dados reais coletados durante a execução
        failed_steps = []  # Substitua por dados reais coletados durante a execução
        generate_pdf_report({
            "passed_steps": passed_steps,
            "failed_steps": failed_steps
        })

        # Envia o relatório para o GitHub Pages
        print("Enviando o relatório para o GitHub Pages...")
        repo_url = "https://github.com/mferreio/neo_liberalizados-automacao.git"  # URL do repositório existente
        upload_to_github_pages(allure_report_dir, repo_url)

    except Exception as e:
        print(f"Erro durante a execução dos testes: {e}")
        test_failed = True

    # Envia o e-mail com o relatório, independentemente do resultado dos testes
    try:
        print("Enviando o e-mail com o relatório...")
        email_context = {
            "allure_report_path": os.path.join(allure_report_dir, "index.html"),
            "pdf_report_path": os.path.join(evidence_dir, "Relatorio_de_Teste.pdf"),
            "test_failed": test_failed
        }
        send_email_report(email_context)
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")

if __name__ == "__main__":
    run_tests()
