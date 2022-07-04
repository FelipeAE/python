#Se necesita desarrollar un programa en Python que use listas y que permita leer 5 notas obtenida por un estudiante. 
# Posteriormente debe mostrar todas las notas, el promedio, la mayor y la menor.
notas=[6.5, 5.7, 7, 2.3, 4.6]

print("Notas= ",end="")
for nota in notas:
    print(nota," ",end="")
print()
print("Nota promedio: ",round(sum(notas)/len(notas), 2))
print("Nota max: ",max(notas))
print("Nota min: ",min(notas))

