#Segundo ejercicio semana 1, uso de while infinito
c=1
while true:
    print(c)
#While validacion
vocal = input("digite vocal:")
while vocal not in('a','e','i','o','u'):
    if vocal=='.':
        break
    vocal = inpu("vocal:")
print('La vocal o punto ingresados es:´{}'.format(vocal))