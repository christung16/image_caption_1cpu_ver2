# 🚀 Running the Application - Quick Reference

## ✅ Everything is Set Up!

The BLIP model has been downloaded locally using `git clone`. You're ready to go!

## 🎯 To Start the Server:

### Option 1: Using the Startup Script (Recommended)
```bash
cd /Users/yitung/Documents/PycharmProjects/image_caption_1cpu_ver2
./start.sh
```

### Option 2: Manual Start
```bash
cd /Users/yitung/Documents/PycharmProjects/image_caption_1cpu_ver2
source .venv/bin/activate
python app.py
```

## 🌐 Access the Application:

Once the server starts, open your browser and go to:
```
http://localhost:5000
```

## ⚡ What to Expect:

**Server Startup (5-10 seconds):**
```
Loading BLIP model from local directory...
Using local model from: .../models/blip-image-captioning-base
Loading weights: 100%|██████████| 473/473
Model loaded successfully!
Server starting on http://localhost:5000
```

**First Caption:** 10-15 seconds (model initialization)
**Subsequent Captions:** 5-10 seconds each

## 🧪 Test It Out:

1. **Image URL Test:**
   - Tab: "Image URL"
   - Paste: `http://picsum.photos/600/400`
   - Click: "Generate Caption"

2. **File Upload Test:**
   - Tab: "Upload File"  
   - Choose: Any image from your computer
   - Click: "Generate Caption"

## 🛑 To Stop the Server:

Press **CTRL + C** in the terminal

## 📁 Project Structure:

```
image_caption_1cpu_ver2/
├── app.py                    # Main application
├── start.sh                  # Startup script
├── requirements.txt          # Dependencies
├── README.md                 # Full documentation
├── QUICKSTART.md            # Quick reference
├── MODEL_DOWNLOAD_GUIDE.md  # Model download info
├── templates/
│   └── index.html           # Web interface
├── static/
│   └── style.css            # Styling
├── models/
│   └── blip-image-captioning-base/  # Local AI model
└── .venv/                   # Virtual environment
```

## 💡 Benefits of Local Model:

✅ **Fast startup** - No downloading
✅ **Works offline** - No internet needed (after setup)
✅ **No SSL issues** - Model is already on disk
✅ **Consistent** - Same model version always

## 🎓 For Students:

### Explore the Code:
- **app.py** - All the Python backend logic (well commented)
- **templates/index.html** - The web page structure
- **static/style.css** - The visual styling

### Explore the Model:
```bash
ls -lh models/blip-image-captioning-base/
```
See the actual AI model files!

### Learn More:
- Check out **README.md** for detailed documentation
- Read **MODEL_DOWNLOAD_GUIDE.md** to understand the download process

---

**Ready to start? Run: `./start.sh`** 🚀

**Then open: http://localhost:5000** 🌐
