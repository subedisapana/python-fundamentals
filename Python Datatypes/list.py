
'''
lists are mutable(that is you are modifying the value at the same location, there will be methods to add, edit,update and modify
ordered : it supports indexing and slicing
Heterogenous datatype: I can store any type of data in a list.(not mandatory), we can add lists into list as well
Basically it allows us to store any type of data
'''


l= [10,20,30,40]
print(l,type(l))



#Heterogeneous
l1=[10,20,30,'sapana','subedi',[100,200,300]]
print(l1)
print(l1,type(l1))


#indexing and slicing
l2=[10,20,30,'sapana','subedi',[100,200,300]]
print(l2[-1])

print(l2[-1][1])
print(l2[::-1]) #reverse the list

l3=[10,20,30,40,50]

for value in l3[::2]: #[start,end,step]
	print(value)



l3.append(60)
print(l3)

#if you want to add multiple element, you can add extend method
l4=[10,20,30,40,50]
l4.append([70,80,90]) #if we append,it will add entire list [70,80,90]
print(l4)


l5=[10,20,30,40,50]
l5.extend([70,80,90]) #extend add all the elements in list
print(l5)


l6=[10,20,30,40,50]
l6.extend("Python")
print(l6)


l7=[10,20,30,40,50]
l7.insert(1,1000)
print(l7)


l8=[10,20,30,40,50]
l9=l8.copy()
print(id(l8),id(l9))
print(l9)

#But.......

l11=[10,20,30,40,50,60,70]
l11.append(80)
print(l11)



'''
Update/Delete Operations
'''
ls=[10,20,30,40,50]
ls[2] = 3000 #update
print(ls)



'''
pop
remove
clear
del
'''

ls1=[10,20,30,40,50]
ls2=ls1.pop(-2)
print(ls1,ls2)


ls3=[10,20,30,40,50]
ls3.remove(20)
print(ls3)

ls4=[10,20,30,40,50]
ls4.clear() #clear the list
print(ls4)


ls5=[10,20,30,40,50]
#del ls5
print(ls5)

#Builtin functions for list
'''sort,reverse,'''

srt=[50,60,60,20,50,10]
srt.sort() #[10, 20, 50, 50, 60, 60]
print(srt)

srt1= sorted(srt) #return in list, it works in any data type be it list,tuple,
print(srt1)

count1=[50,60,60,20,50,10]
count1.count(60)
print(count1)


'''concatination'''
l=[10,20,30,40]
l2=[100,20]
print(l+l2)

l3=[.1]
print(l3*10)
