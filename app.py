import gradio as gr
import requests

# ✅ Your actual API key (DO NOT share this publicly)
API_KEY = "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"

def chat_with_openrouter(prompt):
    if not API_KEY:
        return "Error: Missing API key."

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data
        )

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        elif response.status_code == 401:
            return "Error: Unauthorized. Check your API key."
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"

gr.Interface(
    fn=chat_with_openrouter,
    inputs="text",
    outputs="text",
    title="Vaibhav GPT Chatbot (Fixed)"
).launch(share=True)
