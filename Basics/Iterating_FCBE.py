#BREAK | CONTINUE | ENUMERATE

l = [10, 40, 30, 40]

#key = 4
#for value in l:
#	if value == key:
#		print("Element found")
#print("not found") #not found

#key = 40
#for v in l:
#    if v == key:
#        print("Element Found")
#        break
#    else: 
#    	continue

key = 400
for v in l:
    if v == key:
        print("Element Found")
        break
    else: 
    	#continue
    	pass
    	print("Stmt after continue statement")
else:
	print("Element Not Found")

#print("Statement outside the loop")

		

#ENUMERATE
#position of element-index for that we have enumerate function
#Enumerate function provide function with a value and index.

l1=[10,15,20,25,10]
k= 25

for index, i in enumerate(l1):
	#print(index,value)

    if i == k:
        print("Element Found at index", index)
        break
    else: 
    	continue

	