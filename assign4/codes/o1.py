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
    
    for (a, b, c) in equations:
        y = (-a * x - c) / b
        plt.plot(x, y, label=f'{a}x + {b}y + {c} = 0')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Coincident lines')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.savefig('../plots/plot.png', format='png', bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    equations = read_line_equations('output.txt')
    plot_lines(equations)

