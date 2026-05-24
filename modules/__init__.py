"""
Modules Package
===============
This package contains modular components for the AI Image Captioning application.

Modules:
- model_loader: Load and manage the BLIP AI model
- image_processor: Load and process images from various sources
- caption_generator: Generate captions from images using AI

Each module can be used independently for learning and testing.
"""

# Make it easy to import from the package
from .model_loader import load_blip_model, get_model_info
from .image_processor import (
    load_image_from_url,
    load_image_from_file,
    is_allowed_file,
    resize_image,
    save_image
)
from .caption_generator import (
    generate_caption,
    generate_caption_with_prompt,
    batch_generate_captions,
    compare_captions
)

__all__ = [
    # Model loader
    'load_blip_model',
    'get_model_info',
    
    # Image processor
    'load_image_from_url',
    'load_image_from_file',
    'is_allowed_file',
    'resize_image',
    'save_image',
    
    # Caption generator
    'generate_caption',
    'generate_caption_with_prompt',
    'batch_generate_captions',
    'compare_captions',
]
