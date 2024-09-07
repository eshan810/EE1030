import matplotlib.pyplot as plt

def read_coordinates(output):
    with open(output, 'r') as file:
        lines = file.readlines()
    
    # Read the coordinates from the file
    coordinates = [tuple(map(float, line.strip().split())) for line in lines]
    return coordinates

def plot_coordinates(coordinates):
    if len(coordinates) < 3:
        raise ValueError("Not enough points to plot. Expected exactly 3 points: B, A, and C.")

    # Extract B, A, and C
    B = coordinates[0]
    A = coordinates[1]
    C = coordinates[2]
    
    # Calculate limits for the plot
    all_x = [B[0], A[0], C[0]]
    all_y = [B[1], A[1], C[1]]
    
    margin = 1  # Add some margin around the plot
    plt.xlim(min(all_x) - margin, max(all_x) + margin)
    plt.ylim(min(all_y) - margin, max(all_y) + margin)
    
    # Plot the line BA
    plt.plot([B[0], A[0]], [B[1], A[1]], 'b-', label='Line BA')
    
    # Plot the dotted line AC
    plt.plot([A[0], C[0]], [A[1], C[1]], 'r--', label=None)  # Dotted red line
    
    # Plot the points and add labels
    plt.plot(*B, 'bo')  # Point B
    plt.text(B[0], B[1], f'B ({B[0]:.2f}, {B[1]:.2f})', fontsize=12, color='blue', verticalalignment='bottom')
    
    plt.plot(*A, 'go')  # Point A
    plt.text(A[0], A[1], f'A ({A[0]:.2f}, {A[1]:.2f})', fontsize=12, color='green', verticalalignment='bottom')
    
    plt.plot(*C, 'ro')  # Point C
    plt.text(C[0], C[1], f'C ({C[0]:.1f}, {C[1]:.1f})', fontsize=10, color='red', verticalalignment='bottom')

    # Add labels and title
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Example: B(0,0), A(10,10)')
    plt.legend()
    plt.grid(True)
    
    # Save the plot to a file
    plt.savefig('../plots/plot.png', format='png', bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    # Read coordinates from the file
    coordinates = read_coordinates("output")
    
    # Plot the coordinates
    plot_coordinates(coordinates)

