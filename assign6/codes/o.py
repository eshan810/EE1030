import matplotlib.pyplot as plt
import numpy as np

# Read the points from the file
with open('output.txt', 'r') as file:
    lines = file.readlines()

# Extract vertices from the file
def parse_vertex(line):
    parts = line.strip().split(': ')
    if len(parts) == 2:
        coords = parts[1].strip('()').split(', ')
        return float(coords[0]), float(coords[1])
    return None

# Unpack vertices
A = parse_vertex(lines[0])
O = parse_vertex(lines[1])
B = parse_vertex(lines[2])
C = parse_vertex(lines[3])

# Create a plot
plt.figure()

# Plot the vertices
plt.scatter(*A, label=f'Vertex A ({A[0]}, {A[1]})')
plt.scatter(*O, label=f'Vertex O ({O[0]}, {O[1]})')
plt.scatter(*B, label=f'Vertex B ({B[0]}, {B[1]})')
plt.scatter(*C, label=f'Vertex C ({C[0]}, {C[1]})')

# Annotate the vertices
plt.annotate('A', A, textcoords="offset points", xytext=(-10,10), ha='center')
plt.annotate('O', O, textcoords="offset points", xytext=(-10,10), ha='center')
plt.annotate('B', B, textcoords="offset points", xytext=(-10,10), ha='center')
plt.annotate('C', C, textcoords="offset points", xytext=(-10,10), ha='center')

# Plot the sides of the rectangle as solid lines
plt.plot([A[0], O[0]], [A[1], O[1]], 'b-', linewidth=2)  # AO
plt.plot([O[0], B[0]], [O[1], B[1]], 'b-', linewidth=2)  # OB
plt.plot([O[0], A[0]], [O[1], A[1]], 'b-', linewidth=2)  # OA

# Plot the dotted lines AO, BO, and CO
plt.plot([A[0], C[0]], [A[1], C[1]], 'r--', linewidth=2)  # AC
plt.plot([O[0], C[0]], [O[1], C[1]], 'r--', linewidth=2)  # OC
plt.plot([B[0], C[0]], [B[1], C[1]], 'r--', linewidth=2)  # BC

# Calculate and plot the diagonals with their lengths
def plot_diagonal(x1, y1, x2, y2, color, linestyle, text_color):
    # Plot diagonal
    plt.plot([x1, x2], [y1, y2], color=color, linestyle=linestyle, linewidth=2)
    
    # Calculate length
    length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # Find the point for text placement
    text_x = x1 + 0.5 * (x2 - x1)
    text_y = y1 + 0.5 * (y2 - y1)
    
    # Plot the length text left-centered along the diagonal
    plt.text(text_x, text_y, f'{length:.2f}', color='red', fontsize=12, ha='left', va='center')

# Plot diagonals
plot_diagonal(A[0], A[1], B[0], B[1], 'g', '-', 'purple')  # AB (solid green line with purple text)
plot_diagonal(O[0], O[1], C[0], C[1], 'b', '--', 'pink')  # OC (dotted blue line with orange text)

# Set labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Rectangle AOBC')
plt.legend()
plt.grid(True)
plt.savefig('../plots/plot.png', format='png', bbox_inches='tight')
# Ensure equal scaling
plt.gca().set_aspect('equal', adjustable='box')

# Show the plot
plt.show()

