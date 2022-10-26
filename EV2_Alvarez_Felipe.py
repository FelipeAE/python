#Felipe Alvarez
class Persona:
    def __init__(self,nombre,pais):
        self.nombre=nombre
        self.pais=pais
    
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre
    def getPais(self):
        return self.pais
    def setPais(self,pais):
        self.pais=pais
    def identificar(self):
        return "Hola, soy {}".format(self.getNombre())
    
class Canal:
    def __init__(self,nombreCanal,tipo):
        self.nombreCanal=nombreCanal
        self.tipo=tipo
    
    def getnombreCanal(self):
        return self.nombreCanal
    def setnombreCanal(self,nombreCanal):
        self.nombreCanal=nombreCanal
    def getTipo(self):
        return self.tipo
    def setTipo(self,tipo):
        self.tipo=tipo
        
class Suscriptor(Persona):
    def __init__(self, nombre, pais, nombreUsuario):
        self.suscripciones=[]
        self.nombreUsuario=nombreUsuario
        super().__init__(nombre, pais)
        
    def getnombreUsuario(self):
        return self.nombreUsuario
    def setnombreUsuario(self,nombreUsuario):
        self.nombreUsuario=nombreUsuario
    def agregarSus(self,Canal):
        self.suscripciones.append(Canal)
    def listarSus(self):
        for x in self.suscripciones:
            print(x.getnombreCanal())
    def IdenCompleto(self):
        print("Hola, soy {},mi nombre de usuario es {} y mi pais de origen es {}".format(self.getNombre(),self.getnombreUsuario(),self.getPais()))
        
class Youtuber(Suscriptor):
    def __init__(self, nombre, pais, nombreUsuario,nombreC,tipo):
        self.canalP = Canal(nombreC,tipo)
        super().__init__(nombre, pais, nombreUsuario)
        
    def getcanalP(self):
        return self.canalP
    def setcanalP(self,canalP):
        self.canalP=canalP
    def IdenCompleto(self):
        print("Hola, soy {},mi nombre de usuario es {} y soy youtuber!!!".format(self.getNombre(),self.getnombreUsuario()))
        

c1=Canal("Mala Leche","humor")
c2=Canal("Cocina Misteriosa","Cocina")
y1=Youtuber("Enrique","Chile","El Enri","Entrenando con Enri","deporte")
y2=Youtuber("Alice","Dinamarca","Alicia","Alicia in Wonderland","misc")
s1=Suscriptor("Teresa","Mexico","Tere")
s2=Suscriptor("Asuka","Japon","Aska")
y1.IdenCompleto()
y2.IdenCompleto()
s1.IdenCompleto()
s2.IdenCompleto()
s1.agregarSus(c1)
s1.agregarSus(y1.getcanalP())
s1.agregarSus(y2.getcanalP())
s2.agregarSus(c1)
s2.agregarSus(y2.getcanalP())
s2.agregarSus(c2)
s1.listarSus()
s2.listarSus()