class Animal:
        def __init__(self, especie, edad):
            self.especie = especie
            self.edad = edad    
        def hablar(self):
            pass
        def moverse(self):
        
            pass
        def describeme(self):
            print("Soy un Animal del tipo", type(self).__name__)

class Perro(Animal):
        def hablar(self):
            print("Guau!")
        def moverse(self):
            print("Caminando con 4 patas")

class Vaca(Animal):
        def hablar(self):
            print("Muuu!")
        def moverse(self):
            print("Caminando con 4 patas")

class Abeja(Animal):
        def hablar(self):
            print("Bzzzz!")
        def moverse(self):
            print("Volando")
        def picar(self):
            print("Picar!")

mi_perro = Perro('mamífero', 10)
mi_vaca = Vaca('mamífero', 23)
mi_abeja = Abeja('insecto', 1)
    
mi_perro.describeme()
mi_perro.hablar()
mi_perro.moverse()
mi_vaca.describeme()
mi_vaca.hablar()
mi_vaca.moverse()
mi_abeja.describeme()
mi_abeja.hablar()
mi_abeja.moverse()
mi_abeja.picar()