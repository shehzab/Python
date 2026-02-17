import numpy as np

A = np.array([
  [5, 7],
  [8, 9]
])

detA = np.linalg.det(A)
print(round(detA))

A_inv = np.linalg.inv(A)
print(A_inv)


identity = A_inv @ A
print(identity)

print(np.allclose(identity, np.eye(2)))