import re
from pytest_bdd import scenarios, when, then, parsers
from services.api_client import ApiClient

scenarios("../features/api_carrinho_pedidos.feature")

@when(parsers.parse('o cliente consulta a rota GET "{rota}"'))
def consultar_rota_get(api_client: ApiClient, rota: str, bdd_context: dict):
    if rota == "/api/produtos":
        resp = api_client.get_produtos()
    elif rota.startswith("/api/produtos/"):
        prod_id = rota.split("/")[-1]
        resp = api_client.get_produto_por_id(prod_id)
    else:
        resp = api_client.session.get(f"{api_client.base_url}{rota.replace('/api', '')}")
    bdd_context["response"] = resp

@then(parsers.parse("o status code da resposta deve ser {status_esperado:d}"))
def validar_status_code(bdd_context: dict, status_esperado: int):
    resp = bdd_context["response"]
    assert resp.status_code == status_esperado, f"Esperado status {status_esperado}, mas recebeu {resp.status_code}. Resposta: {resp.text}"

@then(parsers.parse("a resposta deve conter uma lista com {total:d} produtos"))
def validar_total_produtos(bdd_context: dict, total: int):
    dados = bdd_context["response"].json()
    assert isinstance(dados, list), "Resposta da API de produtos não é uma lista."
    assert len(dados) == total, f"Esperava {total} produtos, mas obteve {len(dados)}"

@then(parsers.parse('o produto retornado deve ter o nome "{nome_esperado}" e preço {preco_esperado:f}'))
def validar_dados_produto(bdd_context: dict, nome_esperado: str, preco_esperado: float):
    dados = bdd_context["response"].json()
    assert dados.get("nome") == nome_esperado, f"Esperava nome '{nome_esperado}', mas obteve '{dados.get('nome')}'"
    assert round(dados.get("preco", 0), 2) == round(preco_esperado, 2)

@then(parsers.parse('o código de erro retornado deve ser "{codigo_erro}"'))
def validar_codigo_erro(bdd_context: dict, codigo_erro: str):
    dados = bdd_context["response"].json()
    erro = dados.get("erro", {})
    assert erro.get("codigo") == codigo_erro, f"Esperava código de erro '{codigo_erro}', mas obteve '{erro.get('codigo')}'. Detalhes: {erro}"

@when(parsers.parse('o cliente envia uma requisição para POST "/api/carrinho/calcular" com o produto "{produto_id}", quantidade {quantidade:d} e cupom "{cupom}"'))
def calcular_carrinho_com_cupom(api_client: ApiClient, produto_id: str, quantidade: int, cupom: str, bdd_context: dict):
    resp = api_client.calcular_carrinho(
        itens=[{"produtoId": produto_id, "quantidade": quantidade}],
        cupom=cupom
    )
    bdd_context["response"] = resp

@then(parsers.parse("o subtotal calculado deve ser {subtotal_esperado:f}"))
def validar_subtotal_calculado(bdd_context: dict, subtotal_esperado: float):
    dados = bdd_context["response"].json()
    assert round(dados.get("subtotal", 0), 2) == round(subtotal_esperado, 2)

@then(parsers.parse("o desconto calculado deve ser {desconto_esperado:f}"))
def validar_desconto_calculado(bdd_context: dict, desconto_esperado: float):
    dados = bdd_context["response"].json()
    assert round(dados.get("desconto", 0), 2) == round(desconto_esperado, 2)

@then("o cupom deve ter o status aplicado igual a verdadeiro")
def validar_cupom_aplicado_true(bdd_context: dict):
    dados = bdd_context["response"].json()
    cupom = dados.get("cupom", {})
    assert cupom and cupom.get("aplicado") is True, f"Esperava cupom.aplicado == True, mas obteve {cupom}"

@then(parsers.parse('o cupom deve ter a mensagem "{mensagem_esperada}"'))
def validar_mensagem_cupom(bdd_context: dict, mensagem_esperada: str):
    dados = bdd_context["response"].json()
    cupom = dados.get("cupom", {})
    assert cupom and cupom.get("mensagem") == mensagem_esperada, f"Esperava mensagem '{mensagem_esperada}', mas obteve '{cupom.get('mensagem')}'"

@when("o cliente envia uma requisição de cálculo com lista de itens vazia")
def calcular_carrinho_vazio(api_client: ApiClient, bdd_context: dict):
    resp = api_client.calcular_carrinho(itens=[])
    bdd_context["response"] = resp

@when(parsers.parse('o cliente envia uma requisição de cálculo com o produto "{produto_id}" e quantidade {quantidade:d}'))
def calcular_carrinho_quantidade(api_client: ApiClient, produto_id: str, quantidade: int, bdd_context: dict):
    resp = api_client.calcular_carrinho(itens=[{"produtoId": produto_id, "quantidade": quantidade}])
    bdd_context["response"] = resp

@when(parsers.parse('o cliente envia uma requisição de pedido com dados válidos e cupom "{cupom}"'))
def criar_pedido_valido(api_client: ApiClient, cupom: str, bdd_context: dict):
    resp = api_client.criar_pedido(
        cliente={"nome": "João Santos", "email": "joao@exemplo.com", "cep": "01310-100"},
        itens=[{"produtoId": "P001", "quantidade": 1}],
        cupom=cupom
    )
    bdd_context["response"] = resp

@then(parsers.parse('a resposta deve conter um número de pedido no formato "{formato}"'))
def validar_formato_numero_pedido(bdd_context: dict, formato: str):
    dados = bdd_context["response"].json()
    numero = dados.get("numero")
    assert numero is not None, f"Número do pedido ausente na resposta: {dados}"
    assert re.match(r"^VZ-\d{6}$", numero), f"Número '{numero}' não corresponde ao formato {formato}"

@when(parsers.parse('o cliente envia uma requisição de pedido com cupom "{cupom}"'))
def criar_pedido_cupom_invalido(api_client: ApiClient, cupom: str, bdd_context: dict):
    resp = api_client.criar_pedido(
        cliente={"nome": "João Santos", "email": "joao@exemplo.com", "cep": "01310-100"},
        itens=[{"produtoId": "P001", "quantidade": 1}],
        cupom=cupom
    )
    bdd_context["response"] = resp

@when("o cliente envia uma requisição de pedido com nome sem sobrenome")
def criar_pedido_nome_invalido(api_client: ApiClient, bdd_context: dict):
    resp = api_client.criar_pedido(
        cliente={"nome": "João", "email": "joao@exemplo.com", "cep": "01310-100"},
        itens=[{"produtoId": "P001", "quantidade": 1}]
    )
    bdd_context["response"] = resp

@when(parsers.parse('o cliente envia uma requisição de pedido via API com 6 unidades do produto "{produto_id}"'))
def criar_pedido_seis_unidades(api_client: ApiClient, produto_id: str, bdd_context: dict):
    resp = api_client.criar_pedido(
        cliente={"nome": "Roberta Alves", "email": "roberta@exemplo.com", "cep": "01310-100"},
        itens=[{"produtoId": produto_id, "quantidade": 6}]
    )
    bdd_context["response"] = resp
