class Computador:
    def __init__(self, peca):
        self.peca_pc = peca

    @property
    def peca(self):
        return self.peca_pc
    
    @property
    def cor_motherboard(self):
        return 'Blue'

processador = Computador('Processador')
motherboard = Computador('MotherBoard')

print(processador.peca)
print(processador.peca)
print(processador.peca)
print(processador.peca)
print(processador.peca)
print(motherboard.peca_pc)
print(processador.cor_motherboard)
