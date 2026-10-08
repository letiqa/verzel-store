import re
from pytest_bdd import scenarios, when, then, parsers
from pages.carrinho_page import CarrinhoPage

scenarios("../features/carrinho_limites.feature")


@when(parsers.parse('o cliente tenta aumentar a quantidade do produto "{nome_produto}" até atingir 5 unidades'))
def aumentar_ate_limite(carrinho_page: CarrinhoPage, nome_produto: str):
    for _ in range(6):
        if not carrinho_page.botao_incrementar_desabilitado(nome_produto):
            carrinho_page.incrementar_quantidade(nome_produto)

@when(parsers.parse('o cliente diminui a quantidade do produto "{nome_produto}" em 1 unidade'))
def diminuir_uma_unidade(carrinho_page: CarrinhoPage, nome_produto: str):
    carrinho_page.decrementar_quantidade(nome_produto)

@then(parsers.parse('a quantidade exibida para "{nome_produto}" deve ser {quantidade_esperada:d}'))
def validar_quantidade(carrinho_page: CarrinhoPage, nome_produto: str, quantidade_esperada: int):
    qtd = carrinho_page.obter_quantidade(nome_produto)
    assert qtd == quantidade_esperada, f"Esperado {quantidade_esperada}, mas obteve {qtd}"

@then("o botão de aumentar quantidade deve ficar desabilitado")
def validar_botao_aumentar_desabilitado(carrinho_page: CarrinhoPage):
    assert carrinho_page.botao_incrementar_desabilitado("Camiseta Essencial"), "Botão + deveria estar desabilitado."

@then("o botão de aumentar quantidade deve ficar habilitado")
def validar_botao_aumentar_habilitado(carrinho_page: CarrinhoPage):
    assert not carrinho_page.botao_incrementar_desabilitado("Camiseta Essencial"), "Botão + deveria estar habilitado."

@then("todos os valores exibidos devem possuir formatação com centavos válidos")
def validar_formato_centavos(carrinho_page: CarrinhoPage):
    subtotal = carrinho_page.lbl_subtotal.inner_text()
    desconto = carrinho_page.lbl_desconto.inner_text()
    total = carrinho_page.lbl_total.inner_text()
    
    padrao = r"R\$\s*\d+,\d{2}"
    assert re.search(padrao, subtotal), f"Subtotal '{subtotal}' não tem formato com 2 casas decimais"
    assert re.search(padrao, desconto), f"Desconto '{desconto}' não tem formato com 2 casas decimais"
    assert re.search(padrao, total), f"Total '{total}' não tem formato com 2 casas decimais"

@when(parsers.parse('o cliente remove o produto "{nome_produto}" do carrinho'))
def remover_produto(carrinho_page: CarrinhoPage, nome_produto: str):
    carrinho_page.remover_item(nome_produto)

@when("o cliente clica para esvaziar o carrinho")
def clicar_esvaziar(carrinho_page: CarrinhoPage):
    carrinho_page.esvaziar_carrinho()

@then("o carrinho deve ficar vazio")
def validar_carrinho_vazio(carrinho_page: CarrinhoPage):
    assert carrinho_page.carrinho_vazio(), "O carrinho não ficou vazio após remoção/esvaziamento."
