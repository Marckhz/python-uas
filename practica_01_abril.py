import csv



archivo_csv = open("estado/AGUASCALIENTES.csv", 'r')
read_archivo = archivo_csv.readlines()


#[3] municipio

municipio = []
w_0_to_9_old = [0]
total_men = []

area = []



for line in read_archivo:
	str_ = line.split(',')
	position_municipio = str_[3]
	if position_municipio in municipio:
		pass
	else:
		municipio.append(position_municipio)

	position_area = str_[7]
	if 'URBANO':
		w_0_to_9_old[0] += int(str_[13])
		m_0_to_9_old = str_[12]

		w_10_to_21_old = str_[15]
		m_10_to_21_old = str_[14]

		w_22_to_64_old = str_[17]
		m_22_to_64_old = str_[16]

		w_65_old = str_[19]
		m_65_odl = str_[18]

		if w_0_to_9_old != 0:
			#total_woman.append(w_0_to_9_old)
			#sum(total_woman)
			#total_men.append()
			pass
		if w_10_to_21_old and m_10_to_21_old != '0':
			pass

		else:
			pass


	
	#area.append(position_area)


print(len(municipio))
print(area)
print(w_0_to_9_old)






