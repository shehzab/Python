class BankAccount:
  def __init__(self, name, balance):
    self.name =  name
    self.__balance = balance 


  def deposit(self, amount):
    self.__balance += amount
    print(f"${amount} deposited")

  def withdraw(self, amount):
      if amount <= self.__balance:
         self.__balance -= amount
         print(f"${amount} withdrawn")
      else:
         print("Insufficient balance")
  
  def get_balance(self):
     return self.__balance
  

class SavingsAccount(BankAccount):
  def __init__(self, name, balance):
      super().__init__(name, balance)
    
  def withdraw(self, amount):
    if self.get_balance() - amount >= 500:
        super().withdraw(amount)
    else:
        print("Minimum balance of $500 must be maintainted")

class CurrentAccount(BankAccount):
  def __init__(self, name, balance):
      super().__init__(name, balance)

  def withdraw(self, amount):
     print("Overdraft allowed")
     super().withdraw(amount)



savings = SavingsAccount( "Ameen" , 2500)
current = CurrentAccount("Zahid", 1000)

print("\nSavings Account:")
savings.withdraw(17300)
print("Balance:", savings.get_balance())

print("\nCurrent Account:")
current.withdraw(1500)
print("Balance", current.get_balance())



# Note:
# This program is created for practicing OOP concepts such as inheritance,
# method overriding, encapsulation, and the use of super().
# In the SavingsAccount class, the minimum balance rule is enforced before
# checking for insufficient balance. Hence, when a withdrawal amount exceeds
# the available balance, the program displays the minimum balance message.
# In a real banking system, insufficient balance would be checked first,
# followed by the minimum balance rule.
