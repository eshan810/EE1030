#include <stdio.h>
#include <math.h>

// Function for the tangent line equation
double tangent_line(double x) {
    return 2 * x - 23.0 / 24.0;
}

// Function for the normal line equation
double normal_line(double x) {
    return -0.5 * x + 113.0 / 96.0;
}

// Function to find the intersection point of the tangent and normal lines
void find_intersection(double *x_intersection, double *y_intersection) {
    // Solve 2x - 23/24 = -0.5x + 113/96
    // Rearranging gives us: 2.5x = 113/96 + 23/24
    double right_side = (113.0 / 96.0) + (23.0 / 24.0);
    *x_intersection = right_side / 2.5;
    *y_intersection = tangent_line(*x_intersection);  // Use tangent line equation to find y
}

int main() {
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Calculate and write points for the tangent line
    for (double x = 0; x <= 1; x += 1) {  // Two x values for tangent line
        double y = tangent_line(x);
        fprintf(file, "%.2f %.2f\n", x, y);  // Format: x1 y1
    }

    // Calculate and write points for the normal line
    for (double x = 0; x <= 1; x += 1) {  // Two x values for normal line
        double y = normal_line(x);
        fprintf(file, "%.2f %.2f\n", x, y);  // Format: x1 y1
    }

    // Find and write the intersection point
    double x_intersection, y_intersection;
    find_intersection(&x_intersection, &y_intersection);
    fprintf(file, "%.2f %.2f\n", x_intersection, y_intersection);

    fclose(file);
    return 0;
}

