'''
class and Objects in python
'''
'''
cust id
name
balance
deposit
withdrawl
'''
#self is the object instance

class Account:
	def __init__(self, cust_id, name, initial_blnc=0): #when you create obj, in the background , python createa call to a fxn #call is implicit
		self.id = cust_id # __ makes the variable private and you cannot access from outside of the class
		self.name = name
		self.balance = initial_blnc

	def get_balance(self):
		return self.balance 


	def deposit(self, amount):
		self.balance = self.balance+amount
		return self.balance

	def withdraw(self, amount):
		if amount > self.balance:
			return "insufficient balance"
		else:
			self.balance-=amount
			return self.balance



customer1 = Account("101", "ABC") #customer1 is the account object
customer2 = Account("102", "XYZ") 
customer3 = Account("103", "DEF") 

customer4 = Account("104", "DEr") 


print(customer1.id, customer1.name, customer1.balance)

print(customer1.id, customer1.name, customer1.balance)


print(customer1.get_balance())
print(customer1.deposit(50000))
print(customer1.withdraw(10000))
print(customer1.withdraw(70000))

customer1.deposit(2000)
customer2.deposit(4000)
customer3.deposit(7000)


l = [customer1, customer2, customer3, customer4]

for obj in l:
	if obj.balance < 10000:  #here instead of balance youshould call, get_balance()
		print(obj.id, obj.name) # get_id() and get_name()



#After making all the varible private you cannot acess the variable from outside, so getter and setter is used from outside of the class
