import matplotlib.pyplot as plt

def read_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Read points
    xA, yA = map(int, lines[0].strip().split())
    xB, yB = map(int, lines[1].strip().split())
    
    # Read line coefficients
    X, Y, Z = map(int, lines[2].strip().split())
    
    return (xA, yA), (xB, yB), X, Y, Z

def plot_data(pointA, pointB, X, Y, Z):
    # Unpack points
    xA, yA = pointA
    xB, yB = pointB
    
    # Create the plot
    plt.figure(figsize=(8, 8))  # Square figure for equal aspect ratio

    # Plot the points
    plt.scatter([xA, xB], [yA, yB], color='red', zorder=5)
    plt.text(xA, yA, f'A({xA},{yA})', fontsize=12, verticalalignment='bottom', horizontalalignment='right', color='black')
    plt.text(xB, yB, f'B({xB},{yB})', fontsize=12, verticalalignment='bottom', horizontalalignment='right', color='black')
    
    # Plot the line AB
    plt.plot([xA, xB], [yA, yB], color='green', linestyle='--', zorder=4, label='Line AB')

    # Plot the line defined by the equation Xx + Yy + Z = 0
    x_values = [min(xA, xB) - 10, max(xA, xB) + 10]
    y_values = [(-X * x - Z) / Y for x in x_values]
    plt.plot(x_values, y_values, color='blue', zorder=3, label='Line 3x = 2y')

    # Set the plot limits
    plt.xlim(min(xA, xB) - 10, max(xA, xB) + 10)
    plt.ylim(min(yA, yB) - 10, max(yA, yB) + 10)

    # Set equal scaling
    plt.gca().set_aspect('equal', adjustable='box')

    # Add labels and title
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Perpendicular Bisector of Line AB')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    # Add legend
    plt.legend()
    plt.savefig('../plots/plot.png', format='png', bbox_inches='tight')

    # Show plot
    plt.show()

# Main function
if __name__ == "__main__":
    filename = 'output.txt'
    pointA, pointB, X, Y, Z = read_data(filename)
    plot_data(pointA, pointB, X, Y, Z)

