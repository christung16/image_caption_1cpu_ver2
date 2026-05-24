#!/bin/bash

# Startup script for Image Captioning Web Application
# ====================================================

echo "=========================================="
echo "Image Captioning Web Application"
echo "=========================================="
echo ""

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Activate virtual environment
echo "Activating virtual environment..."
source "$SCRIPT_DIR/.venv/bin/activate"

# Check if requirements are installed
echo "Checking dependencies..."

# Just start the app - Python will tell us if something is missing
echo "✓ Virtual environment activated"
echo ""
echo "Starting the application..."
echo "=========================================="
echo "Note: SSL verification is disabled for educational purposes."
echo "First run will download the BLIP model (~1.8GB)"
echo "This may take 2-5 minutes depending on your connection."
echo "=========================================="
echo "Once you see 'Model loaded successfully!'"
echo "Open your browser and go to: http://localhost:5000"
echo "=========================================="
echo ""

# Run the application
cd "$SCRIPT_DIR"
python app.py
