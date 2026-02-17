A = [
  [4,3],
  [3,2]
 ]

def det_2x2(M):
  a, b = M[0]
  c, d = M[1]
  return a * d - b * c

detA = det_2x2(A)
print(detA)


def inverse_2x2(M):
  det = det_2x2(M)

  if det == 0:
    return None
  
  a, b = M[0]
  c, d = M[1]

  inv= [
    [d/det, -b/det],
    [-c/det, a/det]

  ]
  return inv

A_inv = inverse_2x2(A)
print(A_inv)


def matrix_multiply(A, B):
  result = [
    [0,0],
    [0,0]
  ]

  for i in range(2):
    for j in range(2):
      for k in range(2):
        result[i][j] += A[i][k] * B[k][j]

  return result

identity = matrix_multiply(A_inv, A)

for row in identity:
  print(row)







B = [
  [6, 9],
  [2, 3]
] 

