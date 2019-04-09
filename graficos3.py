import matplotlib.pyplot as plt
import csv
import numpy as np

archivo_csv = open("caracteristicas_demograficas_PSC_20181.txt", "r", encoding = "ISO-8859-1")
entrada = csv.DictReader(archivo_csv, delimiter='|')

'''
CVE_EDO|NOM_EDO|CVE_MUN|NOM_MUN|CVE_LOC|NOM_LOC|CVE_INEGI|AREA|INT_HOM|INT_MUJ|INF_HOM|INF_MUJ|HOM_0_9|MUJ_0_9|HOM_10_21|MUJ_10_21|HOM_22_64|MUJ_22_64|HOM_65|MUJ_65
'''



estado = input("estado > ")


mujer = []
#hombres = []


municipio = []

for reg in entrada:

	if reg['NOM_EDO'] == estado:
		mun = reg['NOM_MUN'], 
		hombres = reg['INT_HOM']
		mujeres = reg['INT_MUJ']
		if mun in municipio:
			pass
		else:
			municipio.append(mun)
			mujer.append(int(mujeres))
			sum(mujer)


lenght = len(municipio)
np_r = np.arange(lenght)

print(mujer)
print(municipio)

plt.xticks(np_r, municipio)

plt.bar(np_r, mujer)
plt.show()