import os
from dotenv import load_dotenv
from google import genai

def main():
    print("Hello from simple-ai-agent!")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("API Key is None")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.5-flash', contents='Test Prompt'
    )
    print(f"Response: {response.text}")
    

if __name__ == "__main__":
    main()
