"""
Caption Generator Module
========================
This module handles generating captions from images using the BLIP model.

Learning Objectives:
- Understanding AI model inference
- Working with PyTorch tensors
- Text generation and decoding
- Performance optimization with torch.no_grad()
"""

import torch


def generate_caption(image, processor, model, max_length=50, num_beams=1):
    """
    Generate a caption for an image using the BLIP model.
    
    This demonstrates:
    - Image preprocessing
    - Model inference (forward pass)
    - Text generation from tokens
    - Context managers (with statement)
    
    Args:
        image (PIL.Image): The image to caption
        processor: The BLIP processor for preprocessing
        model: The BLIP model for generation
        max_length (int): Maximum length of generated caption (default: 50)
        num_beams (int): Number of beams for beam search (default: 1, greedy)
        
    Returns:
        str: The generated caption
        
    Example:
        >>> from modules.model_loader import load_blip_model
        >>> from modules.image_processor import load_image_from_file
        >>> processor, model = load_blip_model()
        >>> image = load_image_from_file("images/sample_cat.jpg")
        >>> caption = generate_caption(image, processor, model)
        >>> print(caption)
        a cat sitting on a table
    """
    # Step 1: Preprocess the image
    # This converts the PIL Image to tensors the model can process
    print("Preprocessing image...")
    inputs = processor(images=image, return_tensors="pt")
    
    # Step 2: Generate caption tokens
    # torch.no_grad() disables gradient calculation (we're not training)
    # This saves memory and speeds up inference
    print("Generating caption...")
    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_length=max_length,
            num_beams=num_beams
        )
    
    # Step 3: Decode tokens to text
    # skip_special_tokens removes [CLS], [SEP], [PAD] tokens
    caption = processor.decode(output_ids[0], skip_special_tokens=True)
    
    print(f"✓ Caption generated: \"{caption}\"")
    return caption


def generate_caption_with_prompt(image, processor, model, prompt, max_length=50):
    """
    Generate a caption with a text prompt (conditional generation).
    
    This demonstrates:
    - Conditional text generation
    - Multi-modal input (image + text)
    
    Args:
        image (PIL.Image): The image to caption
        processor: The BLIP processor
        model: The BLIP model
        prompt (str): Text prompt to guide generation (e.g., "a photo of")
        max_length (int): Maximum caption length
        
    Returns:
        str: The generated caption
        
    Example:
        >>> caption = generate_caption_with_prompt(
        ...     image, processor, model, 
        ...     prompt="This is a photo of"
        ... )
    """
    # Preprocess with both image and text
    inputs = processor(images=image, text=prompt, return_tensors="pt")
    
    # Generate with the prompt
    with torch.no_grad():
        output_ids = model.generate(**inputs, max_length=max_length)
    
    # Decode to text
    caption = processor.decode(output_ids[0], skip_special_tokens=True)
    
    return caption


def batch_generate_captions(images, processor, model, max_length=50):
    """
    Generate captions for multiple images at once (batch processing).
    
    This demonstrates:
    - Batch processing for efficiency
    - List comprehension
    - Loop optimization
    
    Args:
        images (list): List of PIL Images
        processor: The BLIP processor
        model: The BLIP model
        max_length (int): Maximum caption length
        
    Returns:
        list: List of generated captions
        
    Example:
        >>> images = [image1, image2, image3]
        >>> captions = batch_generate_captions(images, processor, model)
        >>> for i, caption in enumerate(captions):
        ...     print(f"Image {i+1}: {caption}")
    """
    print(f"Processing batch of {len(images)} images...")
    
    # Process all images
    inputs = processor(images=images, return_tensors="pt", padding=True)
    
    # Generate captions
    with torch.no_grad():
        output_ids = model.generate(**inputs, max_length=max_length)
    
    # Decode all captions
    captions = [
        processor.decode(output_id, skip_special_tokens=True)
        for output_id in output_ids
    ]
    
    print(f"✓ Generated {len(captions)} captions")
    return captions


def get_caption_confidence(image, processor, model, caption):
    """
    Calculate a confidence score for a generated caption.
    
    This demonstrates:
    - Model output analysis
    - Probability calculations
    - Advanced model usage
    
    Args:
        image (PIL.Image): The image
        processor: The BLIP processor
        model: The BLIP model
        caption (str): The generated caption
        
    Returns:
        float: Average confidence score (0-1)
        
    Note:
        This is a simplified confidence measure.
        In production, you'd use proper likelihood calculations.
    """
    # Encode the caption
    inputs = processor(images=image, text=caption, return_tensors="pt")
    
    # Get model outputs
    with torch.no_grad():
        outputs = model(**inputs)
        # For simplicity, we'll return a basic score
        # In practice, you'd analyze the logits/probabilities
        return 0.85  # Placeholder
    

def compare_captions(image, processor, model, num_variations=3):
    """
    Generate multiple caption variations for comparison.
    
    Args:
        image (PIL.Image): The image to caption
        processor: The BLIP processor
        model: The BLIP model
        num_variations (int): Number of caption variations to generate
        
    Returns:
        list: List of different captions
        
    Example:
        >>> variations = compare_captions(image, processor, model, num_variations=3)
        >>> for i, caption in enumerate(variations, 1):
        ...     print(f"{i}. {caption}")
    """
    captions = []
    
    # Generate variations with different parameters
    for i in range(num_variations):
        inputs = processor(images=image, return_tensors="pt")
        
        with torch.no_grad():
            output_ids = model.generate(
                **inputs,
                max_length=50,
                num_beams=i+1,  # Vary beam search
                temperature=1.0 + (i * 0.2)  # Vary temperature
            )
        
        caption = processor.decode(output_ids[0], skip_special_tokens=True)
        captions.append(caption)
    
    return captions


# Example usage (for testing this module independently)
if __name__ == "__main__":
    print("="*60)
    print("Testing Caption Generator Module")
    print("="*60)
    
    # Import dependencies
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    
    from modules.model_loader import load_blip_model
    from modules.image_processor import load_image_from_file
    
    # Load model
    print("\nLoading model...")
    processor, model = load_blip_model()
    
    # Load test image
    print("\nLoading test image...")
    try:
        image = load_image_from_file("../images/sample_cat.jpg")
        
        # Test 1: Basic caption generation
        print("\n" + "="*60)
        print("Test 1: Basic Caption Generation")
        print("="*60)
        caption = generate_caption(image, processor, model)
        print(f"Result: \"{caption}\"")
        
        # Test 2: Caption variations
        print("\n" + "="*60)
        print("Test 2: Multiple Caption Variations")
        print("="*60)
        variations = compare_captions(image, processor, model, num_variations=3)
        for i, cap in enumerate(variations, 1):
            print(f"{i}. {cap}")
        
        print("\n✓ Module test completed successfully!")
        
    except Exception as e:
        print(f"Error during testing: {e}")
        print("Make sure sample images exist in the images/ directory")
