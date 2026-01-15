# Q&A Notes - Setup Session

**Date:** January 13, 2026  
**Topic:** Python Virtual Environment Setup for LLM Agents Class (macOS)

---

## 🔧 Initial Problem

**Issue:** Trying to activate Python virtual environment but getting exit code 126

**Error Command:**

```bash
.env/bin/activate
# Exit Code: 126
```

**Root Cause:** The activation script was being executed directly instead of being sourced into the shell. On macOS/Linux, activation scripts modify the current shell environment, so they must be sourced.

---

## ✅ Solution

**Correct Command:**

```bash
source .env/bin/activate
# or
. .env/bin/activate
```

**Why it works:** The `source` command runs the script in the current shell context, allowing it to modify environment variables (`PATH`, `VIRTUAL_ENV`, etc.) that persist after the script finishes.

---

## 🎯 Key Learning Points

### 1. Virtual Environment Activation (macOS vs Windows)

| Platform               | Command                     |
| ---------------------- | --------------------------- |
| **macOS/Linux**        | `source .env/bin/activate`  |
| **Windows PowerShell** | `.env\Scripts\activate`     |
| **Windows CMD**        | `.env\Scripts\activate.bat` |

### 2. Why Direct Execution Fails

- `.env/bin/activate` tries to execute the file as a standalone program
- Exit code 126 = "Permission denied" or "Cannot execute"
- Even with execute permission (`chmod +x`), it wouldn't modify your current shell

### 3. Python Command Differences

On macOS (outside virtual environment):

- Use `python3` instead of `python`
- Use `pip3` instead of `pip` (if not in venv)

Inside activated venv:

- Both `python` and `python3` work
- Both `pip` and `pip3` work

---

## 📦 Setup Steps Completed

### 1. Virtual Environment Creation

```bash
python3 -m venv .env
```

### 2. Activation (Correct Method)

```bash
source .env/bin/activate
```

### 3. Package Installation

```bash
pip install openai
```

### 4. Verification

Check if venv is active:

```bash
which python      # Should show: /Users/coello/LLM_agents_class/.env/bin/python
echo $VIRTUAL_ENV # Should show: /Users/coello/LLM_agents_class/.env
```

---

## 📁 Repository Structure Created

```
LLM_agents_class/
├── README.md              # Full setup guide with macOS/Windows comparisons
├── QA_notes.md           # This file - Q&A from setup session
├── requirements.txt      # Python dependencies (openai, python-dotenv, requests)
├── .gitignore           # Protects .env files and virtual environment
├── .env/                # Virtual environment (DO NOT commit)
└── examples/
    ├── basic_chat.py          # Simple OpenAI API example
    ├── interactive_chat.py    # Multi-turn conversation
    ├── api_setup.py          # API key testing utility
    └── simple_agent.py       # Function calling / tool use demo
```

---

## 🔐 API Key Setup

### Option 1: Environment Variable (Temporary)

```bash
export OPENAI_API_KEY='your-api-key-here'
```

### Option 2: .env File (Recommended)

1. Create `.env` file in project root
2. Add: `OPENAI_API_KEY=your-api-key-here`
3. Load with python-dotenv:
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

### Option 3: Permanent Shell Configuration

Add to `~/.zshrc`:

```bash
export OPENAI_API_KEY='your-api-key-here'
```

Then run: `source ~/.zshrc`

---

## 🎓 Course Context

- **Course Platform:** Designed for Windows users
- **User Platform:** macOS
- **Strategy:** Created macOS-specific documentation and command reference
- **Approach:** Self-paced learning - user will run commands to understand each step

---

## 💡 Common Issues & Solutions

### Issue: "command not found: python"

**Solution:** Use `python3` on macOS

```bash
python3 --version
python3 -m venv .env
```

### Issue: pip installs to system instead of venv

**Solution:** Always activate venv first

```bash
source .env/bin/activate
which pip  # Verify it points to .env/bin/pip
pip install package_name
```

### Issue: "No module named 'openai'"

**Solution:**

1. Activate venv: `source .env/bin/activate`
2. Install: `pip install openai`
3. Verify: `pip list | grep openai`

### Issue: VS Code explorer empty

**Solution:** Open folder as workspace

```bash
code /Users/coello/LLM_agents_class
```

---

## 🚀 Next Steps

1. **Set up API key** using one of the methods above
2. **Test connection** with `python examples/api_setup.py`
3. **Run basic example** with `python examples/basic_chat.py`
4. **Follow course** and reference README.md for Windows→macOS command translations
5. **Ask questions** when encountering platform differences

---

## 📚 Reference Files

- **[README.md](README.md)** - Comprehensive setup guide, command reference, troubleshooting
- **[examples/api_setup.py](examples/api_setup.py)** - Test API key configuration
- **[examples/basic_chat.py](examples/basic_chat.py)** - Simple chat completion example
- **[examples/interactive_chat.py](examples/interactive_chat.py)** - Conversation with history
- **[examples/simple_agent.py](examples/simple_agent.py)** - Function calling demonstration

---

## 🔄 Quick Command Reference

**Activate venv:**

```bash
source .env/bin/activate
```

**Deactivate venv:**

```bash
deactivate
```

**Check Python location:**

```bash
which python
```

**List installed packages:**

```bash
pip list
```

**Install from requirements:**

```bash
pip install -r requirements.txt
```

**Update requirements:**

```bash
pip freeze > requirements.txt
```

---

## Notes

- Keep `.env/` and `.env` (environment variables file) out of git (already in .gitignore)
- Always activate virtual environment before running Python code
- Terminal shows `(.env)` prefix when venv is active
- Course is Windows-based, so translate commands using README.md reference table
- GitHub Copilot available in every VS Code window for help

---

## 🐛 Autogen 0.2.0 Issues & Solutions

### Issue: ModuleNotFoundError for autogen

**Problem:** Import error despite package installation  
**Root Cause:** Notebook kernel not set to correct Python environment  
**Solution:**

1. Click kernel selector (top-right of notebook)
2. Select `.env/bin/python` (Python 3.11.14)
3. Reload VS Code window if needed: `Cmd+Shift+P` → "Reload Window"

### Issue: max_turns parameter ignored

**Problem:** `initiate_chat(max_turns=2)` doesn't stop conversation  
**Root Cause:** `max_turns` parameter not supported in autogen 0.2.0  
**Solution:** Use `update_max_consecutive_auto_reply()` instead

```python
agent1.update_max_consecutive_auto_reply(1, agent2)
agent2.update_max_consecutive_auto_reply(1, agent1)
```

### Issue: AttributeError: 'NoneType' has no attribute 'summary'

**Problem:** `initiate_chat()` returns `None` instead of chat_result  
**Root Cause:** API change in autogen 0.2.0  
**Solution:** Manually construct chat_result

```python
from types import SimpleNamespace

# Initiate chat (returns None)
agent1.initiate_chat(recipient=agent2, message="Hello")

# Extract chat history
chat_history = agent1.chat_messages[agent2]

# Build chat_result manually
chat_result = SimpleNamespace(
    chat_history=chat_history,
    cost={},
    summary=chat_history[-1]["content"] if chat_history else ""
)
```

### Issue: Agents asking for human input

**Problem:** Conversation paused waiting for user input  
**Root Cause:** Default `human_input_mode="TERMINATE"`  
**Solution:** Set `human_input_mode="NEVER"` in agent definition

```python
agent = ConversableAgent(
    name="Agent",
    llm_config=llm_config,
    human_input_mode="NEVER"  # Add this
)
```

### Issue: Import "autogen" could not be resolved (Pylance warning)

**Problem:** VS Code shows import warning but code runs fine  
**Root Cause:** Pylance hasn't synced with kernel change  
**Solution:** Ignore it - code works. Or reload: `Cmd+Shift+P` → "Reload Window"

### Issue: initiate_chats not found

**Problem:** `initiate_chats()` (plural) doesn't exist  
**Root Cause:** Feature added in autogen 0.4+, not available in 0.2.0  
**Solution:** Run chats sequentially in a loop

```python
chat_results = []
for chat in chats:
    sender.initiate_chat(
        recipient=recipient,
        message=chat["message"],
        max_turns=chat.get("max_turns", 2)
    )
    chat_history = sender.chat_messages.get(recipient, [])
    chat_result = SimpleNamespace(
        chat_history=chat_history,
        cost={},
        summary=chat_history[-1]["content"] if chat_history else ""
    )
    chat_results.append(chat_result)
```

### Issue: register_nested_chats not found

**Problem:** AttributeError when calling `register_nested_chats()`  
**Root Cause:** Feature not available in autogen 0.2.0  
**Solution:** Nested chats require autogen 0.4+ (Python 3.9-3.12)

### Issue: Cost tracking returns empty {}

**Problem:** `chat_result.cost` is empty  
**Root Cause:** Cost tracking not available in autogen 0.2.0  
**Solution:** Expected behavior - feature added in later versions

---

## 🔐 GitHub Security Issues

### Issue: Push rejected - API keys detected

**Problem:** GitHub blocks push due to secret scanning  
**Root Cause:** API keys committed in files  
**Solution:**

1. **Immediately revoke exposed API keys** at https://platform.openai.com/api-keys
2. Replace all keys with placeholder:

```bash
find . -type f \( -name "*.py" -o -name "*.ipynb" \) -exec sed -i '' 's/sk-proj-[A-Za-z0-9_-]*/YOUR_API_KEY_HERE/g' {} +
```

3. Reset git history and recommit:

```bash
rm -rf .git
git init
git add .
git commit -m "Initial commit with placeholder API keys"
git remote add origin <repo-url>
git push -u origin main
```

### Best Practices:

- Never commit API keys
- Use environment variables or `.env` files
- Add `.env` to `.gitignore`
- Use placeholder text like `YOUR_API_KEY_HERE` in examples

---

## 📦 Package Installation Issues

### Issue: Import "matplotlib.pyplot" could not be resolved

**Solution:** Install matplotlib

```bash
pip install matplotlib
```

### Issue: Import "yfinance" could not be resolved

**Solution:** Install yfinance

```bash
pip install yfinance
```

### Install all required packages:

```bash
pip install yfinance matplotlib pandas pyautogen
```

---

## 🐍 Python Environment Management

### Issue: Python 3.14 incompatibility

**Problem:** autogen 0.2.0 doesn't support Python 3.14  
**Solution:** Create new venv with Python 3.11

```bash
python3.11 -m venv .env
source .env/bin/activate
pip install pyautogen==0.2.0
```

### Verify Python version:

```bash
python --version
# Should show: Python 3.11.x
```

---

## 📊 Git & GitHub Commands Used

### Initialize and push to GitHub:

```bash
# Initialize repo
git init
git add .
git commit -m "Initial commit"

# Add remote
git remote add origin https://github.com/USERNAME/REPO.git

# Check remotes
git remote -v

# Update remote URL
git remote set-url origin https://github.com/USERNAME/REPO.git

# Push
git push -u origin main

# Force push (after fixing issues)
git push -f origin main
```

---

**Sessions Complete ✅**

- Initial setup completed
- Autogen 0.2.0 compatibility issues resolved
- GitHub repository published with clean code
- All API keys replaced with placeholders
