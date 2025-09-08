# Vanilla Agent Template

A minimal, framework-free template demonstrating the core agent loop: **User → LLM → Tool → Result**.

## 🎯 What is a Vanilla Agent?

A Vanilla Agent is a simple AI agent that follows the fundamental pattern without complex frameworks. It's perfect for learning how agents work and building lightweight tools.

## 📁 Project Structure

```
├── CHEATSHEET.md           # One-page agent explanation
├── sanity_check.py         # Test local LLM connection
├── add_numbers_json.py     # JSON parsing approach (universal)
├── add_numbers_tools.py    # Tool calling approach (advanced)
├── requirements.txt        # Dependencies
├── env.example            # Environment template
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🚀 Quick Start

### 1. Setup

```powershell
# Install dependencies
pip install -r requirements.txt

# Copy environment file
copy env.example .env
```

### 2. Start Local LLM Server

**Option A: LM Studio**

- Download and install LM Studio
- Start the app and load a model (e.g., `meta-llama-3.1-8b-instruct`)

**Option B: Ollama**

```powershell
ollama serve
ollama pull meta-llama-3.1-8b-instruct
```

### 3. Test Connection

```powershell
python sanity_check.py
```

### 4. Run Examples

**JSON Approach (Recommended)**

```powershell
python add_numbers_json.py
```

**Tool Calling Approach (If supported)**

```powershell
python add_numbers_tools.py
```

## 🔄 Core Agent Loop

```
User Input → LLM → (Tool Call?) → Python Tool → Tool Result → LLM → Final Answer
```

### Example Flow

1. **User**: "What is 7 plus 9?"
2. **LLM**: Analyzes and extracts numbers
3. **Tool**: `add_numbers_tool(7, 9)` → `16`
4. **LLM**: Processes result and responds
5. **Final**: "The sum of 7 and 9 is 16"

## 📖 Two Approaches

### JSON Parsing (Universal)

- ✅ Works with any local LLM server
- ✅ Simple and reliable
- ✅ Easy to debug
- ❌ Manual JSON parsing required

### Tool Calling (Advanced)

- ✅ Automatic tool selection
- ✅ More sophisticated
- ✅ Better for complex workflows
- ❌ Requires tool calling support

## 🎮 Example Usage

Try these inputs:

- "What is 15 plus 23?"
- "Add 100 and 200"
- "Calculate 7 + 9"

## 🔧 Troubleshooting

1. **Connection Error**: Make sure your local LLM server is running
2. **Model Not Found**: Check the model name in your `.env` file
3. **Tool Call Error**: Your model might not support function calling

## 📚 Learn More

Read `CHEATSHEET.md` for a detailed explanation of the Vanilla Agent pattern and code examples.

## 🎯 Key Benefits

- **Framework-free**: No complex dependencies
- **Local**: Works with LM Studio, Ollama, or any OpenAI-compatible server
- **Debuggable**: Easy to add print statements and see the flow
- **Extensible**: Add more tools as needed
- **Portable**: Single files can be copied anywhere
