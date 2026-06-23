"""Main RAG Agent implementation with agentic behavior."""
from __future__ import annotations

import logging
from pathlib import Path
from typing import List, Optional

from .config import AppConfig
from .pipeline import ExecutionContext, Pipeline
from .retrieval import chunk_text
from .types import AgentResponse, Document

logger = logging.getLogger(__name__)


class AgenticRAG:
    """Main RAG agent with autonomous reasoning capabilities."""

    def __init__(self, context: ExecutionContext) -> None:
        self.context = context
        self.pipeline = Pipeline(context)
        self._initialized = False

    def initialize(self) -> None:
        """Initialize the agent and prepare resources."""
        if self._initialized:
            return

        logger.info("Initializing RAG Agentic System")
        self.pipeline.initialize()
        self._initialized = True
        logger.info("RAG Agentic System ready")

    def _generate_simple_answer(self, query: str, documents: List[Document]) -> str:
        """Generate a simple answer from retrieved documents (no LLM)."""
        if not documents:
            return "I don't have enough information to answer this question."

        # Simple extraction: return most relevant document content
        context = "\n\n".join([f"From {doc.metadata.get('path', doc.id)}:\n{doc.content[:500]}" for doc in documents[:3]])

        return f"Based on the retrieved documents:\n\n{context}\n\n(Note: This is a simple retrieval. For better answers, configure an LLM in the config file.)"

    def query(self, question: str, top_k: Optional[int] = None) -> AgentResponse:
        """Process a user query and return an answer with reasoning steps."""
        if not self._initialized:
            self.initialize()

        if not question.strip():
            return AgentResponse(
                answer="Please provide a valid question.",
                references=[],
                steps=[],
            )

        logger.info("Processing query: %s", question)

        # Step 1: Retrieve relevant documents
        documents = self.pipeline.retrieve_documents(query=question, top_k=top_k)

        if not documents:
            logger.warning("No relevant documents found for query")
            return AgentResponse(
                answer="I couldn't find relevant information to answer your question. Try adding more documents to the system.",
                references=[],
                steps=[],
            )

        # Step 2: Generate answer (simple version without LLM)
        answer = self._generate_simple_answer(question, documents)

        # Step 3: Create response with metadata
        response = self.pipeline.process(query=question, answer=answer, documents=documents)

        logger.info("Query processed successfully")
        return response

    def add_documents(self, file_paths: List[str]) -> int:
        """Add specific text/Markdown documents to the active vector store.

        Args:
            file_paths: Paths to .txt/.md files that should be chunked and indexed.

        Returns:
            Number of chunks added to the vector store.
        """
        if not file_paths:
            return 0

        allowed_extensions = {ext.lower() for ext in self.context.config.retrieval.file_extensions}
        chunked_documents: List[Document] = []

        for raw_path in file_paths:
            path = Path(raw_path).expanduser().resolve()
            if not path.exists() or not path.is_file():
                logger.warning("Skipping missing document: %s", path)
                continue
            if path.suffix.lower() not in allowed_extensions:
                logger.warning("Skipping unsupported document extension: %s", path)
                continue

            document = Document.from_path(path)
            chunks = chunk_text(
                document.content,
                self.context.config.retrieval.chunk_size,
                self.context.config.retrieval.chunk_overlap,
            )
            for idx, chunk in enumerate(chunks):
                metadata = dict(document.metadata)
                metadata.update({"chunk_index": idx, "chunk_size": len(chunk)})
                chunked_documents.append(
                    Document(
                        id=f"{document.id}#chunk-{idx}",
                        content=chunk,
                        metadata=metadata,
                    )
                )

        if not chunked_documents:
            logger.warning("No valid documents were added.")
            return 0

        # Refit TF-IDF fallback on the full corpus to keep vector dimensions stable.
        corpus = [doc.content for doc in self.context.vector_store.documents.values()]
        corpus.extend(doc.content for doc in chunked_documents)
        if self.context.embeddings.config.use_tfidf_fallback:
            self.context.embeddings.fit(corpus)

        all_documents = list(self.context.vector_store.documents.values()) + chunked_documents
        vectors = [
            (doc, self.context.embeddings.embed_single(doc.content))
            for doc in all_documents
        ]
        self.context.vector_store.clear()
        self.context.vector_store.add(vectors)
        logger.info("Added %d document chunks from %d files", len(chunked_documents), len(file_paths))
        return len(chunked_documents)

    def clear_memory(self) -> None:
        """Clear the vector store and reset."""
        self.pipeline.context.retriever.clear()
        logger.info("Vector store cleared")

    def get_stats(self) -> dict:
        """Get system statistics."""
        return {
            "total_documents": len(self.context.vector_store.documents),
            "embeddings_stored": len(self.context.vector_store.embeddings),
            "memory_enabled": self.context.memory.config.enabled,
        }


__all__ = ["AgenticRAG"]