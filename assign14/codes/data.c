#include <stdio.h>
#include <math.h>

int main() {
void find_intersection_points() {
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return;
    }

    // Ellipse equation: x^2 + 4y^2 = 16
    // We will calculate y for x = 0 and x = 2

    double x_values[] = {0, 2};
    double y;

    for (int i = 0; i < 2; i++) {
        double x = x_values[i];
        if (x * x <= 16) { // Ensure x^2 <= 16 to have real y values
            y = sqrt((16 - x * x) / 4); // Upper half of the ellipse
            fprintf(file, "%.2f %.2f\n", x, y);  // Store point (x, y)
            fprintf(file, "%.2f %.2f\n", x, -y); // Store point (x, -y)
        } else {
            fprintf(file, "No intersection point at x = %.2f\n", x);
        }
    }

    fclose(file);
    printf("Intersection points saved to output.txt\n");
}


    find_intersection_points();
    return 0;
}

