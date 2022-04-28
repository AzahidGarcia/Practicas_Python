from operator import truediv


class primo: 
    #Instrucciones para el usuario
    print ('Bienvenido a tu adivinador de numeros primos')
    numero = input ('ingresa el valor a evaluar: ')
    try: 
        numero = int(numero)
    except: 
        numero = 'inválido'
    if numero == 'inválido':
            print ('El valor ingresado no es un entero, por favor verifica los datos')
    #Instrucciones matematicas para la computadora
    def operaciones(numero):
        cont=0;
        numeroEvaluar = numero
	# Funcion que recorre todos los numero desde el 2 hasta el valor recibido
        for i in range(1,numeroEvaluar):
            if(numeroEvaluar%i==0):
			# Si se puede dividir por algun numero mas de una vez, no es primo
                cont +=1
			
            if cont>1:
                return False
        return True
    if operaciones(numero):
        print("El número ", numero, " es primo")
    else:
        print("El número ",numero," NO es primo") 
    exit()
3