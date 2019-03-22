

txt_file = open('peliculas.txt', 'r')

lines = txt_file.readlines()



for line in lines:
	print(line)