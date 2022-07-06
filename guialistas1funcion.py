import random
def suma_acumulada():
    lista = []
    lista_nueva = []
    suma = 0

    for i in range(4):
        lista.append(random.randint(1,3))

    print(lista)

    for i in lista:
        suma += int(i)
        lista_nueva.append(suma)

    print(lista_nueva)

suma_acumulada()