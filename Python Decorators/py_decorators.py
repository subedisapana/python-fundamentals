'''

it is a fxn which takes function as an argument and returns another function


If you want to execute a set odf sted before defining function
'''


'''
concat function
'''

def deco(func):
	def new_func(val1, val2):
		if type(val1)== type(val2):
		    return func(val1, val2) #@deco sulls function concat
		else:
			return func(str(val1), str(val2)) #else convert into str
	return new_func


@deco
def concat(val1, val2):
	return val1+val2



result = concat(10, 10)
print(result)


result = concat("python", "string")
print(result)

result = concat(10, "string") # you cannot concat a string and int value
print(result)
