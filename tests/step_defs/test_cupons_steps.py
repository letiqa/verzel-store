from pytest_bdd import scenarios, when, then, parsers
from pages.carrinho_page import CarrinhoPage

scenarios("../features/cupons.feature")

@then(parsers.parse('o cupom "{codigo_esperado}" deve ser exibido como aplicado'))
def validar_cupom_aplicado(carrinho_page: CarrinhoPage, codigo_esperado: str):
    assert carrinho_page.cupom_esta_aplicado(codigo_esperado), f"Cupom {codigo_esperado} não está visível como aplicado."

@then("o valor do desconto deve ser de 10% sobre o subtotal")
def validar_desconto_dez_porcento(carrinho_page: CarrinhoPage):
    subtotal = carrinho_page.obter_subtotal()
    desconto = carrinho_page.obter_desconto()
    desconto_esperado = round(subtotal * 0.10, 2)
    assert round(desconto, 2) == desconto_esperado, f"Esperado desconto de {desconto_esperado}, mas obteve {desconto}"

@then("o valor do frete não deve sofrer desconto")
def validar_frete_sem_desconto(carrinho_page: CarrinhoPage, bdd_context: dict):
    frete_atual = carrinho_page.obter_frete_valor()
    frete_inicial = bdd_context.get("frete_inicial")
    if frete_inicial is not None:
        assert frete_atual == frete_inicial, f"Frete mudou de {frete_inicial} para {frete_atual}"

@then(parsers.parse('a mensagem "{mensagem_esperada}" deve ser exibida'))
def validar_mensagem_alerta(carrinho_page: CarrinhoPage, mensagem_esperada: str):
    mensagem_obtida = carrinho_page.obter_mensagem_erro_cupom()
    assert mensagem_esperada in mensagem_obtida, f"Esperava '{mensagem_esperada}', mas obteve '{mensagem_obtida}'"

@then("nenhum desconto deve ser aplicado")
def validar_nenhum_desconto(carrinho_page: CarrinhoPage):
    desconto = carrinho_page.obter_desconto()
    assert desconto == 0.0, f"Desconto deveria ser 0, mas foi {desconto}"

@then("o subtotal permanece sem alteração")
def validar_subtotal_inalterado(carrinho_page: CarrinhoPage, bdd_context: dict):
    subtotal_atual = carrinho_page.obter_subtotal()
    subtotal_inicial = bdd_context.get("subtotal_inicial")
    if subtotal_inicial is not None:
        assert subtotal_atual == subtotal_inicial, f"Subtotal alterou de {subtotal_inicial} para {subtotal_atual}"

@then("o campo para digitar outro cupom não deve estar visível")
def validar_campo_cupom_oculto(carrinho_page: CarrinhoPage):
    assert not carrinho_page.campo_cupom_visivel(), "Campo de cupom ainda está visível após aplicar cupom."

@when("o cliente remove o cupom aplicado")
def remover_cupom(carrinho_page: CarrinhoPage):
    carrinho_page.remover_cupom()

@then("o campo de cupom deve ficar visível novamente")
def validar_campo_cupom_visivel(carrinho_page: CarrinhoPage):
    assert carrinho_page.campo_cupom_visivel(), "Campo de cupom deveria estar visível após remoção."

@then("nenhum desconto deve estar ativo")
def validar_sem_desconto_ativo(carrinho_page: CarrinhoPage):
    assert carrinho_page.obter_desconto() == 0.0, "Ainda há desconto ativo após remoção do cupom."
    assert not carrinho_page.cupom_esta_aplicado(), "Cupom ainda consta como aplicado."
