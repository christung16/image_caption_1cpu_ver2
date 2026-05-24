# 🔧 Jupyter Kernel Setup Guide

## ❓ What is a Jupyter Kernel?

A **Jupyter kernel** is the Python environment that runs your notebook code. Think of it like this:

- Your **computer** may have multiple Python installations (system Python, conda environments, virtual environments)
- Each Python installation has its own **packages** (matplotlib, PIL, transformers, etc.)
- Jupyter needs to know **which Python** to use when running your notebooks
- A **kernel** tells Jupyter: "Use THIS Python environment"

---

## 🚨 Why You're Getting Import Errors

### The Problem:
```python
import matplotlib.pyplot as plt
# ModuleNotFoundError: No module named 'matplotlib'
```

### The Cause:
Your Jupyter notebook is using the **wrong Python kernel**!

- ❌ You installed packages in `.venv` (virtual environment)
- ❌ But Jupyter is using **system Python** (which doesn't have those packages)
- ✅ You need to tell Jupyter to use `.venv` instead!

---

## ✅ The Solution (3 Simple Steps)

### Step 1: Register Your Virtual Environment as a Kernel

```bash
# Navigate to your project
cd /Users/yitung/Documents/PycharmProjects/image_caption_1cpu_ver2

# Activate your virtual environment
source .venv/bin/activate

# Register the kernel (one-time setup)
python -m ipykernel install --user --name=image_caption_venv --display-name="Python (image_caption_venv)"
```

**Expected Output:**
```
Installed kernelspec image_caption_venv in /Users/yitung/Library/Jupyter/kernels/image_caption_venv
```

✅ **You only need to do this ONCE per virtual environment!**

---

### Step 2: Start Jupyter Notebook

```bash
# Make sure you're still in the project root
jupyter notebook notebooks/student_notebook.ipynb
```

Your browser will open with the notebook.

---

### Step 3: Select the Correct Kernel

#### In Jupyter Notebook (Classic):
1. Look at the **top-right corner** of the notebook
2. You'll see the current kernel name (e.g., "Python 3")
3. Click on: **Kernel** (menu) → **Change Kernel** → **Python (image_caption_venv)**
4. ✅ The kernel name should now show: `Python (image_caption_venv)`

#### In JupyterLab:
1. Look at the **top-right corner**
2. Click on the kernel name (e.g., "Python 3")
3. Select **Python (image_caption_venv)** from the dropdown
4. ✅ Done!

#### In VS Code:
1. Open the notebook in VS Code
2. Look for **"Select Kernel"** button in the top-right
3. Click it and choose **Python (image_caption_venv)**
4. ✅ Done!

---

## 🔍 How to Verify It's Working

After selecting the kernel, run this in a notebook cell:

```python
import sys
print("Python executable:", sys.executable)
print("\nShould contain '.venv':", '.venv' in sys.executable)

# Try importing packages
import matplotlib
import PIL
import transformers
print("\n✅ All packages imported successfully!")
```

**Expected Output:**
```
Python executable: /Users/yitung/.../image_caption_1cpu_ver2/.venv/bin/python
Should contain '.venv': True

✅ All packages imported successfully!
```

---

## 🐛 Troubleshooting

### Problem: "I don't see Python (image_caption_venv) in the kernel list"

**Solution:**
```bash
# Make sure you registered it
cd /path/to/image_caption_1cpu_ver2
source .venv/bin/activate
python -m ipykernel install --user --name=image_caption_venv --display-name="Python (image_caption_venv)"

# Restart Jupyter completely
# Close browser tab, stop jupyter in terminal (Ctrl+C), then start again
jupyter notebook notebooks/student_notebook.ipynb
```

### Problem: "Still getting ModuleNotFoundError after switching kernel"

**Solution:**
```bash
# 1. Restart the kernel in Jupyter
Kernel → Restart Kernel

# 2. Run cells from the top again
# Make sure to run the setup cell first!

# 3. If still not working, reinstall packages
source .venv/bin/activate
pip install -r requirements.txt
```

### Problem: "How do I remove old/wrong kernels?"

**Solution:**
```bash
# List all kernels
jupyter kernelspec list

# Remove a kernel (replace 'kernel_name' with actual name)
jupyter kernelspec uninstall kernel_name
```

---

## 📋 Quick Reference Card

### First Time Setup (Do Once):
```bash
cd /path/to/image_caption_1cpu_ver2
source .venv/bin/activate
python -m ipykernel install --user --name=image_caption_venv --display-name="Python (image_caption_venv)"
```

### Every Time You Use the Notebook:
1. Start Jupyter: `jupyter notebook notebooks/student_notebook.ipynb`
2. Check top-right corner → Should say `Python (image_caption_venv)`
3. If not → `Kernel` → `Change Kernel` → `Python (image_caption_venv)`
4. Run cells from top to bottom!

---

## 💡 Understanding the Commands

### What does `python -m ipykernel install` do?

```bash
python -m ipykernel install \           # Install the kernel
  --user \                               # For current user only (not system-wide)
  --name=image_caption_venv \            # Internal kernel name
  --display-name="Python (image_caption_venv)"  # What you see in Jupyter
```

This creates a **kernel specification** that tells Jupyter:
- Where to find the Python executable (`.venv/bin/python`)
- What packages are available (everything in `.venv`)
- What to display in the kernel menu

---

## 🎓 Why This Matters for Learning

When you're learning Python and AI:

1. **Isolation**: Each project has its own packages (no conflicts!)
2. **Reproducibility**: Everyone in class uses the same environment
3. **Control**: You know exactly which Python and packages you're using
4. **Best Practice**: This is how professional developers work!

---

## ✅ Checklist

Before running the notebook, make sure:

- [ ] Virtual environment created (`.venv/`)
- [ ] Packages installed (`pip install -r requirements.txt`)
- [ ] Kernel registered (one-time: `python -m ipykernel install ...`)
- [ ] Jupyter started from project root
- [ ] **Correct kernel selected** in Jupyter: `Python (image_caption_venv)`
- [ ] First setup cell runs without errors
- [ ] Imports work (matplotlib, PIL, transformers)

---

## 🆘 Still Having Issues?

1. **Check which Python Jupyter is using:**
   ```python
   import sys
   print(sys.executable)
   # Should show: .../image_caption_1cpu_ver2/.venv/bin/python
   ```

2. **Check which packages are installed:**
   ```python
   import pkg_resources
   installed = {pkg.key for pkg in pkg_resources.working_set}
   print('matplotlib' in installed)  # Should be True
   print('transformers' in installed)  # Should be True
   ```

3. **Still stuck?** Check `notebooks/README.md` for more troubleshooting tips!

---

**Remember**: The kernel selection is the #1 cause of import errors in Jupyter notebooks. Always verify you're using the right kernel! 🎯
