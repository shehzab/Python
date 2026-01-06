# Create a vector that represents the point(3,4)

v = [3, 4]
# print(v)


# Vector Addition
# Add vectors v1 = (2,3 ) and v2= (4,1)

v1 = [1,3]
v2 = [4,1]

result = [v1[0] + v2[0], v1[1] + v2[1]]

# print(result)


# Scalar Multiplication
# Multiply vector(1,5) by scalar 3

v = [1,5]
scalar = 3

result = (scalar * v[0], scalar * v[1])
# print(result)


# Using Loops
# Vector addition

# Add two vectors of any size

v1 = [1,2,3]
v2 = [4,5,6]

result = []

for i in range(len(v1)):
  result.append(v1[i] + v2[i])

#print(result)

v3 = [12,34,32]
v4 = [15,54,650]

result2 = []

for i in range(len(v3)):
  result2.append(v3[i] + v4[i])

# print(result2)


