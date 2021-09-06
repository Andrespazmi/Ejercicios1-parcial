#! TERCERA SEMANA, EJERCICIO 7 - CICLOS FOR
class For:
    def __init__(self):
        pass
    
      #? ciclo repetitivo de incremento o decrementos se ejecuta mientas tenga valores 
    def usoFor(self):
        datos=["Daniel",50,true]
        numeros=(2,5,6,4,1)
        docente = {'nombre': 'daniel','edad':50,'fac':'faci'}
        listaNotas = [(30,40).(20,40),(50,40)]
        listaAlumnos = [{"nombre":"Erick","final":70},{"nombre":"Yady","final":50},{"nombre":"Danny","final":}]
        #! range ([inicio=0],limite,[inc/dec=1]).Genera un rango de valores desde un valor inicial a un valos final
        #* se ejecuta desde inicio hasta el limite 
        for i in range(5): # rango(0,1,2,3,4)
              print("i={}",format(i))
        for i in range(2,10): # rango(2,3,4,5,6,7,8,9)
              pint("i={}",format(i))
        for i in range(4,10,2): # rango(4,6,8,)
              pint("i={}",format(i),end=" ")    
        for i in range(12,3,-3): # rango(4,6,8,)
              pint("i={}",format(i),end=" ")    
      
        longitud = len(datos)
        print(datos[0])
        print(datos[2])
        print(datos[2])
        j=0
        while j < longitud:
            print("while",datos[j])
            j=j+1
            
        for i in range(longitud-1,-1,-1):
            print("for",datos[i])
            
        for i, dato in enumerate(numeros):
            print("for",i,datos)
        # dato toma cada elemento de la coleccion numeros(cadena,lista,tupla)
        for dato in numeros:
            print(dato)
            
        for dato in ['H','o','l','a','que','tal']:
            print(dato)
            
        print("\nDiccionario de notas")
        for clave,valor in docente.items():
            print(clave,":",valor,end=" ")
            
            
         for alumnos in listaAlumnos:              
              for clave,valor in alumnos.items():
                  print(clave,":",valor,end=" ")
              
         listaNotas = [(30,40),[20,40,20],(50,40,20,10)]
         for notas in listaNotas:
             print(notas)
             fo notas in notas:
                 print(notas)
                      
                 
bucle1= For()
bucle1.usoFor()