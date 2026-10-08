# language: pt
Funcionalidade: Aplicação de Cupons de Desconto no Carrinho
  Como cliente da Verzel Store
  Quero aplicar um cupom de desconto
  Para pagar menos nas minhas compras

  Contexto:
    Dado que o cliente está na página inicial da Verzel Store

  @ca01 @ui
  Cenário: Aplicação do cupom válido BEMVINDO10 com 10% de desconto
    Dado que o cliente adicionou o produto "Camiseta Essencial" ao carrinho
    E navega para a página do carrinho
    Quando o cliente aplica o cupom "BEMVINDO10"
    Então o cupom "BEMVINDO10" deve ser exibido como aplicado
    E o valor do desconto deve ser de 10% sobre o subtotal
    E o valor do frete não deve sofrer desconto

  @ca02 @ui
  Esquema do Cenário: Cupom BEMVINDO10 não diferencia maiúsculas de minúsculas e ignora espaços
    Dado que o cliente adicionou o produto "Camiseta Essencial" ao carrinho
    E navega para a página do carrinho
    Quando o cliente aplica o cupom "<codigo_cupom>"
    Então o cupom "BEMVINDO10" deve ser exibido como aplicado
    E o valor do desconto deve ser de 10% sobre o subtotal

    Exemplos:
      | codigo_cupom       |
      | bemvindo10         |
      | BEMVINDO10         |
      |  BEMVINDO10        |
      | BEMVINDO10         |
      |   bemvindo10       |
      | BemVindo10         |

  @ca03 @ui
  Cenário: Tentativa de aplicação de cupom inexistente
    Dado que o cliente adicionou o produto "Camiseta Essencial" ao carrinho
    E navega para a página do carrinho
    Quando o cliente aplica o cupom "CUPOM_INEXISTENTE"
    Então a mensagem "Cupom inválido." deve ser exibida
    E nenhum desconto deve ser aplicado
    E o subtotal permanece sem alteração

  @ca04 @ui
  Cenário: Tentativa de aplicação de cupom expirado
    Dado que o cliente adicionou o produto "Camiseta Essencial" ao carrinho
    E navega para a página do carrinho
    Quando o cliente aplica o cupom "VERAO2026"
    Então a mensagem "Cupom expirado." deve ser exibida
    E nenhum desconto deve ser aplicado

  @ca05 @ui
  Cenário: Aplicação de apenas um cupom por vez e substituição após remoção
    Dado que o cliente adicionou o produto "Camiseta Essencial" ao carrinho
    E navega para a página do carrinho
    Quando o cliente aplica o cupom "BEMVINDO10"
    Então o campo para digitar outro cupom não deve estar visível
    Quando o cliente remove o cupom aplicado
    Então o campo de cupom deve ficar visível novamente
    E nenhum desconto deve estar ativo
