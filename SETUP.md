# Quick Setup Guide

## 🚀 Get Started in 5 Steps

### Step 1: Install Git LFS
```bash
# macOS:
brew install git-lfs

# Ubuntu/Debian:
sudo apt-get install git-lfs

# Windows: Download from https://git-lfs.github.com/

# Initialize:
git lfs install
```

### Step 2: Clone This Repository
```bash
git clone <your-repo-url>
cd image_caption_1cpu_ver2
```

### Step 3: Download the AI Model (REQUIRED!)
```bash
cd models
git clone --progress https://huggingface.co/Salesforce/blip-image-captioning-base
cd ..
```
⏱️ This downloads ~1.8GB and may take 2-10 minutes. The `--progress` flag shows download progress.

### Step 4: Set Up Python Environment
```bash
# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate  # macOS/Linux
# or: .venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### Step 5: Run the Application
```bash
./start.sh
```

Then open: **http://localhost:5000**

---

## ✅ Verification Checklist

Before running, make sure:
- [ ] Git LFS is installed: `git lfs --version`
- [ ] Model is downloaded: `ls models/blip-image-captioning-base/pytorch_model.bin`
- [ ] Model file is ~944MB (not a few KB)
- [ ] Virtual environment is activated: `which python` shows `.venv`
- [ ] Dependencies installed: `pip list | grep torch`

## ❓ Need Help?

See the full **[README.md](README.md)** for:
- Detailed installation instructions
- Troubleshooting guide
- Usage examples
- Educational information

## 🎓 For Students

This is a learning project! The code is well-commented and includes:
- Flask web development
- AI/ML integration with BLIP
- Image processing with PIL
- Modern web interface

**Sample images** are provided in the `images/` folder for testing!
