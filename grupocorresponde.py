# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo con el sexo y el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde
nombre = input("Ingresa tu nombre: ")
genero = input("Ingresa tu genero (M o F): ")
if (genero == "M" and nombre.lower() < 'm') or (genero == "F" and nombre.lower() > 'n'):
    grupo = "A"
else:
    grupo = "B"
print("Tu grupo es " + grupo)