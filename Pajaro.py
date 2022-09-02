class Bird():
    
    def __init__(self, name,age, feather_color, size, ubicacion):
      self.name = name
      self.feather_color = feather_color
      self.size = size
      self.ubicacion = ubicacion
      self.age= age
    def fly(self):
        self.identificar()
        print("Estoy volando!")
    def identificar(self):
        print("soy",self.name)
    def dondeEstoy(self):
        self.identificar()
        print("Estoy en",self.ubicacion)

a=Bird("albatroz",33,"gris","grande","temuco")

a.identificar()
a.fly()
a.dondeEstoy()