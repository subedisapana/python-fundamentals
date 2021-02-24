'''Regular expression



A Regular Expression (RE) in a programming language is a special text string used for describing a search pattern. 
It is extremely useful for extracting information from text such as code, files, log, spreadsheets or even documents.

For regular expression, we have certain meta character:

.(dot)- matches with any character be it alphabet, be it special character except new line
[a-z](character class)- matches with char class a or b or c or..
[0-9]- matches with digit class 0 or class 1 or 2... or 9

+ - atleast one [a-z]+
* -  Zero or more

^ - to match start of the string
$ - for the end of the string

? - optional
[a-z]{4} this means there has to be four occurance of characters

[a-z]{2, 4} It excepts atleast 2 and atmost 4 character


'''


'''
Regular Expression Methods

re.match(): It searchs the re pattern and return the first occurance
            The Python RegEx Match method checks for a match only at the beginning of the string. 
            So, if a match is found in the first line, it returns the match object.
            But if a match is found in some other line, the Python RegEx Match function returns null.
            The expression "w+" and "\W" will match the words starting with letter 's' and thereafter, anything which is not started with 's' is not identifie


'''



import re

list1=["sap1 sub", "sap2 sub", "sap bub1"]


for i in list1:
	z=re.match("(s\w+)\W(b\w+)", i) # expression starting with s, 

	if z:
		print((z.groups()))


'''
re.search():
re.search() function will search the regular expression pattern and return the first occurrence. 
Unlike Python re.match(), it will check all lines of the input string. 
The Python re.search() function returns a match object when the pattern is found and “null” if the pattern is not found
'''


import re

patterns= ['sapana subedi' , 'sangita23 panta', 'geeta']
text = 'is geeta a girl?'

for pattern in patterns:
	print('looking for "%s" in "%s" ->' % (pattern, text), end=' ' ) #%s

	if re.search(pattern, text):
		print('found a match!')
	else:
		print('no match')



'''
re.findall():
findall() module is used to search for “all” occurrences that match a given pattern. 
In contrast, search() module will only return the first occurrence that matches the specified pattern. 
findall() will iterate over all the lines of the file and will return all non-overlapping matches of pattern in a single step.


For example, here we have a list of e-mail addresses, and we want all the e-mail addresses to be fetched out from the list, we use the method re.findall() in Python. 
It will find all the e-mail addresses from the list.


'''

import re

abc = 'sap@gmail.com, ssa@gmail.com, bsam@gmail.com'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', abc)

for email in emails:
	print(email)


#You want to validate whather the PAN number is valid or not

s="ABCDE1234A" #valid
r = re.compile("[A-Z]{5}[0-9]{4}[A-Z]{1}")
l= re.findall(r,s)
print(l) 


s1="AAAABCDE1234A" #valid
r1 = re.compile("[A-Z]{5}[0-9]{4}[A-Z]{1}")
l1= re.findall(r1,s1)
print(l1) 

s1="AAAABCDE1234A" #invalid
r1 = re.compile("^[A-Z]{5}[0-9]{4}[A-Z]{1}")
l1= re.findall(r1,s1)
print(l1) 



#phone number
s3= "9845412345"
r3= re.compile("[4-9]{5}[1-5]{5}")
l3 = re.findall(r3,s3)
print(l3)


# In phone number,  i want to show +977 as optional
s5="+977 8123456789"
r5= re.compile("(?:\+977\s)?([0-9][0-9]{9})") # here ?: specifies non capturing group
#r5= re.compile("(?:\+977\s)?[9][0-9]{9}")
m5= re.search(r5,s5)

if m5:
	print(m5.group(0))
else:
	print("not found")

#dd-mm-yy
s4 = "12-05-2018"
r4 =re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
l4 = re.findall(r4, s4)
print(l4)


'''
instead of writing 
[0-9] we can write \d
[^0-9] : ^compliment, we can write \D
[a-zA-Z0-9] we can write \w
\W : compliment

space \s , other than space \S








'''
