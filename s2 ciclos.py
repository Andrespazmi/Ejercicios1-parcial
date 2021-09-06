#SEGUNDA SEMANA, EJERCICIO 6 - CICLOS
class Ciclos:
    def _init_(self,num1=5):
        self.numero=num1

    def usoWhile(self):
        #ciclo repetitivo que se ejecuta por verdadero y sale por falso 

         car = input("Escriba una vocal: ")
         car = car.lower()
         while car not in('a','e',"i",'o','u'):
            car = input("Escriba una vocal: ").lower()
         print ("En hora buena el caracter:{} es una vocal".format(car))

ciclo1 = ciclos()
ciclo1.usoWhile()