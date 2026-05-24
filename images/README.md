# Images Folder

This folder is used to store images that you want to caption using the directory selection feature.

## How to Use

1. **Place your images here**: Copy or move any images you want to caption into this folder
2. **Open the web app**: Go to http://localhost:5000
3. **Select the "Select from Images Folder" tab**
4. **Choose an image** from the dropdown menu
5. **Click "Generate Caption"**

## Supported Formats

- PNG (.png)
- JPEG (.jpg, .jpeg)
- GIF (.gif)
- BMP (.bmp)
- WEBP (.webp)

## Example Usage

```bash
# Copy an image to this folder
cp ~/Pictures/mycat.jpg images/

# Or download an image
curl -o images/sample.jpg https://picsum.photos/600/400
```

## For Students

This feature demonstrates:
- **File system operations** in Python (listing files in a directory)
- **Dynamic content loading** using JavaScript fetch API
- **Image serving** with Flask routes
- **Dropdown menus** populated dynamically from server data

## Tips

- Keep filenames simple (no special characters)
- Reasonable file sizes (under 16MB)
- Images are NOT uploaded to server - they're already on disk!
- This is faster than uploading files each time

---

**Try it out!** Place some images in this folder and select them from the web interface.
