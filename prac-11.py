


def billetes():

    

    try:
        
        cantidad = int(input("dinero > "))  

        if(cantidad > 1):
            this_change = cantidad / 1000
            this_change2 =  cantidad % 1000
            print("billetes 1000 > ", int(this_change))

                        
            this_change3 = this_change2 / 500
            this_change_3 = this_change2 % 500
            print("billetes de 500 > ", int(this_change3))

                        
            this_change4 = this_change_3 / 200
            this_change_4 = this_change_3 % 200
            print("billetes de 200 > ", int(this_change4))


            this_change5 = this_change_4 / 100
            this_change_5 = this_change_4 % 100
            print("billetes de 100 > ", int(this_change5))


            this_change6 = this_change_5 / 50
            this_change_6 = this_change_5 % 50
            print("billetes de 50 > ", int(this_change6))

            this_change7 = this_change_6 / 20
            this_change_7 = this_change_6 % 20
            print("billetes 20 >", int(this_change7) )

            this_change8 = this_change_7 / 10
            this_change_8 = this_change_7 % 10
            print("monedas de 10 > ", int(this_change8))

            this_change9 = this_change_8 / 5
            this_change_9 = this_change_8 % 5
            print("monedas de 5 pesos > ", int(this_change9))

            this_change10 = this_change_9 / 1
            this_change_10 = this_change_9 % 1
            print("monedas de 1 peso >  ", int(this_change10))
        
        else:
            print("solo se aceptan valores numeros positivos mayores que 1")


    except:
        return print("Solo se aceptan valores numericos positivos")




billetes()