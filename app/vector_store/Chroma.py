import chromadb
from app.config import settings

client = chromadb.PersistentClient(path=settings.chroma_db_path)


def get_collection(doc_id: str):
  return client.get_or_create_collection(
    name=doc_id,
    metadata={"hnsw:space": "cosine"}
  )

def add_chunks(doc_id: str, chunk_ids: list[str], embeddings: list, documents: list[str]):
  collection = get_collection(doc_id)
  collection.add(
    ids=chunk_ids,
    embeddings=embeddings,
    documents=documents
  )

def query_collection(doc_id: str, query_embedding: list, n_results: int = 3):
  collection = get_collection(doc_id)
  return collection.query(
    query_embeddings=query_embedding,
    n_results=n_results,
    include=["documents", "distances"]
  )
