def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        raise ValueError("Cannot multiply: Columns of A must equal rows of B")

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # or rows_B
                result[i][j] += A[i][k] * B[k][j]
    
    return result

A = [
    [1, 2],
    [3, 4],
    [5, 6]
]

B = [
    [7, 8, 9],
    [10, 11, 12]
]

product = multiply_matrices(A, B)

print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nProduct of A x B:")
for row in product:
    print(row)
