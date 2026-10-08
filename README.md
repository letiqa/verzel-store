# 🛍️ Verzel Store - Suíte de Testes Automatizados (Playwright + Python + Gherkin)


Foram realizados testes manuais funcionais e exploratórios, cobrindo as duas funcionalidades implementadas: funcionamento do novo cupom e frete grátis a partir de 200,00. Foram feitos testes de API usando postman.

 Finalizados os testes manuais, foi feita uma suíte de testes automatizados usando **Playwright (Python) e BDD + Gherkin (`pytest-bdd`)**, validando o funcionamento. Os testes automatizados cobrindo as situações onde foram encontrados bugs ficam sinalizados usando o marcador xfail (expected failure), e não quebram a suíte de testes. Quando forem corrigidos serão marcados com xpassed. 

A IA foi utilizada para criar a base dos testes automatizados, correção de sintaxe e formatação de arquivos .md, acelerando os processos.

Tomei a iniciativa de utilizar allure para fazer os reports e implementar CI/CD para deixar a suite de testes mais completa.

O relatório pode ser visualizado aqui:
https://letiqa.github.io/verzel-store/
---
## Casos de teste automatizados

Casos automatizados com Playwright e pytest-bdd, organizados por título, pré-condições, execução, resultado esperado, prioridade e status.

**Status:** “Automatizado” indica que o caso está implementado na suíte; não representa o resultado de uma execução recente. “Xfail esperado” indica que a suíte espera a falha por causa de um defeito conhecido e aberto.

| **Título** | **Pré-condições** | **Passos de execução** | **Resultado esperado** | **Prioridade** | **Status** |
|:---|:---|:---|:---|:---:|:---:|
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


---

##  Arquitetura do Projeto

- **Cenários BDD**: Os arquivos Gherkin em `tests/features/` descrevem os comportamentos de API, carrinho, cupons, frete e checkout. As implementações dos passos ficam separadas em `tests/step_defs/`.
- **Page Object Model (POM)**: `pages/` encapsula as interações de interface com produtos, carrinho e checkout, mantendo seletores e ações fora dos cenários.
- **Cliente de API**: `services/api_client.py` centraliza as chamadas HTTP usadas pelos testes de API.
- **Configuração e fixtures**: `config/settings.py` reúne URL e dados fixos da loja. `tests/conftest.py` configura fixtures de Playwright e API, integra os cenários BDD, marca defeitos conhecidos como `xfail` e anexa screenshots de falhas ao Allure.
- **Collection Postman**: O arquivo `Verzel Store API.postman_collection.json` contém a suíte importável dos testes de API.
- **CI/CD**: `.github/workflows/ci-cd.yml` executa os testes automatizados, gera o relatório Allure e o publica no GitHub Pages após sucesso na branch padrão, quando Pages estiver habilitado.

```text
verzel-store/
├── .github/
│   └── workflows/
│       └── ci-cd.yml                 # Execução dos testes e publicação do relatório Allure
├── config/
│   ├── __init__.py
│   └── settings.py                   # URL e dados fixos usados pela automação
├── pages/                            # Page Objects da interface web
│   ├── __init__.py
│   ├── base_page.py
│   ├── produtos_page.py
│   ├── carrinho_page.py
│   └── checkout_page.py
├── services/
│   ├── __init__.py
│   └── api_client.py                 # Chamadas HTTP para os endpoints da API
├── tests/
│   ├── conftest.py                   # Fixtures, hooks e integração com Allure
│   ├── features/                     # Cenários BDD em Gherkin
│   └── step_defs/                    # Implementações dos passos Gherkin
├── .gitignore                        # Exclusões de arquivos locais e gerados
├── pytest.ini                        # Configuração de coleta, markers e Allure
├── requirements.txt                  # Dependências Python
├── TEST_CASES.md                     # Inventário dos casos automatizados
├── Verzel Store API.postman_collection.json
└── README.md                         # Este documento
```

Os resultados e relatórios Allure são gerados durante a execução. Capturas de tela das falhas de interface são anexadas aos resultados Allure.

---

##  Pré-requisitos e Instalação

1. Acesse o diretório do projeto:
   ```bash
   cd verzel-store
   ```

2. Crie e ative um ambiente virtual (opcional, porém recomendado):
   ```bash
   python -m venv .venv
   # No Windows (PowerShell):
   .venv\Scripts\Activate.ps1
   # No Linux/Mac:
   source .venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Instale os navegadores do Playwright:
   ```bash
   playwright install chromium
   ```

5. Instale o Allure Commandline seguindo a [documentação oficial](https://allurereport.org/docs/install/). O plugin Python coleta os resultados; o Commandline gera e abre o relatório interativo.

---

##  Como Executar os Testes

### 1. Executar todos os testes
```bash
pytest
```
*Executa toda a suíte (UI, API e E2E) e grava os resultados Allure em `reports/allure-results/`. Os resultados anteriores são limpos a cada execução.*



### 4. Collection Postman da API
A collection pronta para importar está no formato **Postman Collection v2.1** em `Verzel Store API.postman_collection.json`. No Postman, escolha **Import → File** e selecione esse arquivo. Depois, execute a collection ou uma de suas pastas: **Produtos**, **Carrinho** ou **Pedidos**. A variável `baseUrl` já aponta para o ambiente de QA.

A suite contém testes com assertions de status, respostas, cálculos, cupons, frete, pedidos e códigos de erro da documentação. Os cenários BUG-001 e BUG-002 verificam o comportamento esperado documentado e podem falhar enquanto esses defeitos conhecidos persistirem.

---

## CI/CD

O workflow em `.github/workflows/ci-cd.yml` instala as dependências e o Chromium e executa toda a suíte em pushes, pull requests, execuções manuais e diariamente às **08:00 (horário de Brasília, UTC−3)**. O GitHub Actions usa UTC, por isso o agendamento está definido para `11:00 UTC`. Os resultados brutos e o relatório HTML do Allure são guardados como artefatos por 14 dias, inclusive quando há falhas nos testes. Após uma execução bem-sucedida na branch padrão, o relatório também é publicado no GitHub Pages.

---

##  Relatórios Allure

Após executar os testes, gere e abra o relatório interativo com:
```text
allure serve reports/allure-results
```

Para gerar os arquivos do relatório sem iniciar o servidor automaticamente:
```bash
allure generate reports/allure-results --clean --output reports/allure-report
allure open reports/allure-report
```

Os resultados brutos ficam em `reports/allure-results/`; o relatório gerado fica em `reports/allure-report/`. Essas pastas são saídas de execução e não são versionadas.

---

##  Relatório de Defeitos (Bug Report) - Verzel Store

Registra as inconformidades e defeitos identificados durante a fase de testes manuais e exploratórios da Verzel Store, posteriormente integrados à suíte de automação com marcação de falha esperada (`@pytest.mark.xfail`).

---

## Bugs Identificados

| ID | Critério | Título | Severidade | Prioridade | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **BUG-001** | **CA06** | Cobrança indevida de frete de R$ 19,90 no limite exato de R$ 200,00 (Valor Limite) | Alta | Alta | Aberto |
| **BUG-002** | **CA10** | API permite pedidos com quantidade superior a 5 unidades por produto sem retornar 422 | Média | Alta | Aberto |

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
- **Evidência no Teste Automatizado:**  
  Cenário BDD em `tests/features/frete.feature` (*"Frete grátis para compras com subtotal exatamente igual a R$ 200,00"*), automatizado em `tests/step_defs/test_frete_steps.py` e anotado com `@pytest.mark.xfail`.

---

### 📌 BUG-002: API Não Bloqueia Quantidades Superiores a 5 Unidades
- **Critério de Aceite Violado:**
  > **CA10:** Cada produto pode ter no máximo 5 unidades por pedido. **A regra vale para a interface e para a API.**  
  > *Documentação da API:* `422 QUANTIDADE_MAXIMA_EXCEDIDA: A quantidade de um produto é maior que 5.`
- **Causa Raiz Identificada:**  
  Na camada de interface gráfica (frontend), o botão de incremento `+` é devidamente desabilitado quando o item atinge 5 unidades. Entretanto, os endpoints `/api/carrinho/calcular` e `/api/pedidos` não validam a regra `quantidade <= 5` na requisição, permitindo criar pedidos com quantidades arbitrárias (ex: 6 unidades).
- **Passos para Reproduzir:**
  1. Enviar uma requisição POST direta para `/api/pedidos`:
     ```http
     POST /api/pedidos HTTP/1.1
     Content-Type: application/json

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
- **Resultado Esperado:**
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
  - Status HTTP `201 Created`
  - Pedido confirmado com 6 unidades gerando código `VZ-XXXXXX`.
- **Evidência no Teste Automatizado:**  
  Cenário BDD em `tests/features/api_carrinho_pedidos.feature` (*"Rejeição de pedido com mais de 5 unidades por produto via API"*), automatizado em `tests/step_defs/test_api_steps.py` e anotado com `@pytest.mark.xfail`.
