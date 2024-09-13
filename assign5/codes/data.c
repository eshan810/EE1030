#include <stdio.h>

int main() {
    // Define the coordinates of points B and C
    double B_x = -4.0, B_y = 0.0;
    double C_x = 10.0, C_y = 0.0;
    
    // Calculate the coordinates of the midpoint A
    double A_x = (B_x + C_x) / 2.0;
    double A_y = 0.0; // Since A is on the X-axis

    // Open file for writing
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Write the coordinates of B, C, and A to the file
    fprintf(file, "%.2f %.2f\n", B_x, B_y);
    fprintf(file, "%.2f %.2f\n", C_x, C_y);
    fprintf(file, "%.2f %.2f\n", A_x, A_y);

    // Close the file
    fclose(file);

    printf("Coordinates of B, C, and A have been written to output.txt\n");
    return 0;
}

