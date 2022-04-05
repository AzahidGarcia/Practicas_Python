#dato = input ('Ingrese dato: ')

#lista = ('hola', 'mundo', 'chanchito', 'feliz', 'dragones')

#if lista.count(dato) > 0:
    #print ('El dato existe: ', dato, ':)')
#else:
   #print ('El dato no existe :(', dato)

print ('Bienvenido a tu calculadora personal de dos numeros')
primero = input ('ingresa el primer número: ')
try: 
    primero = int(primero)
except: 
    primero = 'inválido'
if primero == 'inválido':
    print ('El valor ingresado no es un entero, por favor verifica los datos')
    exit()
segundo = input ('ingresa el segundo número: ')
try: 
    segundo = int(segundo)
except: 
    segundo = 'inválido'
if segundo == 'inválido':
    print ('El valor ingresado no es un entero, por favor verifica los datos')
    exit()  
print ('1.- Suma')
print ('2.- Resta')
print ('3.- Multiplicación')
print ('4.- División')
opcion = input ('Elige una opción: ')
opcionN= int (opcion)
if opcionN ==1:
    print ('El resultado es: ', primero + segundo)
elif opcionN ==2:
    print ('El resultado es: ', primero - segundo)
elif opcionN ==3:
    print ('El resultado es: ', primero * segundo)
elif opcionN ==4:
    print ('El resultado es: ', primero / segundo)
else: 
    print ('La opción seleccionada no es válida, intenta usando algún número que se encuentre en el menú')