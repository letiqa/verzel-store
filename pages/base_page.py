import re
from playwright.sync_api import Page
from config.settings import BASE_URL

class BasePage:
    def __init__(self, page: Page, base_url: str = BASE_URL):
        self.page = page
        self.base_url = base_url

    def navigate(self, path: str = ""):
        url = f"{self.base_url}{path}" if path.startswith("/") else f"{self.base_url}/{path}"
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")

    @staticmethod
    def parse_currency(text: str) -> float:
        """Converte valores como 'R$ 59,90', '- R$ 5,99' ou 'Grátis' para float."""
        if not text:
            return 0.0
        cleaned = text.strip()
        if "grátis" in cleaned.lower() or "gratis" in cleaned.lower():
            return 0.0
        is_negative = "-" in cleaned
        digits = re.sub(r"[^\d,]", "", cleaned)
        val = float(digits.replace(",", ".")) if digits else 0.0
        return -val if is_negative else val
