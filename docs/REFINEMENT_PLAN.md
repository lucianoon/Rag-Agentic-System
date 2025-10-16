# Plano de Refinamento do RAG Agentic System

## Objetivos Principais
1. Transformar o repositório atual (apenas README) em um projeto funcional.
2. Implementar um pipeline RAG mínimo, porém extensível, com comportamento agentic.
3. Fornecer documentação, configuração e testes básicos para facilitar uso e evolução.

## Etapas de Trabalho

### 1. Estrutura do Projeto
- [ ] Criar diretórios principais:
  - `src/rag_agent/` (código-fonte)
  - `config/` (arquivos YAML de configuração)
  - `data/` (subpastas `raw/`, `processed/`, `vector_store/`)
  - `tests/` (testes unitários)
  - `docs/` (documentação adicional)
- [ ] Adicionar `.gitignore` específico para o projeto.

### 2. Core Pipeline Components
- [ ] Definir tipos e modelos de dados (`Document`, `RetrievalResult`, etc.).
- [ ] Implementar módulo de embeddings com fallback (Sentence-Transformers → TF-IDF).
- [ ] Criar vetor store simples baseado em cosine similarity.
- [ ] Implementar retrievers (filesystem/text) e pipeline de parsing básico.
- [ ] Implementar memória usando SQLite (ou fallback em JSON).
- [ ] Implementar verificação básica (heurísticas simples + placeholders).
- [ ] Criar agente principal com loop de raciocínio e integração dos módulos.

### 3. CLI e Execução
- [ ] Criar `main.py` com CLI interativa e modo tarefa única.
- [ ] Suporte a comandos `stats`, `history`, `reload`, `quit`.
- [ ] Prover script para ingestão de documentos (`ingest.py`).

### 4. Configuração e Dependências
- [ ] Adicionar `pyproject.toml` e/ou `requirements.txt`.
- [ ] Criar arquivo `config/default.yaml` com parâmetros bem documentados.
- [ ] Documentar variáveis de ambiente (ex.: chaves de API).

### 5. Documentação
- [ ] Atualizar README para refletir implementação real.
- [ ] Adicionar guia de instalação rápida.
- [ ] Adicionar guia de desenvolvimento (lint, testes, pre-commit).
- [ ] Descrever extensibilidade (como criar novos retrievers/verifiers).

### 6. Testes e Qualidade
- [ ] Implementar testes unitários básicos (ex.: carregar docs, vetor store, pipeline).
- [ ] Configurar `pytest` + `coverage`.
- [ ] Adicionar verificação `black`, `flake8` (opcional) ou documentar.

### 7. Entregáveis Finais
- Projeto funcional que roda localmente com:
  - Ingestão de documentos `.txt`/`.md`.
  - Embeddings e busca vetorial.
  - Resposta gerada via LLM (opções: OpenAI, Transformers local ou fallback).
  - Memória persistente simples.
  - Logging e configurações ajustáveis.

## Notas
- Priorizar componentes desacoplados e interfaces claras.
- Incluir TODOs para funcionalidades avançadas (FAISS, plugins, etc.).
- Garantir que o projeto roda mesmo sem GPU (fallbacks).