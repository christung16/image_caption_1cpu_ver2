"""
Image Processor Module
======================
This module handles loading and processing images from different sources.

Learning Objectives:
- Working with PIL (Python Imaging Library)
- HTTP requests for downloading images
- File I/O operations
- Error handling and validation
"""

from PIL import Image
import requests
from io import BytesIO
import os


# Allowed image file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}


def is_allowed_file(filename):
    """
    Check if a file has an allowed image extension.
    
    This demonstrates:
    - String manipulation (rsplit)
    - Set membership testing
    - Defensive programming
    
    Args:
        filename (str): Name of the file to check
        
    Returns:
        bool: True if the file extension is allowed, False otherwise
        
    Example:
        >>> is_allowed_file("photo.jpg")
        True
        >>> is_allowed_file("document.pdf")
        False
    """
    # Check if filename has a dot (has an extension)
    if '.' not in filename:
        return False
    
    # Split filename and get extension (convert to lowercase)
    extension = filename.rsplit('.', 1)[1].lower()
    
    # Check if extension is in allowed set
    return extension in ALLOWED_EXTENSIONS


def load_image_from_url(url, timeout=10):
    """
    Download and load an image from a URL.
    
    This demonstrates:
    - HTTP requests
    - Error handling with try/except
    - Working with binary data (BytesIO)
    - Image format conversion
    
    Args:
        url (str): The URL of the image to download
        timeout (int): Request timeout in seconds (default: 10)
        
    Returns:
        PIL.Image: The loaded image in RGB format
        
    Raises:
        Exception: If the image cannot be downloaded or loaded
        
    Example:
        >>> image = load_image_from_url("https://picsum.photos/200")
        >>> print(f"Image size: {image.size}")
        Image size: (200, 200)
    """
    try:
        # Step 1: Send HTTP GET request to download the image
        print(f"Downloading image from: {url}")
        response = requests.get(url, timeout=timeout, verify=False)
        
        # Step 2: Check if request was successful
        response.raise_for_status()  # Raises HTTPError for bad status codes
        
        # Step 3: Convert binary data to image
        # BytesIO creates a file-like object from bytes in memory
        image_data = BytesIO(response.content)
        image = Image.open(image_data)
        
        # Step 4: Convert to RGB if needed
        # Some images are in RGBA, grayscale, or other formats
        if image.mode != 'RGB':
            print(f"Converting image from {image.mode} to RGB")
            image = image.convert('RGB')
        
        print(f"✓ Image loaded: {image.size[0]}x{image.size[1]} pixels")
        return image
        
    except requests.exceptions.Timeout:
        raise Exception(f"Request timed out after {timeout} seconds")
    except requests.exceptions.HTTPError as e:
        raise Exception(f"HTTP error: {e}")
    except Exception as e:
        raise Exception(f"Failed to load image from URL: {str(e)}")


def load_image_from_file(file_path):
    """
    Load an image from a local file.
    
    This demonstrates:
    - File system operations
    - PIL Image loading
    - Error handling
    - Image format conversion
    
    Args:
        file_path (str): Path to the image file
        
    Returns:
        PIL.Image: The loaded image in RGB format
        
    Raises:
        Exception: If the file cannot be found or loaded
        
    Example:
        >>> image = load_image_from_file("images/sample_cat.jpg")
        >>> print(f"Image size: {image.size}")
        Image size: (800, 600)
    """
    try:
        # Step 1: Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Step 2: Open the image
        print(f"Loading image from: {file_path}")
        image = Image.open(file_path)
        
        # Step 3: Convert to RGB if needed
        if image.mode != 'RGB':
            print(f"Converting image from {image.mode} to RGB")
            image = image.convert('RGB')
        
        print(f"✓ Image loaded: {image.size[0]}x{image.size[1]} pixels")
        return image
        
    except FileNotFoundError as e:
        raise Exception(str(e))
    except Exception as e:
        raise Exception(f"Failed to load image from file: {str(e)}")


def resize_image(image, max_size=512):
    """
    Resize an image while maintaining aspect ratio.
    
    This demonstrates:
    - Image manipulation
    - Aspect ratio calculations
    - Conditional logic
    
    Args:
        image (PIL.Image): The image to resize
        max_size (int): Maximum dimension (width or height) in pixels
        
    Returns:
        PIL.Image: The resized image
        
    Example:
        >>> image = load_image_from_file("large_image.jpg")
        >>> resized = resize_image(image, max_size=256)
        >>> print(f"New size: {resized.size}")
        New size: (256, 192)
    """
    # Get current dimensions
    width, height = image.size
    
    # Check if resize is needed
    if width <= max_size and height <= max_size:
        return image  # No resize needed
    
    # Calculate new dimensions maintaining aspect ratio
    if width > height:
        new_width = max_size
        new_height = int(height * (max_size / width))
    else:
        new_height = max_size
        new_width = int(width * (max_size / height))
    
    # Resize the image
    print(f"Resizing from {width}x{height} to {new_width}x{new_height}")
    resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    return resized_image


def save_image(image, output_path, quality=95):
    """
    Save an image to a file.
    
    Args:
        image (PIL.Image): The image to save
        output_path (str): Path where to save the image
        quality (int): JPEG quality (1-100, default: 95)
        
    Example:
        >>> image = load_image_from_url("https://picsum.photos/200")
        >>> save_image(image, "downloaded_image.jpg")
        ✓ Image saved to: downloaded_image.jpg
    """
    image.save(output_path, quality=quality)
    print(f"✓ Image saved to: {output_path}")


# Example usage (for testing this module independently)
if __name__ == "__main__":
    print("="*60)
    print("Testing Image Processor Module")
    print("="*60)
    
    # Test 1: Load from file
    print("\nTest 1: Loading from file...")
    try:
        image = load_image_from_file("../images/sample_cat.jpg")
        print(f"Success! Image size: {image.size}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test 2: Check file extensions
    print("\nTest 2: File extension validation...")
    test_files = ["photo.jpg", "image.png", "document.pdf", "picture.gif"]
    for filename in test_files:
        result = "✓ allowed" if is_allowed_file(filename) else "✗ not allowed"
        print(f"  {filename}: {result}")
    
    # Test 3: Load from URL (optional - requires internet)
    print("\nTest 3: Loading from URL...")
    try:
        url = "https://picsum.photos/200"
        image = load_image_from_url(url)
        print(f"Success! Image size: {image.size}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n✓ Module test completed!")
