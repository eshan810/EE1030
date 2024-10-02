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
A = points[0]  # Intersection point of the curves
B = points[1]  # Intersection with x-axis

# Setting up plot with larger figure size
fig = plt.figure(figsize=(10, 8))  # Increase figure size
ax = fig.add_subplot(111, aspect='equal')

# Generate x values for the curve y = sqrt(x) and extend it to x = 10
x_curve = np.linspace(0, 10, 400)
y_curve = np.sqrt(x_curve)  # y = sqrt(x)

# Generate line points using line_gen for the line x = 2y + 3
x_line = np.linspace(0, 10, 400)
y_line = (x_line - 3) / 2

# Use line_gen to generate points for the line between A and B
line_points = line_gen(A, B)

# Plot the curves
plt.plot(x_curve, y_curve, label='$y = \\sqrt{x}$', color='r')
plt.plot(x_line, y_line, label='$y = \\frac{x - 3}{2}$', color='orange')

# Plot line using line_gen
plt.plot(line_points[0, :], line_points[1, :], linestyle='-', color='orange', label='Line between A and B')

# Mark the points of intersection
plt.scatter(*A, color='blue', label='Intersection Point A')
plt.scatter(*B, color='green', label='Intersection with X-axis B')

# Annotate the points
def annotate_point(point, label):
    plt.annotate(f'{label}\n({point[0]:.2f}, {point[1]:.2f})',
                 point,
                 textcoords="offset points",
                 xytext=(0, 10),  # Position above the point
                 ha='center',
                 fontsize=9)

annotate_point(A, 'A')
annotate_point(B, 'B')

#
# Shade the bounded area: from x=0 to x=3 between the parabola and x-axis
x_fill1 = np.linspace(0, 3, 100)
y_parabola_fill1 = np.sqrt(x_fill1)
plt.fill_between(x_fill1, y_parabola_fill1, 0, color='gray', alpha=0.5, label='Bounded Area')

# From x=3 onward, shade the area between the parabola and the line
x_fill2 = np.linspace(3, 9, 100)  # Change upper limit if needed
y_parabola_fill2 = np.sqrt(x_fill2)
y_line_fill = (x_fill2-3)/2

plt.fill_between(x_fill2, y_parabola_fill2, y_line_fill, where=(y_line_fill <= y_parabola_fill2), color='gray', alpha=0.5) 
plt.xlim(0, 10)  # Set x-axis limits
plt.ylim(-2, 5)   # Set y-axis limits

# Customize the plot appearance
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.legend(loc='best')
plt.grid()  # minor
plt.title('Area Bounded by $y = \\sqrt{x}$ and $y = \\frac{x - 3}{2}$')
plt.savefig('../plots/plot.png', format='png', bbox_inches='tight')
plt.show()

