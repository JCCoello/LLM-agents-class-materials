"""
Using Environment Variables with python-dotenv
This example shows how to load API keys from a .env file.
"""

import os
from pathlib import Path
from openai import OpenAI

# Uncomment these lines if using python-dotenv
# from dotenv import load_dotenv
# load_dotenv()  # Load variables from .env file

def test_api_connection():
    """Test the OpenAI API connection."""
    
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("❌ OPENAI_API_KEY not found")
        print("\nOptions to set it:")
        print("1. Create a .env file with: OPENAI_API_KEY=your-key-here")
        print("2. Set temporarily: export OPENAI_API_KEY='your-key-here'")
        print("3. Set permanently in ~/.zshrc or ~/.bash_profile")
        return False
    
    print(f"✅ API Key found (starts with: {api_key[:10]}...)")
    
    try:
        client = OpenAI(api_key=api_key)
        
        # Test with a minimal request
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'API test successful!'"}],
            max_tokens=10
        )
        
        print(f"✅ API Connection Successful!")
        print(f"Response: {response.choices[0].message.content}")
        return True
        
    except Exception as e:
        print(f"❌ API Connection Failed: {e}")
        return False

def create_env_template():
    """Create a template .env file if it doesn't exist."""
    
    env_file = Path(".env")
    
    if env_file.exists():
        print(f"ℹ️  .env file already exists at: {env_file.absolute()}")
        return
    
    template = """# OpenAI API Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Other API keys (if needed)
# ANTHROPIC_API_KEY=your_anthropic_key_here
# HUGGINGFACE_API_KEY=your_hf_key_here
"""
    
    env_file.write_text(template)
    print(f"✅ Created .env template at: {env_file.absolute()}")
    print("⚠️  Remember to add your actual API key!")

if __name__ == "__main__":
    print("🔐 API Key Configuration Check\n")
    
    # Uncomment to create .env template
    # create_env_template()
    
    test_api_connection()
