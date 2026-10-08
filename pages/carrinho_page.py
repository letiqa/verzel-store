from typing import Optional
from playwright.sync_api import Page
from pages.base_page import BasePage

class CarrinhoPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.campo_cupom = page.locator("#campo-cupom")
        self.btn_aplicar_cupom = page.locator("button:has-text('Aplicar cupom')")
        self.btn_remover_cupom = page.locator("button:has-text('Remover cupom')")
        self.bloco_cupom_aplicado = page.locator(".cupom-aplicado")
        self.alerta_cupom = page.locator("[role='alert'], .mensagem-erro")
        self.lbl_subtotal = page.locator("[data-valor='subtotal']")
        self.lbl_desconto = page.locator("[data-valor='desconto']")
        self.lbl_frete = page.locator("[data-valor='frete']")
        self.lbl_total = page.locator("[data-valor='total']")
        self.aviso_frete = page.locator(".aviso-frete")
        self.btn_finalizar = page.locator("a:has-text('Finalizar compra')")
        self.btn_esvaziar = page.locator("button:has-text('Esvaziar carrinho')")

    def abrir(self):
        self.navigate("/carrinho")

    def carrinho_vazio(self) -> bool:
        return self.page.locator(".item-carrinho").count() == 0

    def _item(self, nome: str):
        return self.page.locator(".item-carrinho", has=self.page.locator("h3", has_text=nome))

    def obter_quantidade(self, nome: str) -> int:
        return int(self._item(nome).locator("output").inner_text().strip())

    def incrementar_quantidade(self, nome: str):
        self._item(nome).locator("button", has_text="+").click()
        self.page.wait_for_timeout(200)

    def decrementar_quantidade(self, nome: str):
        self._item(nome).locator("button", has_text="-").click()
        self.page.wait_for_timeout(200)

    def botao_incrementar_desabilitado(self, nome: str) -> bool:
        return self._item(nome).locator("button", has_text="+").is_disabled()

    def remover_item(self, nome: str):
        self._item(nome).locator("button", has_text="Remover").click()
        self.page.wait_for_timeout(200)

    def esvaziar_carrinho(self):
        self.btn_esvaziar.click()
        self.page.wait_for_timeout(200)

    def aplicar_cupom(self, codigo: str):
        self.campo_cupom.fill(codigo)
        self.btn_aplicar_cupom.click()
        self.page.wait_for_timeout(300)

    def obter_mensagem_erro_cupom(self) -> str:
        return self.alerta_cupom.inner_text().strip() if self.alerta_cupom.is_visible() else ""

    def cupom_esta_aplicado(self, codigo: str = "") -> bool:
        if not self.bloco_cupom_aplicado.is_visible():
            return False
        return codigo.upper() in self.bloco_cupom_aplicado.inner_text().upper() if codigo else True

    def remover_cupom(self):
        self.btn_remover_cupom.click()
        self.page.wait_for_timeout(300)

    def campo_cupom_visivel(self) -> bool:
        return self.campo_cupom.is_visible()

    def obter_subtotal(self) -> float:
        return self.parse_currency(self.lbl_subtotal.inner_text())

    def obter_desconto(self) -> float:
        return abs(self.parse_currency(self.lbl_desconto.inner_text())) if self.lbl_desconto.is_visible() else 0.0

    def obter_frete_texto(self) -> str:
        return self.lbl_frete.inner_text().strip()

    def obter_frete_valor(self) -> float:
        return self.parse_currency(self.obter_frete_texto())

    def obter_total(self) -> float:
        return self.parse_currency(self.lbl_total.inner_text())

    def obter_aviso_frete(self) -> Optional[str]:
        return self.aviso_frete.inner_text().strip() if self.aviso_frete.is_visible() else None

    def finalizar_compra(self):
        self.btn_finalizar.click()
        self.page.wait_for_load_state("networkidle")
