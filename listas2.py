#Desarrollar un programa que inicialice una lista de números con valores aleatorios y posteriormente ordene los elementos de menor a mayor.
import random
lista = []
for i in range(1,11):
    lista.append(random.randint(1,10))
# ordenar la lista
lista.sort()

#recorrer el valor
for numero in lista:
    print(numero," ",end="")