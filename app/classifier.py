import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from pathlib import Path

# Device config
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load models once
sexist_model_path = "./sexism_comments_detection_model"
offensive_model_path = "./model_tokenizer"  # Ensure this is a Path object

# Convert to string explicitly to avoid HFValidationError
sexist_tokenizer = DistilBertTokenizer.from_pretrained(str(sexist_model_path), local_files_only=True)
sexist_model = DistilBertForSequenceClassification.from_pretrained(str(sexist_model_path), local_files_only=True).to(device)

offensive_tokenizer = DistilBertTokenizer.from_pretrained(str(offensive_model_path), local_files_only=True)
offensive_model = DistilBertForSequenceClassification.from_pretrained(str(offensive_model_path), local_files_only=True).to(device)

def predict(model, tokenizer, text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    inputs = {k: v.to(device) for k, v in inputs.items()}
    with torch.no_grad():
        outputs = model(**inputs)
        predicted_class = torch.argmax(outputs.logits).item()
    return predicted_class

def is_offensive(message: str) -> bool:
    try:
        print(f"Classifying offensive message: {message}")
        result = predict(offensive_model, offensive_tokenizer, message)
        return result == 0  # Assuming 0 = offensive
    except Exception as e:
        print(f"Error in offensive classification: {e}")
        return False

def is_sexist(message: str) -> bool:
    try:
        print(f"Classifying sexist message: {message}")
        result = predict(sexist_model, sexist_tokenizer, message)
        return result == 1  # Assuming 1 = sexist
    except Exception as e:
        print(f"Error in sexist classification: {e}")
        return False
