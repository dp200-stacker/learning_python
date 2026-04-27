class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.motores = None
        self.fabricante = None
    
    def inserir_motor(self, *motores):
        for motor in motores:
            self.motores.append(motor)

    def listar_motor(self):
        for motor in self.motores:
            print(motor.nome)
    ###########################################
    def inserir_fabricante(self, *fabricantes):
        for fabricante in fabricantes:
            self.fabricantes.append(fabricante)

    def listar_fabricante(self):
        for fabricante in self.fabricantes:
            print(fabricante.nome)

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome


polo = Carro('Polo')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
polo.fabricante = volkswagen
polo.motor = motor_1_0
print(polo.nome, polo.fabricante.nome, polo.motor.nome)

fiat_uno = Carro('Uno')
fiat = Fabricante('Fiat')
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0
print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)

ferrari_1 = Carro('Enzo')
ferrari = Fabricante('Ferrari')
motor_5_0 = Motor('5.0')
ferrari_1.fabricante = ferrari
ferrari_1.motor = motor_5_0
print(ferrari_1.nome, ferrari_1.fabricante.nome, ferrari_1.motor.nome)
