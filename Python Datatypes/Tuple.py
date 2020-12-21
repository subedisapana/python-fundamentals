'''
Tuple

immutable data structure: i cannot add update, modify the value in tuble
ordered indexing and slicing

'''

t=(10,20,30,303,20,20, 30,40 )
print(t,type(t))
#help(tuple)

print(t[1])
print(t[:3])



#In tuple we have only 2 methods i.e index and count

print(t.index(20)) #only return first element
print(t.count(20))


l=[10,20,30,40,50]


for index,value in enumerate(l):
	print(index,value) #it will give index as well as value pair


#Conversion of list into tuple and vice versa
l=[10,20,30,40,50]
t = tuple(l)
print(t)


t=(10,20,30,40,50,"a","b")
l=list(t)
print(l,type(l))

