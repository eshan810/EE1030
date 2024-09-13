#include <stdio.h>
#include <stdlib.h>
int main() {
// Function to solve for r
double find_r() {
    // For coincident lines, 6x - ry + 16 = k(3x - y + 8)
    // Equate coefficients: 6 = 3k, -r = -k, 16 = 8k
    double k = 6.0 / 3.0; // k = 2
    double r = 2.0;       // r = k
    return r;
}

// Function to generate two unique points on a line given the coefficients
void generate_points(double a, double b, double c, double x_values[2], double points[2][2]) {
    for (int i = 0; i < 2; i++) {
        double x = x_values[i];
        points[i][0] = x;
        points[i][1] = (-a * x - c) / b;
    }
}


    // Coefficients for the lines
    double a1 = 3.0, b1 = -1.0, c1 = 8.0; // 3x - y + 8 = 0
    double r = find_r(); // Find the value of r
    double a2 = 6.0, b2 = -r, c2 = 16.0; // 6x - ry + 16 = 0

    // Define unique x-values for each line to ensure uniqueness
    double x_values_line1[2] = {-10.0, 0.0}; // x1 and x2 for the first line
    double x_values_line2[2] = {5.0, -3.0};  // x3 and x4 for the second line

    // Points on the first line
    double points1[2][2];
    generate_points(a1, b1, c1, x_values_line1, points1);

    // Points on the second line
    double points2[2][2];
    generate_points(a2, b2, c2, x_values_line2, points2);

    // Write results to output file
    FILE *file = fopen("output", "w");
    if (file == NULL) {
        perror("Failed to open file");
        return EXIT_FAILURE;
    }

    // Write points for the first line
   
    fprintf(file, "%.2f %.2f\n", points1[0][0], points1[0][1]);
    fprintf(file, "%.2f %.2f\n", points1[1][0], points1[1][1]);

    // Write points for the second line
    fprintf(file, "%.2f %.2f\n", points2[0][0], points2[0][1]);
    fprintf(file, "%.2f %.2f\n", points2[1][0], points2[1][1]);

    fclose(file);
    printf("Points have been written to 'output' file.\n");

    return EXIT_SUCCESS;
}

