'''
str.format() is one of the string formatting methods in Python3, 
which allows multiple substitutions and value formatting. 
This method lets us concatenate elements within a string through positional formatting.

Syntax: { } { } .format(value1, value2)

'''

print ("{}, How are you?".format("Sapana")) 
  
# using format option for a value stored in a variable 
str = "This project is done with {} Programming Language"
print (str.format("Python")) 
  
# formatting a string using a numeric constant 
print ("Hello, I am {} years old !".format(18))  

print("===========================================================")



'''
Formatters with Positional and Keyword Arguments :
Syntax : {0} {1}.format(positional_argument, keyword_argument)

'''

print("{0} love {1}!!".format("I","you")) 
  
# Reverse the index numbers with the 
# parameters of the placeholders 
print("{1} Love {0}!!".format("Me","You")) 
  
# Keyword arguments are called by their keyword name 
print("{a} is a {0} science portal for {1}".format("computer", "ooooo", a ="helll")) 


print("===========================================================")


