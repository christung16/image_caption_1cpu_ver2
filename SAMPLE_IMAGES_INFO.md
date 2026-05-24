# Sample Images Included

## 📸 Three Sample Images Ready to Use!

The `images/` folder now contains three sample images for testing the Image Captioning feature:

### 1. sample_landscape.jpg (14 KB)
- **Description**: A simple landscape scene
- **Contains**: Blue sky, green ground, yellow sun, and a house with a red roof
- **Good for**: Testing outdoor scene recognition

### 2. sample_geometric.jpg (19 KB)
- **Description**: Colorful geometric pattern
- **Contains**: Colorful rectangles and circles in an abstract arrangement
- **Good for**: Testing abstract pattern and color recognition

### 3. sample_cat.jpg (24 KB)
- **Description**: Simple cartoon-style cat drawing
- **Contains**: Orange cat with whiskers, ears, and facial features
- **Good for**: Testing animal/object recognition

## 🧪 How to Test

### Method 1: Use the Web Interface
1. Start the server: `./start.sh`
2. Open browser: `http://localhost:5000`
3. Click: **"Select from Images Folder"** tab
4. Select one of the sample images from the dropdown:
   - sample_landscape.jpg
   - sample_geometric.jpg
   - sample_cat.jpg
5. Click: **"Generate Caption"**
6. Wait 5-10 seconds
7. See what the AI thinks the image shows!

### Method 2: Command Line Test
```bash
# List the images
ls -lh images/

# View image info
file images/sample_cat.jpg
```

## 🎯 Expected AI Captions

The BLIP model should generate captions describing:

**sample_landscape.jpg:**
- May recognize: house, building, outdoor scene, sky

**sample_geometric.jpg:**
- May recognize: colorful pattern, abstract art, shapes

**sample_cat.jpg:**
- May recognize: cat, orange cat, cartoon, drawing

**Note:** Results may vary as these are simple programmatically-generated images. The AI is trained on real photos, so descriptions might be creative!

## ➕ Adding Your Own Images

You can add any images to this folder:

```bash
# Copy your photos
cp ~/Pictures/vacation.jpg images/

# Copy multiple images
cp ~/Downloads/*.jpg images/

# The web interface will automatically list them!
```

## 🎓 For Students

These sample images are created using Python's **PIL (Pillow)** library:
- `Image.new()` - Create blank image
- `ImageDraw.Draw()` - Draw shapes and text
- `.rectangle()`, `.ellipse()`, `.polygon()` - Draw shapes
- `.save()` - Save as JPEG

You can examine the code that created them in the terminal output above!

---

**Try the sample images now!** They're ready to test the directory selection feature! 🚀
