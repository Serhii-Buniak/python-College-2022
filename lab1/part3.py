from functools import reduce
from re import I

row_length = 3
column_length = int(input('column length: '))

matrix = [[0]*row_length for i in range(column_length)]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = int(input(f'[{i}][{j}]: '))
print(f'filled matrix: {matrix}')

average_numbers = [0]*len(matrix)
for i in range(len(matrix)):
    average_numbers[i] = reduce(
        lambda n1, n2: n1+n2,
        matrix[i])/len(matrix[i])
print(f'array of average numbers of matrix: {average_numbers}')

difference_matrix = [[0]*row_length for i in range(column_length)]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        difference_matrix[i][j] = matrix[i][j]-average_numbers[i]
print(f'difference matrix: {difference_matrix}')
