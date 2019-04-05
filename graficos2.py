import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 


df = pd.read_csv("2008.csv")

#Podria agregar una columna donde sea Si Y No.
#Para mes con retraso y un si  y un no.
data_frame = df['DepDelay']> 0 &, df['Month']



print(data_frame)

'''
list_= []
lista = []

for index in dep_delay:
	if index == False:
		list_.append(index)
	else: 
		lista.append(index)

print("cantidad de vuelos con despegue a tiempo", len(list_))
print("cantidad de vuelos con retraso, ", len(lista))
'''
