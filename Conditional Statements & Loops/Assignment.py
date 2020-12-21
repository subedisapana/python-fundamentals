#1 WAP to find numbers which are divisible by 7 and 5, betn 1500 and 2700(both included)

for i in range(1500,2700):
	if i%7 == 0 and i%5 ==0 :
		print(i)



print("====================================================================")


'''
2 WAP to count the number of even and odd no. from the series of number.
Sample: numbers = (1,2,3,4,5,6,7,8,9)
'''
evencount=0
oddcount=0
for i in range(0,9):
	if i%2 ==0:
		evencount= evencount+1
	else:
		oddcount= oddcount+1
print("Number of even numbers", evencount)
print("Number of odd numbers", oddcount)




print("====================================================================")




'''
3. WAP which iterates the integers from 1 to 10. for multiples of 3, print"Fizz" instead of
 number and for the multiple of five, print"BUZZ. For the number which are  multiples of both 3 and 5, 
 print "FizzBuzz

Sample o/p: 
fizzbuzz
1
2
fizz
4
buzz
'''


for a in range(1,11):
	if a%3 == 0:
		print("Fizz")
	if  a%5 == 0:
	    print("Buzz")
	if  a%3 == 0 &  i%5 == 0:
		print("FizzBuzz")



print("====================================================================")

'''
4.WAP to calculate the sum and average of n integer numbers
'''




'''
5.Factorial of any number n is represented by n! & is equal to 1*2*3*...*(n-1)*n.
4!= 1*2*3*4=24
3!=3*2*1=6
2! = 2*1=2
WAP to calculate factorial of number.

'''



