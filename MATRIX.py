#MATRIX

#1.
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]
    
    return transposed_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = transpose_matrix(matrix)

for row in transposed:
    print("[", end="")
    for i in range(len(row)):
        print(row[i], end="")
        if i < len(row) - 1:
            print(",", end="")
    print("]")


#2.
import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

row_sums = np.sum(matrix, axis=1)

col_sums = np.sum(matrix, axis=0)

print("Matrix:")
print(matrix)
print("\nSum of rows:")
print(row_sums)
print("\nSum of columns:")
print(col_sums)


#3.
def sum_diagonal(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    main_diagonal_sum = 0
    secondary_diagonal_sum = 0
    
    for i in range(rows):
        for j in range(cols):
            if i == j:
                main_diagonal_sum += matrix[i][j]
    
    for i in range(rows):
        for j in range(cols):
            if i + j == rows - 1:
                secondary_diagonal_sum += matrix[i][j]
    
    return main_diagonal_sum, secondary_diagonal_sum

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

main_diagonal_sum, secondary_diagonal_sum = sum_diagonal(matrix)

print("Matrix:")
for row in matrix:
    print(row)

print("\nSum of main diagonal:", main_diagonal_sum)
print("Sum of secondary diagonal:", secondary_diagonal_sum)
