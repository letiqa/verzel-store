# 🛍️ Verzel Store - Suíte de Testes Automatizados (Playwright + Python + Gherkin)


Foram realizados testes manuais funcionais e exploratórios, cobrindo as duas funcionalidades implementadas: funcionamento do novo cupom e frete grátis a partir de 200,00. Foram feitos testes de API usando postman.

 Finalizados os testes manuais, foi feita uma suíte de testes automatizados usando **Playwright (Python) e BDD + Gherkin (`pytest-bdd`)**, validando o funcionamento. Os testes automatizados cobrindo as situações onde foram encontrados bugs ficam sinalizados usando o marcador xfail (expected failure), e não quebram a suíte de testes. Quando forem corrigidos serão marcados com xpassed. 

A IA foi utilizada para criar a base dos testes automatizados, correção de sintaxe e formatação de arquivos .md, acelerando os processos.

Tomei a iniciativa de utilizar allure para fazer os reports e implementar CI/CD para deixar a suite de testes mais completa.

O relatório pode ser visualizado aqui:
https://letiqa.github.io/verzel-store/


[Bug Report](https://github.com/letiqa/verzel-store/blob/main/BUG_REPORT.md)


[Test cases manuais](https://github.com/letiqa/verzel-store/blob/main/TEST_CASES_MANUAIS.md)


[Test cases automatizados](https://github.com/letiqa/verzel-store/blob/main/TEST_CASES_AUTOMACAO.md)


---

---

##  Arquitetura do Projeto

- **Cenários BDD**: Os arquivos Gherkin em `tests/features/` descrevem os comportamentos de API, carrinho, cupons, frete e checkout. As implementações dos passos ficam separadas em `tests/step_defs/`.
- **Page Object Model (POM)**: `pages/` encapsula as interações de interface com produtos, carrinho e checkout, mantendo seletores e ações fora dos cenários.
- **Cliente de API**: `services/api_client.py` centraliza as chamadas HTTP usadas pelos testes de API.
- **Configuração e fixtures**: `config/settings.py` reúne URL e dados fixos da loja. `tests/conftest.py` configura fixtures de Playwright e API, integra os cenários BDD, marca defeitos conhecidos como `xfail` e anexa screenshots de falhas ao Allure.
- **Collection Postman**: O arquivo `Verzel Store API.postman_collection.json` contém a suíte importável dos testes de API.
- **CI/CD**: `.github/workflows/ci-cd.yml` executa os testes automatizados e gera o relatório Allure.

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
├── BUG_REPORT.md                     # Bugs encontrados
├── TEST_CASES_AUTOMACAO.md           # Inventário dos casos automatizados
├── TEST_CASES_MANUAIS.md             # Inventário dos casos manuais
├── Verzel Store API.postman_collection.json  # Arquivo com a collection do Postman
└── README.md                         # Este documento
```

Os resultados e relatórios Allure são gerados durante a execução. 

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

###  Executar todos os testes
```bash
pytest
```
*Executa toda a suíte (UI, API e E2E) e grava os resultados Allure em `reports/allure-results/`. Os resultados anteriores são limpos a cada execução.*



###  Collection Postman da API
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


