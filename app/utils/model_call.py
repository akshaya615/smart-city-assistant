import os
import requests
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

MODEL_ENDPOINTS = {
    "chat": os.getenv("MODEL_CHAT"),
    "feedback": os.getenv("MODEL_FEEDBACK"),
    "eco": os.getenv("MODEL_ECO"),
    "health": os.getenv("MODEL_HEALTH"),
    "summary": os.getenv("MODEL_SUMMARY")
}

headers = {
    "Authorization": f"Bearer {HUGGINGFACE_TOKEN}"
}

def query_model(prompt: str, model_key: str):
    url = MODEL_ENDPOINTS.get(model_key)
    if not url:
        return f"Error: Model key '{model_key}' not found."

    payload = {"inputs": prompt}
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            output = response.json()
            if isinstance(output, list):
                # For summarizer output
                return output[0].get("summary_text") or output[0].get("generated_text", str(output))
            elif isinstance(output, dict):
                return output.get("generated_text", str(output))
            else:
                return str(output)
        else:
            return f"Model API error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Request failed: {str(e)}"
