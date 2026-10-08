# 🛍️ Verzel Store - Suíte de Testes Automatizados (Playwright + Python + Gherkin)


Foram realizados testes manuais funcionais e exploratórios, cobrindo as duas funcionalidades implementadas: funcionamento do novo cupom e frete grátis a partir de 200,00. Foram feitos testes de API usando postman.

 Finalizados os testes manuais, foi feita uma suíte de testes automatizados usando **Playwright (Python) ** e ** BDD + Gherkin (`pytest-bdd`)**, validando o funcionamento. Os testes automatizados cobrindo as situações onde foram encontrados bugs ficam sinalizados usando o marcador xfail (expected failure), e não quebram a suíte de testes. Quando forem corrigidos serão marcados com xpassed. 

A IA foi utilizada para criar a base dos testes automatizados, correção de sintaxe e formatação de arquivos .md, acelerando os processos.

Tomei a iniciativa de utilizar allure para fazer os reports e implementar CI/CD para deixar a suite de testes mais completa.



---

##  Arquitetura do Projeto

- **Cenários BDD**: Os arquivos Gherkin em `tests/features/` descrevem os comportamentos de API, carrinho, cupons, frete e checkout. As implementações dos passos ficam separadas em `tests/step_defs/`.
- **Page Object Model (POM)**: `pages/` encapsula as interações de interface com produtos, carrinho e checkout, mantendo seletores e ações fora dos cenários.
- **Cliente de API**: `services/api_client.py` centraliza as chamadas HTTP usadas pelos testes de API.
- **Configuração e fixtures**: `config/settings.py` reúne URL e dados fixos da loja. `tests/conftest.py` configura fixtures de Playwright e API, integra os cenários BDD, marca defeitos conhecidos como `xfail` e anexa screenshots de falhas ao Allure.
- **Collection Postman**: O arquivo `Verzel Store API.postman_collection.json` contém a suíte importável dos testes de API.
- **CI/CD**: `.github/workflows/ci-cd.yml` executa os testes automatizados e publica o relatório Allure no GitHub Pages após sucesso na branch padrão.

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

Os resultados e relatórios Allure são gerados durante a execução e não precisam ser mantidos no projeto. Capturas de tela das falhas de interface são anexadas aos resultados Allure.

---

##  Tecnologias Utilizadas

- **Linguagem:** Python 3.14+
- **Automação Web:** [Playwright](https://playwright.dev/python/)
- **Framework de Testes:** [Pytest](https://pytest.org/)
- **BDD / Gherkin:** [pytest-bdd](https://pytest-bdd.readthedocs.io/)
- **Geração de Relatórios:** [Allure Report](https://allurereport.org/docs/pytest/)
- **Cliente HTTP:** [Requests](https://requests.readthedocs.io/)

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

A suite contém 43 requests com assertions de status, respostas, cálculos, cupons, frete, pedidos e os 12 códigos de erro da documentação. Os cenários BUG-001 e BUG-002 verificam o comportamento esperado documentado e podem falhar enquanto esses defeitos conhecidos persistirem.

---

## CI/CD

O workflow em `.github/workflows/ci-cd.yml` instala as dependências e o Chromium, executa toda a suíte em pushes, pull requests e execuções manuais, e guarda os resultados brutos do Allure como artefato. Após uma execução bem-sucedida na branch padrão, gera o relatório HTML e publica-o no GitHub Pages.

Para habilitar a publicação, configure **Settings → Pages → Build and deployment → Source → GitHub Actions** no repositório. O relatório publicado fica disponível na URL de Pages exibida pela execução do workflow. A publicação não ocorre em pull requests nem em branches diferentes da padrão.

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
