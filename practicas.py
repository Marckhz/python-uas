
import math



#22 junar 2019

############
#Triangulos# 
############

"""
lado_1 = int(input("lado 1:  "))
lado_2 = int(input("lado 2:  "))
lado_3 = int(input("lado 3:  "))

if lado_1 == lado_2 and lado_1 == lado_3:
    print("es equilatero ")

elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    print("es isoceles")

else:
    print("es escaleno")

"""


#################
#Dolares a Pesos# 
#################

"""
dolar = 20
pesos = int(input("ingrese cantidad de dolares"))
for i in range(1, pesos+1):
    total = dolar * i
    print("dolar ", i, " ", "peso", total)

"""

######
#Suma#
######


"""

def int_values(a, b):
    a = int(input("valor 1 > "))
    b = int(input("valor 2 > "))

    return a, b


def suma(a,b):

    
    return print(a + b)

def suma2():

    a = int(input("valor 1 > "))
    b = int(input("valro 2 > "))

    c  = a + b
    return c


def division(x,y):
    return print(x / y)
"""


"""
def suma_for(*args):
    s = 0
    for i in args:
        s+=i
    return print(s)
"""

def volumen_sphere(a = 4/3, pi = math.pi):

    try:
        r = float(input(" introduce el radio : "))
        radio_Sqrt = math.pow(r,3)
        volumen = (a * pi) * radio_Sqrt 
    
        return print("el volumen es > ",  volumen)

    except:
        print("solo se aceptan numeros :V")

    return None
    





def factorial(res = 1):

    num = int(input("ingresa el numero > "))
    for i in range(1, num+1):
        res = res * i
    return print(res)

def my_aveg():

    var = int(input("numero > "))
    empty = []
    for i in range(var):
        i = int(input("var > "))
        empty.append(i)
        sum_vec = sum(empty)/len(empty)
    return print(sum_vec)   

        
class Circulo(object):
    def __init__(self, radio):
        self.radio = radio
    
    def Obetner_area(self):
        return pi.math * self.radio ** 2

    def obetner_permitro(self):
        return 2 * pi.math * self.radio


def f_clase():   

    try:
        r = float(input(" introduce el radio : "))
        circulo = Circulo(r)
        print("el area es > ",  circulo.Obetner_area() )
        print("permietro es >", circulo.obetner_permitro() )

    except:
        pass
    return None


    



if __name__ == "__main__":
    #suma_for(1,1,1,1,1)
    #volumen_sphere()
    #factorial()
    #my_aveg()
    f_clase()


