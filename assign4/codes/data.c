#include <stdio.h>

int main() {
    // Define line equations as coefficients (Ax + By + C = 0)
    double lines[][4] = {
        {3.0, -1.0, 8.0},  // 3x - y + 8 = 0
        {6.0, -2.0, 16.0}  // 6x - 2y + 16 = 0
    };

    // Open file for writing
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Write the first line equation to file
    fprintf(file, "%.1f %.1f %.1f\n", lines[0][0], lines[0][1], lines[0][2]);

    // Write the second line equation to file
    fprintf(file, "%.1f %.1f %.1f\n", lines[1][0], lines[1][1], lines[1][2]);

    // Close file
    fclose(file);

    printf("Line equations have been written to output.txt\n");
    return 0;
}

