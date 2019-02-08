#/user/bin/python3

import math

#Hernandez Inzunza Marco Cesar 4-1


print("#############################")
print("### Ejercicio numero uno ###")
print("##############################")

def numero_de_permutaciones(num):

    fac = 1
    for i in range(1, num+1):
        fac = fac * i
    return fac

def permutaciones(n, m):
    perm = numero_de_permutaciones(n)/numero_de_permutaciones(n-m)
    return perm

def combinaciones(n,m):
    comb = numero_de_permutaciones(n)/numero_de_permutaciones(n-m) * numero_de_permutaciones(m)
    return comb

def vec_para():

    vector = []
    elementos = int(input("cuantos elementos a capturar > "))
    for i in range(elementos):
        numeros = float(input("insertar elemento por favor > "))
        vector.append(numeros)   
    return vector

def fmedia(vector):
    
    media = sum(vector)/ len(vector)
    print("La media es > ", media) 
    return media

def dev_Stand(media, vector):
     
    vec3 = []
    for elemento in range(len(vector)):
        elemento = vector[elemento]
        resultado = (elemento - media) ** 2
        vec3.append(resultado)  
        zigma = sum(vec3)
    sqrt_ = math.sqrt(zigma/ len(vector))
    print("La desviacion estandar es > ", sqrt_)
    return sqrt_

def media_sqrt(vector):

    cuad = []
    for elemento in range(len(vector)):
        elemento = vector[elemento] ** 2
        cuad.append(elemento)       
    vec_sum = sum(cuad)
    media_cuad = math.sqrt(vec_sum/len(vector))
    print("La media cuadratica es >", media_cuad)

    return media_cuad

def num_finder():

    print("\n")
    print("#############################")
    print("### Ejercicio numero Tres ###")
    print("##############################")
    print("Presione Q para dejar de capturar y proceder a buscar el numero")
    
    vector = []
    loop_controler = False
    while loop_controler != True:
        try:
            args = float(input("numero > "))
            vector.append(args)
            if(vector[-1] == 'Q'):
                loop_controler = True
        except ValueError as Error:
            loop_controler = True 
    if loop_controler != True:
        return "ese no esta permitido"
    else:
        to_find = float(input("Que numero desea buscar? > "))
        appeard = vector.count(to_find)

        return print("Cantidad de veces que aparecio > ", appeard)

def fwrapper():

    print("\n")
    print("#############################")
    print("### Ejercicio numero dos ###")
    print("##############################")

    try:
        vector = vec_para()
        media_ = fmedia(vector)
        dev_stand = dev_Stand(media_, vector)
        media_sqrt_ = media_sqrt(vector)
        
    except ValueError:
        print("Solo valores numericos")

if __name__ == "__main__":
    print("numero de combinaciones", combinaciones(5,2))
    print("numero de permutaciones", permutaciones(5,2))
    fwrapper()
    num_finder()
