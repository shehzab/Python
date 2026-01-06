# vector magnitude (length)

# find the length of vector(3,4)

v = [3,4]

length = 0
for x in v:
  length += x * x 

length = length ** 0.5
print(length)