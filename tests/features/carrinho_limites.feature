# language: pt
Funcionalidade: Limites do Carrinho e Precisão Numérica
  Como cliente da Verzel Store
  Quero gerenciar quantidades e itens no carrinho
  Para que as compras respeitem as regras da loja

  Contexto:
    Dado que o cliente está na página inicial da Verzel Store

  @ca10 @ui
  Cenário: Limite máximo de 5 unidades por produto na interface
    Dado que o cliente adicionou o produto "Camiseta Essencial" ao carrinho
    E navega para a página do carrinho
    Quando o cliente tenta aumentar a quantidade do produto "Camiseta Essencial" até atingir 5 unidades
    Então a quantidade exibida para "Camiseta Essencial" deve ser 5
    E o botão de aumentar quantidade deve ficar desabilitado

  @ca10 @ui
  Cenário: Diminuir quantidade após atingir o limite reabilita a adição
    Dado que o cliente adicionou o produto "Camiseta Essencial" ao carrinho
    E navega para a página do carrinho
    Quando o cliente tenta aumentar a quantidade do produto "Camiseta Essencial" até atingir 5 unidades
    E o cliente diminui a quantidade do produto "Camiseta Essencial" em 1 unidade
    Então a quantidade exibida para "Camiseta Essencial" deve ser 4
    E o botão de aumentar quantidade deve ficar habilitado

  @ca11 @ui
  Cenário: Arredondamento correto de valores monetários com 2 casas decimais
    Dado que o cliente adicionou o produto "Camiseta Essencial" ao carrinho
    E o cliente adicionou o produto "Kit 3 Pares de Meias" ao carrinho
    E navega para a página do carrinho
    Quando o cliente aplica o cupom "BEMVINDO10"
    Então todos os valores exibidos devem possuir formatação com centavos válidos

  @ui
  Cenário: Remoção individual de item do carrinho
    Dado que o cliente adicionou o produto "Camiseta Essencial" ao carrinho
    E navega para a página do carrinho
    Quando o cliente remove o produto "Camiseta Essencial" do carrinho
    Então o carrinho deve ficar vazio

  @ui
  Cenário: Esvaziamento completo do carrinho
    Dado que o cliente adicionou o produto "Camiseta Essencial" ao carrinho
    E o cliente adicionou o produto "Boné Aba Curva" ao carrinho
    E navega para a página do carrinho
    Quando o cliente clica para esvaziar o carrinho
    Então o carrinho deve ficar vazio
