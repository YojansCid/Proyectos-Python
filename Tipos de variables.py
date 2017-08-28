"""Tipos de datos y algunas funciones de str"""

"""En la impresion de los datos para que no de un error de tipos de 
    datos se castea a str()"""

"""Python no necesita declaracion de tipo de datos, solo al hacer las operaciones de 
    suma, resta, etc tienen que ser del mismo tipo de dato"""

numero = 3
numero2 = 3
print("Suma de dos numeros: "+ str(numero + numero2))

numero =("3")
numero2 = str("3")
"""Aqui al ser dos str implicitos, son concatenados"""
print("Suma de dos strings (Concatenacion): "+numero + numero2)

numero =int("3")
numero2 = int("3")
"""Al ser dos datos enteros, se suman"""
print("suma de datos int casteados: "+ str(numero + numero2))

numero =int("3")
numero2 = float("3")
"""Al tener un dato de tipo float, transforma el dato a un float"""
print("Suma de dato int con float casteado: "+ str(numero + numero2))


"""Tambien los str tienen varias funciones, por ejemplo cambiar el texto a mayuscula o minuscula"""

texto = "Yojans H. C. V."

texto = texto.upper()
print("Texto pasado a mayuscula: "+texto)

texto = texto.lower()
print("Texto pasado a minuscula: "+texto)

"""Tambien se puede reemplazar alguna letra o conjunto de letras que tenga el str por otra palabra"""
texto = texto.replace("v","Varela")
print("Reemplazando letra: "+texto)

"""Impresion de una letra de la cadena por su posicion"""
print("impresion de la letra [5] de la cadena: "+texto[5])


"""Impresion de las primeras cuatro letras de la cadena"""
print("Imprasion de parte de la cadena: "+texto[0:4])

"""impresion de la parte final de la cadena"""
print("Imprasion de parte de la cadena: "+texto[4:])
