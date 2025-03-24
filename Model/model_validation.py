import mlflow
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

def validate_model_rag(model_name, reviews_df, query, top_k=5):
    with mlflow.start_run():
        mlflow.set_tag("model_name", model_name)
        mlflow.log_param("query", query)
        retrieved_reviews = retrieve_reviews(query, reviews_df, top_k)
        accuracy = evaluate_retrieval_accuracy(retrieved_reviews, query)
        mlflow.log_metric("retrieval_accuracy", accuracy)
        print(f"Model Validation Accuracy for Query: {accuracy:.4f}")
    return accuracy, retrieved_reviews

def retrieve_reviews(query, reviews_df, top_k=5):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    review_embeddings = model.encode(reviews_df['text'].tolist())
    index = faiss.IndexFlatL2(review_embeddings.shape[1])
    index.add(np.array(review_embeddings).astype('float32'))
    query_embedding = model.encode([query])[0]
    D, I = index.search(np.array([query_embedding]).astype('float32'), top_k)
    return reviews_df.iloc[I[0]]

def evaluate_retrieval_accuracy(retrieved_reviews, query):
    correct_count = 0
    for review in retrieved_reviews['text']:
        if query.lower() in review.lower():
            correct_count += 1
    return correct_count / len(retrieved_reviews)
