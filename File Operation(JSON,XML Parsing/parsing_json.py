'''
send data to an api either json or xml format.


in json vs python, we have 

json object                      dict{"key":"value"}
numbers 10 10.5                  int float
array [10,"string"]               list
                                  tuple
" "                               ' '

'''


import json


handle = open("json_input.json", "r")
content = handle.read()
#print(content)

'''
json frovides few methods....
'''

# dict in python
d= json.loads(content)
print(d)
print(d['database']) #datbase is toplevel key
print(d['database']['port'])
d['database']['port'] = 3000
print("--------------------------above json file in python (single quote)-------------------------")

print(d)




'''

Parsing json file using python

modification in python dict

'''
print(d['files'])
print(d['files']['log']) #log key is in file key

d['files']['log'] = ("/log/app.log", "/log/mysql/app.log") #adding two values
print(d)


'''
Writing these in json file
'''

print("--------------------------json file in python dict(double quote)-------------------------")
j = json.dumps(d, indent= 4, sort_keys = True)
#print(j)
handle1 = open("json_output.json", "w")
handle1.write(j)
handle1.close()
