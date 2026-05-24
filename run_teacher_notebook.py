#!/usr/bin/env python3
"""
Script to execute the teacher notebook with all cells.
This ensures the setup cell runs first and modules are properly imported.
"""

import sys
import os

# Setup: Add project root to Python path (same as notebook setup cell)
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

print(f"✓ Project root added to path: {project_root}")
print(f"✓ Python executable: {sys.executable}")
print()

# Now import and execute the notebook
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import warnings
warnings.filterwarnings('ignore')

# Read the teacher notebook
notebook_path = 'notebooks/teacher_notebook.ipynb'
print(f"📓 Loading notebook: {notebook_path}")

with open(notebook_path, 'r') as f:
    nb = nbformat.read(f, as_version=4)

print(f"✓ Notebook loaded: {len(nb.cells)} cells found")
print()

# Configure the preprocessor
ep = ExecutePreprocessor(
    timeout=600,  # 10 minutes per cell
    kernel_name='python3',
    allow_errors=False  # Stop on errors
)

print("🚀 Executing notebook cells...")
print("=" * 70)

try:
    # Execute the notebook
    ep.preprocess(nb, {'metadata': {'path': 'notebooks/'}})
    
    print()
    print("=" * 70)
    print("✅ All cells executed successfully!")
    print()
    
    # Save the executed notebook
    output_path = 'notebooks/teacher_notebook_executed.ipynb'
    with open(output_path, 'w') as f:
        nbformat.write(nb, f)
    
    print(f"✓ Executed notebook saved to: {output_path}")
    print()
    
    # Print summary of outputs
    code_cells = [c for c in nb.cells if c.cell_type == 'code']
    cells_with_output = sum(1 for c in code_cells if c.get('outputs', []))
    
    print("📊 Execution Summary:")
    print(f"   Total cells: {len(nb.cells)}")
    print(f"   Code cells: {len(code_cells)}")
    print(f"   Cells with output: {cells_with_output}")
    print()
    
    # Check for any errors in outputs
    errors = []
    for i, cell in enumerate(code_cells):
        for output in cell.get('outputs', []):
            if output.get('output_type') == 'error':
                errors.append((i, output.get('ename'), output.get('evalue')))
    
    if errors:
        print("⚠️  Errors found in output:")
        for i, ename, evalue in errors:
            print(f"   Cell {i}: {ename}: {evalue}")
    else:
        print("✅ No errors in output!")
    
    print()
    print("🎉 Teacher notebook execution complete!")
    
except Exception as e:
    print()
    print("=" * 70)
    print(f"❌ Error during execution: {type(e).__name__}")
    print(f"   {str(e)}")
    print()
    print("💡 Common issues:")
    print("   - BLIP model not downloaded")
    print("   - Sample images missing")
    print("   - Insufficient memory")
    print()
    sys.exit(1)
