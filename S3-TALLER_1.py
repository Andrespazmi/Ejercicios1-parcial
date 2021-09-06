class Cadena:
    def __init__(self, frase):
        self.__frase= frase
    
    @property
    def frase(self):
        return self.__frase
    
    def long(self):
        num = len(self.__frase)
        return num

    def MostrarValores(self):
        print("""En numero de caracteres de la cadena "{}" es de: {}.""".format(self.__frase, self.long()))
        

class Caracteres(Cadena):
    def __init__(self, frase):
        super().__init__(frase)

    #!def po(self):
        pal=input("Ingrese una palabra la cual desea saber su posicion: ")

        if pal in self.frase:
            pb= self.frase.index(pal)
            return pb
        else:
            return -1
        
    
    def cad(self):
        posiciones=[]
        posicion=0
        subc=input("Ingrese una palabra la cual desea saber sus posiciones: ")
        while posicion != -1:
            posicion=self.frase.find(subc,posicion)
            if posicion !=-1:
                posiciones.append(posicion)
                posicion+=1
        return posiciones
    
    #!def elim(self):
        fra=input("Ingrese la palabra que desee eliminar: ")
        cadena=self.frase
        lista=cadena.split()
        for i in lista:
	        if i == fra:
		        lista.remove(fra)
        
        listan= " ".join(lista)
        return listan

    def ExtrDigitos(self):
        cad= ""
        Digits={}
        for i in self.frase:
            if i in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                cad+=i

        Digits[cad]=len(cad)
        return Digits

    def InsertPalab(self):
        Palab=input("Ingrese una palabra que quiera agregar a la cadena: ")
        if Palab in self.frase:
            lis= self.frase.split()
            i=lis.index(Palab)
            lis.insert(i,Palab)
            lis_t= " ".join(lis)
            return print("La frase con la palabra agregada es: {}".format(lis_t))
        else:
            return print("La palabra que ingreso no coincide con ninguna de la frase.")

    def ExtractCa(self):
        acu=""
        cad=self.frase.lower()
        dicCa={}
        for i in cad:
            if i not in("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
             "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", 
           "6", "7", "8", "9", " "):
                acu+=i
        dicCa[acu]=len(acu)
        return dicCa

    def mostrar1(self):
        super().MostrarValores()
    def mostrar2(self):
        print("La posicion es: {}".format(self.po()))
    def mostrar3(self):
        print('Posiciones: {}'.format(self.cad()))
    def mostrar4(self):
        print("La Cadena con los elementos borrados: '{}'".format(self.elim()))
    def mostrar5(self):
        print("El diccionario de los digitos es: {}".format(self.ExtrDigitos()))
    def mostrar7(self):
        print("El diccionario de los caracteres es: {}".format(self.ExtractCa()))
  
emp="0"
while emp!="8":
    print("\n\t*** Menu xdddd ***")
    print("1)	Numero de caracteres")
    print("2)	Buscar palabra ")
    print("3)	Buscar palabras")
    print("4)	Elimina palabra")
    print("5)	Extraer digitos")
    print("6)	Inserta palabra")
    print("7)	Extraer caracteres especiales")
    print("8)	Salir")
    
    emp=input("Ingrese una opcion:")
    print("")
    if emp=="1":
        Cadena=input("Digite una Frase: ")
        fra= Caracteres(Cadena)
        fra.mostrar1()

    elif emp=="2":
        Cadena=input("Digite una Frase: ")
        fra= Caracteres(Cadena)
        fra.mostrar2()

    elif emp=="3":
        Cadena=input("Digite una Frase: ")
        fra= Caracteres(Cadena)
        fra.mostrar3()

    elif emp=="4":
        Cadena=input("Digite una Frase: ")
        fra= Caracteres(Cadena)
        fra.mostrar4()

    elif emp=="5":
        Cadena=input("Digite una Frase: ")
        fra= Caracteres(Cadena)
        fra.mostrar5()
        
    elif emp=="6":
        Cadena=input("Digite una Frase: ")
        fra= Caracteres(Cadena)
        fra.InsertPalab()

    elif emp=="7":
        Cadena=input("Digite una Frase: ")
        fra= Caracteres(Cadena)
        fra.mostrar7()
    
    elif emp=="8":
        print("Decidio salir")
        break

    else:    
        print("Dato digitado no correcto")