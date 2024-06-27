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

    Σ=['-']   #Alfabeto de entrada
    for i in numero:
       Σ.append(i) 

    EI= 'A'
    EF= 'B,D'
    EA= EI
    
    cadenas=str(cadena)
    for caracter in cadenas:
        #print (caracter)
        if caracter in Σ:
            #print ("El carcacter pertenece al alfabeto")
            for f in tablaEnteros:
                if EA == f[0] and caracter in f[1]:
                    TablaC.append([EA,caracter,f[2]])  
                    EA=f[2]
                    # print ("Estado actual es : " + str(EA))
                    break
        else:
            # print("Cadena no pertenece al alfabeto")
            verificador = False
    
    if EA != EF:
        verificador=False
    return(verificador)

    # if EA in EF and (verificador == True):
    #     print("------------------------------")
    #     print("Es valida la cadena de entrada")
    #     print("____Tabla de transiciones_____")
    #     for t in TablaC:
    #         print (t)
    # else:
    #     print("---------------------------------")
    #     print("NO es valida la cadena de entrada")
    #     print("______Tabla de transiciones______")
    #     for t in TablaC:
    #         print (t)
    
def automata_identificadores(cadena):
    letra = letras()
    numero = numeros()

    tablaIdentificadores=[['A', '_','FINAL'],
                  ['A', letra,'FINAL'],
                  ['A', numero ,'M'],
                  ['FINAL', '_','FINAL'],
                  ['FINAL', numero,'FINAL'],
                  ['FINAL', letra,'FINAL'],
                  ['M', numero,'M'],
                  ['M', '_','M'],
                  ['M', letra,'M']]
    TablaC = []
    verificador = True #revisar que (x ϵ Σ)

    Σ=['_']   #Alfabeto de entrada
    for i in numero:
       Σ.append(i) 

    for i in letra:
       Σ.append(i) 

    EI= 'A'
    EF= 'FINAL'
    EA= EI
    
    palabras=cadena.split()

    cadenas=str(cadena)
    for caracter in cadenas:
        # print (caracter)
        if caracter in Σ:
            # print ("El carcacter pertenece al alfabeto")
            for f in tablaIdentificadores:
                if EA == f[0] and caracter in f[1]:
                    TablaC.append([EA,caracter,f[2]])  
                    EA=f[2]
                    # print ("Estado actual es : " + str(EA))
                    break
        else:
            # print("Cadena no pertenece al alfabeto")
            verificador = False

    if EA != EF:
        verificador=False
    return(verificador)

            # if EA in EF and (verificador == True):
            #     print("------------------------------")
            #     print("Es valida la cadena de entrada")
            #     print("____Tabla de transiciones_____")
            #     for t in TablaC:
            #         print (t)
            # else:
            #     print("---------------------------------")
            #     print("NO es valida la cadena de entrada")
            #     print("______Tabla de transiciones______")
            #     for t in TablaC:
            #         print (t)

def automata_reales(cadena):
    numero = numeros()
    exp=['E','e']
    tablaIdentificadores=[['A', '-','C'],
                  ['A', exp,'M'],
                  ['A', '.' ,'M'],
                  ['A', numero ,'B,D'],
                  ['B,D', '-','M'],
                  ['B,D', exp,'F'],
                  ['B,D', '.','E'],
                  ['B,D', numero,'B,D'],
                  ['C', '-','M'],
                  ['C', exp,'M'],
                  ['C', '.','M'],
                  ['C', numero,'B,D'],
                  ['E', '-','M'],
                  ['E', exp,'M'],
                  ['E', '.','M'],
                  ['E', numero,'G,J'],
                  ['F', '-','I'],
                  ['F', exp,'M'],
                  ['F', '.','M'],
                  ['F', numero,'H,K'],
                  ['G,J', '-','M'],
                  ['G,J', exp,'F'],
                  ['G,J', '.','M'],
                  ['G,J', numero,'G,J'],
                  ['H,K', '-','M'],
                  ['H,K', exp,'M'],
                  ['H,K', '.','M'],
                  ['H,K', numero,'H,K'],
                  ['I', '-','M'],
                  ['I', exp,'M'],
                  ['I', '.','M'],
                  ['I', numero,'H,K'],
                  ['M', '-','M'],
                  ['M', exp,'M'],
                  ['M', '.','M'],
                  ['M', numero,'M'],]
    TablaC = []
    verificador = True #revisar que (x ϵ Σ)

    Σ=['-','e','E','.']   #Alfabeto de entrada
    for i in numero:
       Σ.append(i) 

    EI= 'A'
    EF= 'H,K'
    EA= EI
    
    cadenas=str(cadena)
    for caracter in cadenas:
        # print (caracter)
        if caracter in Σ:
            # print ("El carcacter pertenece al alfabeto")
            for f in tablaIdentificadores:
                if EA == f[0] and caracter in f[1]:
                    TablaC.append([EA,caracter,f[2]])  
                    EA=f[2]
                    # print ("Estado actual es : " + str(EA))
                    break
        else:
            # print("Cadena no pertenece al alfabeto")
            verificador = False
    
    if EA != EF:
        verificador=False
    return(verificador)

    # if EA in EF and (verificador == True):
    #     print("------------------------------")
    #     print("Es valida la cadena de entrada")
    #     print("____Tabla de transiciones_____")
    #     for t in TablaC:
    #         print (t)
    # else:
    #     print("---------------------------------")
    #     print("NO es valida la cadena de entrada")
    #     print("______Tabla de transiciones______")
    #     for t in TablaC:
    #         print (t)
