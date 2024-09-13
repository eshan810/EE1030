#include <stdio.h>
int main() {
// Function to compute the fourth vertex of the rectangle
void computeFourthVertex(float x1, float y1, float x2, float y2, float x3, float y3, float *x4, float *y4) {
    // Compute the fourth vertex (x4, y4) based on given vertices
    *x4 = x1 + x3 - x2;
    *y4 = y1 + y3 - y2;
}


    // Given vertices
    float x1 = 0, y1 = -3; // Vertex A
    float x2 = 0, y2 = 0;  // Vertex B
    float x3 = 4, y3 = 0;  // Vertex C

    // Variables for the fourth vertex
    float x4, y4;

    // Compute the fourth vertex
    computeFourthVertex(x1, y1, x2, y2, x3, y3, &x4, &y4);

    // Open the file for writing
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        perror("Failed to open file");
        return 1;
    }

    // Write all vertices to the file
    fprintf(file, "%.2f %.2f\n", x1, y1);
    fprintf(file, "%.2f %.2f\n", x2, y2);
    fprintf(file, "%.2f %.2f\n", x3, y3);
    fprintf(file, "%.2f %.2f\n", x4, y4);

    // Close the file
    fclose(file);

    printf("Vertices have been written to output.txt\n");

    return 0;
}

