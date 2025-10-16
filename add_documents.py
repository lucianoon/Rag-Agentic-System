"""Script para adicionar documentos ao sistema RAG de forma programática."""
import sys
from pathlib import Path


def create_sample_documents():
    """Cria documentos de exemplo no diretório data/processed/."""
    processed_dir = Path("data/processed")
    processed_dir.mkdir(parents=True, exist_ok=True)

    documents = {
        "ia_conceitos.txt": """
Inteligência Artificial (IA) é a simulação de processos de inteligência humana por máquinas.
Especialmente sistemas de computador que podem aprender e resolver problemas.

As principais áreas da IA incluem:
- Machine Learning: Aprendizado de máquina a partir de dados
- Deep Learning: Redes neurais profundas
- Natural Language Processing (NLP): Processamento de linguagem natural
- Computer Vision: Visão computacional
- Robotics: Robótica inteligente

A IA tem aplicações em diversos setores como saúde, finanças, educação e transporte.
        """,

        "python_basico.txt": """
Python é uma linguagem de programação de alto nível, interpretada e de propósito geral.
Foi criada por Guido van Rossum e lançada pela primeira vez em 1991.

Características principais:
- Sintaxe simples e legível
- Tipagem dinâmica
- Ampla biblioteca padrão
- Suporte a múltiplos paradigmas de programação

Python é muito usada em:
- Ciência de dados e análise
- Desenvolvimento web (Django, Flask)
- Automação e scripts
- Inteligência Artificial e Machine Learning
- Desenvolvimento de jogos

A comunidade Python é grande e ativa, com muitas bibliotecas disponíveis.
        """,

        "machine_learning.txt": """
Machine Learning (ML) é um subcampo da Inteligência Artificial.
Permite que computadores aprendam e melhorem com a experiência sem serem explicitamente programados.

Tipos principais de Machine Learning:
1. Aprendizado Supervisionado: Treina com dados rotulados
2. Aprendizado Não Supervisionado: Encontra padrões em dados não rotulados
3. Aprendizado por Reforço: Aprende através de recompensas e punições

Algoritmos populares:
- Regressão Linear
- Árvores de Decisão
- Random Forest
- Redes Neurais
- Support Vector Machines (SVM)

Aplicações: reconhecimento de imagem, sistemas de recomendação, detecção de fraudes.
        """,

        "data_science.txt": """
Data Science (Ciência de Dados) combina programação, estatística e conhecimento de domínio.
O objetivo é extrair insights e conhecimento de dados estruturados e não estruturados.

Processo típico de Data Science:
1. Coleta de dados
2. Limpeza e preparação
3. Exploração e visualização
4. Modelagem e análise
5. Comunicação de resultados

Ferramentas comuns:
- Python (pandas, numpy, scikit-learn)
- R
- SQL
- Tableau, Power BI
- Jupyter Notebooks

Data Scientists trabalham em diversas indústrias para resolver problemas de negócio com dados.
        """
    }

    created_files = []
    for filename, content in documents.items():
        file_path = processed_dir / filename
        file_path.write_text(content.strip(), encoding="utf-8")
        created_files.append(str(file_path))
        print(f"✅ Criado: {file_path}")

    return created_files


def add_custom_document(filename: str, content: str):
    """
    Adiciona um documento customizado ao sistema.
    
    Args:
        filename: Nome do arquivo (deve terminar com .txt ou .md)
        content: Conteúdo do documento
    """
    processed_dir = Path("data/processed")
    processed_dir.mkdir(parents=True, exist_ok=True)

    if not (filename.endswith('.txt') or filename.endswith('.md')):
        raise ValueError("Arquivo deve ter extensão .txt ou .md")

    file_path = processed_dir / filename
    file_path.write_text(content, encoding="utf-8")
    print(f"✅ Documento adicionado: {file_path}")
    return str(file_path)


def list_documents():
    """Lista todos os documentos no diretório processed."""
    processed_dir = Path("data/processed")
    if not processed_dir.exists():
        print("❌ Diretório data/processed/ não existe")
        return []

    documents = list(processed_dir.glob("*.txt")) + list(processed_dir.glob("*.md"))
    
    if not documents:
        print("📁 Nenhum documento encontrado em data/processed/")
        return []

    print(f"\n📚 Documentos encontrados ({len(documents)}):")
    for doc in documents:
        size = doc.stat().st_size
        print(f"  - {doc.name} ({size} bytes)")

    return documents


def main():
    """Função principal do script."""
    print("🤖 RAG Document Manager\n")

    if len(sys.argv) > 1:
        command = sys.argv[1].lower()

        if command == "create":
            print("Criando documentos de exemplo...\n")
            create_sample_documents()
            print("\n✅ Documentos criados com sucesso!")
            print("Execute 'python main.py' para indexá-los no sistema RAG")

        elif command == "list":
            list_documents()

        elif command == "add":
            if len(sys.argv) < 4:
                print("❌ Uso: python add_documents.py add <filename> <content>")
                sys.exit(1)
            
            filename = sys.argv[2]
            content = " ".join(sys.argv[3:])
            add_custom_document(filename, content)

        elif command == "help":
            print("""
Uso: python add_documents.py [comando]

Comandos disponíveis:
  create    - Cria documentos de exemplo
  list      - Lista documentos existentes
  add       - Adiciona documento customizado
  help      - Mostra esta ajuda

Exemplos:
  python add_documents.py create
  python add_documents.py list
  python add_documents.py add meu_doc.txt "Conteúdo do documento"
            """)

        else:
            print(f"❌ Comando desconhecido: {command}")
            print("Use 'python add_documents.py help' para ver comandos disponíveis")

    else:
        # Modo interativo
        print("Escolha uma opção:")
        print("1. Criar documentos de exemplo")
        print("2. Listar documentos existentes")
        print("3. Adicionar documento customizado")
        print("4. Sair")

        choice = input("\nOpção: ").strip()

        if choice == "1":
            print("\nCriando documentos de exemplo...\n")
            create_sample_documents()
            print("\n✅ Documentos criados!")

        elif choice == "2":
            print()
            list_documents()

        elif choice == "3":
            filename = input("\nNome do arquivo (ex: meu_doc.txt): ").strip()
            print("Digite o conteúdo (Ctrl+D ou Ctrl+Z para finalizar):")
            
            lines = []
            try:
                while True:
                    line = input()
                    lines.append(line)
            except EOFError:
                pass

            content = "\n".join(lines)
            add_custom_document(filename, content)

        elif choice == "4":
            print("Até logo!")
            return

        else:
            print("❌ Opção inválida")

        print("\n💡 Execute 'python main.py' para indexar os documentos no sistema RAG")


if __name__ == "__main__":
    main()