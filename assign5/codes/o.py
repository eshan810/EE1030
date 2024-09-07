import matplotlib.pyplot as plt
import numpy as np

def read_coordinates(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Extract coordinates from the lines
    B = tuple(map(float, lines[0].strip().replace('B(', '').replace(')', '').split(', ')))
    C = tuple(map(float, lines[1].strip().replace('C(', '').replace(')', '').split(', ')))
    A = tuple(map(float, lines[2].strip().replace('A(', '').replace(')', '').split(', ')))
    
    return B, C, A

def plot_lines(B, C, A):
    x_values = np.linspace(-10, 10, 400)
    
    # Coordinates of B and C
    B_x, B_y = B
    C_x, C_y = C
    
    # Plot Line BC
    plt.plot([B_x, C_x], [B_y, C_y], 'r-', label='Line BC')  # Red color for BC
    
    # Coordinates of A
    A_x, A_y = A
    
    # Plot vertical line passing through A
    plt.axvline(x=A_x, color='m', linestyle='--', label=None) # Pink dotted line
    
    # Plot points B, C, and A
    plt.plot(B_x, B_y, 'ro', label=None)  # Red color for B
    plt.plot(C_x, C_y, 'ro', label=None)  # Red color for C
    plt.plot(A_x, A_y, 'go', label='Point A')  # Green color for A
    
    # Annotate the points with their coordinates
    plt.text(B_x, B_y + 1, f'B({B_x}, {B_y})', fontsize=9, ha='center', color='red')
    plt.text(C_x, C_y + 1, f'C({C_x}, {C_y})', fontsize=9, ha='center', color='red')
    plt.text(A_x, A_y + 1, f'A({A_x}, {A_y})', fontsize=9, ha='center', color='green')
    
    # Set plot limits to ensure annotations are visible
    plt.xlim(min(B_x, C_x, A_x) - 5, max(B_x, C_x, A_x) + 5)
    plt.ylim(min(B_y, C_y, A_y) - 5, max(B_y, C_y, A_y) + 5)
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Equidistant Point')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.savefig('../plots/plot.png', format='png', bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    B, C, A = read_coordinates('output.txt')
    plot_lines(B, C, A)

