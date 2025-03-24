from audio import record_audio, transcribe_audio
from rag_system import rag_system 
from tts import text_to_speech
from vault import read_vault, update_vault
import pandas as pd
from model_validation import validate_model_rag
from bias_checking import check_bias_in_reviews
from model_selection import select_best_model_based_on_performance_and_bias
from model_registry import push_model_metadata_to_registry

AUDIO_FILE = "user_input.wav"

def main():
    record_audio(AUDIO_FILE)

    user_query = transcribe_audio(AUDIO_FILE)

    response_text = rag_system(user_query)

    text_to_speech(response_text)

    reviews_df = pd.read_json("data/software_reviews_preprocessed.jsonl", lines=True)
    query = "Tell me about user experiences with the latest software updates."
    accuracy, retrieved_reviews = validate_model_rag("gpt-3.5-turbo-instruct", reviews_df, query)
    bias_metrics = check_bias_in_reviews(reviews_df, query, sensitive_feature_column='user_gender')
    model_metrics = {
        "gpt-3.5-turbo-instruct": {'f1': accuracy}
    }
    selected_model = select_best_model_based_on_performance_and_bias(model_metrics,
                                                                     {'gpt-3.5-turbo-instruct': bias_metrics})
    print(f"Selected model: {selected_model}")
    push_model_metadata_to_registry(selected_model, {"f1": accuracy}, "your-bucket-name")

if __name__ == "__main__":
    main()
