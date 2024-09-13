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
        A = np.array([float(x) for x in lines[0].strip().split()]).reshape(-1, 1)
        B = np.array([float(x) for x in lines[1].strip().split()]).reshape(-1, 1)
    return A, B

# Read points A and B from file
A, B = read_points_from_file('output')

# Ratio for calculating C
n = 1.5

# Compute the position vector of point C
C = A + n * (B - A)

# Print the computed position vector of C
print(f"Position vector of C: {C.flatten()}")

# Generate line segments
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)

# Plotting the lines
plt.plot(x_AB[0, :], x_AB[1, :], label='$AB$')
plt.plot(x_BC[0, :], x_BC[1, :], 'r--', label='$BC$')

# Plotting points
tri_coords = np.block([[A, B, C]])
plt.scatter(tri_coords[0, :], tri_coords[1, :])
vert_labels = ['A', 'B', 'C']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({tri_coords[0, i]:.0f}, {tri_coords[1, i]:.0f})',
                 (tri_coords[0, i], tri_coords[1, i]), 
                 textcoords="offset points",
                 xytext=(20, -10),
                 ha='center')

# Customize the plot
ax = plt.gca()
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.legend(loc='best')
plt.grid(True)
plt.axis('equal')
plt.title('Example: A(0,0) and B(10,10)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.savefig('../plots/plot.png', format='png', bbox_inches='tight')

