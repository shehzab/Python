
# block of reusable code


def hpybdy(name):
  print("Happy birthday", name)
  print("you are old ")


hpybdy("broo")


def display_invoice(username, amount, duedate):
  print(f"Hello{username}")
  print(f"your bill ${amount:.2f} is due : {duedate}")

display_invoice("Ameer", 2000 , "01/01")





def add(a,b):
  return a + b

x = int(input("enter first number:"))
y = int(input("enter second number:"))

print("result:", add(x, y))