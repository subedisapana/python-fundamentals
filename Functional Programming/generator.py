'''
def printVal(l):
	for value in l:
		print(value)


l = [10,20,30,40,50,60]
printVal(l)
'''

def fibo():
	first_num = 0
	sec_num = 1
	while(True):
		next_val = first_num + sec_num
		yield next_val
		first_num, sec_num = sec_num, next_val


g= fibo()

print(next(g))
print(next(g))
print(next(g))
print(next(g))