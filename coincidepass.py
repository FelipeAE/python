# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
password="contrasena"
contra=str(input("Ingrese password: "))
if password==contra:
    print("La pass coincide")
else:
    print("La pass no coincide")