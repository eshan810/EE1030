#include <stdio.h>

int main() {
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write the known coincident line with r = 2
    fprintf(file, "3x - y + 8 = 0\n");
    fprintf(file, "6x - 2y + 16 = 0\n\n");

    // Generate three different lines with various values of r
    int r_values[] = {1, 3, 5}; // Different values of r
    int num_lines = sizeof(r_values) / sizeof(r_values[0]);

    for (int i = 0; i < num_lines; ++i) {
        int r = r_values[i];
        fprintf(file, "3x - y + 8 = 0\n");
        fprintf(file, "6x - %dy + 16 = 0\n\n", r);
    }

    fclose(file);
    printf("Lines have been written to output.txt\n");

    return 0;
}

