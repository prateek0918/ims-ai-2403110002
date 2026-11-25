
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

True 36858.4

import cadquery as cq
from cadquery import func as cf
from google.colab import files

plate = cf.box(80, 50, 10)
hole = cf.cylinder(d=20, h=10).moved(x=20)
part = plate - hole

print(part.isValid(), round(part.Volume(), 1))

filename = "plate_shifted.stl"
cq.exporters.export(part, filename)
files.download(filename)

True 36858.4