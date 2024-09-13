import sys                                          # for path to external scripts
sys.path.insert(0, '/home/eshan/matgeo/codes/CoordGeo')        # path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

# Function to read points from a file
def read_points_from_file(filename):
    # Load the data from the file directly into a NumPy array
    points = np.loadtxt(filename)
    return points

# Read points from file
points = read_points_from_file('output.txt')

# Debugging: Print the points array and its shape
print("Points array:")
print(points)
print("Shape of points array:", points.shape)

# Ensure the points array has the correct shape
if points.ndim == 2 and points.shape[1] == 2:
    # Extracting points B, C, A
    B, C, A = points[0], points[1], points[2]
else:
    raise ValueError("Points array should be of shape (3, 2)")


# Generating line BC
x_BC = line_gen(B, C)

plt.plot(x_BC[0, :], x_BC[1, :], label='$BC$')
# Plotting points B, C, A
plt.scatter([B[0], C[0], A[0]], [B[1], C[1], A[1]], c=[1, 2, 3], label=None)
plt.text(B[0], B[1], f'B\n({B[0]:.2f}, {B[1]:.2f})', fontsize=9, ha='center', va='center')
plt.text(C[0], C[1], f'C\n({C[0]:.2f}, {C[1]:.2f})', fontsize=9, ha='center', va='center')
plt.text(A[0], A[1], f'A\n({A[0]:.2f}, {A[1]:.2f})', fontsize=9, ha='center', va='center')

# Plot vertical line through point A
plt.axvline(x=A[0], color='purple', linestyle='--', label=None)
# Add legend for point A
plt.scatter(A[0], A[1], color='blue', label='Point A')


# Customize the plot
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
plt.grid()  # minor
plt.axis('equal')
plt.legend(loc='best')
plt.savefig('../plots/plot.png', format='png', bbox_inches='tight')
