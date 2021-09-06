#TERCER EJERCICIO SEMANA 1, FUNCIONES EN PYTHON - DEF
"""funciones sin retorno"""
def vocales (frase):
    for car in frase:
        if car in ('a','e',"i",'o','u'):
            print(car)
"""Llamada a funcion"""
oracion=input('Escriba una oracion:')
vocales(oracion.lower())
"""Funcion con retorno de valor"""
def promedio(notas):
    sumn=0