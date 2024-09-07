import matplotlib.pyplot as plt
import numpy as np
import re

# Function to parse line equations from the file
def parse_lines(file_name):
    lines = []
    with open(file_name, 'r') as file:
        while True:
            equation1 = file.readline().strip()
            equation2 = file.readline().strip()
            if not equation1 or not equation2:
                break  # End of file or blank line
            lines.append((equation1, equation2))
    return lines

# Function to extract coefficients from the line equation
def extract_coefficients(equation):
    # Clean the equation
    equation = equation.replace('= 0', '').strip()
    # Use regex to find coefficients
    match = re.match(r'([+-]?\d*)x\s*([+-]?\d*)y\s*([+-]?\d+)', equation)
    if match:
        a_str = match.group(1).replace(' ', '')
        b_str = match.group(2).replace(' ', '')
        c_str = match.group(3).replace(' ', '')
        
        # Handle cases where the coefficient might be empty
        a = float(a_str if a_str and a_str != '+' else '1')
        b = float(b_str if b_str and b_str != '+' else '1')
        c = float(c_str)
        return a, b, c
    else:
        raise ValueError("Invalid line equation format")

# Function to plot a line
def plot_line(a, b, c, color, label):
    x = np.linspace(-10, 10, 400)
    y = (-a * x - c) / b
    plt.plot(x, y, color=color, label=label)

# Main function
def main():
    file_name = 'output.txt'
    lines = parse_lines(file_name)

    plt.figure(figsize=(10, 6))

    for index, (line_eq1, line_eq2) in enumerate(lines):
        # Extract coefficients from the line equations
        try:
            a1, b1, c1 = extract_coefficients(line_eq1)
            a2, b2, c2 = extract_coefficients(line_eq2)
        except ValueError as e:
            print(f"Error parsing line equation '{line_eq1}' or '{line_eq2}': {e}")
            continue
        
        if index == 0:
            # The first line should be pink
            color1 = 'pink'
            color2 = 'pink'
            label1 = 'Coincident line with r = 2 (Equation 1)'
            label2 = 'Coincident line with r = 2 (Equation 2)'
        else:
            color1 = 'blue'
            color2 = 'blue'
            label1 = f'Line with r = {index} (Equation 1)'
            label2 = f'Line with r = {index} (Equation 2)'

        plot_line(a1, b1, c1, color1, label1)
        plot_line(a2, b2, c2, color2, label2)

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.title('Plot of Lines')
    plt.show()

if __name__ == "__main__":
    main()

