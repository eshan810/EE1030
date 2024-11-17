# code for only real matrices
import cmath  # For handling complex numbers

def dot_product(v1, v2):
    """Dot product of two vectors, handling complex numbers."""
    return sum(x * y.conjugate() for x, y in zip(v1, v2))

def sqrt(n, tolerance=1e-10):
    """Square root function that handles complex numbers."""
    if isinstance(n, complex) or n < 0:
        return cmath.sqrt(n)
    x = n
    while True:
        if x == 0:
            return 0  # Handle zero input to avoid division by zero
        new_x = 0.5 * (x + n / x)
        if abs(new_x - x) < tolerance:
            return new_x
        x = new_x

def norm(v):
    """Compute the Euclidean norm of a vector."""
    return sqrt(dot_product(v, v).real)

def subtract(v1, v2):
    """Subtract two vectors."""
    return [x - y for x, y in zip(v1, v2)]

def scale(v, scalar):
    """Scale a vector by a scalar."""
    return [x * scalar for x in v]

def gram_schmidt(A):
    """Perform QR decomposition using the Gram-Schmidt process."""
    m, n = len(A), len(A[0])
    Q = []
    R = [[0] * n for _ in range(n)]
    
    for j in range(n):
        v = [A[i][j] for i in range(m)]
        for i in range(j):
            R[i][j] = dot_product(Q[i], v)
            projection = scale(Q[i], R[i][j])
            v = subtract(v, projection)
        
        norm_v = norm(v)
        if norm_v < 1e-10:  # Handle near-zero norm
            R[j][j] = 0
            Q.append([0] * m)  # Append a zero vector for consistency
            continue
        
        R[j][j] = norm_v
        q_j = scale(v, 1 / R[j][j])
        Q.append(q_j)
    
    Q = list(map(list, zip(*Q)))  # Transpose Q to match dimensions
    return Q, R

def matrix_multiply(A, B):
    """Multiply two matrices."""
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def frobenius_norm(A, B):
    """Compute the Frobenius norm of the difference between two matrices."""
    return sum(abs(A[i][j] - B[i][j]) ** 2 for i in range(len(A)) for j in range(len(A[0]))) ** 0.5

def qr_algorithm_with_shifts(A, max_iterations=1000, tolerance=1e-10, convergence_tolerance=1e-6, max_convergence_iterations=2):
    """Compute eigenvalues of matrix A using QR decomposition with shifts and a new convergence criterion."""
    n = len(A)
    Ak = [row[:] for row in A]  # Copy of A
    iteration_count = 0  # Counter for iterations
    previous_Ak = None  # To store the previous iteration matrix
    convergence_counter = 0  # To count consecutive iterations with small change
    
    for _ in range(max_iterations):
        iteration_count += 1  # Increment the iteration counter
        
        # Apply Wilkinson shift
        if n > 1:
            μ = Ak[-1][-1]  # Shift is the bottom-right element
            Ak = [[Ak[i][j] - (μ if i == j else 0) for j in range(n)] for i in range(n)]
        else:
            μ = 0  # No shift for 1x1 matrix
        
        Q, R = gram_schmidt(Ak)
        Ak = matrix_multiply(R, Q)
        
        # Add the shift back
        if n > 1:
            Ak = [[Ak[i][j] + (μ if i == j else 0) for j in range(n)] for i in range(n)]
        
        # Check for convergence: if the change in Ak is small for a number of iterations
        if previous_Ak is not None:
            norm_change = frobenius_norm(Ak, previous_Ak)
            if norm_change < convergence_tolerance:
                convergence_counter += 1
            else:
                convergence_counter = 0
        
        # If change is small for `max_convergence_iterations` iterations, consider converged
        if convergence_counter >= max_convergence_iterations:
            print(f"Converged after {iteration_count} iterations.")
            break
        
        previous_Ak = [row[:] for row in Ak]  # Update previous matrix
    
    else:
        # If no break occurs, print that it reached the max iterations
        print()
    
    # Extract eigenvalues (diagonal elements of Ak)
    eigenvalues = []
    i = 0
    while i < n:
        if i < n - 1 and abs(Ak[i + 1][i]) > tolerance:
            # Complex eigenvalues from 2x2 block
            a, b, c, d = Ak[i][i], Ak[i][i + 1], Ak[i + 1][i], Ak[i + 1][i + 1]
            trace = a + d
            determinant = a * d - b * c
            eigenvalues.append((trace + sqrt(trace ** 2 - 4 * determinant)) / 2)
            eigenvalues.append((trace - sqrt(trace ** 2 - 4 * determinant)) / 2)
            i += 2
        else:
            # Real eigenvalue
            eigenvalues.append(Ak[i][i])
            i += 1
    
    return eigenvalues, iteration_count

# Example non-symmetric matrix
A = [
        [0, -1],
        [1,  1] 
    ]               # input a real matrix
# Compute eigenvalues
eigenvalues, iterations = qr_algorithm_with_shifts(A)

# Print the eigenvalues and number of iterations
print("Eigenvalues of A:", eigenvalues)



