class circunferencia: 
    def __init__(area):
        print ('Bienvenido a tu calculadora de diametro y radio')
    area = input ('ingresa el área de la circunferencia: ')
    try: 
        area = int(area)
    except: 
        area = 'inválido'
    if area == 'inválido':
            print ('El valor ingresado no es un entero, por favor verifica los datos')
    #Instrucciones matematicas para la computadora
    def operaciones(area):
        import math
        pi = math.pi
        radio = math.sqrt((area / pi))
        diametro = radio * 2
        print ('El valor del radio es:', radio)
        print ('El valor del diametro es:', diametro)
    #Instrucciones para el usuario
    
    #Impresion del resultado final
    resultado = operaciones(area)
    exit()
