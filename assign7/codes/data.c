#include <stdio.h>

int main() {
    // Points A and B
    int xA = 5, yA = 1;
    int xB = -1, yB = 5;

    // Coefficients of the line equation Xx + Yy + Z = 0
    int X = 3;
    int Y = -2;
    int Z = 0;

    // Open the file for writing
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write the numerical values to the file
    fprintf(file, "%d %d\n", xA, yA); // Point A
    fprintf(file, "%d %d\n", xB, yB); // Point B
    fprintf(file, "%d %d %d\n", X, Y, Z); // Coefficients X, Y, Z

    // Close the file
    fclose(file);

    printf("Data written to output.txt\n");

    return 0;
}

