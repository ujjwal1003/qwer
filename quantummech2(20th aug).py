def mat(n):
    matrix = [[0] * n for i in range(n)]
    for i in range(n):
        matrix[i][i] = -2
        if i + 1 < n:
            matrix[i][i + 1] = 1
        if i - 1 >= 0:
            matrix[i][i - 1] = 1
    return matrix

n = 5 
resultmatrix = mat(n)

print(f"matrix of order {n}:")
for row in resultmatrix:
    print(row)