l=[10,2,30,40,50]
print(sum(l))#to add all the list element,you sont have to iterate, instead use sum function

print(max(l))
print(min(l))

num=25.555
print(round(num,2))#round up upto 2


print(dir(__builtins__)) #builtin function lists
#help(__builtins__)



import math

l=[0.1]*10
print(l)
print(sum(l))#0.9999
print(math.fsum(l))#1.0
#15 16

num1 = 15.5559
print(math.floor(15.5559), math.ceil(15.5559))#lower bound and upper bound



print(math.sqrt(25))
print(math.factorial(5))

num1 = 45.5556
print(math.modf(num1))

d, i=math.modf(num1)
print(i)

print(math.pow(10,2))

print(math.log(10))
print(math.log10(2))
print(math.log2(10))



print(math.sin(math.radians(30)))
print(math.cos(math.radians(30)))
print(math.tan(math.radians(30)))

print(dir(math))


'''Random Number'''

import random 
print(random.random())#betn 0 and 1


l=[1,2,3,4,5,6,7]
print(random.choice(l))


print(random.randint(1,3))
print(random.randrange(1,3))

print(random.uniform(10,20))