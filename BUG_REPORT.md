##  Relatório de Defeitos (Bug Report) - Verzel Store

Registra as inconformidades e defeitos identificados durante a fase de testes manuais e exploratórios da Verzel Store, posteriormente integrados à suíte de automação com marcação de falha esperada (`@pytest.mark.xfail`).

---

## Bugs Identificados

| ID | Critério | Título | Severidade | Prioridade | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **BUG-001** | **CA06** | Cobrança indevida de frete de R$ 19,90 no limite exato de R$ 200,00 (Valor Limite) | Alta | Alta | Aberto |
| **BUG-002** | **CA10** | API (cálculo de carrinho e criação de pedido) aceita quantidade superior a 5 unidades por produto sem retornar 422 | Média | Alta | Aberto |

---

## Detalhamento dos Defeitos

### 📌 BUG-001: Cobrança de Frete no Subtotal Exato de R$ 200,00
- **Critério de Aceite Violado:**
  > **CA06:** O frete é grátis para compras com subtotal a partir de R$ 200,00, **inclusive**.  
  > *Regra de cálculo:* `Frete: R$ 0,00 quando o subtotal é igual ou maior que R$ 200,00. Caso contrário, R$ 19,90.`
- **Causa Raiz Identificada:**  
  A condição lógica no cálculo de frete do backend foi implementada como estrita (`subtotal > 200`) ao invés de maior ou igual (`subtotal >= 200`). Isso é evidenciado pelo fato de que o campo `valorFaltanteFreteGratis` retorna `0`, porém `freteGratis` retorna `false` e `frete` retorna `19.9`.
- **Passos para Reproduzir:**
  1. Acessar a loja: `https://verzel-store.qa-test-verzel-store.workers.dev/`
  2. Adicionar 2 unidades da **Mochila Urbana 20L** (R$ 100,00 cada, totalizando R$ 200,00 de subtotal).
  3. Acessar o Carrinho.
  4. Observar a linha do Frete no Resumo do Pedido.
  5. Alternativamente, via API:
     ```http
     POST /api/carrinho/calcular HTTP/1.1
     Content-Type: application/json

     {
       "itens": [{ "produtoId": "P005", "quantidade": 2 }]
     }
     ```
- **Resultado Esperado:**
  - Frete: R$ 0,00 / "Grátis"
  - `freteGratis`: `true`
  - Total: R$ 200,00
- **Resultado Obtido:**
  - Frete: R$ 19,90 cobrado
  - `freteGratis`: `false`
  - Total: R$ 219,90
- **Evidências**
- <img width="1347" height="594" alt="image" src="https://github.com/user-attachments/assets/9a8a750e-4e09-4185-abae-ccc0d72e9338" />

  Cenário BDD em `tests/features/frete.feature` (*"Frete grátis para compras com subtotal exatamente igual a R$ 200,00"*), automatizado em `tests/step_defs/test_frete_steps.py` e anotado com `@pytest.mark.xfail`.
  

---

### 📌 BUG-002: API Não Bloqueia Quantidades Superiores a 5 Unidades
- **Critério de Aceite Violado:**
  > **CA10:** Cada produto pode ter no máximo 5 unidades por pedido. **A regra vale para a interface e para a API.**  
  > *Documentação da API:* `422 QUANTIDADE_MAXIMA_EXCEDIDA: A quantidade de um produto é maior que 5.`
- **Causa Raiz Identificada:**  
  Na camada de interface gráfica (frontend), o botão de incremento `+` é devidamente desabilitado quando o item atinge 5 unidades. Entretanto, os endpoints `POST /api/carrinho/calcular` e `POST /api/pedidos` não validam a regra `quantidade <= 5` na requisição, aceitando quantidades acima do limite (ex: 6 unidades). O `/calcular` calcula normalmente o total e o `/pedidos` chega a confirmar o pedido. Ou seja, a regra existe apenas no frontend e pode ser contornada ao chamar a API diretamente.
- **Passos para Reproduzir — Endpoint 1: `POST /api/carrinho/calcular`**
  1. Abrir o Postman (ou outro cliente HTTP) e criar uma requisição `POST` para `{{baseUrl}}/api/carrinho/calcular`, com `baseUrl` = `https://verzel-store.qa-test-verzel-store.workers.dev`.
  2. Na aba **Body**, selecionar **raw → JSON** e informar o corpo abaixo, com quantidade `6` (acima do limite de 5):
     ```json
     {
       "itens": [
         { "produtoId": "P001", "quantidade": 6 }
       ]
     }
     ```
  3. Garantir o header `Content-Type: application/json` e clicar em **Send**.
  4. Observar o status HTTP e o corpo da resposta.
  5. Equivalente via cURL:
     ```bash
     curl -X POST "https://verzel-store.qa-test-verzel-store.workers.dev/api/carrinho/calcular" \
       -H "Content-Type: application/json" \
       -d '{"itens":[{"produtoId":"P001","quantidade":6}]}'
     ```
- **Passos para Reproduzir — Endpoint 2: `POST /api/pedidos`**
  1. No Postman, criar uma requisição `POST` para `{{baseUrl}}/api/pedidos`.
  2. Na aba **Body**, selecionar **raw → JSON** e informar o corpo abaixo, com quantidade `6` (acima do limite de 5):
     ```json
     {
       "cliente": {
         "nome": "Roberta Alves",
         "email": "roberta@exemplo.com",
         "cep": "01310-100"
       },
       "itens": [
         { "produtoId": "P001", "quantidade": 6 }
       ]
     }
     ```
  3. Garantir o header `Content-Type: application/json` e clicar em **Send**.
  4. Observar o status HTTP e o corpo da resposta.
  5. Equivalente via cURL:
     ```bash
     curl -X POST "https://verzel-store.qa-test-verzel-store.workers.dev/api/pedidos" \
       -H "Content-Type: application/json" \
       -d '{"cliente":{"nome":"Roberta Alves","email":"roberta@exemplo.com","cep":"01310-100"},"itens":[{"produtoId":"P001","quantidade":6}]}'
     ```
- **Resultado Esperado (ambos os endpoints):**
  - Status HTTP `422 Unprocessable Entity`
  - Resposta:
    ```json
    {
      "erro": {
        "codigo": "QUANTIDADE_MAXIMA_EXCEDIDA",
        "mensagem": "A quantidade de um produto é maior que 5.",
        "campo": "itens[0].quantidade"
      }
    }
    ```
- **Resultado Obtido:**
  - `POST /api/carrinho/calcular`: status HTTP `200 OK`, com o item de 6 unidades da Camiseta Essencial calculado normalmente (`precoUnitario` R$ 59,90, `total` R$ 359,40).
  - `POST /api/pedidos`: status HTTP `201 Created`, pedido confirmado com 6 unidades (`total` R$ 359,40), gerando código `VZ-XXXXXX`.
- **Evidências**

  `POST /api/carrinho/calcular` no Postman: `200 OK`, com `"quantidade": 6` e `"total": 359.4`.

 ![alt text](image.png)

  `POST /api/pedidos` no Postman: `201 Created`, com `"quantidade": 6` e `"total": 359.4`.

 ![alt text](image-1.png)

  Cenário BDD em `tests/features/api_carrinho_pedidos.feature` (*"Rejeição de pedido com mais de 5 unidades por produto via API"*), automatizado em `tests/step_defs/test_api_steps.py` e anotado com `@pytest.mark.xfail`.
