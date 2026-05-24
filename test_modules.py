#!/usr/bin/env python3
"""
Test script to validate all modules work correctly.
This simulates what the Jupyter notebooks will do.
"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("="*60)
print("Testing AI Image Captioning Modules")
print("="*60)

# Test 1: Import all modules
print("\n[1/5] Testing module imports...")
try:
    from modules.model_loader import load_blip_model, get_model_info
    from modules.image_processor import (
        load_image_from_file,
        load_image_from_url,
        resize_image,
        is_allowed_file
    )
    from modules.caption_generator import (
        generate_caption,
        batch_generate_captions,
        compare_captions
    )
    print("✓ All modules imported successfully!")
except Exception as e:
    print(f"✗ Import failed: {e}")
    sys.exit(1)

# Test 2: Load the model
print("\n[2/5] Testing model loading...")
try:
    processor, model = load_blip_model()
    info = get_model_info(model)
    print(f"✓ Model loaded successfully!")
    print(f"  - Parameters: {info['num_parameters']:,}")
    print(f"  - Device: {info['device']}")
except Exception as e:
    print(f"✗ Model loading failed: {e}")
    print("  Make sure you've downloaded the BLIP model!")
    sys.exit(1)

# Test 3: Load an image
print("\n[3/5] Testing image loading...")
try:
    test_image_path = "images/sample_cat.jpg"
    if os.path.exists(test_image_path):
        image = load_image_from_file(test_image_path)
        print(f"✓ Image loaded: {image.size[0]}x{image.size[1]} pixels")
    else:
        print(f"⚠ Test image not found: {test_image_path}")
        print("  Skipping image tests...")
        sys.exit(0)
except Exception as e:
    print(f"✗ Image loading failed: {e}")
    sys.exit(1)

# Test 4: Generate a caption
print("\n[4/5] Testing caption generation...")
try:
    caption = generate_caption(image, processor, model)
    print(f"✓ Caption generated: \"{caption}\"")
except Exception as e:
    print(f"✗ Caption generation failed: {e}")
    sys.exit(1)

# Test 5: Test batch processing
print("\n[5/5] Testing batch processing...")
try:
    # Load multiple images
    test_images = []
    image_files = ["sample_cat.jpg", "sample_geometric.jpg", "sample_landscape.jpg"]
    
    for filename in image_files:
        filepath = os.path.join("images", filename)
        if os.path.exists(filepath):
            img = load_image_from_file(filepath)
            test_images.append(img)
    
    if len(test_images) > 0:
        captions = batch_generate_captions(test_images, processor, model)
        print(f"✓ Batch processing successful!")
        print(f"  Generated {len(captions)} captions:")
        for i, cap in enumerate(captions, 1):
            print(f"    {i}. {cap}")
    else:
        print("⚠ No test images found for batch processing")
        
except Exception as e:
    print(f"✗ Batch processing failed: {e}")
    sys.exit(1)

# Test 6: Test utility functions
print("\n[6/6] Testing utility functions...")
try:
    # Test file validation
    assert is_allowed_file("photo.jpg") == True
    assert is_allowed_file("document.pdf") == False
    print("✓ File validation works!")
    
    # Test image resizing
    resized = resize_image(image, max_size=256)
    print(f"✓ Image resizing works! ({resized.size[0]}x{resized.size[1]})")
    
except Exception as e:
    print(f"✗ Utility functions failed: {e}")
    sys.exit(1)

# Summary
print("\n" + "="*60)
print("✓ All tests passed successfully!")
print("="*60)
print("\nThe modules are working correctly and ready for:")
print("  1. Web application (python app.py)")
print("  2. Jupyter notebooks (jupyter notebook notebooks/)")
print("  3. Custom projects using the modules")
print("\n" + "="*60)
