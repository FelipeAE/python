# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta
contra="contraseña"
pas=""
while pas.lower()!=contra:
    pas=str(input("Ingrese contraseña: "))
    print("Ingrese contraseña correcta")
    
    