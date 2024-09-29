import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import sys  # for path to external scripts
sys.path.insert(0, '/home/eshan/matgeo/codes/CoordGeo')  # path to my scripts

# Local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

# Function to read points from a file
def read_points_from_file(filename):
    try:
        return np.loadtxt(filename)
    except ValueError as e:
        print(f"Error reading points from file: {e}")
        sys.exit(1)

# Read points from output.txt
points = read_points_from_file('output.txt')

# Ensure points have the correct shape
if points.shape[1] != 2:
    print("The file must contain points with two coordinates each.")
    sys.exit(1)

# Given points
A = points[0]
B = points[1]

# Setting up plot with larger figure size
fig = plt.figure(figsize=(10, 8))  # Increase figure size
ax = fig.add_subplot(111, aspect='equal')
len = 100
y = np.linspace(-8, 8, len)

# Generate lines between points using line_gen
x_AB = line_gen(A, B)

# Plot all lines with different colors
plt.plot(x_AB[0, :], x_AB[1, :], linestyle='-', color='orange', label='y=x+2')
# Scatter plot for all points without labels
plt.scatter(*A, c='r')
plt.scatter(*B, c='b')

# Annotate the vertices
def annotate_point(point, label):
    plt.annotate(f'{label}\n({point[0]:.2f}, {point[1]:.2f})',
                 point,
                 textcoords="offset points",
                 xytext=(0, 10),  # Position above the point
                 ha='center',
                 fontsize=9)

annotate_point(A, 'A')
annotate_point(B, 'B')

# Conic parameters
V = np.array(([1, 0], [0, 0]))
u = (-1 / 2) * e2
f = 0

n, c, F, O, lam, P, e = conic_param(V, u, f)
flen = parab_param(lam, P, u)

# Standard parabola generation
x = parab_gen(y, flen)
xStandard = np.block([[x], [y]])

# Affine conic generation
Of = O.flatten()
xActual = P @ xStandard + Of[:, np.newaxis]

# Plotting the parabola
plt.plot(xActual[0, :], xActual[1, :], label='$x^2=y$', color='r')

# Shade the bounded region
x_fill = np.linspace(-2, 2, 100)  # Adjust based on intersection points
y_parabola = x_fill**2
y_line = x_fill + 2

# Shade the area between the curves
plt.fill_between(x_fill, y_parabola, y_line, where=(y_line >= y_parabola), color='gray', alpha=0.5, label='Bounded Area')

# Set axis limits to -5 and 5
plt.xlim(-6, 6)  # Set x-axis limits
plt.ylim(-2, 12)  # Set y-axis limits
# Customize the plot appearance
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.legend(loc='best')
plt.grid()  # minor
plt.savefig('../plots/plot.png', format='png', bbox_inches='tight')


