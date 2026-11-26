# 🧱 CadQuery Parametric CAD Challenges

A collection of parametric 3D modeling exercises built using Python and [CadQuery](https://cadquery.readthedocs.io/). These mini-projects demonstrate constructive solid geometry (CSG) boolean operations, coordinate transformations, parametric grid generation, and analytical volume verification.

---

## 📌 Table of Contents
1. [Challenge 1: Parametric Plate with Offset Bore](#challenge-1-parametric-plate-with-offset-bore)
2. [Day 8 Challenge: Parametric 2×4 Clutch Brick](#day-8-challenge-parametric-2x4-clutch-brick)
3. [Setup & Installation](#setup--installation)

---

## 🐍 Challenge 1: Parametric Plate with Offset Bore

### Description
An introductory Constructive Solid Geometry (CSG) exercise demonstrating primitive creation (`box`, `cylinder`), spatial translation (`.moved()`), and boolean subtraction (`-`). The script models a rectangular mounting plate (`80 × 50 × 10 mm`) with a through-hole (`Ø20 mm`) offset `20 mm` along the X-axis, followed by automated geometry validation and STL export.

### Key Concepts
- **Boolean Subtraction:** Drilling features by subtracting tool solids from base primitives.
- **Translation Invariance:** Verifying that translating an internal feature within solid boundaries preserves the net volume:
  $$V_{\text{net}} = (L \times W \times H) - \left(\pi r^2 h\right) = 40000 - 3141.59 = 36858.4\text{ mm}^3$$
- **Automated Verification:** Programmatically checking B-Rep manifold validity (`isValid()`) and comparing computed volume against analytical hand calculations.

### Code
```python
from cadquery import func as cf

# Define base plate and offset cylindrical bore (mm)
plate = cf.box(80, 50, 10)
hole = cf.cylinder(d=20, h=10).moved(x=20)

# Perform boolean subtraction
part = plate - hole

# Validate geometry and export STL
print(part.isValid(), round(part.Volume(), 1))  # Output: True 36858.4
part.exportStl("plate.stl")
```

---

## 🧱 Day 8 Challenge: Parametric 2×4 Clutch Brick

### Description
A fully parametric toy brick generator built with Python and CadQuery. Instead of manually positioning individual features, this script uses nested coordinate loops to dynamically generate a centered $N_x \times N_y$ grid of cylindrical studs (`2 × 4` = 8 studs) fused onto the top face of a rectangular brick body, complete with an automated volume assertion test.

### Key Concepts
- **Parametric Grid Generation:** Computing centered 2D pitch coordinates dynamically from stud counts (`nx`, `ny`) and pitch (`spacing`).
- **Boolean Union (`+`):** Fusing multiple translated stud primitives onto a base solid into a single valid manifold part.
- **Unit Testing for CAD:** Using `assert` statements to verify that the generated 3D solid's volume matches the theoretical formula within floating-point tolerance:
  $$V_{\text{total}} = (L \times W \times H) + (N_x \cdot N_y) \left(\pi \left(\frac{d_{\text{stud}}}{2}\right)^2 h_{\text{stud}}\right)$$

### Code
```python
import math
from cadquery import func as cf

def clutch_brick(length, width, height, stud_d, stud_h, spacing, nx=4, ny=2):
    solid = cf.box(length, width, height)
    stud_template = cf.cylinder(d=stud_d, h=stud_h)

    for i in range(nx):
        for j in range(ny):
            dx = (i - (nx - 1) / 2) * spacing
            dy = (j - (ny - 1) / 2) * spacing
            solid = solid + stud_template.moved(x=dx, y=dy, z=height)

    return solid

# Standard 2x4 brick dimensions (mm)
length, width, height = 31.8, 15.8, 9.6
stud_d, stud_h, spacing = 4.8, 1.7, 8.0
nx, ny = 4, 2

brick = clutch_brick(length, width, height, stud_d, stud_h, spacing, nx=nx, ny=ny)

# Analytical volume verification
expected = (length * width * height) + (nx * ny) * math.pi * (stud_d / 2) ** 2 * stud_h
assert brick.isValid()
assert abs(brick.Volume() - expected) < 0.5

brick.exportStl("brick.stl")
```

---

## ⚙️ Setup & Installation

1. **Install CadQuery:**
   ```bash
   pip install cadquery
   ```
2. **Run a script to generate the `.stl` mesh:**
   ```bash
   python clutch_brick.py
   ```
3. **Inspect the output:** Open `plate.stl` or `brick.stl` in any STL viewer, slicer (PrusaSlicer, Cura), or directly inside VS Code using the `ocp_vscode` extension (`show(brick)`).




