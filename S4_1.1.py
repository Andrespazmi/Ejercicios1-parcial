from S4_1 import Cargo 

class Empleado:
    secuencia=0
    def __init__(self,nom,ced,sue,cargo) :
        self.codigo=self.generarCodigo()
        self.nombre=nom
        self.cedula=ced
        self.sueldo=sue
        self.cargo=cargo
    def mostrar(self):
        print("codigo:{} nombre:{} cargo:{}={}".format(self.codigo,self.nombre,self.cargo.codigo,self.cargo.descripcion))

    def generarCodigo(self):
        Empleado.secuencia=Empleado.secuencia+1
        return Empleado.secuencia
cargo1 = Cargo("docente")
emp1= Empleado("andres","094247",450,cargo1)
emp1.mostrar()