# How to Download BLIP Model Using Git Clone

## ✅ Already Done!

The BLIP model has been successfully downloaded using git clone and is stored locally in:
```
/Users/yitung/Documents/PycharmProjects/image_caption_1cpu_ver2/models/blip-image-captioning-base
```

## Benefits of Using Git Clone

1. **Faster Startup**: No need to download the model every time
2. **Offline Capability**: Can run without internet (after initial download)
3. **No SSL Issues**: Downloaded once via git, which handles SSL better
4. **Version Control**: Can track which version of the model you're using
5. **Educational**: Students can see the model files directly

## What Was Downloaded

The following files are now stored locally (1.84 GB total):

```
models/blip-image-captioning-base/
├── config.json              # Model configuration
├── preprocessor_config.json # Image preprocessing settings
├── pytorch_model.bin        # The actual AI model weights (944 MB)
├── tokenizer.json           # Text tokenizer
├── vocab.txt               # Vocabulary file
└── other files...
```

## How It Was Downloaded

```bash
# Step 1: Create models directory
mkdir -p models

# Step 2: Clone the model from Hugging Face (with progress bar)
cd models
git clone --progress https://huggingface.co/Salesforce/blip-image-captioning-base

# That's it!
```

## For Other Models

You can download any Hugging Face model the same way:

```bash
# General format:
git clone --progress https://huggingface.co/<org-name>/<model-name>

# Examples:
git clone --progress https://huggingface.co/Salesforce/blip-image-captioning-large
git clone --progress https://huggingface.co/nlpconnect/vit-gpt2-image-captioning
```

## Sharing the Model

If you want to share this project with other students:

### Option 1: Without the Model (Smaller)
```bash
# Add to .gitignore
echo "models/" >> .gitignore

# Students will need to run:
git clone --progress https://huggingface.co/Salesforce/blip-image-captioning-base models/blip-image-captioning-base
```

### Option 2: With the Model (Larger, but easier)
- Include the `models/` folder in your project
- Students can run immediately without downloading
- Project size: ~2 GB

## The Code Change

The app.py now automatically uses the local model:

```python
def load_model():
    # Path to the local model directory
    model_path = os.path.join(os.path.dirname(__file__), 
                             "models", 
                             "blip-image-captioning-base")
    
    # Check if local model exists
    if not os.path.exists(model_path):
        print("Local model not found. Downloading from Hugging Face...")
        model_path = "Salesforce/blip-image-captioning-base"
    else:
        print(f"Using local model from: {model_path}")
    
    # Load the processor and model from local path
    processor = BlipProcessor.from_pretrained(model_path)
    model = BlipForConditionalGeneration.from_pretrained(model_path)
```

## Advantages for Students

1. **Learn about ML model structure**: Students can explore the model files
2. **Understand file sizes**: See why AI models need significant storage
3. **Version control**: Understand how to manage large files with Git LFS
4. **Offline development**: Work without internet after initial setup

## Requirements for Git Clone Method

- **Git LFS** (Large File Storage) must be installed
  ```bash
  # Check if installed:
  git-lfs --version
  
  # Install on Mac:
  brew install git-lfs
  
  # Install on Ubuntu/Debian:
  sudo apt-get install git-lfs
  ```

- **Disk Space**: ~2 GB free space for the model

---

**The local model is now configured and working!** 🎉

The application will automatically use it, providing faster startup times and no SSL issues!
