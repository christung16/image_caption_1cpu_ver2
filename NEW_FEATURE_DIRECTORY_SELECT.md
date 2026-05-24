# ✨ New Feature Added: Select Images from Directory!

## What's New?

Your Image Captioning app now has **THREE ways** to provide images:

1. **Image URL** - Paste a URL from the internet
2. **Upload File** - Choose a file from your computer  
3. **Select from Images Folder** ⭐ **NEW!** - Pick images from the `images/` directory

## How to Use the New Feature

### Step 1: Add Images to the Folder

Place any images you want to caption in the `images/` folder:

```bash
# Copy your own images
cp ~/Pictures/*.jpg images/

# Or drag and drop images into the folder
```

### Step 2: Use the Web Interface

1. Start the server: `./start.sh`
2. Open: `http://localhost:5000`
3. Click the **"Select from Images Folder"** tab
4. Choose an image from the dropdown menu
5. Click **"Generate Caption"**

## Why This is Useful

### For Students Learning:
- ✅ **File system operations** - Reading directories with Python
- ✅ **REST API** - Creating endpoints to list files
- ✅ **Dynamic UI** - Populating dropdowns from server data
- ✅ **Image serving** - Serving static files with Flask

### For Practical Use:
- ✅ **Batch processing** - Keep test images in one place
- ✅ **Faster** - No upload time, images already on disk
- ✅ **Organized** - All test images in one folder
- ✅ **Convenient** - No need to browse your entire computer

## Technical Details

### New Backend Routes (app.py)

```python
@app.route('/list-images', methods=['GET'])
def list_images():
    """List all images in the 'images' directory"""
    # Returns JSON: {'success': bool, 'images': list}

@app.route('/images/<filename>')
def serve_image(filename):
    """Serve an image from the images directory"""
    # Returns the image file
```

### Updated Caption Route

The `/caption` endpoint now accepts:
- `image_url` - URL parameter
- `image_file` - Uploaded file
- `directory_image` - Filename from directory ⭐ NEW!

### Frontend Changes

New tab in `templates/index.html`:
- Dropdown menu populated dynamically
- Image preview when selecting
- Security check to prevent directory traversal

### CSS Styling

New styles in `static/style.css`:
- `.directory-select` - Styled dropdown
- `.directory-preview` - Image preview styling

## File Structure

```
image_caption_1cpu_ver2/
├── images/              ⭐ NEW FOLDER!
│   ├── README.md       # Instructions
│   └── (your images here)
├── app.py              # Updated with new routes
├── templates/
│   └── index.html      # Updated with new tab
└── static/
    └── style.css       # Updated with new styles
```

## Example: Adding Test Images

```bash
# Method 1: Copy from your Pictures folder
cp ~/Pictures/vacation.jpg images/

# Method 2: Download from internet (if curl works)
# curl -o images/test.jpg https://example.com/image.jpg

# Method 3: Drag and drop
# Open the images folder in Finder and drag files in
```

## Security Features

✅ **Path validation** - Prevents directory traversal attacks
✅ **File type checking** - Only allows image extensions
✅ **Read-only** - Web app cannot modify or delete files

## For Teaching

This feature adds great educational value:

### Concept 1: File System
```python
# How to list files in a directory
for filename in os.listdir(images_dir):
    if allowed_file(filename):
        image_files.append(filename)
```

### Concept 2: Dynamic Content
```javascript
// How to load data from server
const response = await fetch('/list-images');
const data = await response.json();
```

### Concept 3: Static File Serving
```python
# How to serve files with Flask
from flask import send_from_directory
return send_from_directory(images_dir, filename)
```

## Try It Now!

1. Place some images in the `images/` folder
2. Start the server
3. Go to the "Select from Images Folder" tab
4. See your images listed in the dropdown!
5. Select one and generate a caption

---

**Enjoy the new feature!** 🎉

This makes testing and demonstrating the AI model much easier for students!
