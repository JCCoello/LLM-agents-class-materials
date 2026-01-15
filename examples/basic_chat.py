"""
Basic OpenAI Chat Completion Example
This demonstrates a simple chat interaction using the OpenAI API.
"""

import os
from openai import OpenAI

def main():
    # Initialize the OpenAI client
    # API key should be set as environment variable: OPENAI_API_KEY
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Warning: OPENAI_API_KEY not found in environment variables")
        print("Set it with: export OPENAI_API_KEY='your-key-here'")
        return
    
    # Create a simple chat completion
    print("🤖 Sending request to OpenAI...")
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that provides concise answers."
                },
                {
                    "role": "user",
                    "content": "What is the capital of France?"
                }
            ],
            temperature=0.7,
            max_tokens=150
        )
        
        # Extract and print the response
        assistant_message = response.choices[0].message.content
        print(f"\n✅ Response received:\n{assistant_message}\n")
        
        # Print usage information
        print(f"📊 Token usage:")
        print(f"   - Prompt tokens: {response.usage.prompt_tokens}")
        print(f"   - Completion tokens: {response.usage.completion_tokens}")
        print(f"   - Total tokens: {response.usage.total_tokens}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
