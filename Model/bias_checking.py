import matplotlib.pyplot as plt

def check_bias_in_reviews(reviews_df, query, sensitive_feature_column):
    print(f"Checking bias for query: '{query}'...")
    biased_reviews = {}
    for feature_value in reviews_df[sensitive_feature_column].unique():
        filtered_reviews = reviews_df[reviews_df[sensitive_feature_column] == feature_value]
        retrieved_reviews = retrieve_reviews(query, filtered_reviews)
        biased_reviews[feature_value] = len(retrieved_reviews)
    visualize_bias(biased_reviews)
    return biased_reviews

def visualize_bias(biased_reviews):
    categories = list(biased_reviews.keys())
    values = list(biased_reviews.values())
    plt.bar(categories, values)
    plt.xlabel('Sensitive Feature (e.g., Gender)')
    plt.ylabel('Number of Relevant Reviews Retrieved')
    plt.title('Bias Check in Review Retrieval')
    plt.show()
