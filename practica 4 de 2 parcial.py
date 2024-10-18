print(" ") #para dejar un espacio al momento de ejecutar 
print("jose danie arguijo torres 1325_3-w")
print(" ") #para dejar un espacio al momento de ejecutar 
 
persona = {}  #indica la persona selecciuonada 

def agregar_dato(clave, valor): #pide datos de la persona 
    persona[clave] = valor #indica la persona clave 
    print(f"Contenido del diccionario: {persona}") #pide informacion de la persona 

nombre = input("Ingrese su nombre: ") #pide ingresar tu nombre 
agregar_dato("Nombre", nombre) #indica tu nombre 

edad = input("Ingrese su edad: ") #pide ingresar tu edad 
agregar_dato("Edad", edad) #indica tu edad 
 
sexo = input("Ingrese su sexo (M/F): ") #pide ingresar tu sexo 
agregar_dato("Sexo", sexo) #indica el sexo que eres 

telefono = input("Ingrese su teléfono: ") #pide ingrear un numero telefonico 
agregar_dato("Teléfono", telefono) #indica el numero de telefono 

correo = input("Ingrese su correo electrónico: ") #pide ingrear tu correo electronico 
agregar_dato("Correo Electrónico", correo) #indica tu correo electronico 

print("Información final de la persona:") #finaliza con toda tu informacion personal 
print(persona) #indica los datos de la persona 
 