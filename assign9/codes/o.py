import sys
sys.path.insert(0, '/home/eshan/matgeo/codes/CoordGeo')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen


# Function to read points from a file
def read_points_from_file(filename):
    data = np.loadtxt(filename)
    if data.shape[1] != 3:
        raise ValueError("Each line in the file should contain exactly three values (x, y, z).")
    return data

# Read points from the file
points = read_points_from_file('output.txt')

if len(points) != 2:
    raise ValueError("The file should contain exactly two lines of coordinates.")

P = points[0]
Q = points[1]

# Create a figure and a 3D Axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Generate line between points P and Q
x_PQ = line_gen(P.reshape(3, 1), Q.reshape(3, 1))  # Ensure P and Q are column vectors
ax.plot(x_PQ[0, :], x_PQ[1, :], x_PQ[2, :], label='$PQ$', color='blue')

# Scatter plot for points
tri_coords = np.vstack([P, Q]).T  # Stack P and Q horizontally and transpose to get the shape (3, n)
ax.scatter(tri_coords[0, :], tri_coords[1, :], tri_coords[2, :], c=['red', 'green'])  # Colors for P and Q
vert_labels = ['P', 'Q']

# Annotate each point with its label and coordinates
def format_text(point, label):
    return f'{label}\n({point[0]:.0f}, {point[1]:.0f}, {point[2]:.0f})'

ax.text(P[0], P[1], P[2] + 1, format_text(P, 'P'), fontsize=10, ha='center', va='bottom')
ax.text(Q[0], Q[1], Q[2] - 1, format_text(Q, 'Q'), fontsize=10, ha='center', va='top')

ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.grid()
plt.axis('equal')
plt.savefig('../plots/plot.png', format='png', bbox_inches='tight')


