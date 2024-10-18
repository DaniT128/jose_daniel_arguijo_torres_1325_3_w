print(" ") #para dejar un espacio al momento de ejecutar 
print("jose daniel arguijo torres_1325_3-w")
print(" ") #para dejar un espacio al momento de ejecutar 

def crear_diccionario(entradas): #permite la entada del diccionario 
    diccionario = {} #llaves abiertas 
    for entrada in entradas.split(','): #pide la entrada 
        esp, eng = entrada.split(':') #pide ingresar una palabra en español e ingles 
        diccionario[esp.strip()] = eng.strip() #indica el diccionario en español  
    return diccionario #cierre del diccionario 

def traducir_frase(frase, diccionario): #indica la traducion de la frase 
    palabras = frase.split() #pide al usuario la frase 
    traduccion = [] #traducion de la frase 
    for palabra in palabras: #indica ingresar la frase  
        traduccion.append(diccionario.get(palabra, palabra))  # Traduce o deja la palabra sin traducir
    return ' '.join(traduccion)  #cierre del diccionario 

entradas = input("Introduce las palabras en español e inglés (ejemplo: 'hola:hello, adiós:goodbye'): ") #muestra un ejemplo de como elejir una frase breve 
diccionario = crear_diccionario(entradas) #pide crear un diccionario  

frase = input("Introduce una frase en español para traducir: ") #indica el ingreso de una frase 
traduccion = traducir_frase(frase, diccionario) #traduce la frase elejida 

print("Traducción:", traduccion) #indica la traducion de la frase elejida 
