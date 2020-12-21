#Storing and accessing data in dictionaries...
'''
-Data is stored in a key and value pair
-Mutable data structure
-unordered data structure
-key should be unique
-key should be immutable
-When we create a dict it will create a hash table using key and the value so retrival of value 
using dict is much faster than list 
-from hash table it will fetch data
-key only allows data structure-(int,strings,tuple,float); Dictionary only allows immutable data type as a key
-mutable data structure is not hashable
-There should be unique key; if key is same then it just update value.
'''

d={"emp_id":101,
   "name":"ABC",
   "email":"abc@gmail",
   "name":"CDE"
   }
#There must be unique key

print(d,type(d))

d["contact_no"] = 8888
print(d )

d["contact_no"] = 12345
print(d)

print(d["email"])


#get
#setdefault function

print(d.get("name"))
print(d.get("age",-1)) # Since there is no age as a key, it returns given value
print(d.get("age","key doesnot exist")) 
print(d.setdefault("age"))
print(d)

d1={"emp_id":101,
   "name":"CDE"
   }
print(d1.setdefault("emp_id")) #101
print(d1.setdefault("age")) #None
print(d1)

print(d1.setdefault("Roll",50))
print(d1)

#Incase of set default if there doesn't exist a key then it provides default value as None


for v in d1:
	print(v, d1[v])


#1:1, 2:4, 3:9, 4:16....10:100
d={} #empty dict
for value in range(1,11):
	d[value] = value*value

print(d)

'''
Functions
keys
value
Items
'''
#If you want all the keys, value and items

print(d.keys())
print(d.values())
print(d.items())


for t in d.items():
	print(t)



#Add, Update and Delete Operations

l1=[1,2,3,4,5] #key
l2=[1,2,9,16,25] #value

di=dict(zip(l1,l2)) #combines elements having same index
print(di)


l= [1,2,3,4,5]
d=dict.fromkeys(l,0) #it assigns none value in value
print(d)


d1 = {1:1,2:4, 3:9}
d2 = {4:16,5:25, 6:36}
d1.update(d2)
print(d1)

'''Delete items in dict
we have pop,popitems,del,clear'''

d3 = {1:1,2:4, 3:9}
r=d3.pop(2)# takes key as an argument
print(d3, r) #1: 1, 3: 9} 4



d4 = {1:1,2:4, 3:9}
r1= d4.popitem() #you are not specifying any key value
print(d4, r1) #{1: 1, 2: 4} (3, 9)


d4 = {1:1,2:4, 3:9}
d4.clear()
print(d4)