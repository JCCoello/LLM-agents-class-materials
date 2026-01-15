# LLM Agents Class - macOS Setup Guide

This repository contains setup instructions and example code for the LLM Agents course, adapted for macOS.

## 📋 Table of Contents

- [Initial Setup](#initial-setup)
- [Windows vs macOS Command Differences](#windows-vs-macos-command-differences)
- [Virtual Environment Management](#virtual-environment-management)
- [Running Examples](#running-examples)
- [Troubleshooting](#troubleshooting)

---

## 🚀 Initial Setup

### 1. Check Python Installation

```bash
python3 --version
```

Expected: Python 3.8 or higher. If not installed:

```bash
brew install python
```

### 2. Create Virtual Environment

```bash
python3 -m venv .env
```

### 3. Activate Virtual Environment

**macOS/Linux:**

```bash
source .env/bin/activate
```

**Windows (for reference):**

```powershell
.env\Scripts\activate
```

### 4. Upgrade pip and Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Set Up API Keys

Create a `.env` file in the project root:

```bash
touch .env
```

Add your API keys (never commit this file):

```
OPENAI_API_KEY=your_api_key_here
```

---

## 🔄 Windows vs macOS Command Differences

| Task                      | Windows (PowerShell/CMD) | macOS (zsh/bash)                |
| ------------------------- | ------------------------ | ------------------------------- |
| **Activate venv**         | `.env\Scripts\activate`  | `source .env/bin/activate`      |
| **Deactivate venv**       | `deactivate`             | `deactivate`                    |
| **List directory**        | `dir`                    | `ls` or `ls -la`                |
| **Clear screen**          | `cls`                    | `clear`                         |
| **Environment variables** | `$env:VAR_NAME="value"`  | `export VAR_NAME="value"`       |
| **View env variable**     | `echo $env:VAR_NAME`     | `echo $VAR_NAME`                |
| **Path separator**        | `\` (backslash)          | `/` (forward slash)             |
| **Run Python**            | `python`                 | `python3` or `python` (in venv) |
| **Which Python**          | `where python`           | `which python`                  |

---

## 🐍 Virtual Environment Management

### Activation (IMPORTANT!)

The activation script **must be sourced**, not executed:

✅ **Correct:**

```bash
source .env/bin/activate
# or
. .env/bin/activate
```

❌ **Incorrect (will fail with exit code 126):**

```bash
.env/bin/activate
```

### Check if Activated

When activated, you should see:

1. `(.env)` prefix in your terminal prompt
2. `which python` points to `.env/bin/python`
3. `echo $VIRTUAL_ENV` shows the path to `.env`

```bash
# Verify activation
which python
echo $VIRTUAL_ENV
```

### Deactivation

```bash
deactivate
```

---

## 🏃 Running Examples

### Basic OpenAI Example

```bash
# Ensure venv is activated first
source .env/bin/activate

# Run the example
python examples/basic_chat.py
```

### Using Environment Variables

```bash
# Load from .env file (if using python-dotenv)
python examples/api_example.py

# Or set temporarily
export OPENAI_API_KEY="your_key"
python examples/api_example.py
```

---

## 🔧 Troubleshooting

### Issue: "command not found: python"

**Solution:** Use `python3` instead of `python` on macOS (outside venv):

```bash
python3 -m venv .env
```

### Issue: "zsh: permission denied: .env/bin/activate"

**Solution:** Don't execute directly, use `source`:

```bash
source .env/bin/activate
```

### Issue: "No module named 'openai'"

**Solution:** Ensure venv is activated and reinstall:

```bash
source .env/bin/activate
pip install openai
```

### Issue: pip installs to system Python

**Solution:** Always activate venv first:

```bash
source .env/bin/activate
which pip  # Should show .env/bin/pip
pip install package_name
```

### Issue: "Bad CPU type in executable" (M1/M2 Mac)

**Solution:** Use native ARM Python or Rosetta:

```bash
# Check architecture
arch
# If needed, install ARM version via Homebrew
brew install python@3.11
```

---

## 📦 Installed Packages

Run to see all installed packages:

```bash
pip list
```

Generate current requirements:

```bash
pip freeze > requirements.txt
```

---

## 🔐 Security Notes

- **Never commit `.env` files** containing API keys
- **Never commit the `.env/` virtual environment folder**
- Check `.gitignore` is properly configured
- Rotate API keys if accidentally exposed

---

## 📚 Additional Resources

- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [OpenAI Python Library Docs](https://github.com/openai/openai-python)
- [macOS Terminal Guide](https://support.apple.com/guide/terminal/)

---

**Last Updated:** January 13, 2026
