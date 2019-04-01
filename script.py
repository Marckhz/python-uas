import requests
import csv 
import sys
import pprint


def star_wars_catalog(arg):

	i = 1
	while i <=arg:

		url = "https://swapi.co/api/people/?page=%d"%i
		star_wars_request = requests.get(url)

		if star_wars_request.status_code == 200:
			#print("working like a charm ", star_wars_request.status_code)
			pass
		else:
			print("upps..check something", star_wars_request.status_code)

		json_star_wars_requests = star_wars_request.json()

		for index in json_star_wars_requests["results"]:
			characters = index["name"], index["gender"], index["height"]		
			characters_strings = ','.join(characters)
			print(characters_strings)
			with open("starwars_characters.csv", 'a') as csv_file:				
				write_file = csv.writer(csv_file)
				write_file.writerow([characters_strings])

		i+=1

if __name__ == '__main__':
	print("""
		La api de star wars itera por paginas, por favor introduce cuantas paginas quieres iterar
		para asi obtener N cantidad de personajes y escribirlos despues en un archivo CSV.
		""")
	wars = int(input("cantidad de paginas a iterar > "))
	star_wars_catalog(wars)
