'''
used to use the existinf code
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

'''

class Account:
	def __init__(self, cust_id, name, initial_blnc=0):  #instance class
		self.__id = cust_id 
		self.__name = name
		self.__balance = initial_blnc
	

	def get_balance(self):
		return self.__balance 

	def get_id(self):
		return self.__id


	def get_name(self):
		return self.__name


	def deposit(self, amount):
		self.__balance = self.__balance+amount
		return self.__balance


    
	def withdraw(self, amount):
		if amount > self.__balance:
			return "insufficient balance"
		else:
			self.__balance-=amount
			return self.__balance



class Saving_Account(Account):
	def __init__(self,id,name,initial_blnc=0):
		super().__init__(id, name, initial_blnc)
		self.limit = 50000


	def withdraw(self, amount):
		if amount > self.limit:
			new_blnc = super().withdraw(amount)

			self.limit -= amount
			return new_blnc
		else:
			print("Daily limit reached")


cust1 = Saving_Account(108, "sap")
print(cust1.__dict__)


print(cust1.deposit(80000))
print(cust1.withdraw(1000))
print(cust1.withdraw(100))

#If i want to add a new functionality in child class you can override the parent class but implementation will be different


'''
Multiple inheritence
'''

class A:
	pass
class B:
	pass
class C(B,A):
    pass


obj = C()


help(obj)