'''sets
Sets are mutable
All the elements should be unique
You can add only immutable elements in the set-int, str,float, tuple

'''
s= {10, 20, 30, 40}
print(s,type(s))

s={100,200,300,400}
s.add(500)
print(s)


s1={10, 20, 30, 40}
s2={ 30, 40,50,60}

s3=s1.union(s2)
print(s3)

s4=s1.intersection(s2)
print(s4)

s5=s1.difference(s2)
print(s5)

s6=s1.symmetric_difference(s2) #except common element
print(s6)

print(s1)
s1.update(s2) #it will modify the original set s1
print(s1)

s1.difference_update(s2)
print(s1)


s1.symmetric_difference_update(s2)
print(s1)


print(s2.issubset(s1))#True
print(s2.issuperset(s1))


#COVERSION OF LIST TO SET
l=[100,200,300,400,500]
s=set(l)
print(s)




l1=[100,00,300,400,500,600]
l2=[100,200,300,400,500,00,700]
ss1=set(l1)
ss2=set(l2)
ss3=ss1.union(ss2)
print(ss3)
l3=list(ss3)
l3.sort()
print(l3)


'''Delete Operations
pop
discard
clear
del'''

se={100,200,300,400,500,700,600}
r=se.pop() #pop takes no argument;removes first element
print(se,r)

se.discard(200)
print(se)


se.clear()
print(se)