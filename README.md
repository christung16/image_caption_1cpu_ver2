# AI Image Captioning Web Application

A student-friendly Python web application that uses AI to generate captions for images. Built with Flask and the BLIP (Bootstrapping Language-Image Pre-training) model from Salesforce.

Perfect for junior-level students learning Python and AI!

## Features

- **Three Input Methods**:
  - Upload local image files
  - Provide image URLs from the internet
  - Select images from the local `images/` directory

- **AI-Powered Captioning**: Uses the BLIP-base model to generate accurate image descriptions

- **User-Friendly Interface**: Clean, modern web interface with real-time feedback

- **Educational**: Well-commented code explaining each step for learning purposes

- **Optimized for Low Resources**: Designed to run on 1GB RAM, 1 CPU servers

## Technologies Used

- **Backend**: Python 3.8+ with Flask
- **AI Model**: BLIP-base (Salesforce/blip-image-captioning-base)
- **Libraries**: PyTorch, Transformers, PIL (Pillow)
- **Frontend**: HTML5, CSS3, JavaScript

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git with Git LFS (Large File Storage) installed
- At least 1GB of RAM
- ~2GB free disk space (for the AI model)
- Internet connection (for first-time setup)

## Installation

### Step 1: Clone or Download This Project

```bash
git clone <your-repo-url>
cd image_caption_1cpu_ver2
```

### Step 2: Download the BLIP Model (REQUIRED)

The AI model files are not included in the repository due to their large size (~1.8GB). You must download them separately using Git LFS.

**Install Git LFS (if not already installed):**

```bash
# On macOS:
brew install git-lfs

# On Ubuntu/Debian:
sudo apt-get install git-lfs

# On Windows:
# Download from: https://git-lfs.github.com/

# Initialize Git LFS:
git lfs install
```

**Download the BLIP Model:**

```bash
# Navigate to the models directory
cd models

# Clone the BLIP model from Hugging Face (with progress bar)
git clone --progress https://huggingface.co/Salesforce/blip-image-captioning-base

# Return to project root
cd ..
```

This will download approximately 1.8GB of model files. The download may take 2-10 minutes depending on your internet connection.

**Verify the download:**

```bash
ls -lh models/blip-image-captioning-base/
```

You should see files like:
- `pytorch_model.bin` (~944 MB)
- `config.json`
- `preprocessor_config.json`
- `tokenizer.json`
- etc.

### Step 3: Create a Virtual Environment (Recommended)

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**On Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### Step 4: Install Required Python Packages

```bash
pip install -r requirements.txt
```

**Note**: The first installation will take several minutes as it downloads PyTorch and other large libraries.

## Running the Application

### Quick Start (Using the Startup Script)

```bash
./start.sh
```

### Manual Start

```bash
# Activate virtual environment
source .venv/bin/activate  # macOS/Linux
# or: .venv\Scripts\activate  # Windows

# Run the application
python app.py
```

You should see output like:
```
Loading BLIP model from local directory...
Using local model from: .../models/blip-image-captioning-base
Loading weights: 100%|██████████| 473/473
Model loaded successfully!
============================================================
Image Captioning Web Application
============================================================
Server starting on http://localhost:5000
Press CTRL+C to stop the server
============================================================
```

### Open Your Browser

Navigate to: `http://localhost:5000`

### Try It Out!

**Option A - Use Image URL:**
1. Click the "Image URL" tab
2. Paste an image URL (e.g., `http://picsum.photos/400/300`)
3. Click "Generate Caption"

**Option B - Upload Image:**
1. Click the "Upload File" tab
2. Choose an image from your computer
3. Click "Generate Caption"

**Option C - Select from Directory (NEW!):**
1. Click the "Select from Images Folder" tab
2. Choose one of the sample images from the dropdown
3. Click "Generate Caption"

### View Results

The AI will analyze your image and display:
- The image preview
- A generated caption describing the image

## Project Structure

```
image_caption_1cpu_ver2/
│
├── app.py                  # Main Flask application (Backend)
├── start.sh               # Startup script
├── requirements.txt        # Python dependencies
├── README.md              # This file
│
├── templates/
│   └── index.html         # HTML template (Frontend)
│
├── static/
│   └── style.css          # CSS styling
│
├── models/                # AI model files (download separately)
│   ├── .gitkeep          # Keeps directory in git
│   └── blip-image-captioning-base/  # Downloaded model
│       ├── pytorch_model.bin
│       ├── config.json
│       └── ...
│
├── images/                # Sample images for testing
│   ├── sample_cat.jpg
│   ├── sample_geometric.jpg
│   └── sample_landscape.jpg
│
├── uploads/               # Temporary folder for uploaded images
└── .venv/                # Virtual environment (not in git)
```

## How It Works (For Students)

### 1. **User Interface (HTML/CSS/JavaScript)**
   - User provides an image via URL or file upload
   - JavaScript sends the image to the Flask server
   - Displays loading animation while processing
   - Shows results when complete

### 2. **Flask Web Server (app.py)**
   - Receives the image from the user
   - Loads the image using PIL (Python Imaging Library)
   - Sends the image to the BLIP model
   - Returns the generated caption to the user

### 3. **AI Model (BLIP)**
   - Analyzes the image using computer vision
   - Generates a natural language description
   - Returns the caption as text

## Code Learning Guide

### Key Python Concepts Demonstrated:

1. **Web Development with Flask**
   - Routes (`@app.route`)
   - Request handling
   - JSON responses
   - File uploads

2. **AI/ML Integration**
   - Loading pre-trained models
   - Image preprocessing
   - Model inference
   - Result processing

3. **Image Processing**
   - Loading images from URLs
   - Loading images from files
   - Image format conversion

4. **Error Handling**
   - Try/except blocks
   - Validation
   - User-friendly error messages

## Common Issues and Solutions

### Issue 1: Model Not Found Error
**Error**: `OSError: Can't load processor for 'Salesforce/blip-image-captioning-base'`

**Solution**: You need to download the BLIP model first!
```bash
cd models
git clone --progress https://huggingface.co/Salesforce/blip-image-captioning-base
cd ..
```

**Verify the model is downloaded:**
```bash
ls models/blip-image-captioning-base/
# Should show: pytorch_model.bin, config.json, etc.
```

### Issue 2: Git LFS Not Installed
**Error**: Model files are small (few KB) or empty

**Solution**: Install Git LFS before cloning the model:
```bash
# macOS:
brew install git-lfs

# Ubuntu/Debian:
sudo apt-get install git-lfs

# Then initialize and re-download:
git lfs install
cd models
rm -rf blip-image-captioning-base  # Remove incomplete download
git clone --progress https://huggingface.co/Salesforce/blip-image-captioning-base
```

### Issue 3: "Module not found" Error
**Solution**: Make sure you activated the virtual environment and installed requirements:
```bash
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Issue 4: Model Download is Slow
**Solution**: The model is ~1.8GB. Download time depends on your internet speed:
- Fast connection (100 Mbps): 2-3 minutes
- Medium connection (20 Mbps): 10-15 minutes
- Slow connection (5 Mbps): 30+ minutes

Be patient and keep the connection stable!

### Issue 5: "Out of Memory" Error
**Solution**: Close other applications to free up RAM. The model needs about 800MB-1GB of memory.

### Issue 6: Slow Performance
**Solution**: This is normal on CPU. Image captioning takes 5-10 seconds per image on a 1 CPU server.

## Customization Ideas for Students

1. **Add More Features**:
   - Support for multiple images at once
   - Save caption history
   - Export captions to a text file

2. **Improve the Model**:
   - Try different BLIP variants (large, base, etc.)
   - Add conditional captioning (e.g., "a photo of...")
   - Implement beam search for better captions

3. **Enhance the UI**:
   - Add dark mode
   - Include more example images
   - Add image filters/effects

4. **Add Analytics**:
   - Track most common objects detected
   - Show processing time
   - Create usage statistics

## Learning Resources

- **Flask Documentation**: https://flask.palletsprojects.com/
- **BLIP Model Paper**: https://arxiv.org/abs/2201.12086
- **Hugging Face Transformers**: https://huggingface.co/docs/transformers/
- **Python PIL/Pillow**: https://pillow.readthedocs.io/

## Testing the Application

### Test URLs (Free to Use):
```
https://picsum.photos/600/400
https://images.unsplash.com/photo-1506905925346-21bda4d32df4
https://images.unsplash.com/photo-1518791841217-8f162f1e1131
```

### Expected Processing Time:
- Image loading: 1-2 seconds
- AI processing: 5-10 seconds
- Total: ~7-12 seconds per image

## Troubleshooting

### Model Not Loading?
Check Python version:
```bash
python --version  # Should be 3.8 or higher
```

### Port 5000 Already in Use?
Change the port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change 5000 to 5001
```

### Cannot Access from Another Computer?
Make sure:
1. Firewall allows port 5000
2. You're using `host='0.0.0.0'` (already set)
3. Access using your IP address: `http://YOUR_IP:5000`

## Contributing

This is an educational project. Students are encouraged to:
- Add new features
- Improve the code
- Fix bugs
- Enhance documentation

## License

This project is free to use for educational purposes.

## Credits

- **BLIP Model**: Salesforce Research
- **Framework**: Flask (Pallets Projects)
- **AI Library**: Hugging Face Transformers

## Contact & Support

For questions or issues:
1. Read this README thoroughly
2. Check the code comments in `app.py`
3. Review the error messages carefully
4. Search for similar issues online

---

**Happy Learning! 📚🎓**

Built with ❤️ for students learning Python and AI
