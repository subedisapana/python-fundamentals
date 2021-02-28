# square of list and storing in another list

l= [100,200,300,400,500,600]
l1=[]

for i in l:
	l1.append(i*i)
print(l1)


#Similarly using list comprehension

l2= [100,200,300,400,500,600]
l3=[value*value for value in l2]
print(l3)


#Sum of all the elements

l4 = [10,20,30,40,50,60]
l5 = []
sum=0
for v in l4:
	sum=sum+v
l5.append(sum)
print(l5)


# only even number

l6=[10,20,30,40,50,60,65,70,85]

l7=[val for val in l6 if val%2 == 0]
print(l7)
   
#length
l11=['abc', 'abcd', 'abcde', 'zzzz']
l12= [len(j) for j in l11]
print(l12)


#nested loop

l13 = [(value1,value2) for value1 in range(1,5) for value2 in range(100,103)]
print(l13)
