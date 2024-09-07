import matplotlib.pyplot as plt
import numpy as np

def read_line_equations(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    equations = []
    for line in lines:
        a, b, c = map(float, line.strip().split())
        equations.append((a, b, c))
    
    return equations

def plot_lines(equations):
    x = np.linspace(-10, 10, 400)
    
    plt.figure(figsize=(8, 6))
    
    # Read and plot the first line
    a1, b1, c1 = equations[0]
    y1 = (-a1 * x - c1) / b1
    plt.plot(x, y1, label=f'{a1}x + {b1}y + {c1} = 0')
    
    # Read and plot the second line
    a2, b2, c2 = equations[1]
    y2 = (-a2 * x - c2) / b2
    plt.plot(x, y2, 'r--', label=f'{a2}x + {b2}y + {c2} = 0')  # Red dotted line
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Coincident Lines')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.savefig('../plots/plot.png', format='png', bbox_inches='tight')
    

if __name__ == "__main__":
    equations = read_line_equations('output.txt')
    plot_lines(equations)

