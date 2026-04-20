from langchain_huggingface import HuggingFaceEmbeddings
from ingestion.chunking import chunking_func
from ingestion.loaddoc import load_documents

doc=load_documents()

chunks=chunking_func(doc)

embedding_model=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

embeddings=embedding_model.embed_documents([chunk.page_content for chunk in chunks])

# print(embeddings[0])