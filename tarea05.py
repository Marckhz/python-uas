

"""
CVE_EDO|NOM_EDO|CVE_MUN|NOM_MUN|CVE_LOC|NOM_LOC|CVE_INEGI|AREA|INT_HOM|INT_MUJ|INF_HOM|INF_MUJ|HOM_0_9|MUJ_0_9|HOM_10_21|MUJ_10_21|HOM_22_64|MUJ_22_64|HOM_65|MUJ_65
0		1		2		3		4		5		6			7	8		9		10		11		12		13		14			15		16			17		18		19		
"""


import csv, operator, os, sys



csv_file = open("csv_tara05.txt")
entry = csv_file.readlines()


total_men = []
total_woman = []

dic = {}

this_state =[]
salidaCSV = open("salida.csv", "w")
salida = csv.writer(salidaCSV)

for line in entry:

	split_fields = line.split('|')
	salida.writerow(split_fields)
salidaCSV.close()

open_Salida = open("salida.csv", 'r')
salida2 = csv.DictReader(open_Salida)

data = []

for reg in salida2:
	new_data = reg['NOM_EDO'], int(reg['INT_HOM']), int(reg['INT_MUJ'])
	data.append(new_data)

new_dic_hombres = {}
new_dic_mujeres = {}

for state, man_pob, woman_pob in data:
	total_men = new_dic_hombres.get(state, 0) + man_pob	
	new_dic_hombres[state] = total_men

for state, man_pob, woman_pob in data:
	total_woman = new_dic_mujeres.get(state, 0) + woman_pob
	new_dic_mujeres[state] = total_woman

open_Salida.close()
print("Hombres > ", new_dic_hombres.items())
print("Mujeres > ", new_dic_mujeres.items())

open_Salida = open("salida.csv", 'r')
salida2 = csv.DictReader(open_Salida)


data_ = []

for reg2 in salida2:
	print( reg2["NOM_EDO"], int(reg2['HOM_0_9']), int(reg2['MUJ_0_9']), int(reg2['HOM_10_21']), int(reg2['MUJ_10_21']), int(reg2['HOM_22_64']), int(reg2['MUJ_22_64']))

open_Salida.close()

open_Salida = open("salida.csv", 'r')
salida2 = csv.DictReader(open_Salida)


rural = []
urbana = []
semi_urbana = []

for reg3 in salida2:
	zone = reg3['AREA']

	if "RURAL" in zone:
		rural.append(zone)

	if "SEMIURBANO" in zone:
		semi_urbana.append(zone)

	if "URBANO" in zone:
		urbana.append(zone)

print("cantidad de viviendas rurales > ", len(rural))
print("cantidad de viviendas urbanas > ", len(urbana))
print("Cantidad de viviendas semi urbanas > ", len(semi_urbana))

open_Salida.close()

open_Salida = open("salida.csv", 'r')
salida2 = csv.DictReader(open_Salida)


list_dic = list(salida2)
list_ord_dic = sorted(list_dic, key = operator.itemgetter('AREA'), reverse = False)

for registro in list_ord_dic:
	print(registro['NOM_EDO'], registro['AREA'])


open_Salida.close()

def municipio(clave):

	open_Salida = open("salida.csv", 'r')
	salida2 = csv.DictReader(open_Salida)

	for registro in salida2:
		#clave = ['CVE_EDO']

		if clave in registro['CVE_EDO']:
			print(clave, registro['NOM_EDO'], registro['NOM_MUN'], registro['INT_HOM'], registro['INT_MUJ'])

	open_Salida.close()

municipio(sys.argv[1])