


def billetes():

    cantidad = int(input("dinero > "))

    if (cantidad >=1000):
        this_change = cantidad / 1000
        this_change2 =  cantidad % 1000
        print("billetes", int(this_change),  "residuo",this_change2)

        if(this_change2 >= 500 and this_change2 <= 999):
                
            this_change3 = this_change2 / 500
            this_change_3 = this_change2 % 500
            print("billetes de 500 > ", int(this_change3), "residuo > ", this_change_3)

            if(this_change_3 >=200 and this_change_3 <=499):
                
                this_change4 = this_change_3 / 200
                this_change_4 = this_change_3 % 200
                print("billetes de 200> ", int(this_change4), " ", "residuo > ", this_change_4)

                if (this_change_4 >=100 and this_change_4 <=199):

                    this_change5 = this_change_4 / 100
                    this_change_5 = this_change_4 % 100
                    print("billetes de 100 > ", int(this_change5), " ", "residuo > ", this_change_5)






billetes()