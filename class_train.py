class Garrafa:
    def __init__(self, liquido, tamanho):
        self.liquido = liquido
        self.tamanho = tamanho

g1 = Garrafa('agua', '250ml')
g2 = Garrafa('ice tea', '500ml')

print(g1.liquido)
print(g1.tamanho)
print(g2.liquido)
print(g2.tamanho)

############################################

class Relogio:
    def __init__(self, horas, minutos):
        self.horas = horas
        self.minutos = minutos

r1 = Relogio(12 , 3)
r2 = Relogio(14 , 30)

print(r1.horas)
print(r1.minutos)
print(r2.horas)
print(r2.minutos) 

############################################
