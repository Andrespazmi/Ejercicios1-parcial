#SEGUNDA SEMANA 4 EJERCICIO - TUPLAS

class Sintaxis:
    instancia=0 # variables de clases (opcional)
# _init_ metodoconstrctor que se ejecuta cuando se instancia la clase cuyo objetivo es 
# inicializar los atributos de la clase. self es un objeto que representa la clase creada
def _init_(self,dato="inicializacion"):
    self.frase=dato #variable de instancia 
    #Sintaxis.instancia = Sintaxis.instancia+1

def usoVariable(self):
    edad, _peso = 21, 65.4
    nombres = 'Harold Caicedo' 
    tipo_sexo = 'M'
    civil = true 
    # TUPLAS = () Son colecciones de datos de cualquier tipo inmutables 
#tuplas =() son colecciones de datos de cualquier tipo inmutables
usuario=()
usuario= ('dchiki','1234','Omar@gmail.com')
#usuario[3]="milagro"
# listas = [] colecciones mutables
materias = ['programacion web','PHP','POO']
materias[1]="python"
materias.append("Go")
#diccionario = {} colecciones de objetos clave:valor tipo json
docente = {'nombre':'daniel', 'edad':50, 'fac': 'faci'}
# #presentacion con format
print(""" Mi nombre es {}, tengo {} 
        años""".format(nombres, edad))
print (usuario, materias, docente)
print (usuario, usuario[0],usuario[0:2],usuario[-1])
print (materias, materias[2:],materias[:3],materias[:],materias[-2:])
print (docente, docente['nombre'])

ejercicios = Sintaxis() #se crea un objeto que es una instancia de la clase y se ejecuta el constructor 
ejercicios.usoVariables()