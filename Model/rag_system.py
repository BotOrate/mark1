import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import torch


reviews_df = pd.read_json("data/software_reviews_preprocessed.jsonl", lines=True, nrows=5)
metadata_df = pd.read_json("data/software_metadata_preprocessed.jsonl", lines=True, nrows=5)

print(reviews_df.head())
print(metadata_df.head())



import pandas as pd

# Define chunk size to load only part of the dataset
chunk_size = 30000  # Load 100k rows at a time
reviews_iter = pd.read_json("data/software_reviews_preprocessed.jsonl", lines=True, chunksize=chunk_size)
reviews_df = next(reviews_iter)  # Load first chunk only

print("✅ Loaded a small chunk of the dataset:")
print(reviews_df.head())



from sentence_transformers import SentenceTransformer

# Load the model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Assuming 'reviews_df' contains a column 'text' with review data
embeddings = model.encode(reviews_df['text'].tolist())




import faiss
import numpy as np

# Dimension of embeddings
d = embeddings.shape[1]

# Build the index
index = faiss.IndexFlatL2(d)
index.add(np.array(embeddings).astype('float32'))  # Add embeddings to index


def retrieve_reviews(query, k=5):
    query_embedding = model.encode([query])[0]
    D, I = index.search(np.array([query_embedding]).astype('float32'), k)
    return reviews_df.iloc[I[0]]


from openai import OpenAI
import os

def generate_response_with_openai(prompt):
    client = OpenAI()
    try:
        completion = client.completions.create(
            model="gpt-3.5-turbo-instruct",  # Use the instruct model
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        return completion.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
prompt = "What is the future of artificial intelligence?"
response_text = generate_response_with_openai(prompt)
print(response_text)


def rag_system(query):
    # Retrieve top 5 relevant reviews
    retrieved_reviews = retrieve_reviews(query, k=5)
    retrieved_texts = " ".join(retrieved_reviews['text'])  # Combine texts of retrieved reviews

    # Generate a response based on the retrieved texts
    response_text = generate_response_with_openai(retrieved_texts)
    return response_text

# Example usage
query = "Tell me about the user experiences with recent software updates."
final_response = rag_system(query)
print(final_response)
