class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @classmethod
    def apenas_modelo(cls, modelo):
        return cls('Ford', modelo)
    
    @classmethod
    def apenas_marca(cls, marca):
        return cls(marca, 'Fusca')
    
c1 = Carro('Ford', 'Fiesta')
c2 = Carro('Ford', 'Focus')
c3 = Carro.apenas_modelo('Fusca')
c4 = Carro.apenas_marca('Ford')

print(c1.marca, c1.modelo)
print(c2.marca, c2.modelo)
print(c3.marca, c3.modelo)
print(c4.marca, c4.modelo)

    
