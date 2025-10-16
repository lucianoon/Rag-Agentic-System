"""Main RAG Agent implementation with agentic behavior."""
from __future__ import annotations

import logging
from typing import List, Optional

from .config import AppConfig
from .pipeline import ExecutionContext, Pipeline
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
        """Manually add documents to the system."""
        # This is a placeholder - in a full implementation, this would handle adding new docs
        logger.info("Adding %d documents", len(file_paths))
        self.pipeline.context.retriever.ingest()
        return len(file_paths)

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