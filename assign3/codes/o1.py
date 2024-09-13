import sys
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex

# Add path to external scripts (if needed)
sys.path.insert(0, '/home/eshan/matgeo/codes/CoordGeo')

# Local imports (make sure these modules exist in your environment)
from line.funcs import line_gen
from triangle.funcs import *
from conics.funcs import circ_gen

# Function to read points from a file
def read_points_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        B = np.array([float(x) for x in lines[0].strip().split()]).reshape(-1, 1)
        A = np.array([float(x) for x in lines[1].strip().split()]).reshape(-1, 1)
    return B, A

# Read points A and B from file
B, A = read_points_from_file('output')

# Ratio for calculating C
n = 1.5

# Compute the position vector of point C
C = B + n * (A - B)

# Print the computed position vector of C
print(f"Position vector of C: {C.flatten()}")

# Generate line segments
x_AB = line_gen(A, B)
x_AC = line_gen(A, C)

# Plotting the lines
plt.plot(x_AB[0, :], x_AB[1, :], label='$AB$')
plt.plot(x_AC[0, :], x_AC[1, :], 'r--', label='$AC$')

# Plotting points
tri_coords = np.block([[B, A, C]])
plt.scatter(tri_coords[0, :], tri_coords[1, :])

# Annotating points without using a for loop
plt.text(tri_coords[0, 0], tri_coords[1, 0], f'B\n({tri_coords[0, 0]:.0f}, {tri_coords[1, 0]:.0f})',
         fontsize=9, ha='center', va='center')
plt.text(tri_coords[0, 1], tri_coords[1, 1], f'A\n({tri_coords[0, 1]:.0f}, {tri_coords[1, 1]:.0f})',
         fontsize=9, ha='center', va='center')
plt.text(tri_coords[0, 2], tri_coords[1, 2], f'C\n({tri_coords[0, 2]:.0f}, {tri_coords[1, 2]:.0f})',
         fontsize=9, ha='center', va='center')

# Customize the plot
ax = plt.gca()
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.legend(loc='best')
plt.grid(True)
plt.axis('equal')
plt.savefig('../plots/plot.png', format='png', bbox_inches='tight')
plt.show()
