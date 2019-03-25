import statistics as stats
import csv
import sys
edades = [22, 23, 26, 26, 26, 34, 34, 38, 40, 41]


archivo_csv = open("paises.csv",'r')
read_csv = csv.DictReader(archivo_csv)

ciudades_csv = open("ciudades.csv", 'r')
read_ciudades_csv = csv.DictReader(ciudades_csv)



city_population = []


def filter_city_by_code(code):

	for line in read_ciudades_csv:
		if code in line['CountryCode']:
			population = float(line['Population'])
			if population == "NULL":
				population = 0
			city_population.append(population)


filter_city_by_code(sys.argv[1])


print(stats.mean(city_population))
print(stats.variance(city_population))
print(stats.median(city_population))


print(city_population)



area_continent= []
population_continet = []
life_expectation_contient = []


def filter_continent():

	for line in read_csv:
		if line['Continent']:
			area = float(line['SurfaceArea'])
			population = float(line['Population'])
			life_expectation = line['LifeExpectancy']
			if life_expectation == "NULL":			
				life_expectation = 0


			area_continent.append(area)
			population_continet.append(population)
			life_expectation_contient.append(float(life_expectation))


filter_continent()

#print(life_expectation_contient)
#print(area_continent)

print(stats.mean(area_continent))
print(stats.median(area_continent))
print(stats.variance(area_continent))

#print(population_continet)
print(stats.mean(population_continet))
print(stats.median(population_continet))
print(stats.variance(population_continet))

print(stats.mean(life_expectation_contient))
print(stats.median(life_expectation_contient))
print(stats.variance(life_expectation_contient))



