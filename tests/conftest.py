import allure
import pytest
from typing import Dict, Any
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext
from pytest_bdd import given, when, parsers
from pages.produtos_page import ProdutosPage
from pages.carrinho_page import CarrinhoPage
from pages.checkout_page import CheckoutPage
from services.api_client import ApiClient

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True)
    yield browser
    browser.close()

@pytest.fixture
def context(browser: Browser):
    context = browser.new_context(viewport={"width": 1280, "height": 720}, locale="pt-BR")
    yield context
    context.close()

@pytest.fixture
def page(context: BrowserContext):
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture
def produtos_page(page: Page) -> ProdutosPage:
    return ProdutosPage(page)

@pytest.fixture
def carrinho_page(page: Page) -> CarrinhoPage:
    return CarrinhoPage(page)

@pytest.fixture
def checkout_page(page: Page) -> CheckoutPage:
    return CheckoutPage(page)

@pytest.fixture
def api_client() -> ApiClient:
    return ApiClient()

@pytest.fixture
def bdd_context() -> Dict[str, Any]:
    return {}

# --- Passos Gherkin compartilhados ---

@given("que o cliente está na página inicial da Verzel Store")
def abrir_pagina_inicial(produtos_page: ProdutosPage):
    produtos_page.abrir()

@given(parsers.parse('que o cliente adicionou o produto "{nome_produto}" ao carrinho'))
@given(parsers.parse('o cliente adicionou o produto "{nome_produto}" ao carrinho'))
def adicionar_produto(produtos_page: ProdutosPage, nome_produto: str):
    produtos_page.adicionar_produto_por_nome(nome_produto)

@given("navega para a página do carrinho")
def navegar_para_carrinho(produtos_page: ProdutosPage):
    produtos_page.ir_para_carrinho()

@given(parsers.parse('o cliente aplica o cupom "{codigo_cupom}"'))
@when(parsers.parse('o cliente aplica o cupom "{codigo_cupom}"'))
def aplicar_cupom_global(carrinho_page: CarrinhoPage, codigo_cupom: str, bdd_context: dict):
    bdd_context["subtotal_inicial"] = carrinho_page.obter_subtotal()
    bdd_context["frete_inicial"] = carrinho_page.obter_frete_valor()
    carrinho_page.aplicar_cupom(codigo_cupom)

# --- Gestão de Defeitos Conhecidos identificados na fase exploratória manual ---

def pytest_collection_modifyitems(items):
    """
    Aplica xfail aos cenários com bugs conhecidos já documentados em BUG_REPORT.md.
    Isso documenta o defeito e mantém a suíte de regressão verde no pipeline,
    alertando como XPASS assim que a equipe de desenvolvimento publicar a correção.
    """
    for item in items:
        # BUG-001: Subtotal de exatamente R$ 200,00 cobrando frete
        if "exatamente_igual_a_r_20000" in item.name.lower():
            item.add_marker(
                pytest.mark.xfail(
                    reason="BUG-001: Backend cobra frete de R$ 19,90 no valor exato de R$ 200,00 (subtotal > 200 ao invés de >= 200). Ref: BUG_REPORT.md",
                    strict=False,
                )
            )
        # BUG-002: API permitindo pedidos com mais de 5 unidades por produto
        elif "mais_de_5_unidades" in item.name.lower():
            item.add_marker(
                pytest.mark.xfail(
                    reason="BUG-002: API aceita pedidos com mais de 5 unidades sem retornar 422 QUANTIDADE_MAXIMA_EXCEDIDA. Ref: BUG_REPORT.md",
                    strict=False,
                )
            )

# --- Hook para anexar captura de tela ao Allure em caso de falha ---

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page_fixture = item.funcargs.get("page")
        if page_fixture:
            screenshot = page_fixture.screenshot()
            allure.attach(
                screenshot,
                name="Screenshot da falha",
                attachment_type=allure.attachment_type.PNG,
            )
