# Casos de Teste Manuais - Verzel Store

Casos de teste executados manualmente na interface da Verzel Store, organizados por ID, título, pré-condições, passos de execução, resultado esperado, prioridade e status.

**Status:** "Passou" indica que o resultado obtido foi igual ao esperado. "Falhou" indica divergência entre o resultado obtido e o esperado, com o defeito correspondente registrado.

**Resumo da execução:** 25 casos executados — 24 passaram e 1 falhou (BUG-001).

| **ID** | **Título** | **Pré-condições** | **Passos de execução** | **Resultado esperado** | **Prioridade** | **Status** |
|:---|:---|:---|:---|:---|:---:|:---:|
| TC-01 | Aplicar BEMVINDO10 com 10% de desconto | Loja acessível; camiseta no carrinho; carrinho aberto | Aplicar `BEMVINDO10` | Cupom aparece como aplicado; desconto é 10% do subtotal; frete não é descontado | Alta | Passou |
| TC-02 | Aplicar cupom em minúsculas (`bemvindo10`) | Loja acessível; camiseta no carrinho; carrinho aberto | Aplicar `bemvindo10` | Cupom `BEMVINDO10` aparece como aplicado; desconto é 10% do subtotal | Alta | Passou |
| TC-03 | Aplicar cupom em maiúsculas (`BEMVINDO10`) | Loja acessível; camiseta no carrinho; carrinho aberto | Aplicar `BEMVINDO10` | Cupom `BEMVINDO10` aparece como aplicado; desconto é 10% do subtotal | Alta | Passou |
| TC-04 | Aplicar cupom com espaços antes | Loja acessível; camiseta no carrinho; carrinho aberto | Aplicar `  BEMVINDO10` | Espaços são ignorados; cupom aparece como aplicado; desconto é 10% do subtotal | Alta | Passou |
| TC-05 | Aplicar cupom com espaço no final | Loja acessível; camiseta no carrinho; carrinho aberto | Aplicar `BEMVINDO10 ` | Espaços são ignorados; cupom aparece como aplicado; desconto é 10% do subtotal | Alta | Passou |
| TC-06 | Aplicar cupom com espaços antes e depois e letras minúsculas | Loja acessível; camiseta no carrinho; carrinho aberto | Aplicar `   bemvindo10   ` | Espaços e maiúsculas/minúsculas são ignorados; cupom aparece como aplicado; desconto é 10% do subtotal | Alta | Passou |
| TC-07 | Aplicar cupom com letras maiúsculas e minúsculas (`BemVindo10`) | Loja acessível; camiseta no carrinho; carrinho aberto | Aplicar `BemVindo10` | Cupom `BEMVINDO10` aparece como aplicado; desconto é 10% do subtotal | Alta | Passou |
| TC-08 | Rejeitar cupom inexistente na interface | Loja acessível; camiseta no carrinho; carrinho aberto | Aplicar `CUPOM_INEXISTENTE` | Exibe "Cupom inválido."; desconto é zero; subtotal não muda | Alta | Passou |
| TC-09 | Rejeitar cupom expirado na interface | Loja acessível; camiseta no carrinho; carrinho aberto | Aplicar `VERAO2026` | Exibe "Cupom expirado."; desconto é zero | Alta | Passou |
| TC-10 | Aplicar um cupom e removê-lo | Loja acessível; camiseta no carrinho; carrinho aberto | Aplicar `BEMVINDO10`; verificar que o campo para outro cupom não aparece; remover o cupom | Campo de cupom volta a aparecer; não há desconto nem cupom ativo | Alta | Passou |
| TC-11 | Frete grátis acima de R$ 200,00 | Loja acessível; jaqueta de R$ 229,90 no carrinho | Abrir o carrinho | Frete aparece como grátis; não há aviso de valor faltante | Alta | Passou |
| TC-12 | Frete grátis no subtotal exato de R$ 200,00 | Loja acessível; duas mochilas de R$ 100,00 no carrinho | Abrir o carrinho | Frete aparece como grátis | Alta | Falhou — BUG-001 |
| TC-13 | Cobrar frete abaixo de R$ 200,00 e informar valor faltante | Loja acessível; camiseta de R$ 59,90 no carrinho | Abrir o carrinho | Frete é R$ 19,90; aviso informa corretamente quanto falta para frete grátis | Alta | Passou |
| TC-14 | Calcular frete pelo subtotal antes do desconto | Loja acessível; jaqueta de R$ 229,90 no carrinho; carrinho aberto | Aplicar `BEMVINDO10` | Frete continua grátis; total é subtotal menos desconto | Alta | Passou |
| TC-15 | Não aplicar desconto sobre o frete | Loja acessível; mochila de R$ 100,00 no carrinho; carrinho aberto | Aplicar `BEMVINDO10` | Subtotal R$ 100,00; desconto R$ 10,00; frete R$ 19,90; total R$ 109,90 | Alta | Passou |
| TC-16 | Finalizar pedido com cupom aplicado | Loja acessível; mochila no carrinho | Abrir carrinho; aplicar `BEMVINDO10`; finalizar compra; preencher nome, e-mail e CEP válidos; confirmar | Página de confirmação aparece e gera número no formato `VZ-000000` | Alta | Passou |
| TC-17 | Rejeitar nome sem sobrenome no checkout | Loja acessível; camiseta no carrinho | Abrir carrinho; finalizar compra; informar "Maria", e-mail e CEP válidos; confirmar | Exibe "Informe nome e sobrenome." | Média | Passou |
| TC-18 | Rejeitar e-mail inválido no checkout | Loja acessível; camiseta no carrinho | Abrir carrinho; finalizar compra; informar nome e CEP válidos e e-mail inválido; confirmar | Exibe "Informe um e-mail válido." | Média | Passou |
| TC-19 | Rejeitar CEP incompleto no checkout | Loja acessível; camiseta no carrinho | Abrir carrinho; finalizar compra; informar nome e e-mail válidos e CEP `123`; confirmar | Exibe "Informe um CEP com 8 dígitos." | Média | Passou |
| TC-20 | Aceitar CEP válido sem hífen | Loja acessível; camiseta no carrinho | Abrir carrinho; finalizar compra; informar dados válidos e CEP `01310100`; confirmar | Página de confirmação do pedido aparece | Média | Passou |
| TC-21 | Limitar produto a cinco unidades na interface | Loja acessível; uma camiseta no carrinho; carrinho aberto | Aumentar a quantidade até o limite | Quantidade fica em 5 e o botão de aumentar fica desabilitado | Alta | Passou |
| TC-22 | Reabilitar aumento após diminuir a quantidade | Loja acessível; uma camiseta no carrinho; carrinho aberto | Aumentar até 5; diminuir uma unidade | Quantidade fica em 4 e o botão de aumentar fica habilitado | Alta | Passou |
| TC-23 | Exibir valores monetários com duas casas decimais | Loja acessível; camiseta e meias no carrinho; carrinho aberto | Aplicar `BEMVINDO10`; verificar subtotal, desconto e total | Valores são exibidos em reais com duas casas decimais | Média | Passou |
| TC-24 | Remover um item do carrinho | Loja acessível; camiseta no carrinho; carrinho aberto | Remover a camiseta | Carrinho fica vazio | Média | Passou |
| TC-25 | Esvaziar o carrinho | Loja acessível; camiseta e boné no carrinho; carrinho aberto | Acionar a opção para esvaziar o carrinho | Carrinho fica vazio | Média | Passou |

## Defeito encontrado

| **ID do caso** | **Defeito** | **Resultado obtido** |
|:---|:---|:---|
| TC-12 | BUG-001 — Cobrança indevida de frete de R$ 19,90 no limite exato de R$ 200,00 | Frete de R$ 19,90 cobrado; total de R$ 219,90 em vez de R$ 200,00 |
