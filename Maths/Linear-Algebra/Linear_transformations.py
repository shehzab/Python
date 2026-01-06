A = [
  [1,2],
  [3,4]
]

v = [1,1]

result = []
for row in A:
  total = 0
  for i in range(len(v)):
      total += row[i] * v[i]
  result.append(total)

# print( result)





















M = [
   [3,4],
   [5,6]
]

V = [2,-3]

result = []

for row in M:
   total= 0
   for i in range(len(V)):
      total += row[i] * V[i]
   result.append(total)
print(result)