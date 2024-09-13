#include <stdio.h>
int main() {
// Function to print points to file
void print_points_to_file(const char *filename) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        perror("Error opening file");
        return;
    }

    // Define points A and B
    fprintf(file, "5 1\n");   // Point A
    fprintf(file, "-1 5\n");  // Point B

    // Define points on the line 3x = 2y
    // Example points (calculated for demonstration)
    // For x = 1, y = 3/2 = 1.5
    fprintf(file, "1 1.5\n"); // Point on the line
    
    // Another example point (calculated for demonstration)
    // For x = -2, y = -3
    fprintf(file, "-2 -3\n"); // Point on the line

    fclose(file);
}


    print_points_to_file("output.txt");
    return 0;
}

