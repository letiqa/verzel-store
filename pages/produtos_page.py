from playwright.sync_api import Page
from pages.base_page import BasePage

class ProdutosPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.link_carrinho = page.locator(".link-carrinho")

    def abrir(self):
        self.navigate("/")

    def adicionar_produto_por_nome(self, nome_produto: str):
        card = self.page.locator(".produto", has=self.page.locator("h3", has_text=nome_produto))
        card.locator("button", has_text="Adicionar ao carrinho").click()
        self.page.wait_for_timeout(200)

    def ir_para_carrinho(self):
        self.link_carrinho.click()
        self.page.wait_for_load_state("networkidle")
