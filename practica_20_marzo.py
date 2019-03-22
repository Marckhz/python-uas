import numpy as np
import csv
import sys
from numpy import matrix

"""

Code,Name,Continent,Region,SurfaceArea,IndepYear,Population,LifeExpectancy,GNP,GNPOld,LocalName,GovernmentForm,HeadOfState,Capital,Cod
"""


csv_file = open("paises.csv", "r")
entry = csv.DictReader(csv_file)

new_csv = open("Asia.txt", 'w')
this_csv = csv.writer(new_csv, delimiter=',')

north_csv = open("norht.txt", "w")
this_csv_2 = csv.writer(north_csv, delimiter=',')

def filter_continent(continent_1, continent_2):

	for line in entry:
		
		if continent_1 in line["Continent"]:
			area = line["SurfaceArea"]
			population = line["Population"]
			LifeExpectancy = line["LifeExpectancy"]
			if LifeExpectancy == "NULL":
				LifeExpectancy = 0

			this_csv.writerow([area, population, LifeExpectancy])

		if continent_2 in line["Continent"]:
			area = line["SurfaceArea"]
			population = line["Population"]
			LifeExpectancy = line["LifeExpectancy"]
			if LifeExpectancy == "NULL":
				LifeExpectancy = 0	

			this_csv_2.writerow([area,population, LifeExpectancy])

filter_continent(sys.argv[1],sys.argv[2])


arreglo_Asia = np.loadtxt("Asia.txt", delimiter=',')
arreglo_North = np.loadtxt("norht.txt", delimiter=',')

print(arreglo_Asia)
print(arreglo_North)

m = arreglo_Asia * arreglo_North

print(m)
#print("datos > ", matriz.ndim)

