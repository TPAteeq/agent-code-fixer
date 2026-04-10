# Agent Demo Guide

A Python AI agent that uses Gemini to autonomously explore and modify code via function calls.

## Setup

```bash
# Install dependencies
uv sync
```

## How to Run

```bash
uv run main.py "<your prompt>"
uv run main.py "<your prompt>" --verbose   # shows function calls + raw results
```

---

## Demo Scenarios

### 1. Explore the codebase

The agent lists files and reads them to answer questions.

```bash
uv run main.py "what files are in the root?"
uv run main.py "how does the calculator render results to the console?"
uv run main.py "explain how operator precedence works in the calculator"
```

What to show: the agent calling `get_files_info` then `get_file_content` in sequence, building up context before answering.

---

### 2. Read a specific file

```bash
uv run main.py "read the contents of main.py" --verbose
uv run main.py "what does pkg/calculator.py do?"
```

---

### 3. Run code

```bash
uv run main.py "run the calculator tests"
uv run main.py "run main.py with the expression '10 + 5 * 2'"
```

What to show: the agent calling `run_python_file` and reporting the output back.

---

### 4. Write a file

```bash
uv run main.py "create a new file called notes.txt with the content 'hello from the agent'"
```

Verify it worked:
```bash
cat calculator/notes.txt
```

---

### 5. Fix a bug (the full agentic loop)

This is the flagship demo — the agent reads code, identifies a bug, writes a fix, then verifies it.

**Step 1:** Break the calculator by bumping `+` precedence:
```bash
# In calculator/pkg/calculator.py, change:
#   "+": 1   →   "+": 3
```

**Step 2:** Confirm it's broken:
```bash
uv run calculator/main.py "3 + 7 * 2"
# Should return 20 (wrong — correct answer is 17)
```

**Step 3:** Let the agent fix it:
```bash
uv run main.py "Fix the bug: 3 + 7 * 2 shouldn't be 20" --verbose
```

**Step 4:** Verify the fix:
```bash
uv run calculator/main.py "3 + 7 * 2"
# Should now return 17
```

What to show: the agent calling `get_files_info` → `get_file_content` → `write_file`, all on its own, across multiple loop iterations.

---

## What's Happening Under the Hood

Each loop iteration:
1. The agent gets the full conversation history (user prompt + all previous tool calls + all tool results)
2. It decides what to do next (call a function, or give a final answer)
3. If it calls a function, the result is added to the conversation and the loop continues
4. When it has enough information to answer, it responds in plain text and stops

The agent has four tools available:
| Tool | What it does |
|---|---|
| `get_files_info` | List files in a directory |
| `get_file_content` | Read a file (up to 10,000 chars) |
| `run_python_file` | Execute a `.py` file and capture output |
| `write_file` | Write or overwrite a file |

All file operations are sandboxed to the `calculator/` working directory.
