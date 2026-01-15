"""
Interactive Chat Example with Conversation History
This example maintains a conversation history for multi-turn interactions.
"""

import os
from openai import OpenAI

def chat_session():
    """Run an interactive chat session with conversation history."""
    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Error: OPENAI_API_KEY not set")
        print("Run: export OPENAI_API_KEY='your-key-here'")
        return
    
    # Initialize conversation history
    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant. Be concise and friendly."
        }
    ]
    
    print("🤖 Interactive Chat Session Started")
    print("Type 'quit', 'exit', or 'q' to end the conversation\n")
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Check for exit commands
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Goodbye!")
            break
        
        if not user_input:
            continue
        
        # Add user message to history
        messages.append({
            "role": "user",
            "content": user_input
        })
        
        try:
            # Get AI response
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.8,
                max_tokens=500
            )
            
            # Extract assistant's reply
            assistant_reply = response.choices[0].message.content
            
            # Add assistant's reply to history
            messages.append({
                "role": "assistant",
                "content": assistant_reply
            })
            
            # Display the response
            print(f"\nAssistant: {assistant_reply}\n")
            
        except Exception as e:
            print(f"\n❌ Error: {e}\n")
            # Remove the failed user message
            messages.pop()

if __name__ == "__main__":
    chat_session()
