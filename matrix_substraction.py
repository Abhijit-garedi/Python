# python program for matrix substraction
def input_matrix(rows, cols):
    matrix = []
    print("Enter matrix elements row-wise:")
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Element [{i+1}, {j+1}]: ")))
        matrix.append(row)
    return matrix

# to subtract two matrices
def subtract_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Matrix A:")
matrix1 = input_matrix(rows, cols)

print("Matrix B:")
matrix2 = input_matrix(rows, cols)

result = subtract_matrices(matrix1, matrix2)

# Display the result
print("Resultant Matrix after subtraction:")
for r in result:
    print(r)
