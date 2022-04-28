class Depresion:
    def __init__(self):
        pass
    def sintomas(self):
        print("Tristeza, fatiga, pensamientos trágicos, insomnio")
class tratamiento(Depresion):
    def citalopram(self):
        print("Ayuda a recaptar la serototina")
    def olanzapina(self):
        print("Ayuda con el insomnio")
depresion = tratamiento()
depresion.sintomas()
depresion.citalopram()
depresion.olanzapina()
# basado en mi expeciencia con los antidepresivos