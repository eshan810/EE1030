#include <stdio.h>

// Function to write numerical coordinates to the output file
void writeCoordinatesToFile(const char* output) {
    FILE *file = fopen(output, "w");
    if (!file) {
        // Print an error message if the file cannot be opened
        fprintf(stderr, "Error opening file %s for writing\n", output);
        return;
    }

    // Define the endpoints of the line segment BA
    double B_x = 0.0, B_y = 0.0; // Starting point B
    double A_x = 10.0, A_y = 10.0; // Ending point A

    // Write the coordinates of B and A
    fprintf(file, "%.2f %.2f\n", B_x, B_y);
    fprintf(file, "%.2f %.2f\n", A_x, A_y);

    // Calculate and write the coordinates for each fraction
    double x, y;

    // Fraction 0.3
    x = B_x + 0.3 * (A_x - B_x);
    y = B_y + 0.3 * (A_y - B_y);
    fprintf(file, "%.2f %.2f\n", x, y);

    // Fraction 0.6
    x = B_x + 0.6 * (A_x - B_x);
    y = B_y + 0.6 * (A_y - B_y);
    fprintf(file, "%.2f %.2f\n", x, y);

    // Fraction 0.9
    x = B_x + 0.9 * (A_x - B_x);
    y = B_y + 0.9 * (A_y - B_y);
    fprintf(file, "%.2f %.2f\n", x, y);

    // Fraction 1.5
    x = B_x + 1.5 * (A_x - B_x);
    y = B_y + 1.5 * (A_y - B_y);
    fprintf(file, "%.2f %.2f\n", x, y);

    fclose(file);
}

int main() {
    // Call the function to write coordinates to the file
    writeCoordinatesToFile("output");
    return 0;
}

