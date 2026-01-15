# Command Cheatsheet

## Python Virtual Environment Management

### Create Virtual Environment

```bash
python3.11 -m venv .env
```

### Activate Virtual Environment

```bash
# macOS/Linux
source .env/bin/activate

# Windows
.env\Scripts\activate
```

### Deactivate Virtual Environment

```bash
deactivate
```

### Check Python Version

```bash
python --version
```

### Check Which Python is Active

```bash
which python
```

## Package Management

### Install Packages

```bash
pip install pyautogen==0.2.0
pip install -r requirements.txt
```

### List Installed Packages

```bash
pip list
pip list | grep autogen
```

### Check Package Details

```bash
pip show pyautogen
```

## Autogen 0.2.0 API

### Import

```python
from autogen import ConversableAgent
from types import SimpleNamespace
```

### Create Agent

```python
agent = ConversableAgent(
    name="AgentName",
    llm_config=llm_config,
    system_message="Your system prompt here",
    human_input_mode="NEVER",  # "ALWAYS" | "NEVER" | "TERMINATE"
    is_termination_msg=lambda msg: "terminate" in msg["content"].lower()
)
```

### LLM Configuration

```python
llm_config = {
    "model": "gpt-3.5-turbo",
    "api_key": "your-api-key-here"
}
```

### Control Turn Limits

```python
# Set max consecutive auto replies for specific recipient
agent1.update_max_consecutive_auto_reply(1, agent2)
```

### Initiate Chat

```python
# Note: In autogen 0.2.0, this returns None
agent1.initiate_chat(
    recipient=agent2,
    message="Hello!",
    max_turns=2,
    clear_history=True
)
```

### Manual Chat Result Construction (autogen 0.2.0)

```python
# Extract chat history
chat_history = agent1.chat_messages[agent2]

# Build chat_result object
chat_result = SimpleNamespace(
    chat_history=chat_history,
    cost={},
    summary=chat_history[-1]["content"] if chat_history else ""
)
```

### Send Message Between Agents

```python
agent1.send(message="Your message", recipient=agent2)
```

### Generate Reply

```python
reply = agent.generate_reply(messages=message_list)
```

### Access Chat History

```python
# Get messages between two agents
history = agent1.chat_messages[agent2]
```

### Sequential Chats (Manual Loop for 0.2.0)

```python
chat_results = []

for chat in chats:
    sender = chat["sender"]
    recipient = chat["recipient"]

    sender.initiate_chat(
        recipient=recipient,
        message=chat["message"],
        max_turns=chat.get("max_turns", 2),
        clear_history=chat.get("clear_history", True)
    )

    chat_history = sender.chat_messages.get(recipient, [])
    chat_result = SimpleNamespace(
        chat_history=chat_history,
        cost={},
        summary=chat_history[-1]["content"] if chat_history else ""
    )
    chat_results.append(chat_result)
```

## Jupyter Notebook (VS Code)

### Select Kernel

- Click kernel selector in top-right
- Choose Python environment (e.g., `.env/bin/python`)

### Run Cell

- `Shift + Enter` - Run cell and move to next
- `Ctrl + Enter` - Run cell and stay
- `Alt + Enter` - Run cell and insert below

### Cell Types

- Code cell: Python code execution
- Markdown cell: Documentation

### Restart Kernel

- `Cmd + Shift + P` → "Restart Kernel"

## VS Code Commands

### Reload Window

```
Cmd + Shift + P → "Developer: Reload Window"
```

### Command Palette

```
Cmd + Shift + P
```

## Terminal Commands (macOS)

### Navigate Directories

```bash
cd /path/to/directory
cd ..                    # Go up one level
pwd                      # Print working directory
```

### List Files

```bash
ls                       # List files
ls -la                   # List all files with details
ls -la path/to/dir       # List specific directory
```

### File Operations

```bash
cat filename             # View file contents
head filename            # View first 10 lines
tail filename            # View last 10 lines
grep "pattern" file      # Search in file
```

### Process Management

```bash
ps aux | grep python     # Find Python processes
kill PID                 # Kill process by ID
```

## Git Commands (if needed)

### Check Status

```bash
git status
```

### View Changes

```bash
git diff
```

### Add and Commit

```bash
git add .
git commit -m "message"
```

## Common Issues & Solutions

### Import Error: "autogen" could not be resolved

**Solution:** Make sure notebook kernel is set to `.env/bin/python`

### AttributeError: 'NoneType' has no attribute 'summary'

**Solution:** In autogen 0.2.0, manually construct chat_result object

### Conversation doesn't stop with max_turns

**Solution:** Use `update_max_consecutive_auto_reply()` instead

### Agent asks for human input

**Solution:** Add `human_input_mode="NEVER"` to agent definition

### Python version incompatibility

**Solution:** Use Python 3.11 (pyautogen 0.2.0 supports ≤3.12)

## Keyboard Shortcuts (VS Code)

### General

- `Cmd + S` - Save file
- `Cmd + P` - Quick file open
- `Cmd + Shift + P` - Command palette
- `Cmd + B` - Toggle sidebar

### Editing

- `Cmd + /` - Toggle comment
- `Cmd + D` - Select next occurrence
- `Cmd + Shift + K` - Delete line
- `Option + Up/Down` - Move line up/down

### Navigation

- `Cmd + Click` - Go to definition
- `Cmd + Shift + O` - Go to symbol
- `Ctrl + -` - Go back
- `Ctrl + Shift + -` - Go forward
