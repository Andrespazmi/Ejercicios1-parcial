# SEGUNDA SEMANA, EJERCICIO 5 - CONDICIONES

class Condicion:
    Condicion=0 # variables de clases (opcional)
# _init_ metodoconstrctor que se ejecuta cuando se instancia la clase cuyo objetivo es 
# inicializar los atributos de la clase. self es un objeto que representa la clase creada
def _init_(self,num1=0,num2=1):
    self.numero1=num1# variable de instancia 
    self.numero2=num2# variable de instancia

def usoIf(self):
    # if ... elif ... else ...: permiten condicionar la ejecucion de uno o varios bloques 
    # de sentencias al cumplimiento de una o varias condiciones.
    if self.numero1 == self.numero2:
        print("numero1:{}, numero3:{}: son iguales".format(self.numero1,self.numero2))


# # usar clase
# cond1 = Condicion()
# print(cond1.numero1)
# print(cond1.numero2)

# cond2 = condicion(30)
# print(cond2.numero1)
# print(cond2.numero2)

cond2 = Condicion(10,20)
cond2.usoIf() #llamada a un metodo de la clase
print(cond2.numero1) #llamada a un atributo de la clase