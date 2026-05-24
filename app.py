"""
Image Captioning Web Application
==================================
This is a Flask web application that uses AI to generate captions for images.
Perfect for students learning Python and AI!

Author: Educational Project
Model: BLIP-base (Salesforce)
"""

# Import required libraries
from flask import Flask, render_template, request, jsonify
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
import requests
from io import BytesIO
import os
import ssl
import urllib3
import httpx

# Disable SSL warnings and verification for educational purposes only
# WARNING: Never do this in production!
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

# Monkey-patch httpx to disable SSL verification
original_httpx_client = httpx.Client
def patched_httpx_client(*args, **kwargs):
    kwargs['verify'] = False
    return original_httpx_client(*args, **kwargs)
httpx.Client = patched_httpx_client

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}

# Create upload folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Global variables for model and processor
# We load these once when the app starts to save memory and time
model = None
processor = None


def load_model():
    """
    Load the BLIP model and processor.
    This function is called once when the application starts.
    
    Returns:
        tuple: (processor, model) - The loaded processor and model
    """
    print("Loading BLIP model from local directory...")
    
    # Path to the local model directory
    # Using local model avoids SSL issues and is faster after first download
    model_path = os.path.join(os.path.dirname(__file__), "models", "blip-image-captioning-base")
    
    # Check if local model exists
    if not os.path.exists(model_path):
        print("Local model not found. Downloading from Hugging Face...")
        model_path = "Salesforce/blip-image-captioning-base"
    else:
        print(f"Using local model from: {model_path}")
    
    # Load the processor (handles image preprocessing)
    processor = BlipProcessor.from_pretrained(model_path)
    
    # Load the model with optimizations for 1GB RAM
    model = BlipForConditionalGeneration.from_pretrained(
        model_path,
        torch_dtype=torch.float32,  # Use float32 for CPU
        low_cpu_mem_usage=True  # Optimize memory usage
    )
    
    # Set model to evaluation mode (not training)
    model.eval()
    
    print("Model loaded successfully!")
    return processor, model


def allowed_file(filename):
    """
    Check if the uploaded file has an allowed extension.
    
    Args:
        filename (str): The name of the file
        
    Returns:
        bool: True if file extension is allowed, False otherwise
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def load_image_from_url(url):
    """
    Download and load an image from a URL.
    
    Args:
        url (str): The URL of the image
        
    Returns:
        PIL.Image: The loaded image
        
    Raises:
        Exception: If the image cannot be loaded
    """
    try:
        # Send HTTP request to get the image
        # verify=False disables SSL verification for educational purposes
        response = requests.get(url, timeout=10, verify=False)
        response.raise_for_status()  # Raise error for bad status codes
        
        # Convert the response content to an image
        image = Image.open(BytesIO(response.content))
        
        # Convert to RGB if needed (some images are in different formats)
        if image.mode != 'RGB':
            image = image.convert('RGB')
            
        return image
    except Exception as e:
        raise Exception(f"Failed to load image from URL: {str(e)}")


def load_image_from_file(file_path):
    """
    Load an image from a local file.
    
    Args:
        file_path (str): Path to the image file
        
    Returns:
        PIL.Image: The loaded image
        
    Raises:
        Exception: If the image cannot be loaded
    """
    try:
        image = Image.open(file_path)
        
        # Convert to RGB if needed
        if image.mode != 'RGB':
            image = image.convert('RGB')
            
        return image
    except Exception as e:
        raise Exception(f"Failed to load image from file: {str(e)}")


def generate_caption(image):
    """
    Generate a caption for the given image using the BLIP model.
    
    Args:
        image (PIL.Image): The image to caption
        
    Returns:
        str: The generated caption
    """
    # Preprocess the image
    # This converts the image to the format the model expects
    inputs = processor(images=image, return_tensors="pt")
    
    # Generate caption
    # The model creates text tokens that describe the image
    with torch.no_grad():  # Don't calculate gradients (we're not training)
        output = model.generate(**inputs, max_length=50)
    
    # Decode the tokens back to text
    caption = processor.decode(output[0], skip_special_tokens=True)
    
    return caption


@app.route('/')
def index():
    """
    Render the main page of the application.
    
    Returns:
        str: Rendered HTML template
    """
    return render_template('index.html')


@app.route('/list-images', methods=['GET'])
def list_images():
    """
    List all images in the 'images' directory.
    
    Returns:
        JSON: {'success': bool, 'images': list, 'error': str}
    """
    try:
        images_dir = os.path.join(os.path.dirname(__file__), 'images')
        
        # Create directory if it doesn't exist
        if not os.path.exists(images_dir):
            os.makedirs(images_dir)
            return jsonify({'success': True, 'images': []})
        
        # Get all image files from the directory
        image_files = []
        for filename in os.listdir(images_dir):
            if allowed_file(filename):
                image_files.append(filename)
        
        # Sort alphabetically
        image_files.sort()
        
        return jsonify({'success': True, 'images': image_files})
        
    except Exception as e:
        print(f"Error listing images: {str(e)}")
        return jsonify({'success': False, 'error': str(e)})


@app.route('/images/<filename>')
def serve_image(filename):
    """
    Serve an image from the images directory.
    
    Args:
        filename (str): Name of the image file
        
    Returns:
        File: The image file
    """
    from flask import send_from_directory
    images_dir = os.path.join(os.path.dirname(__file__), 'images')
    return send_from_directory(images_dir, filename)


@app.route('/caption', methods=['POST'])
def caption_image():
    """
    Handle image captioning requests.
    This endpoint accepts either a URL, an uploaded file, or a directory image.
    
    Returns:
        JSON: {'success': bool, 'caption': str, 'error': str}
    """
    try:
        image = None
        
        # Check if user provided a URL
        if 'image_url' in request.form and request.form['image_url'].strip():
            url = request.form['image_url'].strip()
            print(f"Loading image from URL: {url}")
            image = load_image_from_url(url)
            
        # Check if user uploaded a file
        elif 'image_file' in request.files:
            file = request.files['image_file']
            
            # Check if file is valid
            if file.filename == '':
                return jsonify({'success': False, 'error': 'No file selected'})
            
            if file and allowed_file(file.filename):
                # Save the file temporarily
                filename = 'temp_' + file.filename
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                
                print(f"Loading image from file: {filename}")
                image = load_image_from_file(filepath)
                
                # Clean up the temporary file
                os.remove(filepath)
            else:
                return jsonify({'success': False, 'error': 'Invalid file type. Please use: png, jpg, jpeg, gif, bmp, or webp'})
        
        # Check if user selected an image from directory
        elif 'directory_image' in request.form and request.form['directory_image'].strip():
            filename = request.form['directory_image'].strip()
            images_dir = os.path.join(os.path.dirname(__file__), 'images')
            filepath = os.path.join(images_dir, filename)
            
            # Security check: make sure the file is in the images directory
            if not os.path.abspath(filepath).startswith(os.path.abspath(images_dir)):
                return jsonify({'success': False, 'error': 'Invalid file path'})
            
            if not os.path.exists(filepath):
                return jsonify({'success': False, 'error': 'Image file not found'})
            
            print(f"Loading image from directory: {filename}")
            image = load_image_from_file(filepath)
        
        else:
            return jsonify({'success': False, 'error': 'Please provide either a URL, upload an image file, or select from directory'})
        
        # Generate caption
        print("Generating caption...")
        caption = generate_caption(image)
        print(f"Caption generated: {caption}")
        
        return jsonify({'success': True, 'caption': caption})
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'success': False, 'error': str(e)})


@app.route('/health')
def health_check():
    """
    Health check endpoint to verify the application is running.
    
    Returns:
        JSON: {'status': str, 'model_loaded': bool}
    """
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None
    })


if __name__ == '__main__':
    # Load the model when the application starts
    processor, model = load_model()
    
    # Start the Flask web server
    # debug=True allows you to see errors and auto-reloads on code changes
    # host='0.0.0.0' allows access from other computers on your network
    print("\n" + "="*60)
    print("Image Captioning Web Application")
    print("="*60)
    print("Server starting on http://localhost:5000")
    print("Press CTRL+C to stop the server")
    print("="*60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
