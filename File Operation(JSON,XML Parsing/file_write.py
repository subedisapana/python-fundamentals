fp = open("input2.txt", "w")
fp.write(" write this line to a file")

#fp.write(" hey") # this flush the earlier content

fp1 = open("input2.txt", "w+")
fp1.write(" hell yes")


fp2 = open("input3.txt", "+w")
print(fp2.tell()) #initally at 0
fp2.write("sample text line 1")
print(fp2.tell())# at 18
fp2.seek(0,0) # at 0
print(fp2.tell())
content2= fp2.read() #at 18
print(fp2.tell())
print(content2)


'''
content = fp.read()
print(content)

w+ is used to perform read as well as write operation

'''

'''
tell => current fp position
seek => to chane the file position
offset => number of vhar
position => 0 => start of the file
            1 => current position
            2 => end of the filr

seek(15,0) => change the file posn by 15 charfrom start of the file
seek(0,2) => change fp by 0 char from end of the file
seek(15,1) => 
'''




'''
r+ mode: read+ write
'''

fp3 = open("input.txt", "r+")
content3=fp3.read()
print(content3)
fp3.write("\n\nSample line added using python scrip")


'''
append => adding content to existing file

r,r+, w, w+ => fb is at start
a and a+ => at the end
'''

fp4= open ("input.txt", "a")
print(fp4.tell())
content4 = fp4.write("\n\nappended text")
print(content4)

