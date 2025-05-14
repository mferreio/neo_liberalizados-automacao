class DiretrizCurtoPrazoPage:
    def __init__(self, driver):
        self.driver = driver

    def validar_ou_redirecionar_tela_diretriz_curto_prazo(self):
        url_esperada = "https://diretrizes.dev.neoenergia.net/pages/diretriz-irec/listar"
        if self.driver.current_url != url_esperada:
            print(f"Usuário NÃO foi encaminhado para a página correta. Redirecionando para: {url_esperada}")
            self.driver.get(url_esperada)
        else:
            print(f"Usuário já está na página correta: {url_esperada}")

    def validar_ou_redirecionar_tela_diretriz_curto_prazo_curto(self):
        url_esperada = "https://diretrizes.dev.neoenergia.net/pages/diretriz-curto-prazo/listar"
        if self.driver.current_url != url_esperada:
            print(f"Usuário NÃO foi encaminhado para a página correta. Redirecionando para: {url_esperada}")
            self.driver.get(url_esperada)
        else:
            print(f"Usuário já está na página correta: {url_esperada}")

    def validar_ou_redirecionar_tela_cadastro_diretriz_curto_prazo(self):
        url_esperada = "https://diretrizes.dev.neoenergia.net/pages/diretriz-curto-prazo/novo"
        if self.driver.current_url != url_esperada:
            print(f"Usuário NÃO foi encaminhado para a tela de cadastro correta. Redirecionando para: {url_esperada}")
            self.driver.get(url_esperada)
        else:
            print(f"Usuário já está na tela de cadastro correta: {url_esperada}")
