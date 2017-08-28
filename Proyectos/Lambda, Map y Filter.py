lista = [1,2,3,4,5,6,7,8,9,10]

#Funcion que retorna el cuadrado de un numero
def cuadrado(numero):
    r = numero**2
    return r

#La funcion Lambda reemplaza una funcion, dandole un valor , en este caso X
x=5
resultado = (lambda x:x**2)(x)
print("Imprime  un numero transformado con lambda: ")
print (resultado)

#Tambien se puede usar la funcion "map" para operarar iterables
# como listas y aplicarle una funcion (cuadrado) a todos los valores dentro de la lista
resultado2 = list(map(cuadrado,lista))
print("Numeros mapeados y usando una funcion: ")
print(resultado2)


#De la misma  forma se puede hacer con una funcionn en forma de "lambda"
resultado2 = list(map(lambda x:x**2,lista))
print("Numeros mapeados y usando lambda: ")
print(resultado2)

#Gracias  a la funcion "filter" se pueden filtrar datos de una lista si se cumple una condicion
resultado3 = list(filter(lambda x:x%2 == 0 ,lista))
print(resultado3)
