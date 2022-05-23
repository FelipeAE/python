# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
n1=int(input("Ingrese numero: "))
n2=int(input("Ingrese numero: "))
if n2==0:
    print("El divisor debe ser distinto de 0")
else:
    print(n1/n2)
