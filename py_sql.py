import MySQLdb

import sys



db = MySQLdb.connect(host='MySql.aulavirtual.mx',
							user='userdb', passwd='12AB34cd*',
							db='world')

#cursordb = db.cursor()

#cursordb.execute('SELECT first_name, last_name, birth_date FROM employees WHERE birth_date BETWEEN "1965-01-01" AND "1965-12-31" AND gender="F" ')
#cursordb.execute('SELECT first_name, last_name, hire_date FROM employees WHERE hire_date BETWEEN  "1988-02-01" AND "1988-02-29" ')
#cursordb.execute('SELECT first_name, last_name, hire_date FROM employees WHERE hire_date BETWEEN "1991-01-01" AND "1991-12-31" AND gender="F" LIMIT 1 ')


def show_continent(continent):
	##hay que sumar la poblacion y los continentes

	cursordb = db.cursor()
	cursordb.execute('SELECT  Population, SurfaceArea, Continent FROM country WHERE Continent = "{0}" '.format(continent))
	res = []
	for reg in cursordb.fetchall():
		res

	return print(res)

show_continent("Asia")


def show_country(continent):

	cursordb = db.cursor()
	cursordb.execute('SELECT Name, Continent FROM country WHERE Continent = "{0}" '.format(continent))
	res = []
	for reg in cursordb.fetchall():
		res = reg[0], reg[1]

	return print(res)

#show_country("Asia")


def show_country_info(code):

	cursordb = db.cursor()
	cursordb.execute('SELECT * FROM country WHERE Code2 = "{0}" '.format(code))

	res = []
	for reg in cursordb.fetchall():
		res.append(reg)

	return print(res)


show_country_info("WS")

#i = 0
#for reg in cursordb.fetchall():
#	i+=1
#	print(reg[0], reg[1], reg[2])
#print(i)


#print(type(cursordb)) 
#cursordb.close()
db.close()



#i = 0
#for reg in cursordb.fetchall():
#	i+=1
#	print(reg[0], reg[1])

#print(i)
#cursordb.close()
#db.close()





#cursordb.execute('SELECT first_name, last_name FROM employees WHERE hire_date BETWEEN "1991-01-01" AND "1991-12-31" AND gender="F" ')

