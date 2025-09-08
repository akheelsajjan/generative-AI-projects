#!/usr/bin/env python3
"""
Simple Local LLM Number Addition Demo
Uses OpenAI API to connect to local LM Studio or Ollama server.
"""

from openai import OpenAI
import json

# Configuration
client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="not-needed"
)

def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

def main():
    print("🧮 Local LLM Number Addition Demo")
    print("=" * 40)
    
    try:
        # Test connection first
        print("🔄 Testing connection...")
        response = client.chat.completions.create(
            model="meta-llama-3.1-8b-instruct",
            messages=[{"role": "user", "content": "Hello! Just say 'OK' to confirm you're working."}]
        )
        print(f"✅ Connection successful: {response.choices[0].message.content}")
        print()
        
        # Get user input
        user_input = input("💬 Enter your math question (e.g., 'What is 7 plus 9?'): ").strip()
        
        if not user_input:
            print("❌ No input provided. Exiting.")
            return
        
        print(f"🔄 Processing: '{user_input}'")
        
        # Create tightened prompt for strict JSON parsing
        SYSTEM = """You are a strict parser for ADDITION QUESTIONS ONLY.

Return a single JSON object with exactly these keys:
- can_parse: true|false
- a: integer (present only if can_parse is true)
- b: integer (present only if can_parse is true)
- reason: short string (present only if can_parse is false)

Rules:
1) If the user is NOT asking to add two numbers, set can_parse=false and explain in 'reason'.
2) Never invent 0 or placeholders. If uncertain, can_parse=false.
3) Output ONLY valid JSON. No prose, no code fences.
Examples:
User: "What is 7 plus 9?"
{"can_parse": true, "a": 7, "b": 9}

User: "What is earth shape?"
{"can_parse": false, "reason": "Not an addition request"}

User: "Add 10 and -3"
{"can_parse": true, "a": 10, "b": -3}"""
        
        # Ask the model using your working format
        print("🤖 Asking the model...")
        response = client.chat.completions.create(
            model="meta-llama-3.1-8b-instruct",
            messages=[
                {"role": "system", "content": SYSTEM},
                {"role": "user", "content": user_input}
            ]
        )
        
        # Get the response
        model_response = response.choices[0].message.content
        print(f"📝 Model response: {model_response}")
        
        # Parse JSON with new structure
        try:
            data = json.loads(model_response)
            can_parse = data.get("can_parse")
            
            if can_parse is None:
                print("❌ Invalid JSON: missing 'can_parse' field")
                return
                
            if not can_parse:
                reason = data.get("reason", "Unknown reason")
                print(f"❌ Cannot parse: {reason}")
                return
            
            # Extract numbers if parsing is successful
            a = data.get("a")
            b = data.get("b")
            
            if a is None or b is None:
                print("❌ Invalid JSON: missing 'a' or 'b' field")
                return
                
            if not isinstance(a, int) or not isinstance(b, int):
                print("❌ Invalid JSON: 'a' and 'b' must be integers")
                return
                
        except json.JSONDecodeError as e:
            print(f"❌ Failed to parse JSON: {e}")
            return
        
        # Calculate and display result
        result = add_numbers(a, b)
        print()
        print("🎯 SUCCESS!")
        print(f"   First number: {a}")
        print(f"   Second number: {b}")
        print(f"   Sum: {a} + {b} = {result}")
        print()
        print(f"🏆 RESULT: {result}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print()
        print("🔧 Make sure your local LLM server is running:")
        print("   - LM Studio: Start app and load a model")
        print("   - Ollama: Run 'ollama serve' in terminal")

if __name__ == "__main__":
    main()