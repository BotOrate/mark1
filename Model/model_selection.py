import numpy as np

def select_best_model_based_on_performance_and_bias(model_metrics, bias_metrics):
    best_model = None
    best_score = -float('inf')
    for model_name, metrics in model_metrics.items():
        performance = metrics['f1']
        fairness_score = np.mean([len(bias_values) for bias_values in bias_metrics.get(model_name, {}).values()])
        if fairness_score >= 0.8 and performance > best_score:
            best_model = model_name
            best_score = performance
    return best_model
