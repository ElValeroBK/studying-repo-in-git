### List_comprehencion ####

#eje_1
mi_lista = [1,2,3,4,5,6,7,8,9]

mi_list0 = [i for i in mi_lista]

print(mi_list0)




#eje2
from math import pow
def my_funcion(numero):  # function

    numero = int(pow(numero,2))
    #numero = numero ** 2
    return numero
     

mi_list1 = [my_funcion(i) for i in range(2,51)]

print(mi_list1)