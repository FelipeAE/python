#Escriba programa en Python que tome una lista de números ingresados aleatoriamente y devuelva la suma acumulada, es decir, 
# una nueva lista donde el primer elemento es el mismo, el segundo elemento es la suma del primero con el segundo, 
# el tercer elemento es la suma del resultado anterior con el siguiente elemento y así sucesivamente. Por ejemplo, la suma acumulada de [1,2,3] es [1, 3, 6].
import random


lista = []
lista_nueva = []
suma = 0

for i in range(1,4):
    lista.append(random.randint(1,3))

print(lista)

for i in lista:
    suma += int(i)
    lista_nueva.append(suma)

print(lista_nueva)

