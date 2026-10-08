# language: pt
Funcionalidade: Regras de Frete e Frete Grátis
  Como cliente da Verzel Store
  Quero saber as condições de frete e obter frete grátis em compras maiores
  Para economizar nas compras da loja

  Contexto:
    Dado que o cliente está na página inicial da Verzel Store

  @ca06 @ui
  Cenário: Frete grátis para compras com subtotal acima de R$ 200,00
    Dado que o cliente adicionou o produto "Jaqueta Corta-Vento" ao carrinho
    E navega para a página do carrinho
    Então o valor do frete deve ser exibido como "Grátis"
    E a mensagem de valor faltante para frete grátis não deve ser exibida

  @ca06 @ui
  Cenário: Frete grátis para compras com subtotal exatamente igual a R$ 200,00
    Dado que o cliente adicionou o produto "Mochila Urbana 20L" ao carrinho
    E o cliente adicionou o produto "Mochila Urbana 20L" ao carrinho
    E navega para a página do carrinho
    Então o valor do frete deve ser exibido como "Grátis"

  @ca07 @ui
  Cenário: Cobrança de frete fixo de R$ 19,90 e mensagem de faltante para subtotal abaixo de R$ 200,00
    Dado que o cliente adicionou o produto "Camiseta Essencial" ao carrinho
    E navega para a página do carrinho
    Então o valor do frete deve ser de "R$ 19,90"
    E a mensagem informando quanto falta para o frete grátis deve ser exibida com valor correto

  @ca08 @ui
  Cenário: Frete grátis considera o subtotal antes do desconto do cupom
    Dado que o cliente adicionou o produto "Jaqueta Corta-Vento" ao carrinho
    E navega para a página do carrinho
    Quando o cliente aplica o cupom "BEMVINDO10"
    Então o valor do frete deve permanecer como "Grátis"
    E o valor do total deve ser igual ao subtotal menos o desconto

  @ca09 @ui
  Cenário: Desconto do cupom incide apenas sobre os produtos e não sobre o frete
    Dado que o cliente adicionou o produto "Mochila Urbana 20L" ao carrinho
    E navega para a página do carrinho
    Quando o cliente aplica o cupom "BEMVINDO10"
    Então o subtotal deve ser de R$ 100,00
    E o desconto deve ser exatamente R$ 10,00
    E o frete deve ser exatamente R$ 19,90
    E o valor total deve ser de R$ 109,90
