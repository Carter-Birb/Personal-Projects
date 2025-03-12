import requests

# Ollama API endpoint (local)
OLLAMA_API_URL = "http://localhost:11434/api/generate"

# Example text to test the model
input_text = """
The sun dipped below the horizon, casting an orange glow across the sky. Birds flew in the distance, and the world seemed to pause for a moment. As the light faded, the cool breeze whispered through the trees. The day ended, and the night began its quiet embrace. In the distance, the lights of the town flickered on, and the stars started to appear, one by one, as if they were waiting for the right moment to shine.
"""

# Function to test Qwen 1.8b model with the input text
def test_qwen_model(text):
    # Prepare the payload for the request
    payload = {
        "model": "qwen-1.8b",  # Ensure the model name is correct
        "prompt": f"Summarize the following text:\n\n{text}"
    }

    # Send the request to Ollama's API
    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        
        # Extract the model's response
        summary = data.get("response", "No response received from the model.")
        return summary
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Run the test
if __name__ == "__main__":
    print("Testing Qwen 1.8b Model...\n")
    result = test_qwen_model(input_text)
    print("Model Response:\n")
    print(result)