
from dataclasses import dataclass
from cadquery import func as cf


@dataclass
class CellSpec:
    r_cell: float
    h_cell: float


def make_cell(spec):
    return cf.cylinder(d=2 * spec.r_cell, h=spec.h_cell)


def tray(spec, n=3, clearance=0.3, wall=4.0, thickness=6.0, depth=3.0):
    pocket_r = spec.r_cell + clearance
    pitch = 2 * pocket_r + wall
    plate = cf.box(n * pitch + wall, 2 * pocket_r + 2 * wall, thickness)
    pocket = cf.cylinder(d=2 * pocket_r, h=depth + 1).moved(z=thickness - depth)
    for i in range(n):
        plate = plate - pocket.moved(x=(i - (n - 1) / 2) * pitch)
    return plate


def tray_2row(spec, n=3, rows=2, clearance=0.3, wall=4.0, thickness=6.0, depth=3.0):
    """Build an n x rows battery tray (default: 3 x 2 = 6 pockets)."""
    pocket_r = spec.r_cell + clearance
    pitch = 2 * pocket_r + wall

    length_x = n * pitch + wall
    width_y = rows * pitch + wall

    plate = cf.box(length_x, width_y, thickness)
    pocket = cf.cylinder(d=2 * pocket_r, h=depth + 1).moved(z=thickness - depth)

    for r in range(rows):
        y_pos = (r - (rows - 1) / 2) * pitch
        for c in range(n):
            x_pos = (c - (n - 1) / 2) * pitch
            plate = plate - pocket.moved(x=x_pos, y=y_pos)

    return plate


cells = {
    "18650": CellSpec(9.0, 65.0),
    "21700": CellSpec(10.5, 70.0),
    "4680": CellSpec(23.0, 80.0),
}

if __name__ == "__main__":
    for name, spec in cells.items():
        # Single-row verification (expected: 9013.8, 11052.2, 35690.2 mm³)
        t_1row = tray(spec)
        print(f"1-row {name}: valid={t_1row.isValid()}, vol={round(t_1row.Volume(), 1)}")

        # 2-row upgrade (n=3 -> 3x2 = 6 pockets)
        t_2row = tray_2row(spec, n=3, rows=2)
        print(f"2-row {name}: valid={t_2row.isValid()}, vol={round(t_2row.Volume(), 1)}")
        t_2row.exportStl(f"tray_2row_{name}.stl")

