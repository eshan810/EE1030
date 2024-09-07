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

    // Write line equations to file
    for (int i = 0; i < 2; ++i) {
        fprintf(file, "%.1f %.1f %.1f\n", lines[i][0], lines[i][1], lines[i][2]);
    }

    // Close file
    fclose(file);

    printf("Line equations have been written to output.txt\n");
    return 0;
}

