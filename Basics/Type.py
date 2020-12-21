'''
DYNAMICALLY TYPED
STATICALLY TYPED
STRONG-TYPING
WEAK-TYPING
HASHABLE
UNHASHABLE

=====================================================================================================


List of immutable types: int, float, decimal, complex, bool, string, tuple, range, frozenset, bytes
A type of object that cannot be modified after it was created is called immutable object.
All immutable objects are hashable, but all hashable obj are immutable.



List of mutable types: list, dict, set, bytearray, user-defined classes
A type of object that can be modified after it was created is called immutable object.


=======================================================================================================

Dynamically typed language.
1.If the type of the variable is checked at the runtime of the code than the language 
2.Code will get interpreted/compiled even if it contain error.
3.Variable without its type is initialized.
Example: , Python,Js

Statically typed language.
1.If the type of the variable is checked at the compile-time of the code than the language 
2.Variable with its type is initialized.
Example: Java, C, C++

thing = "Hello"
print(type(thing))
#<class 'str'>


========================================================================================================

Strong-typing vs Weak-typing

Weak typing is where a language allows you to treat blocks of memory defined as one type as another (casting).
Languages like C and C++, although statically typed, are weakly typed.

Every variable in python holds an instance of an object. There are two types of objects in python 
i.e. Mutable and Immutable objects. 
Whenever an object is instantiated, it is assigned a unique object id. The type of the object is defined at the runtime and 
it can’t be changed afterwards.
However, it’s state can be changed if it is a mutable object.


TYPE CASTING
a method used for changing the variables/ values declared in a certain data type into a different data type in order to match
for the operation required to be performed by the code snippet.



==========================================================================================================

HASHABLE

Hashing changes object into number

'''

'''
x=2
hash(x) #doesn't show error so hashable

a=[1,2,4,5]
hash(a) #shows error i.e unhashable since its a list
'''

'''
Immutable Dataypes

s="hell"
s.append["o"]

x1=10

x1.append(1) #error
'''
a="hey"
hash(a)