print("*******************************************")
"""Ciclo for con rangos desde 2 a 5"""
print("Ciclo FOR")
print("For desde 2 a 5: \n")
for i in range(2,5):
    print("Iteracion N°: "+ str(i))


print("--------------------------")
"""si solo se le coloca un numero, lo tomara desde cero hasta el numero indicado"""
print("For hasta la posicion 3: \n")
for x in range(3):
    print("Iteracion N°: "+ str(x))

print("--------------------------")
"""Ciclo FOR con sentencia BREAk, lo que permite parar un ciclo bajo una condicion"""
print("For con sentencia BREAK: ")
for x in range(10):
    print("Iteracion N°: "+ str(x))
    if (x==5) :
        print("El ciclo se paro en la iteracion: " + str(x))
        break

print("--------------------------")
"""Ciclo FOR con sentencia CONTINUE, lo que permite saltar una iteracion dentro de un ciclo bajo una condicion"""
print("For con sentencia CONTINUE: ")
for x in range(10):
    print("Iteracion N°: "+ str(x))
    if (x==5) :
        print("Se salto la iteracion N°: " + str(x))
        continue


print("--------------------------")
"""Se puede aplicar el ciclo FOR en una cadena de texto para recorrer esta"""
print("Impresion de cadena letra por letra con ciclo FOR: ")
for y in "Pulpito":
    print(y)
"""Salata una linea en cada letra por que la funcion PRINT() aplica un salto de linea en cada impresion"""

print("--------------------------")
"""Se puede hacer terminar cada impresion de letra de la cadena con algun caracter u otra cadena"""
print("Impresion de cadena con ciclo FOR letra por letra, aplicando un sufijo a cada letra: ")
for y in "Pulpito7":

    if y.isdigit():
        print(y, end="%")
        """Si el caracter recorrido es un numero (con la funcion isdigit() se le agrega un %"""
    else:
        print(y, end="-")