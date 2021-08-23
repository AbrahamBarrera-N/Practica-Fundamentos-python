# Imprime tu nombre

# Cadena de caracteres, o sea plabras, letras (string)
nombre = input("Introduce tu nombre: ")
print(f"Hola {nombre}")
print("Hola {}".format(nombre)) 

# Variable entero (int)
edad = 19
# Variable flotante (decimales)
altura = 1.75

# Convertir a string 
edadString = str(edad)

print(edad + edad)
print(edadString + edadString)

# El type me muestra el tipo de datos que me estan mandando
print(type(edad))
print(type(edadString))

# Esto se llama castear 
tuedad = input("Introduce tu edad: ")
tuedad = int(tuedad)

# Estructura de control: Un pedazo de codigo que nos permite controlar el flujo de la informacion 
# Estructura de control IF
if tuedad >= 18 and tuedad <100:
    print("Eres mayor de edad")
elif tuedad >=100:
    print("¿Eres inmortal?")
elif tuedad<= 0:
    print("No existes")
else:
    print("Eres menor de edad")

# Estructura de control FOR
for i in range(0, 10):
    print(i)