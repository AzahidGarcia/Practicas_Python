class numeroPar: 
    #Instrucciones matematicas para la computadora
    def operaciones(numero):
        numeroEvaluar = numero % 2
        if numeroEvaluar != 0:
            print ('El numero no es par')
        else: 
            print ('El numero es par')    
    #Instrucciones para el usuario
    print ('Bienvenido a tu adivinador de numeros pares')
    numero = input ('ingresa el valor a evaluar: ')
    try: 
        numero = int(numero)
    except: 
        numero = 'inválido'
    if numero == 'inválido':
            print ('El valor ingresado no es un entero, por favor verifica los datos')
    #Impresion del resultado final
    resultado = operaciones(numero)
    exit()
