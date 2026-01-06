A = [
  [1,2,7],
  [3,4,8]
]

B = [
  [34,45,76],
  [32,43,79]
]

result = []

for i in range(len(A)):
  row = []
  for j in range(len(A[0])):
    row.append(A[i][j] + B[i][j])
  result.append(row)

print(result)


# multiply matrix by a scalar

a = [
  [23,34,45],
  [32,43,54]
]

scalar = 2

result = []

for i in range(len(a)):
  row= []
  for j in range(len(a[0])):
    row.append(a[i][j] * scalar)
  result.append(row)

print(result)

# Matrix Transpose

# convert rows --> columns

M = [
  [1,2,3],
  [4,5,6]
]

transpose = []

for j in range(len(M[0])):
  row = []
  for i in range(len(M)):
    row.append(M[i][j])
  transpose.append(row)

print(transpose)