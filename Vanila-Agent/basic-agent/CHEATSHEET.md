# Vanilla Agent Cheatsheet

## What is a Vanilla Agent?

A **Vanilla Agent** is a simple AI agent that follows the core agent loop without any frameworks. It's the fundamental pattern for building AI agents that can use tools.

## Core Agent Loop

```
User Input → LLM → (Tool Call?) → Python Tool → Tool Result → LLM → Final Answer
```

### Step-by-Step Flow

1. **User Input**: User asks a question or gives a task
2. **LLM Processing**: Local LLM analyzes the input
3. **Tool Decision**: LLM decides if it needs to call a tool
4. **Tool Execution**: Python function executes the tool
5. **Tool Result**: Result is passed back to LLM
6. **Final Answer**: LLM processes the result and responds

## Two Approaches

### 1. JSON Parsing (Universal)

- LLM extracts structured data as JSON
- Python parses JSON and executes logic
- Works with any local LLM server
- Simple and reliable

### 2. Tool Calling (Advanced)

- LLM uses OpenAI-style function calling
- Automatic tool selection and execution
- More sophisticated but requires tool support
- Better for complex workflows

## Code Skeleton

```python
from openai import OpenAI
import json

# Setup
client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="not-needed"
)

def tool_function(param1, param2):
    """Your tool implementation"""
    return {"result": param1 + param2}

def vanilla_agent(user_input):
    # 1. Send to LLM
    response = client.chat.completions.create(
        model="meta-llama-3.1-8b-instruct",
        messages=[{"role": "user", "content": user_input}]
    )

    # 2. Check if tool call needed
    if "tool_call" in response.choices[0].message:
        # 3. Execute tool
        result = tool_function(args)
        # 4. Send result back to LLM
        final_response = client.chat.completions.create(...)
        return final_response.choices[0].message.content

    return response.choices[0].message.content
```

## Key Benefits

- **Framework-free**: No dependencies on complex agent frameworks
- **Local**: Works with LM Studio, Ollama, or any OpenAI-compatible server
- **Debuggable**: Easy to add print statements and see the flow
- **Extensible**: Add more tools as needed
- **Portable**: Single file can be copied anywhere

## When to Use

- Learning how agents work
- Prototyping simple agent behaviors
- Building lightweight tools
- Understanding the core agent pattern
- Quick demos and experiments
