#loops in python
#1 for loop
#2 while loop


#Iterable datatypes; str, list, dict, set

#for [Variable_name] in [iterable datatype]:
	#statements


#l=[1,3,4,5,6]

#for value in l:
#	print(value)


#l=[1,3,4,5,6]
#sum = 0
#for i in l:
#	sum = sum+i
#print(sum)  #o/p:19, indentation matters


l=[1,3,4,5,6]
sum = 0
for i in l:
	sum = sum+i
	print(sum)


print("-----------------------------")

#RANGE
#1-1000
#range(5) = 0 1 2 3 4, (0 to n-1)
#range(10,20) = 10 11 12 ...19
#range(10, 100,5) = 10,15,20....100

sum = 0
for value in range(10,100,10):
	print(value)

print("-----------------------------")

s = 0
for val in range(1,10):
	sum = sum+val
	print(sum)

print("-----------------------------")

s = 0
for val in range(1,10):
	sum = sum+val
print(sum)