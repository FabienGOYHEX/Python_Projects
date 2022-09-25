# Functions
def table_de_multiplication(number,min=1,max=10):
    if min < 1 or max > 10 :
        print("Error doit être compris entre 1 et 10")
        return
    else :
        for i in range(min,max+1) :
            print(i , "x", number , "=",  i * number)

table_de_multiplication(4,max=10)