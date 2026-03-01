"""
Spatial Mapping of Rectilinear Patterns
Visualizes the transformation of rectangular grids to:
1. 2D Circular Ring
2. 3D Cylinder
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def create_rectangular_grid(W, H, nx=20, ny=10):
    """
    Create a rectangular grid of points.
    
    Parameters:
    - W: Width of the template
    - H: Height of the template
    - nx: Number of points along x-axis
    - ny: Number of points along y-axis
    
    Returns:
    - x, y: Meshgrid coordinates
    """
    x = np.linspace(0, W, nx)
    y = np.linspace(0, H, ny)
    return np.meshgrid(x, y)


def transform_to_ring(x, y, W, R_in):
    """
    Transform rectangular coordinates to 2D circular ring.
    
    Parameters:
    - x, y: Input rectangular coordinates
    - W: Width of the template
    - R_in: Inner radius of the ring
    
    Returns:
    - x_prime, y_prime: Transformed coordinates
    """
    theta = (2 * np.pi * x) / W
    x_prime = (R_in + y) * np.cos(theta)
    y_prime = (R_in + y) * np.sin(theta)
    return x_prime, y_prime


def transform_to_cylinder(x, y, R):
    """
    Transform rectangular coordinates to 3D cylinder surface.
    
    Parameters:
    - x, y: Input rectangular coordinates
    - R: Radius of the cylinder
    
    Returns:
    - x_prime, y_prime, z_prime: Transformed 3D coordinates
    """
    phi = x / R
    x_prime = R * np.cos(phi)
    y_prime = R * np.sin(phi)
    z_prime = y
    return x_prime, y_prime, z_prime


def visualize_transformations(W=10, H=5, R_in=2, R_cylinder=3):
    """
    Create visualizations of both transformations.
    
    Parameters:
    - W: Template width
    - H: Template height
    - R_in: Inner radius for ring transformation
    - R_cylinder: Radius for cylinder transformation
    """
    # Create rectangular grid
    x, y = create_rectangular_grid(W, H, nx=30, ny=15)
    
    # Create figure with subplots
    fig = plt.figure(figsize=(18, 6))
    
    # 1. Original rectangular grid
    ax1 = fig.add_subplot(131)
    ax1.plot(x, y, 'b-', linewidth=0.5, alpha=0.6)
    ax1.plot(x.T, y.T, 'b-', linewidth=0.5, alpha=0.6)
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title('Original Rectangular Grid')
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)
    
    # Mark corners
    corners = [(0, 0), (W, 0), (W, H), (0, H)]
    for i, (cx, cy) in enumerate(corners):
        ax1.plot(cx, cy, 'ro', markersize=8)
        ax1.text(cx, cy, f'  P{i}', fontsize=10, color='red')
    
    # 2. Circular ring transformation
    ax2 = fig.add_subplot(132)
    x_ring, y_ring = transform_to_ring(x, y, W, R_in)
    ax2.plot(x_ring, y_ring, 'g-', linewidth=0.5, alpha=0.6)
    ax2.plot(x_ring.T, y_ring.T, 'g-', linewidth=0.5, alpha=0.6)
    ax2.set_xlabel('x\'')
    ax2.set_ylabel('y\'')
    ax2.set_title(f'2D Circular Ring (R_in={R_in})')
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.3)
    
    # Mark transformed corners
    corner_coords = [(0, 0), (W, 0), (W, H), (0, H)]
    for i, (cx, cy) in enumerate(corner_coords):
        cx_t, cy_t = transform_to_ring(np.array([[cx]]), np.array([[cy]]), W, R_in)
        ax2.plot(cx_t[0, 0], cy_t[0, 0], 'ro', markersize=8)
    
    # 3. Cylindrical transformation
    ax3 = fig.add_subplot(133, projection='3d')
    x_cyl, y_cyl, z_cyl = transform_to_cylinder(x, y, R_cylinder)
    ax3.plot_surface(x_cyl, y_cyl, z_cyl, alpha=0.7, cmap='viridis', 
                     edgecolor='k', linewidth=0.3)
    
    # Plot grid lines
    for i in range(x_cyl.shape[0]):
        ax3.plot(x_cyl[i, :], y_cyl[i, :], z_cyl[i, :], 'b-', linewidth=0.5, alpha=0.6)
    for j in range(x_cyl.shape[1]):
        ax3.plot(x_cyl[:, j], y_cyl[:, j], z_cyl[:, j], 'b-', linewidth=0.5, alpha=0.6)
    
    ax3.set_xlabel('x\'')
    ax3.set_ylabel('y\'')
    ax3.set_zlabel('z\'')
    ax3.set_title(f'3D Cylinder (R={R_cylinder})')
    
    # Set equal aspect ratio for cylindrical visualization
    ax3.set_box_aspect([1, 1, H/R_cylinder])  # Proper aspect ratio
    max_range = max(R_cylinder, H/2)
    ax3.set_xlim([-R_cylinder, R_cylinder])
    ax3.set_ylim([-R_cylinder, R_cylinder])
    ax3.set_zlim([0, H])
    ax3.view_init(elev=20, azim=45)  # Better viewing angle
    
    # Mark transformed corners in 3D
    for i, (cx, cy) in enumerate(corner_coords):
        cx_t, cy_t, cz_t = transform_to_cylinder(np.array([[cx]]), np.array([[cy]]), R_cylinder)
        ax3.scatter(cx_t[0, 0], cy_t[0, 0], cz_t[0, 0], c='red', s=50)
    
    plt.tight_layout()
    plt.savefig('pattern_transformations.png', dpi=300, bbox_inches='tight')
    print("Visualization saved as 'pattern_transformations.png'")
    plt.show()


def print_corner_coordinates(W=10, H=5, R_in=2, R_cylinder=3):
    """
    Print the transformed coordinates of the template corners.
    """
    corners = [(0, 0), (W, 0), (W, H), (0, H)]
    
    print("\n" + "="*60)
    print("CORNER COORDINATE TRANSFORMATIONS")
    print("="*60)
    print(f"Template dimensions: W={W}, H={H}")
    print(f"Ring inner radius: R_in={R_in}")
    print(f"Cylinder radius: R={R_cylinder}")
    print("-"*60)
    
    print("\n2D RING TRANSFORMATION:")
    print("-"*60)
    for i, (x, y) in enumerate(corners):
        x_t, y_t = transform_to_ring(np.array([[x]]), np.array([[y]]), W, R_in)
        print(f"P{i} ({x:4.1f}, {y:4.1f}) → ({x_t[0,0]:6.2f}, {y_t[0,0]:6.2f})")
    
    print("\n3D CYLINDER TRANSFORMATION:")
    print("-"*60)
    for i, (x, y) in enumerate(corners):
        x_t, y_t, z_t = transform_to_cylinder(np.array([[x]]), np.array([[y]]), R_cylinder)
        print(f"P{i} ({x:4.1f}, {y:4.1f}) → ({x_t[0,0]:6.2f}, {y_t[0,0]:6.2f}, {z_t[0,0]:6.2f})")
    
    print("="*60 + "\n")


if __name__ == "__main__":
    # Default parameters from the report
    R_cylinder = 3  # Radius for cylinder
    W = 2 * np.pi * R_cylinder  # Template width - adjusted for complete cylinder closure
    H = 5   # Template height
    R_in = 2  # Inner radius for ring
    
    print("Spatial Mapping of Rectilinear Patterns")
    print("="*60)
    print("Generating transformations...")
    print(f"\nNote: W={W}, 2πR={2*np.pi*R_cylinder:.2f}")
    if W < 2*np.pi*R_cylinder:
        print(f"The cylinder will NOT close completely.")
        print(f"Coverage: {(W/(2*np.pi*R_cylinder))*360:.1f}° of 360°")
    else:
        print("The cylinder closes completely.")
    
    # Print corner coordinates
    print_corner_coordinates(W, H, R_in, R_cylinder)
    
    # Create visualizations
    visualize_transformations(W, H, R_in, R_cylinder)
    
    print("\nTransformation complete!")
