"""
Configurações globais e massa de dados fixa para a suíte de testes da Verzel Store.
"""

BASE_URL = "https://verzel-store.qa-test-verzel-store.workers.dev"
API_BASE_URL = f"{BASE_URL}/api"

TIMEOUT_DEFAULT = 10000  # ms
TIMEOUT_SHORT = 3000     # ms

# Catálogo fixo de produtos conforme especificações
PRODUTOS = {
    "P001": {
        "id": "P001",
        "nome": "Camiseta Essencial",
        "preco": 59.90,
        "categoria": "Vestuário",
    },
    "P002": {
        "id": "P002",
        "nome": "Calça Jeans Slim",
        "preco": 139.90,
        "categoria": "Vestuário",
    },
    "P003": {
        "id": "P003",
        "nome": "Tênis Casual Urbano",
        "preco": 189.90,
        "categoria": "Calçados",
    },
    "P004": {
        "id": "P004",
        "nome": "Boné Aba Curva",
        "preco": 49.90,
        "categoria": "Acessórios",
    },
    "P005": {
        "id": "P005",
        "nome": "Mochila Urbana 20L",
        "preco": 100.00,
        "categoria": "Acessórios",
    },
    "P006": {
        "id": "P006",
        "nome": "Kit 3 Pares de Meias",
        "preco": 29.90,
        "categoria": "Vestuário",
    },
    "P007": {
        "id": "P007",
        "nome": "Jaqueta Corta-Vento",
        "preco": 229.90,
        "categoria": "Vestuário",
    },
    "P008": {
        "id": "P008",
        "nome": "Garrafa Térmica 750ml",
        "preco": 50.00,
        "categoria": "Acessórios",
    },
}

# Cupons fixos e suas regras
CUPONS = {
    "BEMVINDO10": {
        "codigo": "BEMVINDO10",
        "desconto_percentual": 0.10,
        "status": "VALIDO",
    },
    "VERAO2026": {
        "codigo": "VERAO2026",
        "desconto_percentual": 0.15,
        "status": "EXPIRADO",
        "expiracao": "2026-03-31",
    },
}

# Constantes de regras de negócio
FRETE_FIXO = 19.90
LIMITE_FRETE_GRATIS = 200.00
LIMITE_MAXIMO_UNIDADES = 5
