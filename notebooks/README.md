# Jupyter Notebooks for Teaching

This directory contains interactive Jupyter notebooks designed for teaching AI and Python concepts using the Image Captioning application.

## 📚 Notebooks

### 1. `student_notebook.ipynb` - For Students

**Purpose**: Interactive learning experience with hands-on exercises

**Contents**:
- Introduction to the modular code structure
- Step-by-step walkthrough of each module
- 5 progressive exercises with increasing difficulty
- Visual examples and explanations

**Exercises**:
1. **Exercise 1**: Load and caption an image from URL
2. **Exercise 2**: Image file validation
3. **Exercise 3**: Image resizing pipeline with error handling
4. **Exercise 4**: Caption analysis and word frequency counting
5. **Exercise 5**: Build a complete caption gallery system

**Learning Objectives**:
- Understanding AI model loading and inference
- Image processing with PIL
- Error handling and validation
- Batch processing for efficiency
- Building modular, reusable code

---

### 2. `teacher_notebook.ipynb` - For Teachers

**Purpose**: Complete solutions and teaching guide

**Contents**:
- All exercise solutions with detailed explanations
- Alternative solution approaches
- Teaching tips and discussion points
- Extension ideas for advanced students
- Performance comparisons and best practices
- Assessment suggestions

**Teaching Guide Includes**:
- Pre-class preparation checklist
- In-class activity suggestions
- Common student mistakes to watch for
- Discussion prompts
- Further learning resources

---

## 🚀 Getting Started

### Prerequisites

1. **Install Jupyter**:
   ```bash
   pip install jupyter notebook
   # or
   pip install jupyterlab
   ```

2. **Download the BLIP Model** (if not already done):
   ```bash
   cd models
   git clone --progress https://huggingface.co/Salesforce/blip-image-captioning-base
   cd ..
   ```

3. **Ensure all dependencies are installed**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Register the virtual environment as a Jupyter kernel** (FIRST TIME ONLY):
   ```bash
   # Activate your virtual environment first
   source .venv/bin/activate
   
   # Register the kernel
   python -m ipykernel install --user --name=image_caption_venv --display-name="Python (image_caption_venv)"
   ```
   
   You should see: `Installed kernelspec image_caption_venv in ...`

### Running the Notebooks

**⚠️ Important**: 
1. The notebooks include a setup cell that automatically adds the project root to the Python path
2. **You MUST select the correct Python kernel**: `Python (image_caption_venv)`
3. If matplotlib or other packages are missing, you're using the wrong kernel!

#### Option 1: Jupyter Notebook (Classic) - **Recommended**
```bash
# MUST run from project root directory
cd /path/to/image_caption_1cpu_ver2
source .venv/bin/activate  # Activate virtual environment
jupyter notebook notebooks/student_notebook.ipynb
```

**Then in Jupyter:**
1. Menu: `Kernel` → `Change Kernel` → `Python (image_caption_venv)` ⚠️
2. Run cells from top to bottom

#### Option 2: JupyterLab - **Recommended**
```bash
# MUST run from project root directory
cd /path/to/image_caption_1cpu_ver2
source .venv/bin/activate  # Activate virtual environment
jupyter lab
# Then navigate to notebooks/ in the JupyterLab interface
```

**Then in JupyterLab:**
1. Click the kernel name in the top-right corner
2. Select `Python (image_caption_venv)` ⚠️
3. Run cells from top to bottom

#### Option 3: VS Code
1. Install the Jupyter extension in VS Code
2. Open the project root folder in VS Code
3. Open the notebook file
4. **Click "Select Kernel" in top-right** → Choose `Python (image_caption_venv)` ⚠️
5. Run cells from top to bottom

**📍 Critical Requirements**: 
- Always run Jupyter from the **project root** directory
- Always select the **correct kernel**: `Python (image_caption_venv)`
- The first code cell sets up the Python path automatically
- If you see "No module named 'matplotlib'" → wrong kernel!

---

## 📖 How to Use

### For Students:

1. **Start with the student notebook**: `student_notebook.ipynb`
2. **Read through Parts 1-6** to understand the concepts
3. **Work through the exercises** one at a time
4. **Try to solve them yourself** before checking solutions
5. **Run the code cells** to see results
6. **Experiment** with different parameters and images

**Tips**:
- **CRITICAL**: Select `Python (image_caption_venv)` kernel before running cells!
- **IMPORTANT**: Run the first setup cell before any other cells!
- Execute cells in order (top to bottom)
- Read all comments and documentation
- Try breaking the code to understand error messages
- Use `Shift+Enter` to run cells
- Use `Tab` for autocomplete
- Use `Shift+Tab` to see function documentation
- If you get "ModuleNotFoundError: No module named 'matplotlib'" → wrong kernel!
- If you get "ModuleNotFoundError: No module named 'modules'" → run setup cell first!

### For Teachers:

1. **Review the teacher notebook** before class
2. **Test all examples** in your environment
3. **Prepare additional examples** if needed
4. **Walk through Parts 1-6** with students
5. **Give students time** for exercises (10-15 min each)
6. **Discuss solutions** as a class
7. **Encourage pair programming**

**Teaching Workflow**:
```
1. Introduction (5 min)
   - Overview of AI image captioning
   - Module structure explanation

2. Part 1-2: Setup and Model Loading (10 min)
   - Import modules
   - Load BLIP model
   - Discuss model parameters

3. Part 3-4: Images and Captions (15 min)
   - Load images
   - Generate captions
   - Show examples

4. Part 5-6: Advanced Features (10 min)
   - Caption variations
   - Batch processing

5. Exercises (60-90 min)
   - Students work individually or in pairs
   - Teacher circulates and helps
   - Discussion after each exercise

6. Wrap-up (10 min)
   - Review key concepts
   - Next steps
   - Q&A
```

---

## 📊 Exercise Difficulty Levels

| Exercise | Difficulty | Time | Key Concepts |
|----------|-----------|------|--------------|
| 1 | ⭐ Easy | 10 min | Function calls, basic plotting |
| 2 | ⭐⭐ Medium | 15 min | Dictionary comprehension, validation |
| 3 | ⭐⭐ Medium | 15 min | Error handling, function composition |
| 4 | ⭐⭐⭐ Advanced | 20 min | Text processing, Counter, filtering |
| 5 | ⭐⭐⭐ Advanced | 30 min | File I/O, batch processing, visualization |

---

## 🔧 Troubleshooting

### Issue 1: "ModuleNotFoundError: No module named 'modules'"

**This is the most common issue!**

**Solution 1** (Recommended): Run Jupyter from the project root
```bash
cd /path/to/image_caption_1cpu_ver2
jupyter notebook notebooks/student_notebook.ipynb
```

**Solution 2**: Make sure the first setup cell runs successfully
- The first code cell in both notebooks adds the project root to Python path
- **You must run this cell first** before any imports
- If you get an error, restart the kernel and run cells in order

**Solution 3**: Manually add the path (if above doesn't work)
```python
import sys
import os
# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.getcwd()))
```

### Issue 2: "ModuleNotFoundError: No module named 'matplotlib'" or "No module named 'PIL'"

**This means you're using the WRONG Python kernel!**

**Solution**: Switch to the correct kernel
1. **Check current kernel**: Look at the top-right corner of your notebook
   - If it says "Python 3" or anything other than "Python (image_caption_venv)", you need to switch!

2. **Switch the kernel**:
   - **Jupyter Notebook**: Menu → `Kernel` → `Change Kernel` → `Python (image_caption_venv)`
   - **JupyterLab**: Click the kernel name in top-right → Select `Python (image_caption_venv)`
   - **VS Code**: Click "Select Kernel" button → Choose `Python (image_caption_venv)`

3. **Restart the kernel**: Menu → `Kernel` → `Restart Kernel`

4. **Run all cells again** from the top

**If you don't see `Python (image_caption_venv)` in the kernel list:**
```bash
cd /path/to/image_caption_1cpu_ver2
source .venv/bin/activate
python -m ipykernel install --user --name=image_caption_venv --display-name="Python (image_caption_venv)"
```
Then restart Jupyter and you'll see the kernel in the list.

### Issue 3: "Model not found" error
**Solution**: Download the BLIP model first (see Prerequisites above)

### Issue 4: Plots not showing
**Solution**: Add this at the beginning of your notebook:
```python
%matplotlib inline
```

### Issue 5: Kernel crashes
**Solution**: 
- Restart the kernel: `Kernel > Restart`
- Close other applications to free up RAM
- The BLIP model needs ~800MB-1GB RAM

### Issue 6: Images not loading from URL
**Solution**:
- Check your internet connection
- Try a different image URL
- Some URLs may block automated requests

### Issue 7: Jupyter not found
**Solution**: Install Jupyter
```bash
pip install jupyter matplotlib
# or
pip install -r requirements.txt
```

---

## 🎯 Learning Outcomes

After completing these notebooks, students will be able to:

✅ Load and use pre-trained AI models  
✅ Process images using PIL  
✅ Generate AI captions for images  
✅ Handle errors gracefully  
✅ Work with Python modules  
✅ Use list/dict comprehensions  
✅ Implement batch processing  
✅ Visualize results with matplotlib  
✅ Read and write files  
✅ Understand basic NLP concepts  

---

## 📚 Additional Resources

### Documentation:
- [BLIP Model Paper](https://arxiv.org/abs/2201.12086)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/)
- [PIL/Pillow](https://pillow.readthedocs.io/)
- [Jupyter Notebook Tutorial](https://jupyter-notebook.readthedocs.io/)

### Related Notebooks:
- Try modifying the exercises
- Create your own exercises
- Combine with the Flask web app (`../app.py`)

### Extension Projects:
1. Add support for video frames
2. Build a caption comparison tool
3. Create a multilingual version
4. Integrate with other AI models
5. Build a caption-to-image search

---

## 📝 Notebook Best Practices

### For Students:
- Save your work frequently (`Ctrl+S` or `Cmd+S`)
- Add your own notes in markdown cells
- Experiment with the code
- Don't be afraid to break things!

### For Teachers:
- Make a copy before each class
- Add your own examples
- Customize for your curriculum
- Share student solutions (with permission)

---

## 🤝 Contributing

Have ideas for new exercises or improvements?
- Add them to the notebooks
- Share with other teachers
- Submit pull requests to the repository

---

## 📧 Support

For questions or issues:
1. Check the main [README.md](../README.md)
2. Review [SETUP.md](../SETUP.md)
3. Look at the module source code in `../modules/`
4. Check the troubleshooting section above

---

**Happy Learning! 🎓**

*These notebooks are designed to be educational and beginner-friendly. Feel free to modify them for your specific teaching needs!*
