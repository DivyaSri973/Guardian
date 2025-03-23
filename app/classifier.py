import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

# Global variables for model and tokenizer
model = None
tokenizer = None
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_model():
    """
    Load the model and tokenizer once at startup.
    """
    global model, tokenizer
    model_path = "./model_tokenizer"

    # Load the tokenizer
    tokenizer = DistilBertTokenizer.from_pretrained(model_path)

    # Load the model and move it to the appropriate device
    model = DistilBertForSequenceClassification.from_pretrained(model_path)
    model.to(device)

def predict(text):
    """
    Perform inference on the input text using the preloaded model and tokenizer.
    """
    global model, tokenizer

    # Ensure the model and tokenizer are loaded
    if model is None or tokenizer is None:
        load_model()

    # Tokenize and prepare inputs
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    inputs = {k: v.to(device) for k, v in inputs.items()}

    # Perform inference
    with torch.no_grad():
        outputs = model(**inputs)
        predicted_class = torch.argmax(outputs.logits).item()

    return predicted_class

def is_offensive(message: str) -> bool:
    """
    Classify whether a message is offensive or not.
    
    Returns:
        True if label is 0 (indicating harassment), False otherwise.
    """
    try:
        print(f"Classifying message: {message}")
        result = predict(message)
        # Assuming label 0 indicates harassment
        return result == 0
    except Exception as e:
        print(f"Error in classification: {e}")
        return False


