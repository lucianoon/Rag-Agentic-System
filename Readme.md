# RAG Agentic System 🤖

A comprehensive **Retrieval-Augmented Generation (RAG) system with agentic behavior** for intelligent information retrieval and processing.

## 📋 Overview

This project implements a sophisticated RAG system that goes beyond simple question-answering to provide autonomous, multi-step reasoning and task execution. The system combines:

- **Agentic Behavior**: Multi-step planning, execution, and adaptation
- **Retrieval-Augmented Generation**: Grounded responses using external knowledge
- **Vector Search**: Semantic similarity search for precise fact retrieval
- **Memory System**: Learning from past interactions and continuous improvement
- **Result Verification**: Multi-layered verification for accuracy and reliability

## 🏗️ Architecture

The system follows the complete RAG agentic workflow:

1. **Define Goal** → Clear task definition and objective setting
2. **Retrieve Data** → Extract documents from multiple sources  
3. **Vector Search** → Use embeddings for exact fact finding
4. **Multi-Step Planning** → Generate execution strategy
5. **Execution Loop** → Retrieve → Reason → Act → Verify
6. **Implement Actions** → Execute planned steps with verification
7. **Verify Results** → Multi-dimensional accuracy checking
8. **Update Memory** → Store results for future reuse
9. **Adapt** → Continuous improvement based on feedback

## 🚀 Features

### Core Capabilities
- **Multi-Source Retrieval**: Filesystem, databases, APIs, and web sources
- **Advanced Vector Search**: FAISS or simple vector stores with multiple embedding models
- **Intelligent Memory**: SQLite-based storage with importance scoring and cleanup
- **Comprehensive Verification**: Factual, logical, and source verification
- **Interactive CLI**: User-friendly command-line interface
- **Configurable Pipeline**: YAML-based configuration system

### Agent Features
- **Multi-Step Reasoning**: Break complex tasks into manageable steps
- **Error Handling**: Robust retry mechanisms and graceful failure handling
- **Performance Monitoring**: Built-in metrics and statistics tracking
- **Extensible Design**: Plugin architecture for custom components

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- Git

### Quick Start

```bash
# Clone the repository
git clone https://github.com/username/rag-agentic-system.git
cd rag-agentic-system

# Install basic dependencies
pip install -r requirements.txt

# For enhanced functionality (recommended)
pip install -e .[ml,nlp]

# Run the system
python main.py
```

### Dependencies

#### Core Dependencies (Required)
```bash
pip install numpy>=1.21.0 pyyaml>=6.0 python-dotenv>=0.19.0 requests>=2.28.0 coloredlogs>=15.0.0
```

#### Optional Dependencies (Enhanced Features)
```bash
# Machine Learning
pip install sentence-transformers>=2.2.0 faiss-cpu>=1.7.0 torch>=2.0.0

# Advanced NLP
pip install spacy>=3.4.0 nltk>=3.8.0

# Web Scraping
pip install beautifulsoup4>=4.11.0 selenium>=4.0.0

# Database Integration
pip install sqlalchemy>=1.4.0 psycopg2-binary>=2.9.0

# API Integration
pip install openai>=1.0.0 anthropic>=0.3.0

# Development Tools
pip install pytest>=7.0.0 black>=22.0.0 mypy>=1.0.0
```

## 🎯 Usage

### Interactive Mode (Default)

```bash
python main.py
```

This starts the interactive RAG agent:

```
🤖 RAG Agentic System - Interactive Mode
Type 'help' for commands, 'quit' to exit

RAG> What is machine learning?
🔍 Processing: What is machine learning?
📋 Task defined: What is machine learning
📚 Retrieved 12 documents
🎯 Found 5 relevant facts
📝 Planned 2 execution steps
🎉 Task completed! ✅ Verified
📄 Response: Machine learning is a subset of artificial intelligence...
```

### Single Task Mode

```bash
python main.py --task "Explain quantum computing"
```

### Adding Documents

```bash
python main.py --add-docs document1.txt research_paper.pdf
```

### Custom Configuration

```bash
python main.py --config custom_config.yaml
```

### Available Commands

In interactive mode:
- `help` - Show available commands
- `stats` - Display system statistics
- `history` - Show recent task history
- `quit`/`exit`/`q` - Exit the system

## 📁 Project Structure

```
rag-agentic-system/
├── main.py                 # Main application entry point
├── pyproject.toml          # Project configuration
├── requirements.txt        # Dependencies
├── README.md              # This file
├── .gitignore             # Git ignore rules
│
├── src/rag_agent/         # Core application code
│   ├── __init__.py        # Package initialization
│   ├── agent.py           # Main RAG agent implementation
│   ├── retrieval.py       # Document retrieval system
│   ├── vector_search.py   # Vector search engine
│   ├── memory.py          # Agent memory system
│   └── verification.py    # Result verification
│
├── config/                # Configuration files
│   └── config.yaml        # Main configuration
│
├── data/                  # Data storage
│   ├── raw/              # Raw input documents
│   ├── processed/        # Processed data
│   └── vector_store/     # Vector database files
│
├── tests/                 # Test suite
│   ├── test_agent.py     # Agent tests
│   ├── test_retrieval.py # Retrieval tests
│   └── ...               # Other test files
│
├── docs/                  # Documentation
└── logs/                  # Application logs
```

## ⚙️ Configuration

The system is highly configurable via YAML files. Main configuration sections:

### Agent Configuration
```yaml
agent:
  max_iterations: 10
  timeout_seconds: 300
  retry_attempts: 3
```

### Memory System
```yaml
memory:
  database_path: "data/memory.db"
  cleanup_days: 30
  importance_threshold: 0.3
```

### Vector Search
```yaml
vector_search:
  embedding_model: "all-MiniLM-L6-v2"
  vector_store_type: "simple"  # or "faiss"
  dimension: 384
```

See `config/config.yaml` for complete configuration options.

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/rag_agent

# Run specific test categories
pytest -m "unit"          # Unit tests only
pytest -m "integration"   # Integration tests only
```

## 📊 Performance & Monitoring

### System Statistics
```bash
RAG> stats
📊 System Statistics:
  Vector Documents: 150
  Embedding Model: SentenceTransformerModel
  Vector Store: SimpleVectorStore
  Recent Tasks: 25
  Success Rate: 87.3%
```

### Logging
Comprehensive logging is built-in:
- Console output for user interaction
- File logging for debugging (`logs/rag_agent.log`)
- Configurable log levels per component

## 🔧 Development

### Setup Development Environment

```bash
# Install development dependencies
pip install -e .[dev]

# Setup pre-commit hooks
pre-commit install

# Run code formatting
black src/ tests/
flake8 src/ tests/

# Type checking
mypy src/
```

### Adding Custom Components

The system is designed to be extensible:

1. **Custom Retrievers**: Implement `BaseRetriever` interface
2. **Custom Verifiers**: Implement `BaseVerifier` interface  
3. **Custom Vector Stores**: Implement `BaseVectorStore` interface
4. **Custom Embedding Models**: Implement `BaseEmbeddingModel` interface

Example custom retriever:

```python
from rag_agent.retrieval import BaseRetriever, Document

class CustomRetriever(BaseRetriever):
    def retrieve(self, query: str, filters=None) -> List[Document]:
        # Your custom retrieval logic here
        return documents
```

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide
- Add tests for new features
- Update documentation as needed
- Use type hints for better code clarity

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Sentence Transformers** for embedding models
- **FAISS** for efficient vector search
- **PyTorch** for machine learning capabilities
- The open-source AI community for inspiration

## 📚 Further Reading

### RAG and Agentic Systems
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [Building Agentic RAG with LlamaIndex](https://docs.llamaindex.ai/en/stable/use_cases/agents/)

### Vector Search and Embeddings
- [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://arxiv.org/abs/1908.10084)
- [FAISS: A Library for Efficient Similarity Search](https://github.com/facebookresearch/faiss)

## 🆘 Support

If you encounter issues:

1. Check the [Issues](https://github.com/lucianoon/rag-agentic-system/issues) page
2. Review the logs in `logs/rag_agent.log`
3. Ensure all dependencies are correctly installed
4. Try running with `--debug` flag for detailed logging

For questions or discussions, please open an issue or contact the maintainers.
email: lucianomevam@outlook.com
