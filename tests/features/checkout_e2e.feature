# language: pt
Funcionalidade: Fluxo Completo de Checkout e Confirmação de Pedido
  Como cliente da Verzel Store
  Quero finalizar minha compra informando meus dados de entrega
  Para receber meu pedido e pagar na entrega

  Contexto:
    Dado que o cliente está na página inicial da Verzel Store

  @e2e @ui
  Cenário: Finalização de pedido com cupom de desconto aplicado
    Dado que o cliente adicionou o produto "Mochila Urbana 20L" ao carrinho
    E navega para a página do carrinho
    E o cliente aplica o cupom "BEMVINDO10"
    Quando o cliente clica em "Finalizar compra"
    E preenche o formulário de entrega com nome "Maria Silva", email "maria@exemplo.com" e cep "01310-100"
    E clica em "Confirmar pedido"
    Então a página de confirmação de pedido deve ser exibida
    E um número de pedido válido no formato "VZ-000000" deve ser gerado

  @checkout @ui
  Cenário: Validação de nome sem sobrenome
    Dado que o cliente adicionou o produto "Camiseta Essencial" ao carrinho
    E navega para a página do carrinho
    Quando o cliente clica em "Finalizar compra"
    E preenche o formulário de entrega com nome "Maria", email "maria@exemplo.com" e cep "01310-100"
    E clica em "Confirmar pedido"
    Então deve ser exibida a mensagem de erro "Informe nome e sobrenome."

  @checkout @ui
  Cenário: Validação de e-mail em formato inválido
    Dado que o cliente adicionou o produto "Camiseta Essencial" ao carrinho
    E navega para a página do carrinho
    Quando o cliente clica em "Finalizar compra"
    E preenche o formulário de entrega com nome "Maria Silva", email "email_invalido" e cep "01310-100"
    E clica em "Confirmar pedido"
    Então deve ser exibida a mensagem de erro "Informe um e-mail válido."

  @checkout @ui
  Cenário: Validação de CEP incompleto
    Dado que o cliente adicionou o produto "Camiseta Essencial" ao carrinho
    E navega para a página do carrinho
    Quando o cliente clica em "Finalizar compra"
    E preenche o formulário de entrega com nome "Maria Silva", email "maria@exemplo.com" e cep "123"
    E clica em "Confirmar pedido"
    Então deve ser exibida a mensagem de erro "Informe um CEP com 8 dígitos."

  @checkout @ui
  Cenário: Aceitação de CEP válido sem hífen
    Dado que o cliente adicionou o produto "Camiseta Essencial" ao carrinho
    E navega para a página do carrinho
    Quando o cliente clica em "Finalizar compra"
    E preenche o formulário de entrega com nome "Carlos Andrade", email "carlos@exemplo.com" e cep "01310100"
    E clica em "Confirmar pedido"
    Então a página de confirmação de pedido deve ser exibida
