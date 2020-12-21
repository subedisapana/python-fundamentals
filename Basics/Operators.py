#operators in python(+,-,*,/,//,%,**)
#Add, sub, div,  mul, flow div, mode


num1 = 10
num2 =20
num = num1 + num2
print(num)
print(10/3) # division #true division
print(10//3) #flow division  #only give integer of div
print(10%3) # remainder
print(10**2) #square


#2.Comparison operators <,>,<=,>=, ==, !=

num2 = 100
num3 =200
print(num2 == num3) # it will compare the value of variable, if values are same it will return True else false




#3.Identity Operators: is, is not; it compares the memory locations

print(num1 is num2) #false

lis =[10, 20,30]
lis1 =[10,20,30]
print(lis == lis1) #true, compares the value
print(lis is lis1) #false. why? beacause it compares memory location. Since list is mutable it assigns diff memo laocation
#IS: compareas memory locations as it is mutable datatypes.
print(lis is not lis1)





#4. Assignments operators; =, +=,-=, *=, /=

op1 = 100
op1 = op1 + 5
print (op1)
op1+=5
print(op1)




#5, BITWISE Operator;  & AND,| OR, ^, Right shift >>, leftshift <<, 

n11 = 2
n12 = 1
n13 = 4
print(bin(n11), bin(n12), bin(n13)) #binary representation
print(n11 & n12) # it will n11 to its binary representation
# 010  & 000
print(n11 | n12)
print(2 << 1) # shift left handside by 1 bit
#binary representation of 2 is 0b10, im sifting 1 to left and becomes 0b100
print(3 << 1) # 3 = 0011 shifting 1 to left, it becomes 0110



#6 Logical Operators; and or not

print(10 == 10 and 20 == 20) # true
print(10 == 15 and 20 == 20)
print(10 == 15 or 20 == 20)
print(not(10==10)) # complement of true is false



#7 Membership operators: in, not in

l=[1,5,7]
print(3 in l) #false
s= "Python String"
print("Python" not in s) #false

