import re
from pytest_bdd import scenarios, when, then, parsers
from pages.carrinho_page import CarrinhoPage
from pages.checkout_page import CheckoutPage

scenarios("../features/checkout_e2e.feature")


@when('o cliente clica em "Finalizar compra"')
def clicar_finalizar_compra(carrinho_page: CarrinhoPage):
    carrinho_page.finalizar_compra()

@when(parsers.parse('preenche o formulário de entrega com nome "{nome}", email "{email}" e cep "{cep}"'))
def preencher_formulario(checkout_page: CheckoutPage, nome: str, email: str, cep: str):
    checkout_page.preencher_dados(nome=nome, email=email, cep=cep)

@when('clica em "Confirmar pedido"')
def clicar_confirmar_pedido(checkout_page: CheckoutPage):
    checkout_page.confirmar_pedido()

@then("a página de confirmação de pedido deve ser exibida")
def validar_pagina_confirmacao(checkout_page: CheckoutPage):
    assert checkout_page.pedido_confirmado(), "Não foi redirecionado para a tela de confirmação de pedido."

@then(parsers.parse('um número de pedido válido no formato "{formato}" deve ser gerado'))
def validar_numero_pedido(checkout_page: CheckoutPage, formato: str):
    numero = checkout_page.obter_numero_pedido()
    assert numero is not None, "Número de pedido não foi encontrado na página de confirmação."
    assert re.match(r"^VZ-\d{6}$", numero), f"Número do pedido '{numero}' não segue o formato {formato}."

@then(parsers.parse('deve ser exibida a mensagem de erro "{mensagem_erro}"'))
def validar_mensagem_erro_checkout(checkout_page: CheckoutPage, mensagem_erro: str):
    erros = checkout_page.obter_erros_validacao()
    assert any(mensagem_erro in e for e in erros), f"Esperava '{mensagem_erro}' entre os erros: {erros}"
