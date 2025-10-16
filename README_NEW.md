# RAG Agentic System 🤖

A comprehensive **Retrieval-Augmented Generation (RAG) system with agentic behavior** for intelligent information retrieval and processing.

## ✨ Features

- **Multi-Source Retrieval**: Filesystem-based document ingestion
- **Flexible Embeddings**: Sentence-Transformers with automatic TF-IDF fallback
- **Vector Search**: In-memory cosine similarity search
- **Task Memory**: SQLite-based storage for task history
- **Interactive CLI**: User-friendly command-line interface
- **Configurable Pipeline**: YAML-based configuration

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Git

### Quick Start

```bash
# Clone the repository
git clone https://github.com/lucianoon/Rag-Agentic-System.git
cd Rag-Agentic-System

# Install dependencies
pip install -r requirements.txt

# Run the system
python main.py
```

## 📖 Usage

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

📄 Response:
Based on the retrieved documents...
```

### Single Task Mode

```bash
python main.py --task "Explain quantum computing"
```

### Adding Documents

1. Place your `.txt` or `.md` files in the `data/processed/` directory
2. Run the system - it will automatically index them on startup

### Configuration

Edit `config/default.yaml` to customize:
- Embedding models
- Vector store settings
- Retrieval parameters
- Memory settings

### Available Commands

In interactive mode:
- `<question>` - Ask a question
- `stats` - Display system statistics
- `history` - Show recent task history
- `clear` - Clear vector store
- `quit`/`exit`/`q` - Exit the system

## 📁 Project Structure

```
rag-agentic-system/
├── main.py                     # Main CLI entry point
├── requirements.txt            # Dependencies
├── README.md                   # This file
├── config/
│   └── default.yaml           # Configuration file
├── src/rag_agent/             # Core application code
│   ├── __init__.py            # Package initialization
│   ├── agent.py               # Main RAG agent
│   ├── config.py              # Configuration management
│   ├── embeddings.py          # Embedding backends
│   ├── memory.py              # Task memory store
│   ├── pipeline.py            # Pipeline orchestration
│   ├── retrieval.py           # Document retrieval
│   ├── types.py               # Data models
│   └── vector_store.py        # Vector storage
├── data/
│   └── processed/             # Place documents here
└── docs/
    └── REFINEMENT_PLAN.md     # Development roadmap
```

## ⚙️ Configuration

The system uses YAML configuration in `config/default.yaml`:

### Embeddings
```yaml
embeddings:
  model_name: "sentence-transformers/all-MiniLM-L6-v2"
  use_tfidf_fallback: true  # Fallback if transformers unavailable
```

### Vector Store
```yaml
vector_store:
  top_k: 5  # Number of documents to retrieve
```

### Retrieval
```yaml
retrieval:
  sources:
    - "data/processed"
  file_extensions:
    - ".txt"
    - ".md"
  chunk_size: 512
  chunk_overlap: 64
```

## 🔧 Development

### Dependencies

Core:
- `numpy` - Numerical operations
- `pyyaml` - Configuration parsing
- `scikit-learn` - TF-IDF fallback embeddings

Optional (recommended):
- `sentence-transformers` - Better embeddings
- `torch` - Required for transformers

Development:
- `pytest` - Testing
- `black` - Code formatting
- `flake8` - Linting

### Running Tests

```bash
pytest tests/
```

### Code Formatting

```bash
black src/ tests/
flake8 src/ tests/
```

## 📊 How It Works

1. **Document Ingestion**: Reads files from `data/processed/`
2. **Chunking**: Splits documents into manageable chunks
3. **Embedding**: Converts chunks to vector representations
4. **Indexing**: Stores embeddings in vector store
5. **Query Processing**: 
   - User asks a question
   - Question is embedded
   - Most similar chunks are retrieved
   - Answer is generated from retrieved context
6. **Memory**: Task history is saved for future reference

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- **Sentence Transformers** for embedding models
- **scikit-learn** for TF-IDF fallback
- **PyTorch** for machine learning capabilities

## 📚 Next Steps

See [`docs/REFINEMENT_PLAN.md`](docs/REFINEMENT_PLAN.md) for planned improvements:
- LLM integration (OpenAI, Anthropic)
- FAISS vector store backend
- Web scraping capabilities
- Advanced verification systems
- Plugin architecture

## 🆘 Support

For issues or questions:
- Email: lucianomevam@outlook.com
- GitHub Issues: https://github.com/lucianoon/Rag-Agentic-System/issues

---

**Built with ❤️ for the AI community**