class Empleado():
    def __init__(self, nombre, cargo, pagoXhora):
        self.nombre = nombre
        self.cargo = cargo
        self.pagoXhora = pagoXhora
    def sueldo(self):
        pass
class Emp_Jornada(Empleado):
    def sueldo(self):
        print("su sueldo es",self.pagoXhora*40)
class Emp_planta(Empleado):
    def sueldo(self):
        print("su sueldo es",self.pagoXhora*168)
class Emp_Contrata(Empleado):
    def __init__(self, nombre, cargo, pagoxHora, horasTrabajo):
        self.horasTrabajo = horasTrabajo
        super().__init__(nombre,cargo,pagoxHora)
    def sueldo(self):
        sueldo=self.pagoXhora*self.horasTrabajo
        if self.horasTrabajo>40:
            sueldo=sueldo+sueldo*0.1
        print("su sueldo es",sueldo)

a=Emp_Jornada("Marcos","Junior",20000)
b=Emp_planta("Juan","Analista P",30000)
c=Emp_Contrata("Fernanda","Diseñadora",15000,41)

a.sueldo()
b.sueldo()
c.sueldo()