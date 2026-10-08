import re
from typing import List, Optional
from playwright.sync_api import Page
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.campo_nome = page.locator("#campo-nome")
        self.campo_email = page.locator("#campo-email")
        self.campo_cep = page.locator("#campo-cep")
        self.btn_confirmar = page.locator("button:has-text('Confirmar pedido')")
        self.mensagens_erro = page.locator("[role='alert'], .mensagem-erro")
        self.conteudo_principal = page.locator("main")

    def preencher_dados(self, nome: str = "", email: str = "", cep: str = ""):
        self.campo_nome.fill(nome)
        self.campo_email.fill(email)
        self.campo_cep.fill(cep)

    def confirmar_pedido(self):
        self.btn_confirmar.click()
        self.page.wait_for_timeout(500)

    def obter_erros_validacao(self) -> List[str]:
        return [el.inner_text().strip() for el in self.mensagens_erro.all() if el.is_visible()]

    def pedido_confirmado(self) -> bool:
        return "/pedido-confirmado" in self.page.url

    def obter_numero_pedido(self) -> Optional[str]:
        match = re.search(r"VZ-\d{6}", self.conteudo_principal.inner_text())
        return match.group(0) if match else None
