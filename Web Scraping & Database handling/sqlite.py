import sqlite3

conn = sqlite3.connect("example1.db")
c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS EMP(ID INT PRIMARLY KEY, NAME, TEXT, SALARY REAL) """) 
c.execute("INSERT INTO EMP(ID, NAME, SALARY) VALUES(101, 'ABC',4000)")
c.execute("INSERT INTO EMP(ID, NAME, SALARY) VALUES(102, 'ABgC',4000)")
c.execute("INSERT INTO EMP(ID, NAME, SALARY) VALUES(103, 'gBC',4000)")
c.execute("INSERT INTO EMP(ID, NAME, SALARY) VALUES(104, 'AgBC',4000)")
c.execute("INSERT INTO EMP(ID, NAME, SALARY) VALUES(105, 'ABgC',4000)")
conn.execute("COMMIT")


c.execute("""SELECT * FROM EMP""")
#print(next(c))

for row in c:
	print(row)

print("-----------------------------------------")
c.execute("UPDATE EMP SET SALARY= 65000 WHERE ID = 102")
conn.execute("COMMIT")

c.execute("SELECT * FROM EMP WHERE ID = 102")
print(next(c))

print("-----------------------------------------")
c.execute("""DELETE FROM EMP WHERE ID = 103""")
conn.execute("COMMIT")

c.execute("""SELECT * FROM EMP""")
for r in c:
	print(r)
