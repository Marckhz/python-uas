#/usr/bin/python3

import math
import random
import csv
from os import system


class Esfera():

    def __init__(self, radio):
       self.radio = radio
       
    def volumen(self):

        vol = 4/3*math.pi*self.radio**3
        return vol

    def area(self):
        
        area = 4*math.pi*self.radio**2
        return area

class Estadistica():

    """ a implementar leer un archivo CSV para calcular las desviaciones"""

    def __init__(self, *vector):
        self.vector = vector

    def fmedia(self):
    
        self.media = sum(self.vector)/ len(self.vector)
        return float(self.media)


    def dev_Stand(self):
     
        vec3 = []
        for elemento in range(len(self.vector)):
            elemento = self.vector[elemento]
            resultado = (elemento - self.fmedia() ) ** 2
            vec3.append(resultado)  
            zigma = sum(vec3)
        sqrt_ = math.sqrt(zigma/ len(self.vector))
        return sqrt_


    def media_sqrt(self):
            
        cuad = []
        for elemento in range(len(self.vector)):
            elemento = self.vector[elemento] ** 2
            cuad.append(elemento)       
        vec_sum = sum(cuad)
        media_cuad = math.sqrt(vec_sum/len(self.vector))
        #print("La media cuadratica es >", media_cuad)

        return media_cuad



stat = Estadistica(1,2,3,4,5,6,7,8)
print("la desviacion es > ", stat.dev_Stand() )
print("la media cuadratica es > ", stat.media_sqrt() )



#esfera = Esfera(5)
#print("El volumen es ", esfera.volumen() )
#print("EL area es ", esfera.area() )



"""Hacer funcion para crear samples"""

#rand = random.sample(range(300), 100)
#print(rand)

#with open('sample.csv', 'w', newline='') as csvfile:
#    sampler = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
#    sampler.writerow(rand)


