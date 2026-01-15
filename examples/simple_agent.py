"""
Simple Agent Example - Function Calling
This demonstrates using OpenAI's function calling feature for tool use.
"""

import os
import json
from openai import OpenAI

# Define available functions
def get_current_weather(location: str, unit: str = "celsius"):
    """Simulated weather function."""
    # In a real scenario, this would call a weather API
    weather_data = {
        "location": location,
        "temperature": "22",
        "unit": unit,
        "forecast": "sunny"
    }
    return json.dumps(weather_data)

def calculate(expression: str):
    """Safely evaluate a mathematical expression."""
    try:
        # Note: eval is dangerous in production - use a proper math parser
        result = eval(expression, {"__builtins__": {}}, {})
        return json.dumps({"result": result, "expression": expression})
    except Exception as e:
        return json.dumps({"error": str(e)})

# Function definitions for OpenAI
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city name, e.g. San Francisco"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"]
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Calculate a mathematical expression",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Mathematical expression to evaluate, e.g. '2 + 2'"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]

# Map function names to actual functions
available_functions = {
    "get_current_weather": get_current_weather,
    "calculate": calculate
}

def run_agent(user_query: str):
    """Run the agent with function calling capability."""
    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Error: OPENAI_API_KEY not set")
        return
    
    messages = [{"role": "user", "content": user_query}]
    
    print(f"🤖 Query: {user_query}\n")
    
    try:
        # First API call
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )
        
        response_message = response.choices[0].message
        messages.append(response_message)
        
        # Check if the model wants to call functions
        tool_calls = response_message.tool_calls
        
        if tool_calls:
            print("🔧 Function calls requested:\n")
            
            # Execute each function call
            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)
                
                print(f"   - Calling: {function_name}({function_args})")
                
                # Call the function
                function_to_call = available_functions[function_name]
                function_response = function_to_call(**function_args)
                
                # Add function response to messages
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": function_name,
                    "content": function_response
                })
            
            # Second API call to get final response
            print("\n🤖 Getting final response...\n")
            second_response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            
            final_message = second_response.choices[0].message.content
            print(f"✅ Final Response:\n{final_message}\n")
        else:
            # No function calls needed
            print(f"✅ Direct Response:\n{response_message.content}\n")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    # Example queries
    queries = [
        "What's the weather like in Paris?",
        "What is 156 * 234?",
        "What's the weather in Tokyo and what is 50 + 50?"
    ]
    
    for query in queries:
        run_agent(query)
        print("-" * 60 + "\n")
