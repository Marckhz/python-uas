import csv
import os

archivo_csv = open("caracteristicas_demograficas_PSC_20181.txt", 'r', encoding = "ISO-8859-1")
my_csv = archivo_csv.readlines()

'''


Realmente No estoy seguro si este paso era necesario. Creo que NO
Bien pude haber simplemente hecho lo de abajo... 


def convert_in_comas(file):

for line in  my_csv:
	fields_by_comma = line.split('|')
	print(fields_by_comma[1])

	join_strings = ','.join(fields_by_comma)
	print(type(join_strings))
	with open("demograficas_csv.csv", 'a') as csv_file:
		csv_file.write(join_strings)
'''


nuevo_csv = open("demograficas_csv.csv", 'r')
my_csv = nuevo_csv.readlines()
estado = []

for line in my_csv:
	split_ = line.split(',')

	name_estado = split_[1]
	join_strings = ','.join(split_)

	if name_estado in estado:
		estado.pop()
	else:
		estado.append(name_estado)

		for index in estado:
			if index in name_estado:
				with open(os.path.join('estado/', "%s.csv" % index), 'a') as csv_file:
					csv_file.write(join_strings)
		estado.pop(0)

del estado #Liberando memoria porque pues #Yee