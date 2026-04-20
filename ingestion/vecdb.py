from langchain_community.vectorstores import FAISS

from ingestion.embed import embedding_model
from ingestion.chunking import chunked_doc
chunks=chunked_doc

vectorstore=FAISS.from_documents(documents=chunks, embedding=embedding_model)


retriever=vectorstore.as_retriever()