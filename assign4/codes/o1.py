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
points = read_points_from_file('output')

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


# Line AB
slope_AB = (B[1] - A[1]) / (B[0] - A[0])
intercept_AB = A[1] - slope_AB * A[0]
plt.plot(x_range, slope_AB * x_range + intercept_AB, label='$3x-y+8=0$', color='blue')

# Line CD
slope_CD = (D[1] - C[1]) / (D[0] - C[0])
intercept_CD = C[1] - slope_CD * C[0]
plt.plot(x_range, slope_CD * x_range + intercept_CD, label='$6x-2y+16=0$', color='red', linestyle='--')

# Plotting points
colors = np.arange(1, 5)  # 4 points
plt.scatter(points[:, 0], points[:, 1], c=colors, label=None)

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

