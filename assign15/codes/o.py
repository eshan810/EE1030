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
C = points[2]
D = points[3]
q = points[4]
# Setting up the plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
num = 100
y = np.linspace(-2, 2, num)

# Generate lines between points using line_gen
x_AB = line_gen(A, B)
x_CD = line_gen(C, D)

# Extend the lines AB and CD
def extend_line(point1, point2, factor=2):
    direction = point2 - point1
    extended_start = point1 - factor * direction
    extended_end = point2 + factor * direction
    return np.array([extended_start, extended_end])
    


# Extend lines
extended_AB = extend_line(A, B)
extended_CD = extend_line(C, D)

# Plot the extended lines with different colors
plt.plot([extended_AB[0][0], extended_AB[1][0]], [extended_AB[0][1], extended_AB[1][1]], linestyle='--', color='orange', label='Tangent')
plt.plot([extended_CD[0][0], extended_CD[1][0]], [extended_CD[0][1], extended_CD[1][1]], linestyle='--', color='r', label='Normal')



# Generate x values for the curve y = sqrt(3x - 2) and extend it to x = 10
x_curve = np.linspace(0, 10, 400)
y_curve = np.sqrt(3 * x_curve - 2)  # y = sqrt(3x - 2)

# Plot the curve
plt.plot(x_curve, y_curve, label='$y = \\sqrt{3x-2}$', color='r')

# Label the q point
plt.scatter(q[0], q[1], color='blue')  # Mark the point q
plt.annotate(f'q\n({q[0]:.2f}, {q[1]:.2f})',
             (q[0], q[1]),
             textcoords="offset points",
             xytext=(0, 10),  # Position above the point
             ha='center',
             fontsize=9,
             color='blue')


# Customize the plot appearance
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.legend(loc='best')
plt.grid()  # minor
plt.savefig('../plots/plot.png', format='png', bbox_inches='tight')
plt.show()

