'''
We wuse user defined function for 2 reaseons:
code resuse
Modularity: If we are logicall grouping your code into function;easy to debug, code
'''

s="Python,Html,css"
print(s.index("Html"))


#function defining, we have func call and func def


#def value_reverse(value): #fxn defn
#	reverse=value[::-1]
#	print(reverse)

#s="python"
#result=value_reverse(s) #fxn call



#l=[10,20,30,40]
#l.append(50)
#


#for list and string


def x_reverse(a):  #fxn defn
	if type(a) == list or type(a)==str:
		reverse = a[::-1]
	else:
		temp = str(a)
		reverse=temp[::-1]
	return(reverse)

x="python"
result=x_reverse(x)#fxn call
print(result)