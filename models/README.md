# Models Directory

## Purpose

This directory contains the AI model files needed for image captioning.

## ⚠️ IMPORTANT: Model Files Not Included

The BLIP model files are **NOT included** in the git repository because they are very large (~1.8GB). You must download them separately.

## 📥 How to Download the Model

### Prerequisites
Make sure Git LFS (Large File Storage) is installed:

```bash
# Check if installed:
git lfs --version

# If not installed:
# macOS:
brew install git-lfs

# Ubuntu/Debian:
sudo apt-get install git-lfs

# Windows:
# Download from https://git-lfs.github.com/

# Initialize Git LFS:
git lfs install
```

### Download the BLIP Model

```bash
# Navigate to this directory
cd models

# Clone the BLIP model from Hugging Face Hub (with progress bar for ~1.8GB download)
git clone --progress https://huggingface.co/Salesforce/blip-image-captioning-base

# Return to project root
cd ..
```

### Verify the Download

```bash
# List the downloaded files
ls -lh models/blip-image-captioning-base/

# You should see:
# - pytorch_model.bin (~944 MB) ← IMPORTANT: Should be large!
# - config.json (~4 KB)
# - preprocessor_config.json (~287 bytes)
# - tokenizer.json (~695 KB)
# - vocab.txt (~226 KB)
# - and more...
```

**⚠️ Critical Check**: The `pytorch_model.bin` file should be approximately **944 MB**. If it's only a few KB, Git LFS didn't download it properly. Re-install Git LFS and try again.

## 📁 Expected Structure After Download

```
models/
├── .gitkeep                           # Keeps directory in git
└── blip-image-captioning-base/       # Downloaded model (not in git)
    ├── pytorch_model.bin              # Main model weights (~944 MB)
    ├── tf_model.h5                    # TensorFlow model (~944 MB)
    ├── config.json                    # Model configuration
    ├── preprocessor_config.json       # Image preprocessing settings
    ├── tokenizer.json                 # Text tokenizer
    ├── tokenizer_config.json          # Tokenizer configuration
    ├── special_tokens_map.json        # Special tokens
    ├── vocab.txt                      # Vocabulary file
    └── README.md                      # Model documentation
```

## 🚫 Why Not Include in Git?

The model files are excluded from git because:
1. **Size**: ~1.8GB is too large for git repositories
2. **Git LFS limitations**: Not all git platforms support large files well
3. **Bandwidth**: Would slow down repository cloning significantly
4. **Best practice**: AI models are typically downloaded separately

## 🔄 Alternative: Automatic Download (Not Recommended)

If you skip the git clone step, the application will attempt to download the model from Hugging Face Hub on first run. However, this may cause SSL certificate issues and is slower. **We strongly recommend using git clone as described above.**

## ℹ️ About the BLIP Model

- **Name**: BLIP (Bootstrapping Language-Image Pre-training)
- **Developer**: Salesforce Research
- **Size**: Base model (~944 MB)
- **Purpose**: Image captioning and visual understanding
- **Paper**: https://arxiv.org/abs/2201.12086
- **License**: BSD-3-Clause

## 🎓 For Students

This directory demonstrates:
- How large AI models are managed separately from code
- The importance of Git LFS for large files
- How to structure ML projects with external model dependencies
- Best practices for distributing AI applications

## 📚 Additional Models

You can download other models from Hugging Face the same way:

```bash
# Example: Larger BLIP variant (more accurate but slower)
git clone --progress https://huggingface.co/Salesforce/blip-image-captioning-large

# Example: Different model (ViT-GPT2)
git clone --progress https://huggingface.co/nlpconnect/vit-gpt2-image-captioning
```

Remember to update `app.py` to point to the new model path if you use a different model!

---

**Need help?** See the main [README.md](../README.md) or [SETUP.md](../SETUP.md)
