from utilidades import numeros, letras

def automata_enteros(cadena):
    numero = numeros()

    tablaEnteros=[['A', '-','C'],
                  ['A', numero,'B,D'],
                  ['C', '-','M'],
                  ['C', numero,'B,D'],
                  ['M', '-','M'],
                  ['M', numero,'M'],
                  ['B,D', '-','M'],
                  ['B,D', numero,'B,D']]
    TablaC = []
    verificador = True #revisar que (x ϵ Σ)

    Σ=[numero , '-']   #Alfabeto de entrada

    EI= 'A'
    EF= ['B,D']
    EA= EI
    
    cadenas=str(cadena)
    for caracter in cadenas:
        print (caracter)
        if caracter in Σ or numero:
            print ("El carcacter pertenece al alfabeto")
            for f in tablaEnteros:
                if EA == f[0] and caracter in f[1]:
                    TablaC.append([EA,caracter,f[2]])  
                    EA=f[2]
                    print ("Estado actual es : " + str(EA))
                    break
        else:
            print("Cadena no pertenece al alfabeto")
            verificador = False

    if EA in EF and (verificador == True):
        print("------------------------------")
        print("Es valida la cadena de entrada")
        print("____Tabla de transiciones_____")
        for t in TablaC:
            print (t)
    else:
        print("---------------------------------")
        print("NO es valida la cadena de entrada")
        print("______Tabla de transiciones______")
        for t in TablaC:
            print (t)
