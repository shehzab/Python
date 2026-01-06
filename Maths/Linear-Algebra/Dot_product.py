# Dot product 

# Find dot product of (1,2) and (3,4)

v1 = [1,2]
v2 = [3,4]

dot= 0

for i in range(len(v1)):
  dot += v1[i] * v2[i]

# print(dot)

v3 = [0,5]
v4 = [1, -2]

dot = 0
for i in range(len(v3)):
  dot += v3[i] * v4[i]

print(dot)