# Quick Start Guide

## The Application is Now Running! 🎉

Your Image Captioning web application is now active and running on your computer.

## How to Access

1. **Open your web browser** (Chrome, Safari, Firefox, etc.)
2. **Go to:** `http://localhost:5000`
3. You should see the Image Captioning interface!

## How to Use

### Method 1: Using Image URL
1. Click on the "Image URL" tab
2. Paste an image URL (examples below)
3. Click "Generate Caption"
4. Wait 5-10 seconds
5. See the AI-generated caption!

### Method 2: Upload a File
1. Click on the "Upload File" tab
2. Click "Choose an Image File" and select an image from your computer
3. Click "Generate Caption"
4. Wait 5-10 seconds
5. See the AI-generated caption!

## Test Image URLs

Try these free image URLs:
```
http://picsum.photos/600/400
https://images.unsplash.com/photo-1518791841217-8f162f1e1131
https://images.unsplash.com/photo-1506905925346-21bda4d32df4
```

## What's Happening in the Terminal

- **First run**: The BLIP model is being downloaded (~1.8GB)
  - This happens only once
  - Takes 2-5 minutes depending on your internet speed
  
- **"Loading BLIP model..."**: The model is loading into memory
  
- **"Model loaded successfully!"**: Ready to use!
  
- **Flask server messages**: Normal server activity logs

## How to Stop the Server

Press **CTRL + C** in the terminal window where the server is running.

## Troubleshooting

### Can't Access http://localhost:5000?
- Make sure the terminal shows "Model loaded successfully!"
- Wait for the model download to complete (first run only)
- Try refreshing your browser

### "Taking too long"?
- First image: 5-15 seconds (model initialization)
- Subsequent images: 5-10 seconds
- This is normal on a 1 CPU server

### Server Not Responding?
- Check the terminal for error messages
- Make sure port 5000 isn't being used by another program
- Restart the server: CTRL+C, then run `./start.sh` again

## For Students

This is a great learning project! Check out:
- **app.py** - The main Python code (well-commented)
- **templates/index.html** - The web interface HTML
- **static/style.css** - The styling
- **README.md** - Full documentation

---

**Enjoy learning Python and AI!** 🚀📚

Last updated: 2026-05-24
