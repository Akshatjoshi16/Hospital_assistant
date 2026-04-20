from langchain_text_splitters import RecursiveCharacterTextSplitter

from ingestion.loaddoc import load_documents

doc=load_documents()


def chunking_func(doc):
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        length_function=len,
        add_start_index=True,
    )

    return text_splitter.split_documents(doc)


chunked_doc=chunking_func(doc)

# print(len(chunked_doc))