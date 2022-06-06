# Usando las estructuras de programacion que hasta ahora conocemos; ingresar 4 cadenas por teclado y contabilizar en cada una de ellas, cuantas vocales tiene
def contar_vocales(cadena):
    cont=0
    for letra in cadena:
        if letra.lower() in "aeiou":
            cont+=1
    return cont
cadena1=input("Ingrese cadena1: ")
cadena2=input("Ingrese cadena2: ")
cadena3=input("Ingrese cadena3: ")
cadena4=input("Ingrese cadena4: ")
cantidad1= contar_vocales(cadena1)
cantidad2= contar_vocales(cadena2)
cantidad3= contar_vocales(cadena3)
cantidad4= contar_vocales(cadena4)
print("En la cadena",cadena1,"hay",cantidad1,"vocales")
print("En la cadena",cadena2,"hay",cantidad2,"vocales")
print("En la cadena",cadena3,"hay",cantidad3,"vocales")
print("En la cadena",cadena4,"hay",cantidad4,"vocales")