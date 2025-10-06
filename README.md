# Eros — Agente Orquestrador (Prototype)

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org)  
[![License](https://img.shields.io/badge/license-MIT-green)](#license)  
[![CI](https://github.com/JoaoPSFranca/eros-assistant/actions/workflows/python-ci.yml/badge.svg)](#ci)  

**Eros** é um agente orquestrador escrito em Python que delega raciocínio a LLMs via API (ex.: Gemini, OpenAI, Mistral) e executa ferramentas locais (execução segura de comandos, OCR, automação de UI, agenda). O foco do projeto: privacidade, baixo custo operacional, facilidade de integração em Python e possibilidade futura de modo híbrido (cloud + local).


## Status do projeto
**Estado atual:** protótipo alfa — CLI básica e client Gemini integrados.


## Principais funcionalidades
- Adapter layer para providers (ProviderAdapter) — permite trocar provider sem refatorar a aplicação.
- Function-calling / tool invocation (planejado; schema validation).
- Roteamento e failover entre providers (Gemini → OpenAI → Mistral → Local).
- Monitoramento de uso (tokens) e métricas (latência p50/p90).
- Scripts de teste (latency / billing simulation).


## Estrutura do Projeto
```
eros/
├─ src/eros/ # código principal
│  ├─ init.py
│  ├─ main.py
│  ├─ brain.py
│  ├─ config.py
│  └─ providers/
│     ├─ base.py
│     ├─ gemini_adapter.py
│     ├─ mistral_adapter.py
│     └─ openai_adapter.py
├─ tests/
├─ scripts/
│  ├─ latency_test.py
│  ├─ simulate_usage.py
│  └─ billing_alerts.py
```

## Quickstart — rodando localmente

1. Clone o repositório:
```bash
git clone https://github.com/JoaoPSFranca/eros-assistant.git
cd eros
```

2. Crie ambiente virtual e instale dependências:
```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
# .venv\Scripts\activate    # Windows (PowerShell)
pip install -r requirements.txt
```

3. Variáveis de ambiente (`.env`):
```bash
# .env (exemplo)
GEMINI_API_KEY=sk-...
OPENAI_API_KEY=sk-...
MISTRAL_API_KEY=sk-...
DEFAULT_PROVIDER=gemini
```

4. Rodar CLI (exemplo):
```bash
python src/eros/main.py
```


## Development 

- `pre-commit`: utilizado para formatação de commits.
    -  Utilizados: **black**, **isort**, **flake8**.

- `pytest`: para rodar os testes.


### CI (GitHub Actions)
- Há um workflow `python-ci.yml` que roda lint e testes em push/PR para `main` e `dev`.


## Adapters de Providers (como funciona)
O projeto usa um padrão *ProviderAdapter* para abstrair detalhes específicos de cada API. Implementações previstas:
- `GeminiAdapter` (Gemini / Vertex AI)
- `OpenAIAdapter` (OpenAI API)
- `MistralAdapter` (Mistral API)
- `LocalAdapter` (inferência local via llama.cpp / HF runtime — POC/experimental)

**Interface mínima esperada (`providers/base.py`)**
- `initialize()`
- `start_chat_session()`
- `send_message(session, prompt, **kwargs) -> dict`  
`send_message` deve retornar: `{"text": str, "tokens_used": int|None, "latency_ms": float, "meta": {...}}`


## Como fazer failover / roteamento (prático)
A ideia é ter uma `ProviderFactory` + `Router` que decide:
- Prioridade (ex.: `high` → Gemini; `medium` → OpenAI; `low` → Mistral/local)
- Políticas de custo/latência (se alarme de custo ativo, redirecionar a low-cost)
- Circuit breaker: se provider falhar X vezes seguidas, abrir circuito por Y segundos (usar `tenacity` e/ou simples contador)


## Scripts úteis
- `scripts/latency_test.py` — mede p50/p90 para 512 tokens contra cada provider.
- `scripts/simulate_usage.py` — simula dias de tráfego para estimar tokens/mês e custo aproximado.
- `scripts/billing_alerts.py` — mínima lógica para alertar por email/Slack quando atingir threshold.


## Contribuição (breve)
1. Fork / branch feature: `feature/<nome>`
2. Siga o `CONTRIBUTING.md`
3. Rode `pre-commit` e `pytest`
4. Abra PR com template preenchido e vincule issue correspondente


## Segurança e segredos
- **Nunca** commit `.env` ou chaves. Use GitHub Secrets para workflows.
- Para execuções sensíveis, configure *Zero Data Retention* quando o provider suportar e use contratos empresariais para governança de dados.
- Filtre logs que possam conter PII antes de persistir.


## Referências & Links úteis
- Issue templates e PR templates em `.github/`.


## Licença
Este repositório usa a licença **MIT**. Veja o arquivo `LICENSE` para detalhes.


## Contato
Autor: **João Pedro Franca**  
Repo: `https://github.com/JoaoPSFranca/eros-assistant`  
Email: `francasjoaopedro@gmail.com` — para reports de segurança use `SECURITY.md`.
