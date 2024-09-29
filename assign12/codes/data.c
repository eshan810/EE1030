#include <stdio.h>
#include <math.h>

int main() {
    // Coefficients for the quadratic equation x^2 - x - 2 = 0
    double a = 1, b = -1, c = -2;
    double discriminant, root1, root2;

    // Calculate the discriminant
    discriminant = b * b - 4 * a * c;

    // Check if the discriminant is non-negative
    if (discriminant >= 0) {
        // Calculate the two roots
        root1 = (-b + sqrt(discriminant)) / (2 * a);
        root2 = (-b - sqrt(discriminant)) / (2 * a);

        // Open the file for writing
        FILE *file = fopen("output.txt", "w");
        if (file == NULL) {
            printf("Error opening file!\n");
            return 1;
        }

        // Write the intersection points to the file in the format x1 y1
        fprintf(file, "%.2f %.2f\n", root1, root1 * root1); // For x1, y1
        fprintf(file, "%.2f %.2f\n", root2, root2 * root2); // For x2, y2

        // Close the file
        fclose(file);
        printf("Intersection points saved to output.txt\n");
    } else {
        printf("No real intersection points.\n");
    }

    return 0;
}

