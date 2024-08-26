import matplotlib.pyplot as plt

def read_coordinates(file_name):
    x_coords = []
    y_coords = []
    
    with open("output.txt", 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 2:
                try:
                    x, y = float(parts[0]), float(parts[1])
                    x_coords.append(x)
                    y_coords.append(y)
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
    
    return x_coords, y_coords


    
    plt.figure(figsize=(10, 6))
    plt.plot(x_coords, y_coords, marker='o', linestyle='-', color='b')
    
    for i, (x, y) in enumerate(zip(x_coords, y_coords)):
        label = f"({x},{y})"
        plt.text(x, y, label, fontsize=9, verticalalignment='bottom')
    
    plt.title('Plot of BA with external divisor C')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.savefig('fig.png')
    plt.grid(True)
    plt.show()


