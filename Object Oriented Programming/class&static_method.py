#i have to count the number of customer
class Account:
	count = 0


	@staticmethod
	def print_Val():
		print("Static method in print class")

	@classmethod
	def inc_count(cls): #class method
	    cls.count+=1

	@classmethod
	def get_count(cls):
	    return cls.count

   

	def __init__(self, cust_id, name, initial_blnc=0):  #instance class
		self.__id = cust_id 
		self.__name = name
		self.__balance = initial_blnc
		#Account.count+=1
		Account.inc_count()

	def get_balance(self):
		return self.__balance 

	def get_id(self):
		return self.__id


	def get_name(self):
		return self.__name


customer1 = Account("101", "ABC")
customer2 = Account("102", "XYZ") 
customer3 = Account("103", "DEF") 
customer4 = Account("104", "DEr") 


print(customer1.get_id(), customer1.get_name(), customer1.get_balance())


print(Account.count)
print(customer1.count)
print(Account.__dict__)



print(Account.get_count())



Account.print_Val()


'''
static method: we will not pass any extra character
'''

