import pandas as pd
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall
)

from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper

from eval_dataset import load_eval_dataset
from rag_qa import rag
from model import llm
from ingestion.embed import embedding_model


def generate_rag_answers(dataset):
    questions = dataset["question"]

    answers = []
    contexts = []

    for question in questions:
        response = rag.invoke({
            "input": question,
            "chat_history": []
        })

        answers.append(response["answer"])

        retrieved_context = [
            doc.page_content for doc in response["context"]
        ]
        contexts.append(retrieved_context)

    dataset = dataset.add_column("answer", answers)
    dataset = dataset.add_column("contexts", contexts)

    return dataset


def main():
    print(" evaluation dataset")
    dataset = load_eval_dataset()

    print("Generate RAG answer")
    dataset = generate_rag_answers(dataset)

    print("Prepare RAGAS wrappers")

    ragas_llm = LangchainLLMWrapper(llm)
    ragas_embeddings = LangchainEmbeddingsWrapper(embedding_model)

    print("evaluation")

    result = evaluate(
        dataset=dataset,
        metrics=[
            faithfulness,
            answer_relevancy,
            context_precision,
            context_recall,
        ],
        llm=ragas_llm,
        embeddings=ragas_embeddings
    )

  
    print(result)

  
if __name__ == "__main__":
    main()