from pytest_bdd import scenarios, then, parsers
from pages.carrinho_page import CarrinhoPage

scenarios("../features/frete.feature")

@then(parsers.parse('o valor do frete deve ser exibido como "{texto_frete}"'))
def validar_frete_texto(carrinho_page: CarrinhoPage, texto_frete: str):
    frete_texto = carrinho_page.obter_frete_texto()
    assert texto_frete.lower() in frete_texto.lower(), f"Esperava frete '{texto_frete}', mas obteve '{frete_texto}'"

@then("a mensagem de valor faltante para frete grátis não deve ser exibida")
def validar_sem_mensagem_faltante(carrinho_page: CarrinhoPage):
    aviso = carrinho_page.obter_aviso_frete()
    assert aviso is None, f"Aviso de frete não deveria ser exibido, mas foi: '{aviso}'"

@then(parsers.parse('o valor do frete deve ser de "{valor_frete}"'))
def validar_frete_valor_texto(carrinho_page: CarrinhoPage, valor_frete: str):
    frete_texto = carrinho_page.obter_frete_texto()
    assert valor_frete in frete_texto, f"Esperava frete '{valor_frete}', mas obteve '{frete_texto}'"

@then("a mensagem informando quanto falta para o frete grátis deve ser exibida com valor correto")
def validar_mensagem_faltante_valor(carrinho_page: CarrinhoPage):
    subtotal = carrinho_page.obter_subtotal()
    faltante_esperado = round(200.00 - subtotal, 2)
    aviso = carrinho_page.obter_aviso_frete()
    assert aviso is not None, "Aviso de frete faltante deveria ser exibido."
    # Ex: 'Faltam R$ 140,10 para o frete grátis.'
    faltante_formatado = f"{faltante_esperado:.2f}".replace(".", ",")
    assert faltante_formatado in aviso, f"Esperava '{faltante_formatado}' na mensagem '{aviso}'"

@then(parsers.parse('o valor do frete deve permanecer como "{texto_frete}"'))
def validar_frete_permanece_gratis(carrinho_page: CarrinhoPage, texto_frete: str):
    frete_texto = carrinho_page.obter_frete_texto()
    assert texto_frete.lower() in frete_texto.lower(), f"Frete deveria permanecer '{texto_frete}', mas obteve '{frete_texto}'"

@then("o valor do total deve ser igual ao subtotal menos o desconto")
def validar_total_subtotal_menos_desconto(carrinho_page: CarrinhoPage):
    subtotal = carrinho_page.obter_subtotal()
    desconto = carrinho_page.obter_desconto()
    frete = carrinho_page.obter_frete_valor()
    total = carrinho_page.obter_total()
    total_esperado = round(subtotal - desconto + frete, 2)
    assert total == total_esperado, f"Esperado total {total_esperado}, mas obteve {total}"

@then("o subtotal deve ser de R$ 100,00")
def validar_subtotal_cem(carrinho_page: CarrinhoPage):
    assert carrinho_page.obter_subtotal() == 100.00

@then("o desconto deve ser exatamente R$ 10,00")
def validar_desconto_dez(carrinho_page: CarrinhoPage):
    assert carrinho_page.obter_desconto() == 10.00

@then("o frete deve ser exatamente R$ 19,90")
def validar_frete_dezenove_noventa(carrinho_page: CarrinhoPage):
    assert carrinho_page.obter_frete_valor() == 19.90

@then("o valor total deve ser de R$ 109,90")
def validar_total_cento_e_nove_noventa(carrinho_page: CarrinhoPage):
    assert carrinho_page.obter_total() == 109.90
