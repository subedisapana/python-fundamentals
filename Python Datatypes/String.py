
'''
Sring
s='', " ", """ """

1.Strings are immutable
2.Strings is ordered data structure; so it supports indexing
'''


s= "Hey, Its me."
print(type(s))

s1 = "Python"
print(id(s1))

s1 = "Java"
print(id(s1))


#Indexing
s2 ="Python Sample string"
print(s2[1]) #index[0,1,2....]
print(s2[-2])

#Slicing
print(s2[0:6])
print(s2[7:])
print(s2[:6])


#Stride
print(s2[::2])
print(s2[::-2])
print(s2[::3])
print(s2[6:0])



for value in s2[::2]:
	print(value)

help(str)


ss="Sapana Subedi!"
print(ss[::4])  #Snui
print(ss[::-1]) #!idebuS anapaS
print(ss[::-2]) #!dbSaaa

'''
BuiltIn Functions'''

num1 = 100
num2 = 200
print('value of num1 is', num1,'value of num2', num2)



print("==========String Methods=========")
#string methods
#define string with a format method
print("value of num1 is {} value of num2 is {}".format(num1,num2)) #inside of place holder you can specify index

s="python sample string"
print(id(s))

s=s.capitalize() #first letter
print(s)
print(id(s)) #different memory location

print(s.isupper())
s1=s.title() #Python Sample String
print(s1)

print(s1.istitle() )
print(s1.islower())

print("==========String Methods=========")

print(s.find("sample")) #7
print(len(s)) #20






'''Split/Join'''

s2 ="HTML,CSS,PYTHON, DJANGO" #string contains comma seperated value
lis=s2.split(",")
print(lis)
print(type(lis))

s3=(" ").join(lis)
print(s3)
print(type(s3))



s1="abcd"
s2="1234"
s3="python sample string abcd"


'''maketrans/translate'''

table = str.maketrans(s1,s2)
result = s3.translate(table)
print(result)


''' index'''
s = "HTML,CSS,PYTHON, PYTHON"
print("PYTHON" in s)
print(s.index("PYTHON")) 

print(s.find("PYTHON"))

print(s.find("Python"))


''' In case of find function, if it doesnot find an element .o/p:-1
'''

s="***This is the sample string****"
s1 = s.lstrip("*")
s2 = s.rstrip("*")
print(s1)
print(s2)


x="   This is the sample string  " 
x1= x.strip(" ") # removes the space around
print(x)
print(x1)

xx = "python"
xx1 = xx.center(10,"*")
print(xx1)

xx2 = xx.ljust(10,"*")
print(xx2)


xx2 = xx.rjust(10,"*")
print(xx2)



r="html, python,DJANGO, HTML"
r1 = r.replace('html', 'HTML')
print(r1)