
import math
from itertools import product
from cadquery import func as cf

def clutch_brick(length, width, height, stud_d, stud_h, spacing, cols=4, rows=2):
    body = cf.box(length, width, height)
    stud = cf.cylinder(d=stud_d, h=stud_h)

    # Center the grid around (0, 0) on the top face (z=height)
    x_offsets = [(c - (cols - 1) / 2) * spacing for c in range(cols)]
    y_offsets = [(r - (rows - 1) / 2) * spacing for r in range(rows)]

    for x, y in product(x_offsets, y_offsets):
        body += stud.moved(x=x, y=y, z=height)

    return body

# Standard 2x4 brick dimensions (spacing = 8.0 mm; length = 4*8 - 0.2 = 31.8, width = 2*8 - 0.2 = 15.8)
length, width, height = 31.8, 15.8, 9.6
stud_d, stud_h, spacing = 4.8, 1.7, 8.0
cols, rows = 4, 2

brick = clutch_brick(length, width, height, stud_d, stud_h, spacing, cols, rows)

# Task 2: Updated volume check for (cols * rows) = 8 studs
num_studs = cols * rows
expected = (length * width * height) + num_studs * (math.pi * (stud_d / 2) ** 2 * stud_h)
assert abs(brick.Volume() - expected) < 0.5

brick.exportStl("brick.stl")

True
```
