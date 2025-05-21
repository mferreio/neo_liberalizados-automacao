import datetime
import logging
import os
import shutil
import stat
import subprocess
import sys

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
            shutil.rmtree(directory, onexc=remove_readonly, ignore_errors=True)
            os.makedirs(directory, exist_ok=True)

        # Caminho do Allure CLI
        allure_executable = r"C:\allure\bin\allure.bat"
        if not os.path.exists(allure_executable):
            raise FileNotFoundError(
                f"Executável do Allure não encontrado: {allure_executable}"
            )

        # Executa os testes com o Behave
        print("Executando os testes com o Behave...")
        behave_command = [
            "behave",
            "--no-capture",
            "-f",
            "allure_behave.formatter:AllureFormatter",
            "-o",
            allure_results_dir,
        ]
        feature_file = sys.argv[1] if len(sys.argv) > 1 else "features/login.feature"
        if feature_file:
            behave_command.append(feature_file)
        subprocess.run(behave_command, check=True)

        end_time = datetime.datetime.now()

        # Gera o relatório do Allure
        print("Gerando o relatório do Allure...")
        subprocess.run(
            [
                allure_executable,
                "generate",
                allure_results_dir,
                "-o",
                allure_report_dir,
                "--clean",
            ],
            check=True,
        )

        # Envia o relatório para o GitHub Pages
        print("Enviando o relatório para o GitHub Pages...")
        # upload_to_github_pages(allure_report_dir, repo_url)  # Removido: função não definida

        # Retorna o contexto necessário
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
        run_tests()
        print("Testes executados com sucesso!")
    except Exception as e:
        logging.error(f"Erro durante a execução dos testes: {e}")
