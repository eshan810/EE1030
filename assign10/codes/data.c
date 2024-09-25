#include <stdio.h>

int main() {
    // Define the points
    double points[][2] = {
        {1.5, 2.598},   // A
        {0.0, 0.0},     // B
        {5.0, 0.0},     // C
        {6.5, 2.598},   // D
        {2.0, 3.46},    // A'
        {6.67, 0.0},   // C'
        {8.67, 3.46}    // D'
    };

    // Open the file for writing
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Write points to the file
   
    fprintf(file, "%.2f %.3f\n", points[0][0], points[0][1]);
    fprintf(file, "%.2f %.3f\n", points[1][0], points[1][1]);
    fprintf(file, "%.2f %.3f\n", points[2][0], points[2][1]);
    fprintf(file, "%.2f %.3f\n", points[3][0], points[3][1]);
    fprintf(file, "%.2f %.3f\n", points[4][0], points[4][1]);
    fprintf(file, "%.2f %.3f\n", points[5][0], points[5][1]);
    fprintf(file, "%.2f %.3f\n", points[6][0], points[6][1]);

    // Close the file
    fclose(file);
    printf("Points have been written to output.txt\n");

    return 0;
}

