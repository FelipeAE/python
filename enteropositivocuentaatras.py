# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas
n=int(input("Ingrese un numero positivo: "))
for i in range(n,-1,-1):
    print(i, end=", ")