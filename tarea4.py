

#Mes posicion 1, los meses estan guardados como numericos del 1 a 12
#Numero de vuelo
#1928

#'DepDelay  deploy time [15]

'''
['Year', 
'Month',[1]#mes
'DayofMonth',[2] #dia del mes 
'DayOfWeek',[3] 
'DepTime', 
'CRSDepTime', 
'ArrTime', 
'CRSArrTime', 
'UniqueCarrier', 
'FlightNum', 
'TailNum', 
'ActualElapsedTime', 
'CRSElapsedTime', 
'AirTime', 
'ArrDelay', 
'DepDelay', 
'Origin', 
'Dest', 
'Distance', 
'TaxiIn', 
'TaxiOut', 
'Cancelled', [21] 
'CancellationCode',[22] 
'Diverted', 
'CarrierDelay', 
'WeatherDelay', 
'NASDelay', 
'SecurityDelay', 
'LateAircraftDelay\n']
'''

print("leyendo archivo (: hagase un cafecito")
archivo = open("2008.csv", 'r')
lines = archivo.readlines()

def ejercicio_1():

	mes = input('numero de mes')
	numero_vuelo = input("numero de vuelo")
	times_done = 0
	i = 0
	
	for line in lines:
		i+=1
		if i > 1:
			str_ = line.split(',')
			if mes in str_[1] and numero_vuelo in str_[9]:
				times_done +=1
	print(times_done)


def ejercicio_2():
#el numero de vuelo con su totoal de horas y minutos retrasado
#el archivo tiene valores NA
	i = 0
	increment = 0
	mes = input('numero de mes > ')
	numero_vuelo = input("numero de vuelo > ")
	invalid = 'NA'
	for line in lines:
		i+=1	
		if i >1:
			header = line	
			str_ = header.split(',')
			if invalid in str_[15]:
				str_[15] = 0	
			if mes in (str_[1]) and numero_vuelo in str_[9]:			
				if int((str_[15])) > 0:
					time_elapsed = int(str_[15])
					increment += time_elapsed				
	hour = increment // 60
	minutes = increment % 60
	print("el numero de vuelo es > {} con un retraso de {} horas y {} minutos".format(
			numero_vuelo, hour, minutes))

i = 0
yes = 0
no = 0
for line in lines:
	i+=1
	if i > 1:
		header = line
		str_ = header.split(',')
		#this_index = str_[22]
		print(type(str_[21]))
		
		if str_[21] == '0': 
			#yes+=1
			no+=1
		if str_[21] =='1':
			yes+=1
	if i > 1000:
		break	
	#print(header)
	#break
print(yes)
print(no)


archivo.close()

#if __name__ == '__main__':
#	ejercicio_2()
