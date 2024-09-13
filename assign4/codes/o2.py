import sys                                          # for path to external scripts
sys.path.insert(0, '/home/eshan/matgeo/codes/CoordGeo')        # path to my scripts
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex

# local imports
from line.funcs import line_gen
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
# import subprocess
# import shlex
# end if

# Function to read points from a file
def read_points_from_file(filename):
    points = []
    with open(filename, 'r') as file:
        for line in file:
            # Assuming each line contains x and y coordinates separated by space
            x, y = map(float, line.strip().split())
            points.append([x, y])
    return np.array(points)

# Read points from file
points = read_points_from_file('output')

# Debugging: Print the points array and its shape
print("Points array:")
print(points)
print("Shape of points array:", points.shape)

# Check if the points array has exactly 4 points
if points.shape[0] != 4:
    raise ValueError("The points array does not contain exactly 4 points. Please check the 'output' file.")

# Extracting points A, B, C, and D
A, B, C, D = points[0], points[1], points[2], points[3]

# Generating all lines
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CD = line_gen(C, D)
x_DA = line_gen(D, A)

# Plotting all lines
plt.plot(x_AB[0, :], x_AB[1, :], label='$AB$')
plt.plot(x_BC[0, :], x_BC[1, :], label='$BC$')
plt.plot(x_CD[0, :], x_CD[1, :], label='$CD$')
plt.plot(x_DA[0, :], x_DA[1, :], label='$DA$')

# Plotting points
colors = np.arange(1, 5)  # 4 points
plt.scatter(points[:, 0], points[:, 1], c=colors, label='Points')

# Annotating points without a loop
vert_labels = ['A', 'B', 'C', 'D']
for i in range(len(points)):
    plt.text(points[i, 0], points[i, 1], f'{vert_labels[i]}\n({points[i, 0]:.2f}, {points[i, 1]:.2f})',
             fontsize=9, ha='center', va='center', bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))

# Customize the plot
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
plt.grid()  # minor
plt.axis('equal')
plt.legend(loc='best')


