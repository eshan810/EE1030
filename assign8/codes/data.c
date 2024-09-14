#include <stdio.h>

int main() {
    // Coefficients of a and b
    double a_i = 1.0, a_j = 1.0, a_k = -2.0;
    double b_i = 2.0, b_j = -4.0, b_k = 5.0;

    // Coefficients for 3a + 2b
    double coef_3a_i = 3.0 * a_i;
    double coef_3a_j = 3.0 * a_j;
    double coef_3a_k = 3.0 * a_k;
    
    double coef_2b_i = 2.0 * b_i;
    double coef_2b_j = 2.0 * b_j;
    double coef_2b_k = 2.0 * b_k;
    
    // Resultant vector 3a + 2b
    double result_i = coef_3a_i + coef_2b_i;
    double result_j = coef_3a_j + coef_2b_j;
    double result_k = coef_3a_k + coef_2b_k;

    // Open file for writing
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write coefficients of a and b
   
    fprintf(file, "%.2f %.2f %.2f\n", a_i, a_j, a_k);
    fprintf(file, "%.2f %.2f %.2f\n", b_i, b_j, b_k);

    // Write resultant vector 3a + 2b
    fprintf(file, "%.2f %.2f %.2f\n", result_i, result_j, result_k);

    // Close the file
    fclose(file);

    printf("Results have been written to output.txt\n");

    return 0;
}

