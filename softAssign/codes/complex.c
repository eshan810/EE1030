#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <math.h>

#define N 3  // Size of the matrix
#define MAX_ITER 1000  // Maximum number of iterations
#define TOLERANCE 1e-10  // Convergence tolerance

// Function to print a matrix
void print_matrix(double complex* A, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("(%.6f + %.6fi) ", creal(A[i * n + j]), cimag(A[i * n + j]));
        }
        printf("\n");
    }
}

// Function to multiply matrix A by vector v
void matrix_vector_multiply(double complex* A, double complex* v, double complex* result, int n) {
    for (int i = 0; i < n; i++) {
        result[i] = 0.0;
        for (int j = 0; j < n; j++) {
            result[i] += A[i * n + j] * v[j];
        }
    }
}

// Function to compute the norm of a vector
double norm(double complex* v, int n) {
    double norm_value = 0.0;
    for (int i = 0; i < n; i++) {
        norm_value += creal(v[i]) * creal(v[i]) + cimag(v[i]) * cimag(v[i]);
    }
    return sqrt(norm_value);
}

// QR Decomposition using Gram-Schmidt process
void qr_decompose(double complex* A, double complex* Q, double complex* R, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            Q[i * n + j] = A[i * n + j];
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            R[j * n + i] = 0.0;
            for (int k = 0; k < n; k++) {
                R[j * n + i] += conj(Q[k * n + j]) * Q[k * n + i];
            }
            for (int k = 0; k < n; k++) {
                Q[k * n + i] -= R[j * n + i] * Q[k * n + j];
            }
        }

        R[i * n + i] = 0.0;
        for (int k = 0; k < n; k++) {
            R[i * n + i] += conj(Q[k * n + i]) * Q[k * n + i];
        }

        R[i * n + i] = sqrt(R[i * n + i]);

        for (int k = 0; k < n; k++) {
            Q[k * n + i] /= R[i * n + i];
        }
    }
}

// Matrix multiplication (C = A * B)
void matrix_multiply(double complex* A, double complex* B, double complex* C, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            C[i * n + j] = 0.0;
            for (int k = 0; k < n; k++) {
                C[i * n + j] += A[i * n + k] * B[k * n + j];
            }
        }
    }
}

// Function to compute the eigenvalues using QR with shifts
void qr_algorithm(double complex* A, int n, double complex* eigenvalues) {
    double complex* Q = (double complex*)malloc(n * n * sizeof(double complex));
    double complex* R = (double complex*)malloc(n * n * sizeof(double complex));
    double complex* A_next = (double complex*)malloc(n * n * sizeof(double complex));
    double shift, norm_change;
    int iterations = 0;

    // Initialize matrix A
    double complex* A_copy = (double complex*)malloc(n * n * sizeof(double complex));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            A_copy[i * n + j] = A[i * n + j];
        }
    }

    while (iterations < MAX_ITER) {
        iterations++;

        // QR Decomposition of A_copy
        qr_decompose(A_copy, Q, R, n);

        // Multiply R and Q to get A_next
        matrix_multiply(R, Q, A_next, n);

        // Check for convergence
        norm_change = 0.0;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                norm_change += creal(A_next[i * n + j]) * creal(A_next[i * n + j]) + 
                               cimag(A_next[i * n + j]) * cimag(A_next[i * n + j]);
            }
        }

        // If off-diagonal elements are small enough, stop
        if (norm_change < TOLERANCE) {
            break;
        }

        // Update A_copy for the next iteration
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                A_copy[i * n + j] = A_next[i * n + j];
            }
        }
    }

    // Extract eigenvalues from the diagonal of A_next
    for (int i = 0; i < n; i++) {
        eigenvalues[i] = A_next[i * n + i];  // Eigenvalues are on the diagonal
    }

    free(Q);
    free(R);
    free(A_next);
    free(A_copy);
}

int main() {
    // Define a 3x3 complex matrix A (example matrix)
    double complex A[N * N] = {
        1 + 0*I, 2 - 0*I, 3 + 0*I,
        4 + 3*I, 5 + 0*I, 6 - 0*I,
        7 - 0*I, 8 + 0*I, 9 - 0*I
    };					//input a complex matrix with atleast one entry with non-zero imaginary part

    // Print the initial matrix
    printf("Initial Matrix A:\n");
    print_matrix(A, N);

    // Array to store eigenvalues
    double complex eigenvalues[N];

    // Compute eigenvalues using QR algorithm
    qr_algorithm(A, N, eigenvalues);

    // Print the eigenvalues
    printf("\nEigenvalues:\n");
    for (int i = 0; i < N; i++) {
        printf("Eigenvalue %d: %.6f + %.6fi\n", i + 1, creal(eigenvalues[i]), cimag(eigenvalues[i]));
    }

    return 0;
}


