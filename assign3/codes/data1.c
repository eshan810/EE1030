#include <stdio.h>

int main() {
    // Define the name of the output file
    const char* filename = "output";

    // Open the file for writing
    FILE *file = fopen(filename, "w");
    if (!file) {
        // Print an error message if the file cannot be opened
        fprintf(stderr, "Error opening file %s for writing\n", filename);
        return 1; // Return a non-zero value to indicate failure
    }

    // Define the endpoints of the line segment BA
    double B_x = 0.0, B_y = 0.0; // Starting point B
    double A_x = 10.0, A_y = 10.0; // Ending point A

    // Write the coordinates of B and A
    fprintf(file, "%.2f %.2f\n", B_x, B_y);
    fprintf(file, "%.2f %.2f\n", A_x, A_y);

    // Define the fraction for the point
    double fraction = 1.5;

    // Calculate the coordinates for the given fraction
    double x = B_x + fraction * (A_x - B_x);
    double y = B_y + fraction * (A_y - B_y);

    // Write the coordinates to the file
    fprintf(file, "%.2f %.2f\n", x, y);

    // Close the file
    fclose(file);

    return 0; // Return 0 to indicate success
}

