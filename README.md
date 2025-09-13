# Eros: Um Assistente Virtual Pessoal

*Um projeto educativo para construir um agente orquestrador de IA, focado em automação, privacidade e aprendizado contínuo.*

---

![Alt](https://repobeats.axiom.co/api/embed/b6d93cc31b7f99828bf90922c9065d546c0dd92e.svg "Repobeats analytics image")

## Tabela de Conteúdos
1. [Sobre o Projeto](#sobre-o-projeto)
2. [Arquitetura Fundamental](#arquitetura-fundamental)
3. [Roadmap Estratégico](#roadmap-estratégico)
4. [Começando](#começando)
5. [Como Usar](#como-usar)
6. [Estrutura do Projeto](#estrutura-do-projeto)

## Sobre o Projeto

Eros é um assistente virtual pessoal desenvolvido em Python. O objetivo principal deste projeto é educativo: explorar, passo a passo, a construção de um sistema de IA complexo, desde um simples chatbot de terminal até um assistente completo capaz de automatizar tarefas no desktop.

A filosofia do projeto é a **soberania operacional**, visando a longo prazo a independência de APIs comerciais através do uso de modelos de código aberto e infraestrutura local.

## Arquitetura Fundamental

Eros é projetado como um **Agente Orquestrador**. Esta arquitetura distingue quatro componentes principais:

1.  **Orquestrador (O Corpo):** O núcleo em Python que recebe comandos e decide qual "ferramenta" usar.
2.  **Cérebro de Raciocínio (O Cérebro Alugado):** Para tarefas complexas, o orquestrador consulta uma API de um LLM externo (como o Gemini) para obter capacidades de raciocínio e compreensão.
3.  **Ferramentas (Os Braços e Pernas):** Um conjunto de funções Python que executam ações concretas (ex: agendar um evento, ler a tela, controlar a luz). A especialização de Eros vem de suas ferramentas.
4.  **Memória (O Hipocampo):** Um Vector Database local para armazenar e recuperar informações contextuais, permitindo que Eros aprenda e se personalize com o tempo.

## Roadmap Estratégico

O desenvolvimento de Eros seguirá um plano incremental:

- **Fase 0 (MVP):** Orquestrador básico com CLI, chamada de API, e execução de comandos seguros.
- **Fase 1 (Ferramentas e Function Calling):** Integração com agenda, automação de desktop (OCR) e um robusto sistema de segurança.
- **Fase 2 (Memória e Personalização):** Implementação do Vector Database para aprendizado de longo prazo.
- **Fase 3 (Otimização e Soberania):** Implementação de um "gatekeeper" para reduzir custos de API e explorar modelos locais.
- **Fase 4 (Distribuição e Acesso Remoto):** Transformação em uma API pessoal com FastAPI para acesso de múltiplos dispositivos.
- **Fase 5 (Interação por Voz):** Implementação de módulos Speech-to-Text e Text-to-Speech.

## Começando

Siga estas instruções para configurar o ambiente de desenvolvimento localmente.

### Pré-requisitos

- Git
- Python 3.11+
- Ambiente: Testado no Fedora 41/42

### Instalação

1.  **Clone o repositório:**
    ```sh
    git clone https://github.com/JoaoPSFranca/eros-assistant.git
    cd eros-assistant
    ```

2.  **Crie e ative o ambiente virtual:**
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Instale as dependências (quando existirem):**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Configure suas chaves de API:**
    *Crie um arquivo `.env` a partir do exemplo `.env.example` e adicione suas chaves.*

## Como Usar

Para iniciar a interface de linha de comando (CLI) do Eros, execute:

```sh
python -m eros.main
```

## Estrutura do Projeto

O projeto segue uma estrutura padrão para aplicações Python, separando o código fonte (`eros/`), os testes (`tests/`) e a documentação.

