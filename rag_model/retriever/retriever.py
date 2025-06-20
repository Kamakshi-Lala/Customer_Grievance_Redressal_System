from retriever.embedder import get_embedding
from retriever.vector_store import VectorStore
import json

def load_complaints(path='data/complaints.json'):
    with open(path, 'r') as f:
        return json.load(f)

def build_store():
    data = load_complaints()
    store = VectorStore(dim=384)
    vectors = [get_embedding(c['complaint_text']) for c in data]
    store.add(vectors, data)
    return store
