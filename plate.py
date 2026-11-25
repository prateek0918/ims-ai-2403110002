```py
from cadquery import func as cf
from google.colab import files

# Build the geometry
plate = cf.box(80, 50, 10)          # length, width, height (mm)
hole = cf.cylinder(d=20, h=10)      # diameter, height
part = plate - hole                 # subtract = drill!

# Validate and export
print(part.isValid(), round(part.Volume(), 1))
part.exportStl("plate.stl")

# Download the STL file to your computer
files.download("plate.stl")
```