# language: pt
Funcionalidade: Testes de API de Produtos, Carrinho e Pedidos
  Como sistema consumidor da API da Verzel Store
  Quero calcular carrinhos e criar pedidos com validações estritas
  Para garantir a integridade das regras de negócio no backend

  @api @smoke
  Cenário: Listagem completa de produtos via API
    Quando o cliente consulta a rota GET "/api/produtos"
    Então o status code da resposta deve ser 200
    E a resposta deve conter uma lista com 8 produtos

  @api
  Cenário: Consulta de produto por ID existente
    Quando o cliente consulta a rota GET "/api/produtos/P001"
    Então o status code da resposta deve ser 200
    E o produto retornado deve ter o nome "Camiseta Essencial" e preço 59.9

  @api
  Cenário: Consulta de produto com ID inexistente
    Quando o cliente consulta a rota GET "/api/produtos/P999"
    Então o status code da resposta deve ser 404
    E o código de erro retornado deve ser "PRODUTO_NAO_ENCONTRADO"

  @api @ca01 @ca02
  Cenário: Cálculo do carrinho com cupom válido BEMVINDO10
    Quando o cliente envia uma requisição para POST "/api/carrinho/calcular" com o produto "P005", quantidade 1 e cupom " bemvindo10 "
    Então o status code da resposta deve ser 200
    E o subtotal calculado deve ser 100.0
    E o desconto calculado deve ser 10.0
    E o cupom deve ter o status aplicado igual a verdadeiro

  @api @ca03
  Cenário: Cálculo do carrinho com cupom inexistente não gera erro HTTP mas não aplica desconto
    Quando o cliente envia uma requisição para POST "/api/carrinho/calcular" com o produto "P005", quantidade 1 e cupom "INEXISTENTE"
    Então o status code da resposta deve ser 200
    E o desconto calculado deve ser 0.0
    E o cupom deve ter a mensagem "Cupom inválido."

  @api @ca04
  Cenário: Cálculo do carrinho com cupom expirado
    Quando o cliente envia uma requisição para POST "/api/carrinho/calcular" com o produto "P005", quantidade 1 e cupom "VERAO2026"
    Então o status code da resposta deve ser 200
    E o desconto calculado deve ser 0.0
    E o cupom deve ter a mensagem "Cupom expirado."

  @api
  Cenário: Validação de lista de itens vazia no cálculo do carrinho
    Quando o cliente envia uma requisição de cálculo com lista de itens vazia
    Então o status code da resposta deve ser 422
    E o código de erro retornado deve ser "ITENS_OBRIGATORIOS"

  @api
  Cenário: Validação de quantidade negativa ou zero no cálculo do carrinho
    Quando o cliente envia uma requisição de cálculo com o produto "P001" e quantidade 0
    Então o status code da resposta deve ser 422
    E o código de erro retornado deve ser "QUANTIDADE_INVALIDA"

  @api @ca10
  Cenário: Rejeição de pedido com mais de 5 unidades por produto via API
    Quando o cliente envia uma requisição de pedido via API com 6 unidades do produto "P001"
    Então o status code da resposta deve ser 422
    E o código de erro retornado deve ser "QUANTIDADE_MAXIMA_EXCEDIDA"

  @api @e2e
  Cenário: Criação bem-sucedida de pedido via API
    Quando o cliente envia uma requisição de pedido com dados válidos e cupom "BEMVINDO10"
    Então o status code da resposta deve ser 201
    E a resposta deve conter um número de pedido no formato "VZ-000000"

  @api @ca03
  Cenário: Rejeição de pedido com cupom inexistente via API
    Quando o cliente envia uma requisição de pedido com cupom "INEXISTENTE"
    Então o status code da resposta deve ser 422
    E o código de erro retornado deve ser "CUPOM_INVALIDO"

  @api @ca04
  Cenário: Rejeição de pedido com cupom expirado via API
    Quando o cliente envia uma requisição de pedido com cupom "VERAO2026"
    Então o status code da resposta deve ser 422
    E o código de erro retornado deve ser "CUPOM_EXPIRADO"

  @api
  Cenário: Rejeição de pedido com dados de cliente incompletos via API
    Quando o cliente envia uma requisição de pedido com nome sem sobrenome
    Então o status code da resposta deve ser 422
    E o código de erro retornado deve ser "DADOS_INVALIDOS"
