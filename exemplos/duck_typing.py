class Pato:
    def voar(self):
        print("Pato voando...")

class Aviao:
    def voar(self):
        print("Aviao voando...")

def fazer_voar(objeto):
    objeto.voar()

potolino = Pato()
aviao = Aviao()

fazer_voar(potolino)
fazer_voar(aviao)