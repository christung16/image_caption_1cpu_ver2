"""
Model Loader Module
===================
This module handles loading the BLIP AI model.

Learning Objectives:
- Understanding how to load pre-trained AI models
- Working with local vs. remote model files
- Memory optimization for limited resources
"""

import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
import os


def load_blip_model(model_name="blip-image-captioning-base"):
    """
    Load the BLIP model and processor from local directory or Hugging Face.
    
    This function demonstrates:
    1. Local file system navigation
    2. Conditional logic for fallback behavior
    3. Model initialization with memory optimization
    
    Args:
        model_name (str): Name of the model directory (default: "blip-image-captioning-base")
    
    Returns:
        tuple: (processor, model) - The loaded processor and model objects
        
    Example:
        >>> processor, model = load_blip_model()
        >>> print(f"Model loaded: {model is not None}")
        Model loaded: True
    """
    print(f"Loading BLIP model: {model_name}...")
    
    # Step 1: Determine the model path
    # First try to use local model, then fall back to Hugging Face
    base_dir = os.path.dirname(os.path.dirname(__file__))  # Go up one directory
    local_model_path = os.path.join(base_dir, "models", model_name)
    
    # Step 2: Check if local model exists
    if os.path.exists(local_model_path):
        print(f"✓ Found local model at: {local_model_path}")
        model_path = local_model_path
    else:
        print(f"⚠ Local model not found. Will download from Hugging Face...")
        model_path = f"Salesforce/{model_name}"
    
    # Step 3: Load the processor
    # The processor handles image preprocessing (resizing, normalization, etc.)
    print("Loading processor...")
    processor = BlipProcessor.from_pretrained(model_path)
    
    # Step 4: Load the model with memory optimizations
    print("Loading model weights...")
    model = BlipForConditionalGeneration.from_pretrained(
        model_path,
        torch_dtype=torch.float32,      # Use 32-bit floating point for CPU
        low_cpu_mem_usage=True          # Optimize for limited RAM (1GB)
    )
    
    # Step 5: Set model to evaluation mode
    # This disables training features like dropout for better inference performance
    model.eval()
    
    print("✓ Model loaded successfully!")
    print(f"  - Model type: {type(model).__name__}")
    print(f"  - Parameters: ~{sum(p.numel() for p in model.parameters()) / 1e6:.1f}M")
    
    return processor, model


def get_model_info(model):
    """
    Get information about the loaded model.
    
    Args:
        model: The loaded BLIP model
        
    Returns:
        dict: Dictionary with model information
        
    Example:
        >>> processor, model = load_blip_model()
        >>> info = get_model_info(model)
        >>> print(info['num_parameters'])
    """
    info = {
        'model_name': type(model).__name__,
        'num_parameters': sum(p.numel() for p in model.parameters()),
        'num_trainable_parameters': sum(p.numel() for p in model.parameters() if p.requires_grad),
        'device': next(model.parameters()).device,
        'dtype': next(model.parameters()).dtype,
    }
    return info


# Example usage (for testing this module independently)
if __name__ == "__main__":
    print("="*60)
    print("Testing Model Loader Module")
    print("="*60)
    
    # Load the model
    processor, model = load_blip_model()
    
    # Display model information
    info = get_model_info(model)
    print("\nModel Information:")
    print(f"  Name: {info['model_name']}")
    print(f"  Parameters: {info['num_parameters']:,}")
    print(f"  Device: {info['device']}")
    print(f"  Data type: {info['dtype']}")
    
    print("\n✓ Module test completed successfully!")
