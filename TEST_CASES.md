# Casos de teste automatizados

Inventário simples dos 38 casos definidos nas features Gherkin e automatizados com Playwright e pytest-bdd.

**Status:** “Automatizado” indica que o caso está implementado na suíte; não representa o resultado de uma execução recente. “Xfail esperado” indica que a suíte espera a falha por causa de um defeito conhecido e aberto.

| Título | Pré-condições | Passos de execução | Resultado esperado | Prioridade | Status |
|---|---|---|---|---|---|
| Aplicar BEMVINDO10 com 10% de desconto | Loja acessível; camiseta no carrinho; carrinho aberto | Aplicar `BEMVINDO10` | Cupom aparece como aplicado; desconto é 10% do subtotal; frete não é descontado | Alta | Automatizado |
| Aplicar cupom em minúsculas (`bemvindo10`) | Loja acessível; camiseta no carrinho; carrinho aberto | Aplicar `bemvindo10` | Cupom `BEMVINDO10` aparece como aplicado; desconto é 10% do subtotal | Alta | Automatizado |
| Aplicar cupom em maiúsculas (`BEMVINDO10`) | Loja acessível; camiseta no carrinho; carrinho aberto | Aplicar `BEMVINDO10` | Cupom `BEMVINDO10` aparece como aplicado; desconto é 10% do subtotal | Alta | Automatizado |
| Aplicar cupom com espaços antes | Loja acessível; camiseta no carrinho; carrinho aberto | Aplicar `  BEMVINDO10` | Espaços são ignorados; cupom aparece como aplicado; desconto é 10% do subtotal | Alta | Automatizado |
| Aplicar cupom com espaço no final | Loja acessível; camiseta no carrinho; carrinho aberto | Aplicar `BEMVINDO10 ` | Espaços são ignorados; cupom aparece como aplicado; desconto é 10% do subtotal | Alta | Automatizado |
| Aplicar cupom com espaços antes e depois e letras minúsculas | Loja acessível; camiseta no carrinho; carrinho aberto | Aplicar `   bemvindo10   ` | Espaços e maiúsculas/minúsculas são ignorados; cupom aparece como aplicado; desconto é 10% do subtotal | Alta | Automatizado |
| Aplicar cupom com letras maiúsculas e minúsculas (`BemVindo10`) | Loja acessível; camiseta no carrinho; carrinho aberto | Aplicar `BemVindo10` | Cupom `BEMVINDO10` aparece como aplicado; desconto é 10% do subtotal | Alta | Automatizado |
| Rejeitar cupom inexistente na interface | Loja acessível; camiseta no carrinho; carrinho aberto | Aplicar `CUPOM_INEXISTENTE` | Exibe “Cupom inválido.”; desconto é zero; subtotal não muda | Alta | Automatizado |
| Rejeitar cupom expirado na interface | Loja acessível; camiseta no carrinho; carrinho aberto | Aplicar `VERAO2026` | Exibe “Cupom expirado.”; desconto é zero | Alta | Automatizado |
| Aplicar um cupom e removê-lo | Loja acessível; camiseta no carrinho; carrinho aberto | Aplicar `BEMVINDO10`; verificar que o campo para outro cupom não aparece; remover o cupom | Campo de cupom volta a aparecer; não há desconto nem cupom ativo | Alta | Automatizado |
| Frete grátis acima de R$ 200,00 | Loja acessível; jaqueta de R$ 229,90 no carrinho | Abrir o carrinho | Frete aparece como grátis; não há aviso de valor faltante | Alta | Automatizado |
| Frete grátis no subtotal exato de R$ 200,00 | Loja acessível; duas mochilas de R$ 100,00 no carrinho | Abrir o carrinho | Frete aparece como grátis | Alta | Xfail esperado — BUG-001 aberto |
| Cobrar frete abaixo de R$ 200,00 e informar valor faltante | Loja acessível; camiseta de R$ 59,90 no carrinho | Abrir o carrinho | Frete é R$ 19,90; aviso informa corretamente quanto falta para frete grátis | Alta | Automatizado |
| Calcular frete pelo subtotal antes do desconto | Loja acessível; jaqueta de R$ 229,90 no carrinho; carrinho aberto | Aplicar `BEMVINDO10` | Frete continua grátis; total é subtotal menos desconto | Alta | Automatizado |
| Não aplicar desconto sobre o frete | Loja acessível; mochila de R$ 100,00 no carrinho; carrinho aberto | Aplicar `BEMVINDO10` | Subtotal R$ 100,00; desconto R$ 10,00; frete R$ 19,90; total R$ 109,90 | Alta | Automatizado |
| Finalizar pedido com cupom aplicado | Loja acessível; mochila no carrinho | Abrir carrinho; aplicar `BEMVINDO10`; finalizar compra; preencher nome, e-mail e CEP válidos; confirmar | Página de confirmação aparece e gera número no formato `VZ-000000` | Alta | Automatizado |
| Rejeitar nome sem sobrenome no checkout | Loja acessível; camiseta no carrinho | Abrir carrinho; finalizar compra; informar “Maria”, e-mail e CEP válidos; confirmar | Exibe “Informe nome e sobrenome.” | Média | Automatizado |
| Rejeitar e-mail inválido no checkout | Loja acessível; camiseta no carrinho | Abrir carrinho; finalizar compra; informar nome e CEP válidos e e-mail inválido; confirmar | Exibe “Informe um e-mail válido.” | Média | Automatizado |
| Rejeitar CEP incompleto no checkout | Loja acessível; camiseta no carrinho | Abrir carrinho; finalizar compra; informar nome e e-mail válidos e CEP `123`; confirmar | Exibe “Informe um CEP com 8 dígitos.” | Média | Automatizado |
| Aceitar CEP válido sem hífen | Loja acessível; camiseta no carrinho | Abrir carrinho; finalizar compra; informar dados válidos e CEP `01310100`; confirmar | Página de confirmação do pedido aparece | Média | Automatizado |
| Limitar produto a cinco unidades na interface | Loja acessível; uma camiseta no carrinho; carrinho aberto | Aumentar a quantidade até o limite | Quantidade fica em 5 e o botão de aumentar fica desabilitado | Alta | Automatizado |
| Reabilitar aumento após diminuir a quantidade | Loja acessível; uma camiseta no carrinho; carrinho aberto | Aumentar até 5; diminuir uma unidade | Quantidade fica em 4 e o botão de aumentar fica habilitado | Alta | Automatizado |
| Exibir valores monetários com duas casas decimais | Loja acessível; camiseta e meias no carrinho; carrinho aberto | Aplicar `BEMVINDO10`; verificar subtotal, desconto e total | Valores são exibidos em reais com duas casas decimais | Média | Automatizado |
| Remover um item do carrinho | Loja acessível; camiseta no carrinho; carrinho aberto | Remover a camiseta | Carrinho fica vazio | Média | Automatizado |
| Esvaziar o carrinho | Loja acessível; camiseta e boné no carrinho; carrinho aberto | Acionar a opção para esvaziar o carrinho | Carrinho fica vazio | Média | Automatizado |
| Listar produtos pela API | API acessível | Consultar `GET /api/produtos` | Resposta HTTP 200 com uma lista de 8 produtos | Média | Automatizado |
| Consultar produto existente pela API | API acessível | Consultar `GET /api/produtos/P001` | Resposta HTTP 200; produto é “Camiseta Essencial”, preço R$ 59,90 | Média | Automatizado |
| Consultar produto inexistente pela API | API acessível | Consultar `GET /api/produtos/P999` | Resposta HTTP 404 com código `PRODUTO_NAO_ENCONTRADO` | Média | Automatizado |
| Calcular carrinho pela API com cupom válido | API acessível | Enviar POST `/api/carrinho/calcular` com produto `P005`, quantidade 1 e cupom ` bemvindo10 ` | Resposta HTTP 200; subtotal R$ 100,00; desconto R$ 10,00; cupom aplicado | Alta | Automatizado |
| Calcular carrinho pela API com cupom inexistente | API acessível | Enviar POST `/api/carrinho/calcular` com produto `P005`, quantidade 1 e cupom `INEXISTENTE` | Resposta HTTP 200; desconto zero; mensagem “Cupom inválido.” | Alta | Automatizado |
| Calcular carrinho pela API com cupom expirado | API acessível | Enviar POST `/api/carrinho/calcular` com produto `P005`, quantidade 1 e cupom `VERAO2026` | Resposta HTTP 200; desconto zero; mensagem “Cupom expirado.” | Alta | Automatizado |
| Rejeitar cálculo de carrinho sem itens | API acessível | Enviar cálculo com lista de itens vazia | Resposta HTTP 422 com código `ITENS_OBRIGATORIOS` | Média | Automatizado |
| Rejeitar quantidade zero no cálculo da API | API acessível | Calcular carrinho com produto `P001` e quantidade 0 | Resposta HTTP 422 com código `QUANTIDADE_INVALIDA` | Média | Automatizado |
| Rejeitar pedido com mais de cinco unidades pela API | API acessível | Enviar pedido com 6 unidades do produto `P001` | Resposta HTTP 422 com código `QUANTIDADE_MAXIMA_EXCEDIDA` | Alta | Xfail esperado — BUG-002 aberto |
| Criar pedido válido pela API | API acessível | Enviar pedido com dados válidos e cupom `BEMVINDO10` | Resposta HTTP 201 com número de pedido no formato `VZ-000000` | Alta | Automatizado |
| Rejeitar pedido pela API com cupom inexistente | API acessível | Enviar pedido com cupom `INEXISTENTE` | Resposta HTTP 422 com código `CUPOM_INVALIDO` | Alta | Automatizado |
| Rejeitar pedido pela API com cupom expirado | API acessível | Enviar pedido com cupom `VERAO2026` | Resposta HTTP 422 com código `CUPOM_EXPIRADO` | Alta | Automatizado |
| Rejeitar pedido pela API com nome incompleto | API acessível | Enviar pedido com nome sem sobrenome | Resposta HTTP 422 com código `DADOS_INVALIDOS` | Média | Automatizado |
