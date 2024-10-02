#include <stdio.h>
#include <math.h>

int main() {
    // Coefficients for the equations
    // y = sqrt(x)
    // x = 2y + 3 => y = (x - 3) / 2

    double intersectionX1, intersectionY1;
    double xAxisIntersectionX, xAxisIntersectionY;

    // Finding intersection points of y = sqrt(x) and x = 2y + 3
    // We can express the equations as:
    // 1. y = sqrt(x)
    // 2. y = (x - 3) / 2

    // Set sqrt(x) = (x - 3) / 2
    // 2 * sqrt(x) = x - 3
    // 2 * sqrt(x) + 3 = x
    // Rearranging gives: x - 2*sqrt(x) - 3 = 0

    // Let t = sqrt(x), then x = t^2
    // t^2 - 2t - 3 = 0
    double a = 1, b = -2, c = -3;
    double discriminant = b * b - 4 * a * c;

    if (discriminant >= 0) {
        double root1 = (-b + sqrt(discriminant)) / (2 * a);
        double root2 = (-b - sqrt(discriminant)) / (2 * a);

        // The values of x at the intersection points
        intersectionX1 = root1 * root1; // x = (sqrt(x))^2
        intersectionY1 = root1; // y = sqrt(x)

        // Finding intersection of line x = 2y + 3 with x-axis (y = 0)
        // When y = 0: x = 2*0 + 3 => x = 3
        xAxisIntersectionX = 3;
        xAxisIntersectionY = 0;

        // Calculate area bounded by the curve and the line
        // We will integrate from x = 3 to intersectionX1
        // Area = ∫ (sqrt(x) - (x - 3)/2) dx from 3 to intersectionX1

        double area = 0.0;
        // Using the trapezoidal rule or numerical integration for simplicity
        double step = 0.001; // Step size for integration
        for (double x = 3; x <= intersectionX1; x += step) {
            double yCurve = sqrt(x);
            double yLine = (x - 3) / 2;
            area += (yCurve - yLine) * step;
        }

        // Open the file for writing
        FILE *file = fopen("output.txt", "w");
        if (file == NULL) {
            printf("Error opening file!\n");
            return 1;
        }

        // Write the intersection points in the format x1 y1
        fprintf(file, "%.2f %.2f\n", intersectionX1, intersectionY1); // Point of intersection of curves
        fprintf(file, "%.2f %.2f\n", xAxisIntersectionX, xAxisIntersectionY); // Intersection with x-axis
       
        // Close the file
        fclose(file);
        printf("Results saved to output.txt\n");
    } else {
        printf("No real intersection points.\n");
    }

    return 0;
}

