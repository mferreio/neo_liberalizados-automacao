import os
import shutil
import subprocess
import logging
import stat

def remove_readonly(func, path, excinfo):
    """Remove o atributo somente leitura de arquivos/diretórios."""
    os.chmod(path, stat.S_IWRITE)
    func(path)

def upload_to_github_pages(report_dir, repo_url, branch="allure_report"):
    """Faz o upload do relatório Allure para o GitHub Pages na branch 'allure_report'."""
    try:
        if not os.path.exists(report_dir):
            raise FileNotFoundError(f"Diretório do relatório Allure não encontrado: {report_dir}")
        logging.info(f"Iniciando upload do relatório Allure do diretório: {report_dir}")

        temp_repo_dir = "temp_repo"

        # Clona o repositório na branch especificada
        if os.path.exists(temp_repo_dir):
            shutil.rmtree(temp_repo_dir, onerror=remove_readonly)
        subprocess.run(["git", "clone", "--branch", branch, repo_url, temp_repo_dir], check=True)

        # Copia os arquivos do relatório para a raiz do repositório
        for item in os.listdir(report_dir):
            source_path = os.path.join(report_dir, item)
            dest_path = os.path.join(temp_repo_dir, item)
            if os.path.isdir(source_path):
                if os.path.exists(dest_path):
                    shutil.rmtree(dest_path, onerror=remove_readonly)
                shutil.copytree(source_path, dest_path)
            else:
                shutil.copy2(source_path, dest_path)

        # Faz o commit e o push para o repositório
        os.chdir(temp_repo_dir)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Atualização do relatório Allure"], check=True)
        subprocess.run(["git", "push", "origin", branch], check=True)
        os.chdir("..")

        # Remove o diretório temporário
        shutil.rmtree(temp_repo_dir, onerror=remove_readonly)
        logging.info(f"Relatório enviado para o GitHub Pages: https://mferreio.github.io/neo_liberalizados-automacao/")
    except Exception as e:
        logging.error(f"Erro ao enviar o relatório para o GitHub Pages: {e}")
        raise
