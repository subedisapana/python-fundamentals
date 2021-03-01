'''
iterators are much more better in case of time and space complexcit'''


l =[10,20,30,40,50]
i= iter(l)
#print(i)
#print(next(i))
#print(next(i))


#for val in i:
#	print (val)


import itertools

l1=[10,20,30,40,50,60]
l2=[100,200,300,400,500,600]
l3 = [1000,2000,3000,4000,5000,6000]

i= itertools.chain(l1,l2,l3)
#print(i)
#print(next(i))
#print(next(i))

#for value in i:
#	print(value) #iterates over all 3 list

'''
l4=[10,20,30,40,50]
count = 0
for value in itertools.cycle(l):
	if count<20:
		print(value)
	else:
		break
	count+=1
'''

#if we want multible obj of the same iterator


l=[10,20,30,40]

i = iter(l)
t= itertools.tee(i) # tee is the method of iter
print(t)

for value in t[0]:
	print(value)


for value in t[1]:
	print(value)



'''itertools.chain()
itertools.isslice()
itertools.permutations()
itertools.combinations()


'''