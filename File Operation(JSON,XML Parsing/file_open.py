
'''
r => read
r+
w => write
w+
a => append
a+ 
'''

fp = open("input.txt","r")
content = fp.read()
#content = fp.read(25)
print(content)
#after read() file pointer pointer is at the end. so
#even if you print content again nth is printed.

print("-------------------------------------------------------")

fp1 = open("input.txt","r")
content1 = fp1.read()
print(content1)



print("-----------------------------------------------------")
fp2 = open("input.txt","r")
content2 = fp2.readlines() #if you want to read one line at a time
print(content2[:5])

