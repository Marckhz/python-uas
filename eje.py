import csv

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
