import requests
from typing import Any, Dict, List, Optional
from config.settings import API_BASE_URL

class ApiClient:
    def __init__(self, base_url: str = API_BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def get_produtos(self) -> requests.Response:
        return self.session.get(f"{self.base_url}/produtos")

    def get_produto_por_id(self, produto_id: str) -> requests.Response:
        return self.session.get(f"{self.base_url}/produtos/{produto_id}")

    def calcular_carrinho(self, itens: List[Dict[str, Any]], cupom: Optional[str] = None) -> requests.Response:
        payload = {"itens": itens}
        if cupom is not None:
            payload["cupom"] = cupom
        return self.session.post(f"{self.base_url}/carrinho/calcular", json=payload)

    def criar_pedido(
        self,
        cliente: Dict[str, str],
        itens: List[Dict[str, Any]],
        cupom: Optional[str] = None
    ) -> requests.Response:
        payload = {"cliente": cliente, "itens": itens}
        if cupom is not None:
            payload["cupom"] = cupom
        return self.session.post(f"{self.base_url}/pedidos", json=payload)
