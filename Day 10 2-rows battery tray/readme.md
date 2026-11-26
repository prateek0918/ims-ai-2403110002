# Parametric Cylindrical Battery Tray (`models.py`)


* **Challenge / Portfolio Submission:**
  > **Class 10 Challenge — Code Drop #1: The Three-Format Tray.** A parametric CadQuery script that models modular battery trays across standard cylindrical cell formats, upgraded with a symmetric 2-row ($n \times 2$) pocket matrix and real datasheet dimensions.

---

## Overview

`models.py` programmatically generates manifold 3D solid models and exports ready-to-slice `.stl` files for cylindrical battery cells. By defining cell dimensions via the `CellSpec` dataclass, tray envelopes and pocket pitches automatically scale while preserving consistent wall thickness and radial clearance.

### Supported Cell Formats

| Format | Reference Datasheet | Radius $r_{\text{cell}}$ (mm) | Diameter $D$ (mm) | Height $h_{\text{cell}}$ (mm) |
| :--- | :--- | :---: | :---: | :---: |
| **18650** | Standard Cylindrical Li-ion | `9.0` | `18.0` | `65.0` |
| **21700** | Standard Cylindrical Li-ion | `10.5` | `21.0` | `70.0` |
| **4680** | Tabless Large-Format Li-ion | `23.0` | `46.0` | `80.0` |

---

## Parametric Geometry

Given cell radius $r_{\text{cell}}$, radial clearance $c$, wall thickness $w$, plate thickness $t$, and pocket depth $d$:

* **Pocket Radius:** $r_{\text{pocket}} = r_{\text{cell}} + c$
* **Center-to-Center Pitch:** $P = 2r_{\text{pocket}} + w$
* **Tray Outer Dimensions ($n$ columns $\times$ $m$ rows):**
  $$L_x = n \cdot P + w, \quad W_y = m \cdot P + w$$
* **Expected Solid Volume:**
  $$V = (L_x \cdot W_y \cdot t) - \left(n \cdot m \cdot \pi \cdot r_{\text{pocket}}^2 \cdot d\right)$$

---

## Getting Started

### Prerequisites

Install CadQuery in your Python environment:

```bash
pip install cadquery
```

### Usage

Run `models.py` directly to validate geometry and export STL meshes:

```bash
python models.py
```

### Expected Verification Output (`n=3`, `clearance=0.3`, `wall=4.0`, `thickness=6.0`, `depth=3.0`)

| Format | 1×3 Single-Row Volume ($\text{mm}^3$) | 3×2 Dual-Row Volume ($\text{mm}^3$) | Valid Solid |
| :--- | :---: | :---: | :---: |
| **18650** | `9013.8` | `16304.2` | `True` |
| **21700** | `11052.2` | `20165.6` | `True` |
| **4680** | `35690.2` | `67996.4` | `True` |

---

## Repository Structure

```text
models.py          # Parametric CellSpec definitions, tray(), and tray_2row() builders
README.md          # Project documentation and verification reference
tray_18650.stl     # Generated 3D printable STL meshes
tray_21700.stl     # Generated 3D printable STL meshes
tray_4680.stl      # Generated 3D printable STL meshes
