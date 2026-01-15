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

| Platform | Command |
|----------|---------|
| **macOS/Linux** | `source .env/bin/activate` |
| **Windows PowerShell** | `.env\Scripts\activate` |
| **Windows CMD** | `.env\Scripts\activate.bat` |

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

**Session Complete ✅**  
All setup files created, virtual environment working, ready to start course.
