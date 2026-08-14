# Environment Setup & Study Notes

> **Repository**: [ml-roadmap](file:///C:/Users/Nick/mlRoadMap)  
> **GitHub Remote**: [https://github.com/whatsnextnick/new-ml-roadmap](https://github.com/whatsnextnick/new-ml-roadmap)  
> **Python Interpreter**: `C:\Users\Nick\mlRoadMap\.venv\Scripts\python.exe`

---

## 1. Environment Architecture & Setup

### Virtual Environment (`.venv`)
A virtual environment isolates your project's Python dependencies from global system Python packages.

#### Recommended Creation & Repair Command:
```powershell
# Create or clear an existing virtual environment with pip included
python -m venv .venv --clear

# Activate in PowerShell
.\.venv\Scripts\activate

# Upgrade essential build tools (Always run python -m pip instead of raw pip)
python -m pip install --upgrade pip setuptools wheel
```

---

## 2. Troubleshooting: PyCharm & `pip` Bootstrap Issue

### What Happened?
When attempting to install `torch`, `torchvision`, `tensorflow`, and `numpy` via PyCharm's UI, the following error occurred:
```text
ERROR: To modify pip, please run the following command:
C:\Users\Nick\mlRoadMap\.venv\Scripts\python.exe -m pip install --no-index ...
Process finished with exit code 1
```

### Root Cause
1. **Missing/Broken `pip` Bootstrap**: The initial `.venv` did not have `pip` properly registered in its `site-packages`.
2. **Path Mismatch**: PyCharm's internal package helper tried to invoke `pip` as a standalone executable module on a `.whl` file, which failed because the virtual environment's executable context didn't recognize `pip`.

### The Solution
1. Re-initialized `.venv` using `python -m venv .venv --clear` (forcing `ensurepip` to run).
2. Upgraded core tooling (`pip 26.2.1`, `setuptools 84.0.0`, `wheel 0.48.0`).
3. Installed packages directly via the virtual environment interpreter:
   ```powershell
   & "C:\Users\Nick\mlRoadMap\.venv\Scripts\python.exe" -m pip install -r requirements.txt
   ```

---

## 3. Package Managers: `pip` vs `uv`

### Comparison

| Feature | Standard `pip` + `venv` | `uv` (Astral) |
| :--- | :--- | :--- |
| **Speed** | Standard download & build times | **10x – 100x faster** (written in Rust) |
| **Caching** | Basic pip cache | Global, deduplicated parallel cache |
| **Environment Creation** | `python -m venv .venv` (~5–10s) | `uv venv` (~0.05s) |
| **Dependency Resolution** | Backtracking resolver | High-speed parallel resolver |
| **Compatibility** | Built-in standard | 100% drop-in replacement for `pip` |

### Package Manager Cheatsheet

#### Modern Workflow with `uv` (Recommended)
```powershell
# 1. One-time Windows install
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# 2. Create environment
uv venv

# 3. Install dependencies
uv pip install -r requirements.txt
# OR install specific packages:
uv pip install torch torchvision tensorflow numpy
```

#### Standard Workflow with `pip`
```powershell
# 1. Create environment
python -m venv .venv

# 2. Upgrade pip & build tools
python -m pip install --upgrade pip setuptools wheel

# 3. Install dependencies
python -m pip install -r requirements.txt
```

---

## 4. PyCharm IDE Configuration Guide

To configure PyCharm to use your virtual environment:

1. Open **Settings** (`Ctrl` + `Alt` + `S`).
2. Navigate to **Project: mlRoadMap** → **Python Interpreter**.
3. Click **Add Interpreter** → **Add Local Interpreter...**
4. Choose **Existing Environment**.
5. Browse and select:
   `C:\Users\Nick\mlRoadMap\.venv\Scripts\python.exe`
6. Click **Apply** and **OK**.

---

## 5. Git & GitHub Workflow

### Initializing & Linking
```powershell
# Initialize local repo
git init

# Add all files & initial commit
git add .
git commit -m "Initial commit: full ml-roadmap structure"

# Set branch name to main
git branch -M main

# Link to GitHub Remote (HTTPS or SSH)
git remote add origin https://github.com/whatsnextnick/new-ml-roadmap.git

# Push main branch
git push -u origin main
```

### Regular Commit & Push Cycle
```powershell
git add .
git commit -m "Update study notes and project progress"
git push
```

---

## 6. Q&A & Knowledge Log

*(Use this section to record future questions, answers, and setup notes as you progress through the roadmap.)*

#### Q1: Why should I run `python -m pip` instead of just `pip` in PowerShell?
- **Answer**: `pip` executes whichever `pip.exe` happens to be first in your system `PATH` (which might be global Python or another installation). Running `python -m pip` guarantees that `pip` runs inside the specific Python executable context you explicitly targeted (e.g. `C:\Users\Nick\mlRoadMap\.venv\Scripts\python.exe`).

#### Q2: What is the purpose of `.gitignore` in ML projects?
- **Answer**: `.gitignore` prevents large data files (`*.h5`, `*.pkl`, `*.pth`), virtual environment folders (`.venv/`), checkpoints (`.ipynb_checkpoints`), and API credentials (`.env`) from being uploaded to GitHub.
