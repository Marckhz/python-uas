import MySQLdb

import sys



db = MySQLdb.connect(host='MySql.aulavirtual.mx',
							user='userdb', passwd='12AB34cd*',
							db='employees')

cursordb = db.cursor()

#cursordb.execute('SELECT first_name, last_name, birth_date FROM employees WHERE birth_date BETWEEN "1965-01-01" AND "1965-12-31" AND gender="F" ')
#cursordb.execute('SELECT first_name, last_name, hire_date FROM employees WHERE hire_date BETWEEN  "1988-02-01" AND "1988-02-29" ')
cursordb.execute('SELECT first_name, last_name, hire_date FROM employees WHERE hire_date BETWEEN "1991-01-01" AND "1991-12-31" AND gender="F" ')

i = 0
for reg in cursordb.fetchall():
	i+=1
	print(reg[0], reg[1], reg[2])
print(i)


cursordb.close()
db.close()



#i = 0
#for reg in cursordb.fetchall():
#	i+=1
#	print(reg[0], reg[1])

#print(i)
#cursordb.close()
#db.close()





#cursordb.execute('SELECT first_name, last_name FROM employees WHERE hire_date BETWEEN "1991-01-01" AND "1991-12-31" AND gender="F" ')

