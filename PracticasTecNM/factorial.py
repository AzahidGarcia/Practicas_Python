class factorial: 
    #Instrucciones matematicas para la computadora
    def factorial(num): 
        if num < 0: 
            print("Factorial of negative num does not exist")

        elif num == 0: 
            return 1
        else: 
            fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 
    #Instrucciones para el usuario
    print ('Bienvenido a tu adivinador de factorial')
    num = input ('ingresa el valor a evaluar: ')
    try: 
        num = int(num)
    except: 
        num = 'inválido'
    if num == 'inválido':
            print ('El valor ingresado no es un entero, por favor verifica los datos')
    #Impresion del resultado final
    print("El factorial de",num," es ", factorial(num))
    exit()
