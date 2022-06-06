# vocalesencadenas
def contar_vocales(cadena):
    cont=0
    for letra in cadena:
        if letra.lower() in "aeiou":
            cont+=1
    print("En la cadena",cadena,"hay",cont,"vocales")
for i in range(4):
    contar_vocales(input("Ingrese cadena: "))
