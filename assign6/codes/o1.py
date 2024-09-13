import sys                                          # For path to external scripts
sys.path.insert(0, '/home/eshan/matgeo/codes/CoordGeo')  # Path to my scripts
import numpy as np
import matplotlib.pyplot as plt

# Local imports
from line.funcs import line_gen

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

# Flatten the array if necessary
if points.ndim == 3:
    points = points.reshape(-1, 2)

# Extracting points A, O, B, and C
A, O, B, C = points[0], points[1], points[2], points[3]

# Generating all lines
x_AB = line_gen(A, B)
x_AO = line_gen(A, O)
x_CO = line_gen(C, O)
x_AC = line_gen(A, C)
x_OB = line_gen(O, B)
x_BC = line_gen(B, C)

# Plotting lines without labels
plt.plot(x_BC[0, :], x_BC[1, :], 'r--')  # Line BC
plt.plot(x_AC[0, :], x_AC[1, :], 'r--')  # Line AC
plt.plot(x_AB[0, :], x_AB[1, :])          # Line AB
plt.plot(x_AO[0, :], x_AO[1, :])          # Line AO
plt.plot(x_CO[0, :], x_CO[1, :], 'r--')  # Line CO
plt.plot(x_OB[0, :], x_OB[1, :])          # Line OB

# Plotting points
plt.scatter(points[:, 0], points[:, 1], c='k')  # Plot points in black for visibility

# Annotate the vertices
plt.annotate('A', A, textcoords="offset points", xytext=(-10, 10), ha='center')
plt.annotate('O', O, textcoords="offset points", xytext=(-10, 10), ha='center')
plt.annotate('B', B, textcoords="offset points", xytext=(-10, 10), ha='center')
plt.annotate('C', C, textcoords="offset points", xytext=(-10, 10), ha='center')

# Add dummy plots for the legend
plt.scatter([], [], c='k', label='Point A(0,-3)')
plt.scatter([], [], c='k', label='Point O(0,0)')
plt.scatter([], [], c='k', label='Point B(4,0)')
plt.scatter([], [], c='k', label='Point C(4,-3)')

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

