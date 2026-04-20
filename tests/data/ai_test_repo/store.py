import pinecone

def sync_data(user_documents):
    # VECTOR DB POISONING: Inserting external data without validation
    index = pinecone.Index("my-index")
    index.upsert(vectors=user_documents)
