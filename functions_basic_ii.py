# #1
def countdown (num):
    x=[]
    for i in range(num,-1,-1):
        x.append(i)
    return x

print(countdown(20))

lista=[4,2]
# #2
def imprimir_y_devolver (devuelta):
    print (devuelta[0])
    return devuelta[1]

imprimir_y_devolver(lista)
x = imprimir_y_devolver(lista)
print(x)

# #3
def primero_mas_longitud (x):
    y= (x[0]+len(x))
    return y

print(primero_mas_longitud([2,4,6,8,10]))

#4
you =[0,2,4,6,8,1,9,2,10,1]
def valores_mayores_que_el_segundo(rex):
    listanueva=[]
    if len(rex)>=2:
        for i in rex:
            if i>rex[1]:
                listanueva.append(i)
        print (len(listanueva))
        return (listanueva)
    else:
        return False

print (valores_mayores_que_el_segundo(you))



#5


def length_and_value (tamaño, valor):
    lista2=[]
    for i in range (tamaño):
        lista2.append(valor)
    print (lista2)

length_and_value(8,5)