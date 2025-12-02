# 1
# 12
# 123
# 1234
# 12345

n = int(input("enter number of rows needed:"))

for i in range(n):
  for j in range(i + 1):
    print(j, end="")
  print()




n = 5
for i in range( 1 , n+1 ):
  print("*" *i)