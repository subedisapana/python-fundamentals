import xmltodict


handle = open("xml_input.xml","r")
content = handle.read()
#print(content)
print("-------------------------------------------------------")

d= xmltodict.parse(content)
print(d)
print(d['Result']['RequestCode'])

d['Result']['RequestCode']= 4
print(d)

print("-------------------------------------------------------")
x= xmltodict.unparse(d)
print(x)