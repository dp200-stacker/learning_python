class Dinheiro:
    nota = 50

    def __init__(self, nota, moeda):
        self.nota = nota
        self.moeda = moeda

    def nota_menos_moeda(self):
        return Dinheiro.nota - self.moeda
    

d1 = Dinheiro('Nota', 20)
d2 = Dinheiro('Moeda', 2)

print(Dinheiro.nota)
print(d1.nota_menos_moeda()) 
print(d2.nota_menos_moeda()) 
