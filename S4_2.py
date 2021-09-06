class tarea:
    def __init__(self) :
        pass
    def pagoJornadaExtra(self):
        horas_trabajadas, horas_extras, horas_extras_triple=0,0,0
        valor_hora, pago_hora_extra,pago_total=0,0,0
        horas_trabajadas= int(input("Ingresar horas trabajadas: "))
        valor_hora=float(input("ingrese valor hora: "))
        if (horas_trabajadas>40):
            horas_extras=horas_trabajadas-40
            if (horas_extras>8):
                horas_extras_triple=horas_extras=8
                pago_hora_extra=valor_hora*2*8+valor_hora*3*horas_extras_triple
            else:
                pago_hora_extra=valor_hora*2*horas_extras
            pago_total=valor_hora*40+pago_hora_extra
        else:
            pago_total=valor_hora*horas_trabajadas
        
        print("""Horas Trabajadas:{} Horas Extras:{} Horas Triple:{} Valor Hora:{} Pago ValorExtra:{} Pago Total:{}""".format(horas_trabajadas,horas_extras,
                                                                                                                     horas_extras_triple,valor_hora,pago_hora_extra,pago_total))
pago=tarea()
pago.pagoJornadaExtra()
