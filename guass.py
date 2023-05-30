import numpy as np

def gaussian_elimination(matrix, vector):
    n = len(matrix)
    augmented_matrix = np.column_stack((matrix, vector))

    for i in range(n):
        # Find the maximum element in the current column
        max_row = i
        for j in range(i + 1, n):
            if abs(augmented_matrix[j, i]) > abs(augmented_matrix[max_row, i]):
                max_row = j

        # Swap rows to bring the maximum element to the diagonal position
        augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]

        # Perform row operations to eliminate the elements below the diagonal
        for j in range(i + 1, n):
            factor = augmented_matrix[j, i] / augmented_matrix[i, i]
            augmented_matrix[j, :] -= factor * augmented_matrix[i, :]

    # Back substitution to obtain the solution
    solution = np.zeros(n)
    for i in range(n - 1, -1, -1):
        solution[i] = (augmented_matrix[i, -1] - np.dot(augmented_matrix[i, :-1], solution)) / augmented_matrix[i, i]

    return solution

# Get matrix size from user
n = int(input("Enter the number of equations: "))

# Get matrix coefficients from user
print("Enter the coefficients of the matrix (row-wise):")
matrix = []
for _ in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

# Get vector values from user
print("Enter the values of the vector:")
vector = list(map(float, input().split()))

matrix = np.array(matrix)
vector = np.array(vector)

# Calculate solution using Gaussian elimination
solution = gaussian_elimination(matrix, vector)

# Print the solution
print("Solution:", solution)
