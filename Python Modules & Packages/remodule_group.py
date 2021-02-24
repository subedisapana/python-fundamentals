import re


#dd-mm-yy
s4 = "12-05-2018"
r4 =re.compile("^([0-9]{2})-([0-9]{2})-([0-9]{4})$")
m4=re.search(r4,s4) #it will give only one occurance
#print(m4.group())

if m4:
	print(m4.group(1)) #group is differentiated by()
else:
	print("pattern doesnot exist")




'''if there is 5 or 10 groups in a reular expression then it becomes tedious to remember so python provide a named groups here
'''

'''
s4 = "12-05-2018"
r4 = re.compile("^(?P<date>[0-9]{2})-(?P<month>[0-9]{2})-(?P<year>[0-9]{4})> $")
m4=re.search(r4,s4)

if m4:
	print(m4.group("date")) #group is differentiated by()
else:
	print("pattern doesnot exist")

'''



