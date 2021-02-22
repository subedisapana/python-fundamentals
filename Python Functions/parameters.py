#1 Positional Argument: If function defination and function call have a same number of argumrnt then i
#2 Default
#3 Keyword
def linear_search(l,key):
	for value in l:
		if key==value:
			return True
		else:
			return False


l=[10,20,30,40,50,60]
key = 400
result=linear_search(l,key)
print(result)

 

 #2 Default Argument
'''
 #password generator
 1 uppercase
 8 char
 1 lower
 1 special char
 5 digits



 ord:ASCII value; lowercase is accessed in ord
 chr:for uppercae;ASCII value
 '''

import random
print(ord('a'),ord('z'))
print(ord('A'),ord('Z'))

print(chr(97))

a=chr(random.randint(97,122))
print(a)


import random
def gen_password(length=8):
	l=['@','#','$','&']

	upper= chr(random.randint(65,90))
	lower = chr(random.randint(97,122))
	special=random.choice(l)
	digit=random.randint(10000,99999)
	password = upper+lower+special+str(digit)
	l=random.sample(password,length)
	password=("").join(l)
	return password


result=gen_password(5)
print(result)



print("--------------------------------------------")



#3 kEYWORD
#VALIDATING USERNAME AND password
def validate(username,password):
    if username=="ABC" and password=="abc123":
    	print("valid password")
    else:
    	print("Invalid password")

validate("abc123", "abc@123")
validate("ABC", "abc123")
validate(password="abc123",username="ABC")#explicitly assignin value

'''print statement'''
print(100, 200, sep=",", end=" ")
print("Hi")


l1=[100,200,300,400]
l1.append(500) #only add single element
print(l1)


def add_value(*args): #variable length parameters exists so
    l=[]
    for value in args:
    	l.append(value)

    return l



result =add_value(100,200,300,400,500)
print(result)

result =add_value(100,200)
result =add_value(100,200,300,400,500,600,700,800)
print(result)







'''
variable length keyword arument
fields: name, email, contact, dob'''

def get_details(**kwargs):
	print(kwargs)



get_details(name="sapana", email="subedisapana@gmail.com",contact=2222,dob ="2-05-2029")
get_details(name="sapana", email="subedisapana@gmail.com",dob="2-05-2029")
get_details(name="sapana",dob="2-05-2029")

#args:The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function.
#t is used to pass a non-key worded, variable-length argument list. 
#kwargs:



