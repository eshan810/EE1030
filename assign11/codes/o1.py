import sys
sys.path.insert(0, '/home/eshan/matgeo/codes/CoordGeo')
import numpy as np
import matplotlib.pyplot as plt
from line.funcs import line_gen

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
B = points[0]
C = points[1]
D = points[2]
E = points[3]
A = points[4]
# Setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
num = 100
# Scatter plot for all points without labels
plt.scatter(*B, c='r')
plt.scatter(*C, c='r')
plt.scatter(*D, c='r')
plt.scatter(*E, c='purple')
plt.scatter(*A, c='purple')
# Annotate the vertices
def annotate_point(point, label):
    plt.annotate(f'{label}\n({point[0]:.2f}, {point[1]:.2f})',
                 point,
                 textcoords="offset points",
                 xytext=(0, 10),  # Position above the point
                 ha='center',
                 fontsize=9)
                 
annotate_point(B, 'B')
annotate_point(C, 'C')
annotate_point(D, 'D')
annotate_point(E, 'E')
annotate_point(A, 'A')
# Circle parameters
center = np.array([0, 0])  # Center of the circle
radius = 13 / 2  # Radius of the circle

# Generate circle points
theta = np.linspace(0, 2 * np.pi, num)
x_circ = center[0] + radius * np.cos(theta)
y_circ = center[1] + radius * np.sin(theta)
# Plotting
plt.plot(x_circ, y_circ, label='Circle (Radius = 13/2)', color='blue')
# Final plot adjustments
plt.xlim(-5, 10)
plt.ylim(-5, 5)
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
plt.legend(loc='lower right')
plt.grid()

plt.axis('equal')

plt.savefig('../plots/plot.png', format='png', bbox_inches='tight')

