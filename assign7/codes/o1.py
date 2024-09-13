import sys                                          #for path to external scripts
sys.path.insert(0, '/home/eshan/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
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
# Flatten the array if necessary
if points.ndim == 3:
    points = points.reshape(-1, 2)

# Extracting points A, B, C, and D
A, B, C, D = points[0], points[1], points[2], points[3]

# Define a range of values for plotting infinitely
x_range = np.linspace(-15, 15, 100)  # Adjust as necessary to ensure lines extend sufficiently
# Generating all lines
x_AB = line_gen(A, B)

x_CD = line_gen(C, D)


plt.plot(x_AB[0, :], x_AB[1, :], 'b--', label='$AB$')
# Line CD
slope_CD = (D[1] - C[1]) / (D[0] - C[0])
intercept_CD = C[1] - slope_CD * C[0]
plt.plot(x_range, slope_CD * x_range + intercept_CD, label='$3x=2y$', color='red')

# Plotting points
colors = np.arange(1, 5)  # 4 points
plt.scatter(points[:, 0], points[:, 1], c=colors, label=None)

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
