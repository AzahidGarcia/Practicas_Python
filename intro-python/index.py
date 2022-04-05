#Acá va un comentario
if 3 > 5 :
    print('Esto no se imprime 3')

#if 5 > 3 :
    #print('5 es mayor que 3')

x = 6
y = 'chanchito feliz' 
print (x, y)

email = 'chanchito@feliz.com'

print (email)

a, b, c = 'lala', 'Lele', 'Lili'

print (a, b, c)

valor1 = valor2 = valor3 = 'chanchito feliz'

print (valor1, valor2, valor3)

inicio = 'hola '
final ='mundo'

print (inicio + final)


palabra = 'hola mundo' 
oracion = "hola mundo comilla doble" 

entero = 20 

conDecimales = 20.2 

complejo = 1j

#print (palabra, oracion, entero, conDecimales, complejo)

lista = [1, 2, 3]
lista2 = lista.copy()
lista.append(4)
#lista.clear()
#print (lista, lista2.count(2))
#print (len(lista2))
largolista=len(lista)
largolista2 =len(lista2)
#print (largolista, largolista2)

#print(lista[0])

#lista.pop()
#lista.remove(1)

#lista.reverse() de atras para adelante
#lista.sort() ordena listas pero solo cuando tienen el mismo tipo de datos.
tupla = ('hola', 'mundo', 'somos', 'tupla')
#print (tupla.count('hola'))
#print (tupla.index('mundo'))

listaDeTupla = list(tupla)
listaDeTupla.append('chanchito')
#print(listaDeTupla)

rango = range(6)
#print (rango)
diccionario = {
    "nombre": "chanchito feliz",
    "raza": "persa",
    "edad": 5
}
#print (diccionario)
#print (diccionario['nombre'])
#print (diccionario.get ('nombre'))
diccionario['nombre']='Fluffy'
#print (diccionario)
#print (len(diccionario))

diccionario ['ronronea'] = 'Si'

#diccionario.pop ('ronronea')
#diccionario.popitem()
#del diccionario ['ronronea']
diccionario.clear()
#copiagatito = diccionario.copy() o podemos usar copiagatito = dict(diccionario)
#print (diccionario, copiagatito)


gatitos = {
    "Fluffy": {
        "nombre": "Fluffy",
        "edad": 4
    },
    "Mamba": {
        "nombre": "Black Mamba",
        "edad": 12
    }
}
#print(gatitos)

perritos = dict(nombre= "Chanchito Feliz", edad=6)
print (perritos)
#boleanos, verdaderos o falsos

verdadero = True 
falso = False
print (verdadero, falso)