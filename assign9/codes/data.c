#include <stdio.h>
#include <math.h>

// Function to write points P, Q, and direction cosines to a file
void write_points_to_file(const char *filename, float x1, float y1, float z1, float x2, float y2, float z2, float l, float m, float n) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        printf("Error opening file for writing.\n");
        return;
    }
    
    // Write points P and Q
    fprintf(file, "%.2f %.2f %.2f\n", x1, y1, z1);
    fprintf(file, "%.2f %.2f %.2f\n", x2, y2, z2);
    
    // Write direction cosines
    fprintf(file, "%.2f %.2f %.2f\n", l, m, n);
    
    fclose(file);
}

// Function to compute the square root using the Newton-Raphson method
float sqrt_newton_raphson(float number) {
    if (number < 0) return -1; // Invalid input for square root

    float tolerance = 1e-6; // Define the tolerance level
    float estimate = number;
    float next_estimate = (estimate + number / estimate) / 2.0;

    while (fabs(next_estimate - estimate) > tolerance) {
        estimate = next_estimate;
        next_estimate = (estimate + number / estimate) / 2.0;
    }

    return next_estimate;
}

int main() {
    // Define points P and Q
    float x1 = 4.0, y1 = 3.0, z1 = -5.0;  // Coordinates of point P
    float x2 = -2.0, y2 = 1.0, z2 = 8.0;  // Coordinates of point Q

    // Compute direction ratios
    float dx = x1 - x2;
    float dy = y1 - y2;
    float dz = z1 - z2;

    // Compute squared magnitude of the direction vector
    float squared_magnitude = dx * dx + dy * dy + dz * dz;

    // Compute magnitude using the Newton-Raphson method
    float magnitude = sqrt_newton_raphson(squared_magnitude);

    // Compute direction cosines
    float l = dx / magnitude;
    float m = dy / magnitude;
    float n = dz / magnitude;

    // Output the direction cosines to the console
    printf("Direction Cosines:\n");
    printf("l = %.6f\n", l);
    printf("m = %.6f\n", m);
    printf("n = %.6f\n", n);

    // Write points P, Q, and direction cosines to a file
    write_points_to_file("output.txt", x1, y1, z1, x2, y2, z2, l, m, n);

    return 0;
}

