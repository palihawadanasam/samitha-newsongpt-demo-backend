from databricks.vector_search.client import VectorSearchClient
from app.models.schemas import DocumentResponse

class VectorDBService:
    def __init__(self):
        self.client = VectorSearchClient()
        self.index_name = "rag_documents"

    def add_document(self, text: str, user_id: str) -> DocumentResponse:
        """Add document to Databricks Vector Search"""
        doc_id = f"doc_{uuid.uuid4()}"
        embedding = self._generate_embedding(text)
        
        self.client.upsert(
            index_name=self.index_name,
            inputs=[{
                "id": doc_id,
                "text": text,
                "embedding": embedding,
                "owner_id": user_id
            }]
        )
        
        return DocumentResponse(
            id=doc_id,
            text=text,
            created_at=datetime.now(),
            owner_id=user_id
        )