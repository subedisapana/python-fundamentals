'''factorial(5)= 5*fact(4)
                      4 * fact(3)
                           3 * fact(2)
                                     2* fact(1)
                                             1
                                             '''




def factorial(num):
    if num == 1:
        return 1
    else:
    	return num*factorial(num-1) #4*3!


num1=4 #4*3*2*1
result = factorial(num1)
print(result)  




'''Binary Search
mid element is compared with the key if the 700 is greater or samaller than mid is compared with key'''



def binary_search(l,key):
    mid = len(l) // 2

    if l[mid] == key:
        return True

    elif key < l[mid]:
        return binary_search(l[:mid], key)

    else:
        return binary_search(l[mid+1:], key)


l= [100,200,300,400,500]
key = 500
result= binary_search(l, key)
print(result)


'''
Algorithm:
l= [100,200,300,400,500]
1)findin out mid element
mid=300
2)then comparing key value with the did value of the list
3)if key> mid then, take all the element from the lis
[400,500]
mid=2/2= 2 =500 ==500 true
'''