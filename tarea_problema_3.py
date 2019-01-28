
def creditos():

   cantidad  = int(input("prestamo de "))
   tasa = int(input("porcentaje de interes "))
   
   plazos = int(input("cuantos plazos? >"))
   interes = cantidad / tasa

   prestame_final = 0
   acumulador = 0
   acumulador = interes / cantidad
   total = cantidad * acumulador 
   
   final = cantidad * 1.10**plazos
   print(final)    



creditos()