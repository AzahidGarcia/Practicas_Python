class Vehiculos:
    def __init__(self):
        pass
    def color(self):
        print("Color Azul")
    def ruedas(self):
        print("4 ruedas")
class automovil(Vehiculos):
    def velocidad(self):
        print("150km/h")
    def cilindrada(self):
        print("1200 cc")

auto = automovil()
auto.color()
auto.ruedas()
auto.velocidad()
auto.cilindrada()
