import csv

"""
arch_csv = open('empleados.csv')
entry = csv.DictReader(arch_csv)

outCSV = open('empleados_1965_femenino.csv', 'w')
out = csv.writer(outCSV, delimiter = ',')

outCSV_2 = open('empleados_hire_1988.csv', 'w')
out_2 = csv.writer(outCSV_2, delimiter=',')

print("Writing file...")



#emp_no,birth_date,first_name,last_name,gender,hire_date
#out.writerow(['Birth Date', 'Gender'])
for line in entry:
	if '1965' in (line['birth_date']) and 'F' in line['gender']:	
		out.writerow([line['birth_date'],
			line['gender'],
			line['first_name'],
			line['last_name']])
	if '1988' in (line['hire_date']):
		out_2.writerow([line['hire_date']])


print("Process done")

outCSV.close()
outCSV_2.close()
del outCSV
"""

class Perro():

	def ladrar(self):

		return print("wuaua")

"""

csv_file = open('paises.csv')
entry  = csv.DictReader(csv_file)

#csv_outFile = open('paises_poblacion_superficie.csv', 'w')
#write_in_csv = csv.writer('csv_outFile', delimiter = ',')

print('Reading\n')

continent_input = input('Ingrese Continente')
country_code = input('country_code')
# SurfaceArea Continent
#Name
#'\ufeffCode' ABW





for line in entry:
	#if continent_input in (line['Continent']):
	#	print(line['SurfaceArea'], line['Population'])
	
	#if continent_input in (line['Continent']):
	#	print(line['Name'])
	if c in (line['\ufeffCode']):
		print(line[continent_input])	

print('Done')

csv_file.close()
#csv_outFile.close()
"""