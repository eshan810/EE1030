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
A = points[0]
B = points[1]
C = points[2]
D = points[3]
A_prime = points[4]
C_prime = points[5]
D_prime = points[6]

# Create a figure for 2D plotting
plt.figure(figsize=(8, 6))

# Generate lines between points using line_gen
x_AB = line_gen(A, B)
x_AC = line_gen(A, C)
x_BC = line_gen(B, C)
x_DC = line_gen(D, C)
x_ApDp = line_gen(A_prime, D_prime)
x_CpDp = line_gen(C_prime, D_prime)
x_BAp = line_gen(B, A_prime)  # Line BA'
x_AD = line_gen(A, D)         # Line AD
x_BCp = line_gen(B, C_prime)   # Line BC'
x_BD = line_gen(B, D)         # Line BD
x_BDp = line_gen(B, D_prime)   # Line BD'

# Plot all lines with different colors
plt.plot(x_AB[0, :], x_AB[1, :], linestyle='-', color='red', label='Line AB')
plt.plot(x_AC[0, :], x_AC[1, :], linestyle='-', color='orange', label='Line AC')
plt.plot(x_BC[0, :], x_BC[1, :], linestyle='-', color='yellow', label='Line BC')
plt.plot(x_DC[0, :], x_DC[1, :], linestyle='-', color='green', label='Line DC')
plt.plot(x_ApDp[0, :], x_ApDp[1, :], linestyle='--', color='blue', label="Line A'D'")
plt.plot(x_CpDp[0, :], x_CpDp[1, :], linestyle='--', color='purple', label="Line C'D'")
plt.plot(x_BAp[0, :], x_BAp[1, :], linestyle='--', color='cyan', label='Line BA\'')
plt.plot(x_AD[0, :], x_AD[1, :], linestyle='-', color='magenta', label='Line AD')
plt.plot(x_BCp[0, :], x_BCp[1, :], linestyle='--', color='brown', label='Line BC\'')
plt.plot(x_BD[0, :], x_BD[1, :], linestyle='-', color='pink', label='Line BD')
plt.plot(x_BDp[0, :], x_BDp[1, :], linestyle='--', color='lime', label='Line BD\'') 

# Scatter plot for all points without labels
plt.scatter(*A, c='r')
plt.scatter(*B, c='g')
plt.scatter(*C, c='b')
plt.scatter(*D, c='purple')
plt.scatter(*A_prime, c='orange')
plt.scatter(*C_prime, c='cyan')
plt.scatter(*D_prime, c='magenta')

# Annotate each point manually with its label
plt.text(A[0], A[1], ' A', fontsize=10, ha='right')
plt.text(B[0], B[1], ' B', fontsize=10, ha='right')
plt.text(C[0], C[1], ' C', fontsize=10, ha='right')
plt.text(D[0], D[1], ' D', fontsize=10, ha='right')
plt.text(A_prime[0], A_prime[1], " A'", fontsize=10, ha='right')
plt.text(C_prime[0], C_prime[1], " C'", fontsize=10, ha='right')
plt.text(D_prime[0], D_prime[1], " D'", fontsize=10, ha='right')

# Calculate lengths of AB and BC
length_AB = np.linalg.norm(A - B)
length_BC = np.linalg.norm(B - C)

# Annotate lengths
plt.text((A[0] + B[0]) / 2, (A[1] + B[1]) / 2 + 0.5, f'|AB| = {length_AB:.2f}', fontsize=9, ha='center')
plt.text((B[0] + C[0]) / 2, (B[1] + C[1]) / 2 + 0.5, f'|BC| = {length_BC:.2f}', fontsize=9, ha='center')

# Annotate angle ABC
angle_text_x = (B[0] + 0.5)  # Adjust position for angle text
angle_text_y = (B[1] + 0.5)
plt.text(angle_text_x, angle_text_y, r'$\angle B = 60^\circ$', fontsize=10, ha='center')

# Draw the quarter arc at point B to denote angle B
arc_radius = 2  # Radius of the arc
theta = np.linspace(0, np.pi / 3, 100)  # 60 degrees in radians
arc_x = B[0] + arc_radius * np.cos(theta)
arc_y = B[1] + arc_radius * np.sin(theta)

plt.plot(arc_x, arc_y, color='black', linestyle='-', linewidth=1)

# Set plot aesthetics
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.grid()
plt.xlim(-12, 12)
plt.ylim(-12, 12)
plt.xlabel('$x$')
plt.ylabel('$y$')

plt.legend(loc='best')
plt.axis('equal')
plt.savefig('../plots/plot.png', format='png', bbox_inches='tight')
plt.show()

