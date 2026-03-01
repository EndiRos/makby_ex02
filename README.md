Technical Report: Spatial Mapping of Rectilinear Patterns

Candidate: Endika

Submission Date: 02.03.2026

Tools Used: Gemini 3 Flash (Assistance in mathematical derivation and visualization).

## 1. Introduction

The objective of this study is to define the geometric transformations necessary to project a rectilinear pattern, defined in a template of dimensions W×H, onto two distinct topologies: a 2D circular ring and a 3D cylinder. This process is fundamental in tissue engineering to adapt flat scaffolds to curved anatomical geometries.

## 2. Part A: 2D Circular Mapping (Ring)

It is required to transform the Cartesian plane (x,y) into a polar coordinate system (r,θ), where the x-axis controls the angular advance and the y-axis controls the radius.

### Equation Derivation

To ensure complete coverage of 360° (2π radians):

- **Angular Variable:** θ = (x/W) · 2π

- **Radial Variable:** r = R_in + y (where R_in is the inner radius of the ring)

**Transformation to Cartesian Coordinates (x′,y′):**

x′ = (R_in + y) · cos((2πx)/W)

y′ = (R_in + y) · sin((2πx)/W)

### Corner Coordinates

For a template with W=10, H=5, and R_in=2:

- (0, 0): (2·cos(0), 2·sin(0)) = (2, 0)
- (W, 0): (2·cos(2π), 2·sin(2π)) = (2, 0)
- (W, H): (7·cos(2π), 7·sin(2π)) = (7, 0)
- (0, H): (7·cos(0), 7·sin(0)) = (7, 0)

## 3. Part B: 3D Cylindrical Mapping

The template is projected onto the surface of a cylinder with radius R. The x-axis becomes the circumferential arc length and the y-axis becomes the height z.

### Equation Derivation

- **Phase Angle:** ϕ = x/R
- **Height:** z = y

**General Transformation Function:**

x′ = R · cos(x/R)

y′ = R · sin(x/R)

z′ = y

### Corner Coordinates (Case W=2πR)

When the width equals the perimeter, the pattern closes perfectly:

- (0, 0): (R, 0, 0)
- (W, 0): (R, 0, 0)
- (W, H): (R, 0, H)
- (0, H): (R, 0, H)

## 4. Reasoning and Resolution Process

My approach to this problem was based on the following points:

- **Topological Continuity:** I selected transformations that ensure the points x=0 and x=W coincide in the transformed space. This allows complex patterns (such as honeycomb) to present no seams or visual jumps.

- **Scalability:** The proposed equations are parametric; they allow adjusting the inner radius or cylinder radius according to specific biomodel requirements without changing the algorithm logic.

- **Visual Validation:** A Python script was developed using the matplotlib library to verify that the grid deformation was coherent with the expected differential geometry.

## 5. Citations and References

- **AI Used:** Gemini 3 Flash
- **Prompts:**
  1. "Derive the transformation equations to map a WxH rectangle to a ring and a cylinder."
  2. "Generate a Python script with Matplotlib to visualize a rectangular grid transformed into a 2D ring and a 3D cylinder."
  3. "Explain the utility of these transformations in the design of cartilage biomodels."
