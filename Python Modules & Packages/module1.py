'''
DocString: this module includes binary search implementation '''




def binary_search(l,key):

	""" 
	Binary search: input a list and a key
	return True if key exists or else return False """

	if len(l)==0:
		return False
	else:
		mid =len(l)//2
		if l[mid] == key:
			return True

		elif key < l[mid]:
			return binary_search(l[:mid],key)
		else:
			return binary_search(l[mid+1:],key)


#print(__name__) 
'''It is a special variable & provides the functionality of main. 
Python stores the name of a current module as a main'''


if __name__ == '__main__':

	l=[10,20,30,40,50]
	key=50
	result = binary_search(l, key)
	print(result)




