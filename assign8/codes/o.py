import sys
sys.path.insert(0, '/home/eshan/matgeo/codes/CoordGeo')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from line.funcs import line_gen

# Function to read points from a file
def read_points_from_file(filename):
    return np.loadtxt(filename)

# Read points from output.txt
try:
    points = read_points_from_file('output.txt')
    if points.shape[0] != 3 or points.shape[1] != 3:
        raise ValueError("The file must contain exactly three points, each with three coordinates.")
except Exception as e:
    print(f"Error reading points from file: {e}")
    sys.exit(1)

# Given points
A = points[0]
B = points[1]
C = points[2]

# Create a figure and a 3D Axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Combine all points into a single array
all_points = np.vstack([A, B, C])
origin = np.array([0, 0, 0])

# Generate lines from each point to the origin
x_AO = line_gen(origin, A)
x_BO = line_gen(origin, B)
x_CO = line_gen(origin, C)

# Plot all lines from points to origin
ax.plot(x_AO[0, :], x_AO[1, :], x_AO[2, :], linestyle='--', color='grey')
ax.plot(x_BO[0, :], x_BO[1, :], x_BO[2, :], linestyle='--', color='grey')
ax.plot(x_CO[0, :], x_CO[1, :], x_CO[2, :], linestyle='--', color='grey')

# Scatter plot
ax.scatter(*A, c='r', label='a')
ax.scatter(*B, c='g', label='b')
ax.scatter(*C, c='b', label='3a+2b')

# Annotate each point with its label and coordinates
def format_text(point, label):
    return f'{label}\n({point[0]:.0f}, {point[1]:.0f}, {point[2]:.0f})'

ax.text(A[0], A[1], A[2] + 1, format_text(A, 'a'), fontsize=10, ha='center', va='bottom')
ax.text(B[0], B[1], B[2] - 1, format_text(B, 'b'), fontsize=10, ha='center', va='top')
ax.text(C[0], C[1] + 1, C[2], format_text(C, '3a+2b'), fontsize=10, ha='center', va='bottom')

ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.savefig('../plots/plot.png', format='png', bbox_inches='tight')

