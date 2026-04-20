from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

def load_documents():
    loader = DirectoryLoader(
        "ingestion/hospital_docs/",
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )
    documents = loader.load()
    return documents