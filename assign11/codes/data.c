#include <stdio.h>

int main() {
    // Define the points
    double points[][2] = {
        {-3.0 / 4.0, 1},  // Point 1
        {2, 7.0 / 3.0},   // Point 2
        {5, -1.0 / 2.0},  // Point 3
        {-6, -5 / 2.0},   // Point 4
	{6.50, 0}         // Point 5
    };

    // Open file for writing
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write points to file in the format "x y"
    for (int i = 0; i < 5; i++) {
        fprintf(file, "%.2f %.2f\n", points[i][0], points[i][1]);
    }

    // Close the file
    fclose(file);

    printf("Points have been written to output.txt\n");
    return 0;
}

