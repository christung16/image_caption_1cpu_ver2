# 📓 Jupyter Notebooks - Quick Start Guide

## 🚀 How to Start the Notebooks

### Step 1: Make sure you're in the project root directory
```bash
cd /path/to/image_caption_1cpu_ver2
pwd  # Should show: /path/to/image_caption_1cpu_ver2
```

### Step 2: Activate virtual environment (if using one)
```bash
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate     # Windows
```

### Step 3: Start Jupyter Notebook
```bash
# Option A: Classic Notebook (Recommended for beginners)
jupyter notebook notebooks/student_notebook.ipynb

# Option B: JupyterLab (More features)
jupyter lab
# Then navigate to notebooks/ folder in the interface
```

---

## ⚠️ IMPORTANT: Run Cells in Order!

**The first code cell is critical!** It sets up the Python path so the notebooks can find the `modules` package.

### Correct Order:
1. ✅ **Run Setup Cell** (First code cell - adds project root to path)
2. ✅ **Run Import Cell** (Imports all modules)
3. ✅ **Run remaining cells** in order from top to bottom

### What NOT to Do:
- ❌ Don't skip the first setup cell
- ❌ Don't run cells out of order
- ❌ Don't start Jupyter from the notebooks/ directory

---

## 🐛 Troubleshooting

### Problem: `ModuleNotFoundError: No module named 'modules'`

**Solution**: You forgot to run the setup cell! 
1. Go to the first code cell in the notebook
2. Run it (Shift+Enter)
3. You should see: `✓ Project root added to path: /path/to/project`
4. Now run the import cell

### Problem: Setup cell doesn't help

**Solution**: Restart kernel and start from project root
1. Close the notebook
2. Make sure you're in the project root: `pwd`
3. Start Jupyter again: `jupyter notebook notebooks/student_notebook.ipynb`
4. In Jupyter: `Kernel > Restart & Clear Output`
5. Run cells from top to bottom

---

## 📚 Notebook Overview

### `student_notebook.ipynb` - For Learning
- **5 hands-on exercises** (Easy → Advanced)
- Learn by doing
- Complete the exercises yourself
- Hints provided for each exercise

### `teacher_notebook.ipynb` - Solutions & Teaching Guide
- Complete solutions to all exercises
- Teaching tips and discussion points
- Common mistakes to watch for
- Extension ideas for advanced students

---

## ⌨️ Useful Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Shift+Enter` | Run current cell and move to next |
| `Ctrl+Enter` | Run current cell and stay |
| `A` | Insert cell above (in command mode) |
| `B` | Insert cell below (in command mode) |
| `D D` | Delete cell (press D twice) |
| `M` | Convert cell to Markdown |
| `Y` | Convert cell to Code |
| `Tab` | Autocomplete |
| `Shift+Tab` | Show function help |

**Tip**: Press `Esc` to enter command mode, `Enter` to enter edit mode

---

## 🎯 Exercise Time Estimates

| Exercise | Difficulty | Time | What You'll Build |
|----------|-----------|------|-------------------|
| Exercise 1 | ⭐ Easy | 10 min | Load image from URL and display caption |
| Exercise 2 | ⭐⭐ Medium | 15 min | Validate multiple image files |
| Exercise 3 | ⭐⭐ Medium | 15 min | Resize images with error handling |
| Exercise 4 | ⭐⭐⭐ Advanced | 20 min | Analyze caption text (word frequency) |
| Exercise 5 | ⭐⭐⭐ Advanced | 30 min | Build complete caption gallery system |

**Total Time**: ~90-120 minutes for all exercises

---

## 💡 Tips for Success

1. **Read before you code**: Read the exercise description carefully
2. **Use the hints**: Each exercise has hints to guide you
3. **Test as you go**: Run cells frequently to check your work
4. **Don't be afraid to break things**: Errors are learning opportunities!
5. **Ask for help**: If stuck for >10 minutes, check the teacher notebook or ask
6. **Experiment**: Try modifying the code to see what happens

---

## 🎓 Learning Path

### For Students:
1. Start with `student_notebook.ipynb`
2. Complete exercises 1-3 first (easier)
3. Take a break!
4. Complete exercises 4-5 (advanced)
5. Check your solutions against `teacher_notebook.ipynb`
6. Try the extension ideas

### For Teachers:
1. Review `teacher_notebook.ipynb` before class
2. Test all examples in your environment
3. Prepare to walk through the setup together
4. Give students 10-15 minutes per exercise
5. Discuss solutions as a class
6. Encourage pair programming

---

## 📞 Need Help?

Check the detailed troubleshooting guide in:
- `notebooks/README.md` - Full documentation
- `README.md` - Project overview
- `SETUP.md` - Installation guide

---

## ✅ Checklist Before Starting

- [ ] BLIP model downloaded to `models/blip-image-captioning-base/`
- [ ] All requirements installed (`pip install -r requirements.txt`)
- [ ] Virtual environment activated (optional but recommended)
- [ ] Currently in project root directory (use `pwd` to check)
- [ ] Jupyter installed (`jupyter --version` to check)

**Ready?** Run: `jupyter notebook notebooks/student_notebook.ipynb`

Happy Learning! 🚀
