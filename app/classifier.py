from transformers import pipeline

# Load model once at startup
classifier = pipeline("text-classification", model="unitary/toxic-bert")

def is_offensive(message: str) -> bool:
    try:
        print(f"Classifying message: {message}")
        result = classifier(message)[0]
        label = result['label']
        score = result['score']
        return label.lower() == 'toxic' and score > 0.7
    except Exception as e:
        print(f"Error in classification: {e}")
        return False