'''
much more faster than comprehension function'''



def sqr(num1):
	return num1**2


l = [10,20,30,40,50]
result = list(map(sqr,l))    #function as an argument
print(result) # we will get map object


#or value in result:
#print(value)




def add(num1, num2):
	return num1+num2

l1=[100,200,300,400]
l2=[10,20,30,40,50]

result = list(map(add,l1,l2))
print(result)


'''filter'''
def check_num(num1):
	if num1 % 2 == 0:
		return True
	else:
		return False


l3= [100,20,300,4000,500]
result1= list(filter(check_num, l3))
print(result1)



'''
lamda
'''

l4=[1,2,3,4,5]

r= list(map(lambda num1: num1**2, l4))
print(r)



d= {8:50, 3:40, 5:10, 1:20}

l6= sorted(d.items()) #sort in accordance to key
print(l6)




d1={ 3:40, 5:10, 1:20}

lp=sorted(d1.items(),key= lambda x:x[1]) #sorting on the basis of value pair
print(lp)