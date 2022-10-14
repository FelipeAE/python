class Perro:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

class Perros:
    def __init__(self):
        self.perros=[]
    
    def agregaPerros(self,perro):
        self.perros.append(perro)
    
    def listar(self):
        for x in self.perros:
            print(x.nombre)

p1=Perro("firulais",18)
p2=Perro("laika",5)
p3=Perro("sandokan",10)

a=Perros()
a.agregaPerros(p1)
a.listar()
print()
a.agregaPerros(p2)
a.agregaPerros(p3)
a.listar()
